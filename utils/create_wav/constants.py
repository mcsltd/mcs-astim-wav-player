"""Общие константы для генерации FFR WAV-файлов."""

from __future__ import annotations

import numpy as np

MIN_INT16 = int(np.iinfo(np.int16).min)
MAX_INT16 = int(np.iinfo(np.int16).max)

DEFAULT_SAMPLE_RATE = 44100
DEFAULT_PERCENT_VAR_PAUSE = 0.1

TRIGGER_OFFSET = 1
TRIGGER_LENGTH = 6

TRIGGER_6_LOW = (
    MAX_INT16,
    MIN_INT16,
    MIN_INT16,
    MAX_INT16,
    MIN_INT16,
    MAX_INT16,
)
TRIGGER_6_HIGH = (
    MAX_INT16,
    MIN_INT16,
    MIN_INT16,
    MAX_INT16,
    MAX_INT16,
    MIN_INT16,
)
TRIGGER_7_LOW = (
    MAX_INT16,
    MIN_INT16,
    MAX_INT16,
    MIN_INT16,
    MIN_INT16,
    MAX_INT16,
)
TRIGGER_7_HIGH = (
    MAX_INT16,
    MIN_INT16,
    MAX_INT16,
    MIN_INT16,
    MAX_INT16,
    MIN_INT16,
)
