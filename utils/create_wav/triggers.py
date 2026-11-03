"""Добавление триггерных команд в правый канал стимула."""

from __future__ import annotations

import numpy as np

from .constants import (
    MAX_INT16,
    TRIGGER_6_HIGH,
    TRIGGER_6_LOW,
    TRIGGER_7_HIGH,
    TRIGGER_7_LOW,
    TRIGGER_LENGTH,
    TRIGGER_OFFSET,
)

_TRIGGER_START = {
    False: TRIGGER_6_LOW,
    True: TRIGGER_7_LOW,
}
_TRIGGER_END = {
    False: TRIGGER_6_HIGH,
    True: TRIGGER_7_HIGH,
}


def to_int16(signal: np.ndarray) -> np.ndarray:
    """Преобразует сигнал из диапазона [-1, 1] в ``int16``.

    Args:
        signal: Монофонический сигнал в диапазоне от -1 до 1.

    Returns:
        Массив ``int16`` с клиппированием значений.

    Raises:
        ValueError: Если массив содержит нечисловые значения.
    """
    values = np.asarray(signal, dtype=np.float64)
    if not np.all(np.isfinite(values)):
        raise ValueError("signal contains non-finite values")
    return np.rint(np.clip(values, -1.0, 1.0) * MAX_INT16).astype(np.int16)


def add_triggers(stimulus: np.ndarray, inv: bool) -> np.ndarray:
    """Формирует стереосигнал с триггерами начала и конца стимула.

    Левый канал содержит стимул, правый канал содержит 3-битные команды
    AStimWavPatcher. Для обычного стимула используются команды 100 и 101,
    для инвертированного — 110 и 111.

    Args:
        stimulus: Монофонический стимул в диапазоне от -1 до 1.
        inv: Признак инвертированного стимула.

    Returns:
        Двухканальный массив ``int16`` формы ``(n_samples, 2)``.

    Raises:
        ValueError: Если стимул слишком короткий для размещения триггеров.
    """
    left = to_int16(stimulus)
    min_length = TRIGGER_OFFSET + 2 * TRIGGER_LENGTH
    if left.size < min_length:
        raise ValueError(
            f"stimulus must contain at least {min_length} samples"
        )

    right = np.zeros(left.size, dtype=np.int16)
    start = _TRIGGER_START[inv]
    end = _TRIGGER_END[inv]

    right[TRIGGER_OFFSET : TRIGGER_OFFSET + TRIGGER_LENGTH] = start
    right[-TRIGGER_LENGTH:] = end

    return np.column_stack((left, right))
