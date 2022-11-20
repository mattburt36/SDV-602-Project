"""
Data Source controller module
"""
import sys
import pandas as pd
sys.dont_write_bytecode = True

data = pd.read_csv("data/wfp_food_prices_ukr.csv") 