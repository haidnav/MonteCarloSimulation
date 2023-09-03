# Monte Carlo Simulation: Asset Price Prediction

![Demo Monte Carlo Simulated graph](https://github.com/haidnav/MonteCarloSimulation/blob/main/demo.png)

## Overview
This project is a Monte Carlo simulation tool that predicts future asset prices using a simplified version of the geometric Brownian motion model. It's designed to provide a practical demonstration of the Monte Carlo method and its application in financial modeling.

The app allows users to input various parameters such as the initial asset price, annualized rate of return, annualized volatility, time horizon, number of time steps, and the number of simulations. After inputting these parameters, users can visualize the simulated asset price paths and export the results to a CSV file.

## Features
**Real-Time Simulation:** The app provides real-time updates of the asset price simulation as users adjust input parameters, allowing for interactive exploration.

**Interactive Visualization:** Users can visualize multiple asset price paths to gain insights into potential future outcomes.

**CSV Export:** Simulated asset prices can be exported to a CSV file for further analysis or record-keeping.

**Error Handling:** Input validation and error handling ensure that user inputs are within reasonable ranges and formats.

## Usage
Install the required dependencies using **pip install -r requirements.txt**.

Run the app with Streamlit using **streamlit run app.py**.

Enter the desired input parameters and observe the real-time asset price simulation.

Click the "Export to CSV" button to save the simulated asset prices to a CSV file.

Dependencies
**Streamlit**
**NumPy**
**Matplotlib**
**Pandas**
Credits
This app was created by Haider Naveed. You can find the source code and additional projects on  my GitHub profile.

License
This project is open-source and available under the MIT License.

