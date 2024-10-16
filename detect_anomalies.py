import numpy as np

def is_anomaly(data_point, ewma, residuals, threshold=2.5):
    """
    Checks if the current data point is an anomaly based on the deviation from the EWMA.

    :param data_point: The current data point from the stream.
    :param ewma: The current EWMA value.
    :param residuals: List of past residuals for calculating standard deviation.
    :param threshold: Multiplier for the standard deviation to define the anomaly threshold.
    :return: Tuple (bool, updated residuals). True if an anomaly, and the updated residuals list.
    """
    residual = abs(data_point - ewma)
    residuals.append(residual)
    
    # Calculate the standard deviation of the residuals for the threshold
    std_dev = np.std(residuals) if len(residuals) > 1 else 1.0  # Avoid division by zero

    # Determine if the current point is an anomaly
    is_anomaly = residual > threshold * std_dev
    
    # Keep only the latest 100 residuals for efficiency
    if len(residuals) > 100:
        residuals.pop(0)
    
    return is_anomaly, residuals
