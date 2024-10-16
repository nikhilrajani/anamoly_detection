def update_ewma(previous_ewma, new_data_point, alpha=0.3):
    """
    Update the EWMA with the new data point.

    :param previous_ewma: The previous EWMA value.
    :param new_data_point: The new incoming data point.
    :param alpha: Smoothing factor between 0 and 1 (higher values react faster to changes).
    :return: Updated EWMA value.
    """
    return alpha * new_data_point + (1 - alpha) * previous_ewma
