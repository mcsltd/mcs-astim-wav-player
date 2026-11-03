"""Расчёт длительности пауз между стимулами."""

from __future__ import annotations

import random

from .constants import DEFAULT_PERCENT_VAR_PAUSE


def pause_samples(
    inter_stimulus_interval_ms: float,
    sample_rate: int,
    percent_var_pause: float = DEFAULT_PERCENT_VAR_PAUSE,
) -> int:
    """Возвращает длину случайной паузы в отсчётах.

    Длительность паузы равномерно варьируется вокруг
    ``inter_stimulus_interval_ms`` на ``±percent_var_pause``.

    Args:
        inter_stimulus_interval_ms: Базовый межстимульный интервал
            в миллисекундах.
        sample_rate: Частота дискретизации в герцах.
        percent_var_pause: Относительная вариация паузы (от 0 до 1).

    Returns:
        Количество отсчётов паузы.

    Raises:
        ValueError: Если интервал отрицателен, частота дискретизации
            не положительна или вариация выходит за диапазон.
    """
    if inter_stimulus_interval_ms < 0:
        raise ValueError("inter_stimulus_interval_ms must not be negative")
    if sample_rate <= 0:
        raise ValueError("sample_rate must be positive")
    if not 0 <= percent_var_pause < 1:
        raise ValueError("percent_var_pause must be in the range [0, 1)")

    variation = random.uniform(-percent_var_pause, percent_var_pause)
    pause_ms = inter_stimulus_interval_ms * (1 + variation)
    return max(0, int(round(sample_rate * pause_ms / 1000)))
