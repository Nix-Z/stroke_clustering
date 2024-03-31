import pandas as pd

def load_data():
  data = pd.read_csv('stroke_data.csv')
  return data

load_data()
