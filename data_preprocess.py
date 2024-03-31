from data_analysis import analyze_data

def preprocess_data():
    data, categorical_features, numerical_features = analyze_data()

    data.dropna(axis=0, how='any', inplace=True) # Drop any rows with null values
    data = data.drop(data[data['gender'] == 'Other'].index) # Remove third gender type, unhelpful
    data['age'] = data['age'].astype(int) # Convert age from float to int, to prevent decimals
    data.drop(['id'], axis=1, inplace=True)

    # Convert numerical features with binary values to categorical for graphing purposes
    data.replace({'hypertension': {0:'No', 1:'Yes'}}, inplace=True)
    data.replace({'heart_disease': {0:'No', 1:'Yes'}}, inplace=True)
    data.replace({'stroke': {0:'No', 1:'Yes'}}, inplace=True)

    categorical_features = data.select_dtypes("object").columns
    numerical_features = data.select_dtypes("number").columns

    print(data.head())

    return data, categorical_features, numerical_features

preprocess_data()



    
