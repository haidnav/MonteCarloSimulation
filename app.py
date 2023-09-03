import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from simulation import run_sim
import pandas as pd


def main():
    st.title('Monte Carlo Simulation: Asset Price Prediction')
    st.markdown('Welcome to my Streamlit Monte Carlo Asset Price Prediction model, this uses a simplified version of the geometric Brownian motion model to simulate future asset prices.')
    st.markdown('''The formula i have used is as follows
                **S_t = S_(t-1) * e^(drift + diffusion)**''')
    st.markdown('''
**S_t**: This represents the asset price at the current time step (t).

**S_{t-1}**: This represents the asset price at the previous time step (t-1).

**e**: This is the mathematical constant known as Euler's number, approximately equal to 2.71828. It's raised to the power of (drift + diffusion).

**drift**: This is a term that represents the expected average change in the asset price. It's calculated using the annualized rate of return (mu) and the annualized volatility (sigma) of the asset.

**diffusion**: This term adds randomness to the model. It's calculated using random numbers drawn from a normal distribution, which simulate the randomness and volatility in real-world markets.

So, the formula calculates the future asset price by taking the previous asset price, adjusting it with the expected average change (drift), and then adding the random fluctuation (diffusion) to simulate the uncertainty and variability in the asset's price movement over time.
''')
    st.markdown('Created by **Haider Naveed**')
    st.markdown('https://github.com/haidnav')
    # gather user inputs
    s0 = st.number_input('Initial Asset Price', min_value=0.0)
    mu = st.number_input('Annualised Rate of Return', min_value=0.0)
    st.markdown(
        f'<span style="color: green;">You have set the Annualised Rate of Return to: {mu*100:.2f}%</span>',
        unsafe_allow_html=True)
    sigma = st.number_input('Annualised Volatility', min_value=0.0)
    time = st.number_input('Time Horizon in Years', min_value=0.0)
    n_steps = st.slider('Number of Time Steps', min_value=1,
                        max_value=1000, value=252)
    n_simulations = st.slider('Number of Simulations',
                              min_value=1, max_value=50, value=5)

    # run simulation and generate plot
    # if st.button('Run Simulation'):
    asset_paths = run_sim(s0, mu, sigma, time, n_steps, n_simulations)

    # plot simulated asset prices
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(asset_paths)
    ax.set_xlabel('Time Steps')
    ax.set_ylabel('Asset Price')
    ax.set_title('Monte Carlo Simulation: Asset Price Paths')
    st.pyplot(fig)

    def export_to_csv(asset_paths):
        df = pd.DataFrame(asset_paths, columns=[
            f'Simulation {i+1}' for i in range(n_simulations)])
        csv_data = df.to_csv(index=False)

        # Create a download button
        st.download_button(
            label="Download Data",
            data=csv_data.encode(),
            file_name='simulated_asset_prices.csv',
            key='csv_export_button'  # Optional key to track the button
        )

    if st.button('Export to CSV'):
        export_to_csv(asset_paths)


if __name__ == '__main__':
    main()
