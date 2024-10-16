# from data_stream import data_stream
# from ewma import update_ewma
# from detect_anomalies import is_anomaly
# from plot_data import plot_real_time
# import matplotlib.pyplot as plt

# def main():
#     """
#     Main function to simulate the data stream, compute EWMA, detect anomalies in real-time, and visualize results.
#     """
#     data_gen = data_stream()
#     data = []
#     ewma_values = []
#     anomalies = []
#     residuals = []
    
#     alpha = 0.3  # Smoothing factor for EWMA
#     threshold = 2.5  # Threshold for detecting anomalies
    
#     previous_ewma = None
    
#     try:
#         plt.ion()  # Enable interactive mode for real-time plotting
#         while True:
#             # Get the next data point from the stream
#             new_data_point = next(data_gen)
#             data.append(new_data_point)
            
#             # Initialize EWMA with the first data point
#             if previous_ewma is None:
#                 previous_ewma = new_data_point
            
#             # Update EWMA with the new data point
#             ewma = update_ewma(previous_ewma, new_data_point, alpha)
#             ewma_values.append(ewma)
#             previous_ewma = ewma
            
#             # Check if the current data point is an anomaly
#             anomaly, residuals = is_anomaly(new_data_point, ewma, residuals, threshold)
#             anomalies.append(anomaly)
            
#             # Visualize the data in real-time
#             plot_real_time(data, ewma_values, anomalies)

#             # Break the loop if the plot window is closed by the user
#             if not plt.fignum_exists(1):
#                 break
    
#     except KeyboardInterrupt:
#         print("\nReal-time data stream interrupted by user.")
    
#     finally:
#         plt.ioff()  # Disable interactive mode
#         plt.show()  # Ensure the final state of the plot is displayed

# if __name__ == "__main__":
#     main()


from data_stream import data_stream
from ewma import update_ewma
from detect_anomalies import is_anomaly
from plot_data import plot_real_time
import matplotlib.pyplot as plt
import pandas as pd  # Import pandas for CSV handling

def main():
    """
    Main function to simulate the data stream, compute EWMA, detect anomalies in real-time, and visualize results.
    """
    data_gen = data_stream()
    data = []  # List to store data points
    ewma_values = []  # List to store EWMA values
    anomalies = []  # List to store anomaly flags
    residuals = []  # List to store residuals for anomaly detection
    
    alpha = 0.3  # Smoothing factor for EWMA
    threshold = 2.5  # Threshold for detecting anomalies
    
    previous_ewma = None  # Variable to hold the previous EWMA value
    
    # List to store records for CSV output
    records = []

    try:
        plt.ion()  # Enable interactive mode for real-time plotting
        while True:
            # Get the next data point from the stream
            new_data_point = next(data_gen)
            data.append(new_data_point)
            
            # Initialize EWMA with the first data point
            if previous_ewma is None:
                previous_ewma = new_data_point
            
            # Update EWMA with the new data point
            ewma = update_ewma(previous_ewma, new_data_point, alpha)
            ewma_values.append(ewma)
            previous_ewma = ewma
            
            # Check if the current data point is an anomaly
            anomaly, residuals = is_anomaly(new_data_point, ewma, residuals, threshold)
            anomalies.append(anomaly)
            
            # Store the data point and its anomaly status for CSV output
            records.append({'Value': new_data_point, 'Anomaly': anomaly})

            # Visualize the data in real-time
            plot_real_time(data, ewma_values, anomalies)

            # Break the loop if the plot window is closed by the user
            if not plt.fignum_exists(1):
                break
    
    except KeyboardInterrupt:
        print("\nReal-time data stream interrupted by user.")
    
    finally:
        plt.ioff()  # Disable interactive mode
        plt.show()  # Ensure the final state of the plot is displayed

        # Create a DataFrame and save to CSV
        df = pd.DataFrame(records)
        csv_file_path = "anomaly_detection_results.csv"
        df.to_csv(csv_file_path, index=False)
        print(f"Data recorded. You can download the results from {csv_file_path}.")

if __name__ == "__main__":
    main()
