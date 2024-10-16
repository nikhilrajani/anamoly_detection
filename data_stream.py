import math
import random
import time

def data_stream():
    """
    Simulates a continuous data stream with seasonal variations, noise, and occasional anomalies.

    Uses a sine wave to model seasonal behavior and random noise to introduce variability.
    Occasionally, random spikes are added to simulate anomalies.
    """
    period = 100       # Length of the sine wave period
    amplitude = 10     # Amplitude of the sine wave
    noise_level = 2    # Range of random noise

    while True:
        # Generate a seasonal pattern using a sine wave
        base = amplitude * math.sin(time.time() * 2 * math.pi / period)

        # Add random noise to the base value
        noise = random.uniform(-noise_level, noise_level)

        # Introduce a spike anomaly with a 5% chance
        if random.random() < 0.05:
            # 5% chance of anomaly occurrence
            anomaly = random.uniform(15, 20)
            yield base + noise + anomaly
        else:
            yield base + noise

        # Simulate real-time data with a short delay
        time.sleep(0.1)
