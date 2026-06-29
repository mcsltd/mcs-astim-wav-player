import numpy as np
import sounddevice as sd
import wave

DEVICE_NAME = "Динамики (2- MCS A-Stim R1.1 )"

def read_vaw(filepath):
    with wave.open(filepath, "rb") as wav:
        n_channels = wav.getnchannels()
        samplwidth = wav.getsampwidth()
        n_frames = wav.getnframes()
        samplerate = wav.getframerate()

        frames = wav.readframes(n_frames)

        dtype = {1: np.int8, 2:np.int16, 4: np.int32}[samplwidth]
        data = np.frombuffer(frames, dtype=dtype)

        if n_channels > 1:
            data = data.reshape(-1, n_channels)

        return samplerate, data

wav_file = "../data/Da_syll_TS250.0ms_TP150.0ms_N4000_INV1_June26.wav"
samplerate, signal = read_vaw(filepath=wav_file)
device: dict = sd.query_devices(device=12)

with sd.OutputStream(samplerate=device["default_samplerate"], blocksize=0, device=12, channels=2, dtype=np.int16) as stream:
    stream.write(data=signal)