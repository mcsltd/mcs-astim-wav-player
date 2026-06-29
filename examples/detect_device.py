import sounddevice as sd

"""
    name: Динамики (2- MCS A-Stim R1.1 )
    index: 4
    hostapi: 0
    max_input_channels: 0
    max_output_channels: 2
    default_low_input_latency: 0.09
    default_low_output_latency: 0.09
    default_high_input_latency: 0.18
    default_high_output_latency: 0.18
    default_samplerate: 44100.0
"""

device: dict = sd.query_devices(kind="output")
for k, v in device.items():
    print(f"{k}: {v}")