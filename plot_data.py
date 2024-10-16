import matplotlib.pyplot as plt

def plot_real_time(data, ewma_values, anomalies):
    """
    Plots the data stream, EWMA, and detected anomalies in real-time.
    
    :param data: List of data points.
    :param ewma_values: List of EWMA values.
    :param anomalies: Boolean list indicating which points are anomalies.
    """
    plt.clf()  # Clear the plot for real-time updates
    plt.plot(data, label='Data Stream', color='blue', alpha=0.6)
    plt.plot(ewma_values, label='EWMA', color='orange', linewidth=2)
    plt.scatter(
        [i for i, anomaly in enumerate(anomalies) if anomaly],
        [data[i] for i, anomaly in enumerate(anomalies) if anomaly],
        color='red', label='Anomalies', marker='x'
    )
    plt.title('Real-time Data Stream with EWMA and Detected Anomalies')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.pause(0.1)  # Pause to allow real-time update
