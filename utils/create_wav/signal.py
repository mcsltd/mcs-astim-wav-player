"""Сборка полного сигнала из повторяющихся стимулов и пауз."""

from __future__ import annotations

import random

import numpy as np

from .constants import DEFAULT_PERCENT_VAR_PAUSE
from .pauses import pause_samples
from .triggers import add_triggers


def build_full_signal(
    stimulus: np.ndarray,
    inter_stimulus_interval_ms: float,
    num_repetitions: int,
    sample_rate: int,
    add_inv: bool = False,
    percent_var_pause: float = DEFAULT_PERCENT_VAR_PAUSE,
) -> np.ndarray:
    """Собирает полный стереосигнал из стимулов и пауз.

    Стимулы перемешиваются случайным образом. Если ``add_inv`` равно ``True``,
    стимулы чередуются с инвертированными, которые помечаются триггерами 7.

    Args:
        stimulus: Монофонический стимул в диапазоне от -1 до 1.
        inter_stimulus_interval_ms: Базовый межстимульный интервал
            в миллисекундах.
        num_repetitions: Общее количество стимулов в файле.
        sample_rate: Частота дискретизации в герцах.
        add_inv: Добавлять ли инвертированные стимулы.
        percent_var_pause: Относительная вариация длительности пауз
            (от 0 до 1).

    Returns:
        Двухканальный массив ``int16`` формы ``(n_samples, 2)``.

    Raises:
        ValueError: Если количество повторений меньше единицы или параметры
            стимула некорректны.
    """
    if num_repetitions < 1:
        raise ValueError("num_repetitions must be at least 1")

    stimulus = np.asarray(stimulus, dtype=np.float64)
    if stimulus.ndim != 1:
        raise ValueError("stimulus must be a one-dimensional array")

    stimuli = []
    for index in range(num_repetitions):
        inv = add_inv and index % 2 == 1
        current = -stimulus if inv else stimulus
        stimuli.append(add_triggers(current, inv))

    random.shuffle(stimuli)

    chunks = []
    for current in stimuli:
        chunks.append(current)
        n_pause = pause_samples(
            inter_stimulus_interval_ms,
            sample_rate,
            percent_var_pause,
        )
        chunks.append(np.zeros((n_pause, 2), dtype=np.int16))

    return np.concatenate(chunks, axis=0)
