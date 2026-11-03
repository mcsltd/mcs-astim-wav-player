"""Публичный интерфейс генерации FFR WAV-файлов."""

from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path

from .constants import DEFAULT_PERCENT_VAR_PAUSE, DEFAULT_SAMPLE_RATE
from .io import read_syllable, save_wav
from .signal import build_full_signal
from .stimulus import make_ramp_window, make_stimulus


def _format_frequencies(frequencies: Sequence[float]) -> str:
    return "-".join(f"{frequency:g}" for frequency in frequencies)


def _build_file_name(
    output_name: str | None,
    frequencies: Sequence[float] | None,
    stimulus_duration_ms: float,
    inter_stimulus_interval_ms: float,
    num_repetitions: int,
    add_inv: bool,
) -> str:
    if output_name is not None:
        return output_name if output_name.lower().endswith(".wav") else f"{output_name}.wav"

    mode = f"{_format_frequencies(frequencies)}Hz" if frequencies else "Syllable"
    return (
        f"Da_{mode}"
        f"_TS{stimulus_duration_ms:.1f}ms"
        f"_TP{inter_stimulus_interval_ms:.1f}ms"
        f"_N{num_repetitions}"
        f"_INV{int(add_inv)}.wav"
    )


def create_wav(
    output_dir: str | Path,
    inter_stimulus_interval_ms: float,
    num_repetitions: int,
    *,
    syllable_wav: str | Path | None = None,
    frequencies: Sequence[float] | None = None,
    stimulus_duration_ms: float | None = None,
    sample_rate: int = DEFAULT_SAMPLE_RATE,
    add_inv: bool = False,
    amplitude: float = 1.0,
    percent_var_pause: float = DEFAULT_PERCENT_VAR_PAUSE,
    output_name: str | None = None,
) -> Path:
    """Создаёт WAV-файл с повторяющимися FFR-стимулами и триггерами.

    Стимул может быть задан либо готовым WAV-файлом со слогом, либо набором
    частот для синтеза синусоидального сигнала. Стимулы разделяются паузами
    случайной длительности и перемешиваются. Каждый стимул записывается в
    левый канал, а в правый канал добавляются 3-битные триггеры AStimWavPatcher.

    Args:
        output_dir: Каталог для сохранения результата. Создаётся, если его нет.
        inter_stimulus_interval_ms: Базовый межстимульный интервал
            в миллисекундах.
        num_repetitions: Общее количество стимулов в файле.
        syllable_wav: Путь к WAV-файлу с образцом слога. Взаимоисключающий
            параметр с ``frequencies``.
        frequencies: Частоты синусоид в герцах. Взаимоисключающий параметр
            с ``syllable_wav``. Поддерживается не более четырёх частот.
        stimulus_duration_ms: Длительность синтезируемого стимула
            в миллисекундах. Обязательна при использовании ``frequencies``.
        sample_rate: Частота дискретизации итогового файла в герцах.
        add_inv: Если ``True``, добавляет инвертированные стимулы, чередуя их
            с обычными. Инвертированные стимулы помечаются триггерами 7.
        amplitude: Амплитуда стимула в диапазоне от 0 до 1.
        percent_var_pause: Относительная вариация длительности пауз
            (от 0 до 1).
        output_name: Имя итогового файла. Если не задано, имя формируется
            автоматически из параметров генерации.

    Returns:
        Путь к созданному WAV-файлу.

    Raises:
        ValueError: Если не задан или задан одновременно источник стимула,
            отсутствует длительность синусоидального стимула либо другие
            параметры имеют недопустимые значения.
        FileNotFoundError: Если файл ``syllable_wav`` не найден.

    Example:
        '>>> create_wav(
        ...     output_dir="output",
        ...     inter_stimulus_interval_ms=100,
        ...     num_repetitions=100,
        ...     syllable_wav="da.wav",
        ...     add_inv=True,
        ... )''
        PosixPath('output/Da_Syllable_TS200.0ms_TP100.0ms_N100_INV1.wav')
    """
    if sample_rate <= 0:
        raise ValueError("sample_rate must be positive")
    if (syllable_wav is None) == (frequencies is None):
        raise ValueError("provide exactly one of syllable_wav or frequencies")

    if frequencies is not None:
        frequencies = list(frequencies)
        if not frequencies:
            raise ValueError("frequencies must not be empty")
        if any(frequency <= 0 for frequency in frequencies):
            raise ValueError("frequencies must be positive")
        if stimulus_duration_ms is None:
            raise ValueError(
                "stimulus_duration_ms is required when frequencies are provided"
            )
        ramp_window, t_stim = make_ramp_window(stimulus_duration_ms, sample_rate)
        stimulus = make_stimulus(
            sin_tone=True,
            t_stim=t_stim,
            ramp_window=ramp_window,
            frequencies=frequencies,
            amplitude=amplitude,
        )
        duration_ms = stimulus_duration_ms
    else:
        syllable, _ = read_syllable(syllable_wav, sample_rate)
        stimulus = make_stimulus(
            sin_tone=False,
            syllable=syllable,
            amplitude=amplitude,
        )
        duration_ms = stimulus.size / sample_rate * 1000

    full_signal = build_full_signal(
        stimulus=stimulus,
        inter_stimulus_interval_ms=inter_stimulus_interval_ms,
        num_repetitions=num_repetitions,
        sample_rate=sample_rate,
        add_inv=add_inv,
        percent_var_pause=percent_var_pause,
    )

    output_dir = Path(output_dir)
    file_name = _build_file_name(
        output_name=output_name,
        frequencies=frequencies,
        stimulus_duration_ms=duration_ms,
        inter_stimulus_interval_ms=inter_stimulus_interval_ms,
        num_repetitions=num_repetitions,
        add_inv=add_inv,
    )
    return save_wav(output_dir / file_name, sample_rate, full_signal)
