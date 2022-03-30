import datetime as dt
import matplotlib.pyplot as plt
import pandas_datareader as pdr
import streamlit as st

"""To run this in stremlit:
1. open a terminal or command line interface
2. enter streamlit run [filename]
"""

# sidebar
def user_inputs():
    st.sidebar.header("User Inputs")
    symbol = st.sidebar.text_input("Enter Symbol", "AMZN")
    start = dt.date.today() - dt.timedelta(days=365)
    start_date = st.sidebar.date_input("Enter Start Date", start)
    end_date = st.sidebar.date_input("Enter End Date", dt.date.today())
    button = st.sidebar.button("Click here!")
    return symbol, start_date, end_date, button

def get_data(symbol, start, end):
    data = pdr.get_data_yahoo(symbol, start, end)
    return data

def plot(symbol, start, end):
    data = get_data(symbol, start, end)
    fig, ax = plt.subplots(figsize=(10,4))
    ax = plt.plot(data['Close'])
    st.write(fig)

# main
def main():
    symbol, start, end, button = user_inputs()
    st.write(f"### Closing prices for {symbol} from {start} to {end}")

    if button:
        data = get_data(symbol, start, end)
        plot(symbol, start,end)
        #st.line_chart(data['Close'])


if __name__ == "__main__":
    main()





