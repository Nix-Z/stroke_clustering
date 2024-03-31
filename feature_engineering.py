import pandas as pd
import numpy as np
from datavisualization import visualize_data

def engineer_features():
    data = visualize_data()

    # Convert categorical features to numerical
    data.replace({'hypertension': {'No':0, 'Yes':1}}, inplace=True)
    data.replace({'heart_disease': {'No':0, 'Yes':1}}, inplace=True)
    data.replace({'stroke': {'No':0, 'Yes':1}}, inplace=True)
    data.replace({'gender': {'Male':0, 'Female':1}}, inplace=True)
    data.replace({'ever_married': {'No':0, 'Yes':1}}, inplace=True)
    data.replace({'work_type': {'Private':0, 'Self-employed':1, 'Govt_job':2, 'children':3, 'Never_worked':4}}, inplace=True)
    data.replace({'Residence_type': {'Urban':0, 'Rural':1}}, inplace=True)
    data.replace({'smoking_status': {'formerly smoked':0, 'never smoked':1, 'smokes':2, 'Unknown':3}}, inplace=True)

    data.to_csv('stroke_cleansed_data.csv', index=False)

    return data

engineer_features()


    
