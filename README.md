
# Stock Price Forecasting

In this project, I designed and implemented a robust Stock Price Prediction and Forecasting model utilizing the Long Short-Term Memory (LSTM) architecture. The entire process, from model training to testing, was executed within a Jupyter notebook using Python.



## Features

#### Data Retrieval:
Utilizes the Yahoo Finance API to fetch historical stock data based on user input.
Supports a user-friendly interface for specifying start and end dates, as well as entering the stock ticker symbol.

#### Data Visualization:
Generates interactive charts depicting the closing price over time.
Displays additional charts with moving averages (DMA) for better trend analysis.

#### Machine Learning Model:
Implements a Long Short-Term Memory (LSTM) neural network for stock price prediction.
Trains the model on historical stock data within a Jupyter notebook.
Saves and loads the trained model for real-time predictions.

#### User Interface:
Develops a user-friendly interface using Streamlit, allowing users to interact with the application effortlessly.
Includes a sidebar for input parameters and an image for visual appeal.



## Screenshots

### Dashboard
![Screenshot (2583)](https://github.com/saumyajitpal/Stock-Price-Prediction-and-Forecasting-Model-with-LSTM-and-Streamlit-Web-Application/assets/86984943/235cadb3-60cc-49d0-86dd-465a7e3a8639)

![Screenshot (2584)](https://github.com/saumyajitpal/Stock-Price-Prediction-and-Forecasting-Model-with-LSTM-and-Streamlit-Web-Application/assets/86984943/38c89a93-2597-4cba-b136-ef31056899a8)


![Screenshot (2586)](https://github.com/saumyajitpal/Stock-Price-Prediction-and-Forecasting-Model-with-LSTM-and-Streamlit-Web-Application/assets/86984943/f3e2432e-d301-45d5-b7c4-b9b825d9740d)

![Screenshot (2585)](https://github.com/saumyajitpal/Stock-Price-Prediction-and-Forecasting-Model-with-LSTM-and-Streamlit-Web-Application/assets/86984943/ca18b3dd-109c-45c8-8105-43e3c5d71b94)


![Screenshot (2587)](https://github.com/saumyajitpal/Stock-Price-Prediction-and-Forecasting-Model-with-LSTM-and-Streamlit-Web-Application/assets/86984943/283e90ef-2ca0-4354-895a-c2ce887eda6a)



## Methodology

### Data Preprocessing:
#### Data Retrieval:
Utilized the yfinance library to fetch historical stock data from Yahoo Finance.
Captured relevant data features such as Open, High, Low, Close, and Volume.

#### Date Range Selection:
Implemented a sidebar in the Streamlit application for users to input start and end dates for the stock data.

#### User Input Handling:
Incorporated a text input field for users to enter the stock ticker symbol.
Retrieved data specific to the user-provided stock ticker symbol.

#### Data Description:
Displayed a summary table of descriptive statistics for the fetched data using the describe function.

### LSTM Model Development:

#### Data Splitting:
Divided the historical stock data into training and testing sets.

#### Data Normalization:
Utilized the MinMaxScaler from scikit-learn to scale the closing prices between 0 and 1.

#### LSTM Architecture:
Implemented a Long Short-Term Memory (LSTM) neural network for time series prediction.
Designed the model architecture with appropriate input and output layers.

#### Training:
Trained the LSTM model on the training dataset, considering a window of 100 past days for each prediction.


### Model Evaluation:
#### Performance Metrics:
Evaluated the model's performance on a separate test dataset.
Calculated Mean Squared Error (MSE) and Root Mean Squared Error (RMSE) to assess prediction accuracy.


### Web Application Development with Streamlit:
#### Streamlit Integration:
Leveraged the Streamlit library to develop a web application for stock screening and analysis.

#### User Interface Design:
Created an intuitive and visually appealing user interface with Streamlit.
Integrated a sidebar for user input, displaying the start and end date pickers and a text input for stock ticker symbols.

#### Real-time Prediction:
Incorporated a spinner to enhance user experience while the application processes data.
Enabled real-time stock price prediction and forecasting capabilities within the Streamlit application.

#### Data Visualization:
Utilized Matplotlib to generate interactive charts depicting closing prices over time.
Showcased additional charts with 50-day and 200-day Moving Averages for comprehensive trend analysis.
