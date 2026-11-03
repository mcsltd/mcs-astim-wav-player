"""Формирование одного стимула и огибающей."""

from __future__ import annotations

from collections.abc import Sequence

import numpy as np

SINE_AMPLITUDE_FACTORS = (1.0, 0.7, 0.5, 0.3)


def make_ramp_window(
    stimulus_duration_ms: float,
    sample_rate: int,
    rate: float = 0.1,
    growth_rate: float = 3.0,
) -> tuple[np.ndarray, np.ndarray]:
    """Создаёт временную ось и окно с экспоненциальным нарастанием и спадом.

    Args:
        stimulus_duration_ms: Длительность стимула в миллисекундах.
        sample_rate: Частота дискретизации в герцах.
        rate: Доля длительности стимула, отводимая на нарастание и спад
            (от 0 до 0.5).
        growth_rate: Коэффициент крутизны экспоненциального окна.

    Returns:
        Кортеж ``(ramp_window, t_stim)``, где ``ramp_window`` — окно
        амплитуды, а ``t_stim`` — временная ось в секундах.

    Raises:
        ValueError: Если длительность не положительна, частота дискретизации
            не положительна или ``rate`` выходит за допустимый диапазон.
    """
    if stimulus_duration_ms <= 0:
        raise ValueError("stimulus_duration_ms must be positive")
    if sample_rate <= 0:
        raise ValueError("sample_rate must be positive")
    if not 0 < rate <= 0.5:
        raise ValueError("rate must be in the range (0, 0.5]")

    stimulus_duration_s = stimulus_duration_ms / 1000
    n_samples = max(1, int(round(sample_rate * stimulus_duration_s)))
    t_stim = np.arange(n_samples, dtype=np.float64) / sample_rate

    ramp_duration_samples = max(1, int(round(n_samples * rate)))
    ramp_window = np.ones(n_samples, dtype=np.float64)

    x = np.linspace(0, 1, ramp_duration_samples)
    exp_ramp = (np.exp(growth_rate * x) - 1) / (np.exp(growth_rate) - 1)
    ramp_window[:ramp_duration_samples] = exp_ramp

    x = np.linspace(0, 1, ramp_duration_samples)
    exp_decay = (np.exp(growth_rate * (1 - x)) - 1) / (np.exp(growth_rate) - 1)
    ramp_window[-ramp_duration_samples:] = exp_decay

    return ramp_window, t_stim


def make_stimulus(
    sin_tone: bool,
    t_stim: np.ndarray | None = None,
    syllable: np.ndarray | None = None,
    ramp_window: np.ndarray | None = None,
    frequencies: Sequence[float] | None = None,
    amplitude: float = 1.0,
) -> np.ndarray:
    """Создаёт монофонический стимул из слога или суммы синусоид.

    Args:
        sin_tone: Если ``True``, стимул синтезируется из синусоид, иначе
            используется готовый слог.
        t_stim: Временная ось стимула в секундах. Обязательна, если
            ``sin_tone`` равно ``True``.
        syllable: Массив отсчётов слога в диапазоне от -1 до 1. Обязателен,
            если ``sin_tone`` равно ``False``.
        ramp_window: Огибающая для синусоидального стимула. Обязательна,
            если ``sin_tone`` равно ``True``.
        frequencies: Частоты синусоид в герцах. Обязательны, если ``sin_tone``
            равно ``True``. Используется не более четырёх частот.
        amplitude: Итоговая амплитуда стимула в диапазоне от 0 до 1.

    Returns:
        Монофонический стимул в виде массива ``float64`` в диапазоне от -1 до 1.

    Raises:
        ValueError: Если переданы некорректные или неполные параметры.
    """
    if not 0 < amplitude <= 1:
        raise ValueError("amplitude must be in the range (0, 1]")

    if sin_tone:
        if t_stim is None:
            raise ValueError("t_stim is required for a sine stimulus")
        if ramp_window is None:
            raise ValueError("ramp_window is required for a sine stimulus")
        if not frequencies:
            raise ValueError("frequencies are required for a sine stimulus")
        if len(frequencies) > len(SINE_AMPLITUDE_FACTORS):
            raise ValueError(
                f"at most {len(SINE_AMPLITUDE_FACTORS)} frequencies are supported"
            )

        sinus = np.zeros_like(t_stim, dtype=np.float64)
        for factor, frequency in zip(SINE_AMPLITUDE_FACTORS, frequencies):
            sinus += factor * ramp_window * np.sin(2 * np.pi * frequency * t_stim)

        peak = np.max(np.abs(sinus))
        if peak == 0:
            raise ValueError("the sine stimulus has zero amplitude")
        sinus /= peak
        return amplitude * sinus

    if syllable is None:
        raise ValueError("syllable is required when sin_tone is False")

    return amplitude * np.asarray(syllable, dtype=np.float64)
