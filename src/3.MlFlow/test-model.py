import mlflow
logged_model = 'runs:/961df40333be4dcb90d38af649b8e422/RandomForestClassifier'

# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model(logged_model)

# Predict on a Pandas DataFrame.
import pandas as pd
data = [[
    1.0,
    0.0,
    0.0,
    0.0,
    0.0,
    4.987654,
    360.0,
    1.0,2.0,
    8.696
]]
print("Prediction: ",loaded_model.predict(pd.DataFrame(data)))