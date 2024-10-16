# Efficient Data Stream Anomaly Detection

## Project Overview

This project is designed to detect anomalies in a continuous data stream in real-time. It simulates a data stream, processes the data using the Exponential Weighted Moving Average (EWMA) algorithm, and visualizes both the data and detected anomalies in real-time.

### Problem Statement

- **Objective**: Detect anomalies in real-time from a continuously streaming data source.
- **Challenges**: Handling concept drift and seasonal variations in the data, optimizing for speed, and ensuring accurate detection.

---

## Objective Breakdown

### 1. Algorithm Selection

- **Chosen Algorithm**: Exponential Weighted Moving Average (EWMA).
- **Reasoning**: EWMA is well-suited for real-time data streams as it provides a way to adaptively smooth out noise and track changes in data trends. It is capable of adapting to _concept drift_ (gradual changes in the statistical properties of the data over time) due to its emphasis on recent observations.
- **Adaptability**: The algorithm uses a smoothing factor, `alpha`, to control how much weight is given to recent vs. older observations. This allows it to adapt to changes while being simple and computationally efficient.

### 2. Data Stream Simulation

- **Function**: `data_stream()`
- **Implementation**:
  - Generates a stream of floating-point numbers with a seasonal component using a sine wave.
  - Adds random noise to simulate real-world data variability.
  - Occasionally introduces spikes to emulate anomalies.
- **Outcome**: This function effectively mimics a real-time data stream that could represent various metrics like financial transactions or system logs.

### 3. Anomaly Detection

- **Mechanism**: Anomalies are detected by comparing each new data point to the EWMA.
- **Approach**:
  - Residuals (difference between the observed data point and EWMA) are calculated.
  - If the residual exceeds a pre-defined threshold, the point is flagged as an anomaly.
- **Real-time Processing**: The detection occurs as each new data point is streamed, enabling immediate identification of unusual events.

### 4. Optimization

- **Speed & Efficiency**:
  - The use of EWMA allows each new data point to be processed in constant time, `O(1)`.
  - Data processing and anomaly detection are streamlined to avoid unnecessary computations.
- **Memory Management**: Only recent data points are stored, reducing memory overhead.
- **Potential Tweaks**:
  - Adjusting the smoothing factor `alpha` to find a balance between responsiveness and stability.
  - Experimenting with different anomaly detection thresholds to minimize false positives/negatives.

### 5. Visualization

- **Tool**: Matplotlib for real-time visualization.
- **Function**: `plot_real_time()`
- **Features**:
  - Plots the data stream as it is generated, alongside the EWMA trendline.
  - Highlights detected anomalies directly on the graph.
  - Uses interactive plotting mode (`plt.ion()`) to update the plot without blocking the data stream.
- **Outcome**: A clear visual representation of the data and detected anomalies that helps in understanding the algorithm's performance. At the end of the execution, you can also collect the data from the csv file with the flagged anomalies.

---

## Project Structure
```
anomaly_detection/
├── data_stream.py              # Contains the data_stream() function for generating the simulated data stream.
├── ewma.py                     # Implements the EWMA calculation.
├── detect_anomalies.py         # Contains the function to detect anomalies based on residuals.
├── plot_data.py                # Manages real-time data visualization.
├── main.py                     # Main script to run the data streaming, anomaly detection, and visualization.
├── requirements.txt            # Lists the required Python libraries.
└── README.md                   # Project documentation.
```

## How to Run the Project

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-repo/Efficient-Data-Stream-Anomaly-Detection.git
   cd Efficient-Data-Stream-Anomaly-Detection
   ```

2. **Install Dependencies**:

   ```
   pip install -r requirements.txt
   ```

3. **Run the project**:
   ```
   python main.py
   ```

## Exponentially Weighted Moving Average (EWMA)

### Overview

The Exponentially Weighted Moving Average (EWMA) is a statistical method used to analyze time series data by smoothing out short-term fluctuations and highlighting longer-term trends. Unlike a simple moving average, where all data points are given equal weight, EWMA assigns exponentially decreasing weights to older observations. This makes it particularly sensitive to recent changes in the data, which is valuable for detecting anomalies in time series.

### How It Works

1. **Formula**

The Exponentially Weighted Moving Average (EWMA) is calculated using the formula:

$$
EWMA_t = \alpha \times X_t + (1 - \alpha) \times EWMA_{t-1}
$$

where:

- \(EWMA_t\) is the current EWMA value,
- \(X_t\) is the current data point,
- \(\alpha\) (where \(0 < \alpha \leq 1\)) is the smoothing factor that determines the weight given to the most recent observation. A higher \(\alpha\) places more emphasis on recent data.


2. **Initialization**: The EWMA starts with an initial value, which could be the first data point or a predetermined value.

3. **Adaptability**: Since EWMA uses a smoothing factor, it can adapt to changes in the underlying process, making it effective for detecting concept drift in data streams.

### Advantages

- **Sensitivity to Recent Changes**: By giving more weight to recent observations, EWMA can quickly react to changes in the data.
- **Simplicity**: The calculations are straightforward and can be implemented easily in programming languages like Python.
- **Flexibility**: Adjusting the smoothing factor allows you to control the responsiveness of the EWMA to fluctuations in the data.

### Applications

EWMA is widely used in various fields, including finance for risk management, manufacturing for process control, and data analysis for anomaly detection.

### Relevant Resources

- [Wikipedia: Exponentially Weighted Moving Average](https://en.wikipedia.org/wiki/Moving_average#Exponentially_weighted_moving_average)
- [Introduction to Exponential Smoothing](https://otexts.com/fpp3/ets.html) (Online Textbook)
- [Understanding Exponential Smoothing and Its Applications](https://www.analyticsvidhya.com/blog/2021/06/understanding-exponential-smoothing-and-its-applications/) (Analytics Vidhya)
