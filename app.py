# Import necessary libraries
import streamlit as st
import pandas as pd
import os
import json

# Function to load balance sheet data
def load_balance_sheet_data(stock_symbol):
    data_folder = 'data'
    file_path = os.path.join(data_folder, f'{stock_symbol}_balance_sheet.json')
    
    if os.path.exists(file_path):
        with open(file_path, 'r') as json_file:
            balance_sheet_data = json.load(json_file)
        return balance_sheet_data
    else:
        return None

# Streamlit app
def main():
    st.title('Stock Balance Sheet Viewer')

    # User input for stock symbol
    stock_symbol = st.text_input('Enter Stock Symbol (e.g., AAPL):')

    if stock_symbol:
        # Load balance sheet data
        balance_sheet_data = load_balance_sheet_data(stock_symbol)

        if balance_sheet_data is not None:
            # Convert JSON data to DataFrame
            df = pd.json_normalize(balance_sheet_data)
            
            # Display the balance sheet data
            st.subheader(f'Balance Sheet Data for {stock_symbol}')
            st.dataframe(df)

        else:
            st.warning(f'No data found for {stock_symbol}. Please check the stock symbol.')

if __name__ == '__main__':
    main()
