import logging
import re
from typing import Iterable

import sounddevice as sd

from PySide6.QtCore import QObject, Signal
from PySide6.QtMultimedia import QMediaDevices

logger = logging.getLogger(__name__)


def normalize_name(name: str) -> str:
    return re.sub(r"\s+", " ", name).strip().casefold()


def is_same_device(name: str, device_name: str) -> bool:
    return normalize_name(device_name) in normalize_name(name)


def refresh_portaudio() -> bool:
    try:
        sd._terminate()
        sd._initialize()
        logger.debug("PortAudio reinitialized")
        return True
    except Exception:
        logger.exception("failed to reinitialize PortAudio")
        return False


def query_wasapi_output_devices() -> list[dict]:
    try:
        hostapis = sd.query_hostapis()
        wasapi_indexes = {
            idx for idx, api in enumerate(hostapis)
            if "WASAPI" in api["name"]
        }
        devices = sd.query_devices()
    except Exception:
        logger.exception("failed to query audio devices")
        return []

    result = []
    for device in devices:
        if device["max_output_channels"] <= 0:
            continue
        if wasapi_indexes and device["hostapi"] not in wasapi_indexes:
            continue
        result.append(device)
    return result


def find_astim_device(devices: Iterable[dict], device_name: str) -> dict | None:
    for device in devices:
        if is_same_device(device["name"], device_name):
            return device
    return None


class DeviceMonitor(QObject):
    connection_changed = Signal(bool)
    devices_changed = Signal()

    def __init__(self, device_name: str, parent=None):
        super().__init__(parent)
        self._device_name = device_name
        self._connected = self._detect()

        self._media_devices = QMediaDevices(self)
        self._media_devices.audioOutputsChanged.connect(
            self._on_audio_outputs_changed
        )

    @property
    def connected(self) -> bool:
        return self._connected

    def _detect(self) -> bool:
        try:
            outputs = QMediaDevices.audioOutputs()
        except Exception:
            logger.exception("failed to query multimedia audio outputs")
            return False

        connected = any(
            is_same_device(device.description(), self._device_name)
            for device in outputs
        )
        logger.debug(f"A-Stim connected: {connected}")
        return connected

    def _on_audio_outputs_changed(self):
        connected = self._detect()
        self.devices_changed.emit()

        if connected != self._connected:
            self._connected = connected
            state = "connected" if connected else "disconnected"
            logger.info(f"A-Stim {state}")
            self.connection_changed.emit(connected)
