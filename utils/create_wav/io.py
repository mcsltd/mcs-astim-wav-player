"""Чтение слогов и сохранение готовых WAV-файлов."""

from __future__ import annotations

from math import gcd
from pathlib import Path

import numpy as np
from scipy.io import wavfile
from scipy.signal import resample_poly


def _to_float_signal(data: np.ndarray) -> np.ndarray:
    if np.issubdtype(data.dtype, np.unsignedinteger):
        info = np.iinfo(data.dtype)
        midpoint = (int(info.max) + 1) / 2
        signal = (data.astype(np.float64) - midpoint) / midpoint
    elif np.issubdtype(data.dtype, np.signedinteger):
        info = np.iinfo(data.dtype)
        scale = max(abs(int(info.min)), int(info.max))
        signal = data.astype(np.float64) / scale
    else:
        signal = data.astype(np.float64)
    return np.clip(signal, -1.0, 1.0)


def read_syllable(
    path: str | Path,
    target_sample_rate: int | None = None,
) -> tuple[np.ndarray, int]:
    """Читает WAV-файл со слогом и приводит его к нужной частоте.

    Многоканальный файл сводится к первому каналу. Целочисленные отсчёты
    нормализуются в диапазон от -1 до 1. При необходимости выполняется
    передискретизация.

    Args:
        path: Путь к WAV-файлу со слогом.
        target_sample_rate: Требуемая частота дискретизации в герцах.
            Если ``None``, используется частота из файла.

    Returns:
        Кортеж ``(signal, sample_rate)`` с нормализованным монофоническим
        сигналом и итоговой частотой дискретизации.

    Raises:
        FileNotFoundError: Если файл не найден.
        ValueError: Если WAV-файл пуст или частота дискретизации некорректна.
    """
    path = Path(path)
    if not path.is_file():
        raise FileNotFoundError(f"WAV file not found: {path}")

    file_sample_rate, data = wavfile.read(path)
    if data.size == 0:
        raise ValueError(f"WAV file is empty: {path}")
    if file_sample_rate <= 0:
        raise ValueError(f"invalid sample rate in WAV file: {file_sample_rate}")

    if data.ndim > 1:
        data = data[:, 0]

    signal = _to_float_signal(data)

    if target_sample_rate is None or target_sample_rate == file_sample_rate:
        return signal, file_sample_rate

    if target_sample_rate <= 0:
        raise ValueError("target_sample_rate must be positive")

    divisor = gcd(file_sample_rate, target_sample_rate)
    signal = resample_poly(
        signal,
        target_sample_rate // divisor,
        file_sample_rate // divisor,
    )
    return np.clip(signal, -1.0, 1.0), target_sample_rate


def save_wav(
    path: str | Path,
    sample_rate: int,
    signal: np.ndarray,
) -> Path:
    """Сохраняет готовый сигнал в WAV-файл.

    Args:
        path: Путь к создаваемому WAV-файлу.
        sample_rate: Частота дискретизации в герцах.
        signal: Двухканальный или монофонический массив ``int16``.

    Returns:
        Путь к сохранённому файлу.

    Raises:
        ValueError: Если сигнал пуст или имеет неверный тип.
    """
    path = Path(path)
    values = np.asarray(signal)
    if values.size == 0:
        raise ValueError("signal must not be empty")
    if values.dtype != np.int16:
        raise ValueError("signal must have int16 dtype")

    path.parent.mkdir(parents=True, exist_ok=True)
    wavfile.write(path, sample_rate, values)
    return path
