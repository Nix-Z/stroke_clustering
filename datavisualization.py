import pandas as pd
import numpy as np
import plotly.express as px
import plotly.figure_factory as ff
from data_preprocess import preprocess_data

def visualize_data():
    data, categorical_features, numerical_features = preprocess_data()

    # Create correlation plot for numerical features
    corr_data_num = data[numerical_features].corr()
    fig = px.imshow(corr_data_num, labels=dict(color="Correlation"), x=corr_data_num.columns, y=corr_data_num.index, text_auto=True)
    #fig.show()
    fig.write_image('fig_corrplot.jpg')

    # Create distribution plots for each numerical feature
    for numerical_feature in numerical_features:
        fig = ff.create_distplot(hist_data=[data[numerical_feature]], group_labels=[numerical_feature], show_rug=False)
        fig.update_layout(showlegend=False)
        fig.update_xaxes(title_text=numerical_feature, showgrid=False)
        fig.update_yaxes(title_text="Probability Density", showgrid=False)
        #fig.show()
        fig.write_image(f'fig_distplot_{numerical_feature}.jpg')
    
    # Create boxplots for each numerical feature
    for numerical_feature in numerical_features:
        fig = px.box(data, y=numerical_feature)
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        #fig.show()
        fig.write_image(f'fig_boxplot_{numerical_feature}.jpg')

    # Create histogram for each categorical feature
    for categorical_feature in categorical_features:
        fig = px.histogram(data, x=categorical_feature)
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        #fig.show()
        fig.write_image(f'fig_histplot_{categorical_feature}.jpg')
    
    return data

visualize_data()
