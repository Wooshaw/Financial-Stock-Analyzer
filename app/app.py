# Goal: Automating the process of performing a financial analysis and getting information on investments
# Ultimate Goal: Understand companies and perform competitor analysis

# Important Libararies to Import

from shiny import(
    App, ui, render, reactive, Session, req
)

from shinywidgets import (
    output_widget, render_widget
) 

import numpy as np 
import pandas as pd
import yfinance as yf 
import datetime as dt 
import plotly.express as px
import plotly.graph_objects as go 
from pathlib import Path

# Default App Inputs 
Title = "Financial Stock Analyzer"



# Data input

symbol = 'MSFT'
period = '5y'
window_mavg_short = 30
window_mavg_long = 90

# Get Stock Data

stock = yf.Ticker(symbol)

stock_info = stock.info
stock_history = stock.history(period=period)

# Exploratory Data Analysis

# Meta Data of the stock
stock_info.keys()

# General Information
stock_info['industry']
stock_info['fullTimeEmployees']
stock_info['website']

# Financial Informations
stock_info['profitMargins']
stock_info['revenueGrowth']
stock_info['currentRatio']
stock_info['totalRevenue']
stock_info['ebitda']
stock_info['operatingCashflow']

# Stock Income Statement
stock_incomestmt = stock.incomestmt

# Stock History
stock_history.reset_index().info()

# Data Transformation
stock_df = stock_history[['Close']].reset_index()

stock_df['mavg_short'] = stock_df[['Close']].rolling(window=window_mavg_short).mean()
stock_df['mavg_long'] = stock_df[['Close']].rolling(window=window_mavg_long).mean()

# Data Visualization 

fig = px.line(
    data_frame=stock_df.set_index('Date'),
    color_discrete_map={
        "Close": "#2C3E50",
        "mavg_short": "#E31A1C",
        "mavg_long": "#18BC9C"
    },
    title = "Stock Chart"
)

fig = fig.update_layout(
    plot_bgcolor = 'rgba(0,0,0,0)',
    paper_bgcolor = 'rgba(0,0,0,0)',
    legend_title_text = ''
)

fig = fig.update_yaxes(
    title = "Share Price",
    tickprefix="$",
    gridcolor = '#2c3e50'
)

fig = fig.update_xaxes(
    title = "",
    gridcolor = '#2c3e50'
)

fig
