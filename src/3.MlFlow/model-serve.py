import pandas as pd
import mlflow
model_name = 'Prediction_Model_RF'

# Load model as a PyFuncModel.
stage = "Production"
mlflow.set_tracking_uri("http://10.32.5.73:5002/")
loaded_model = mlflow.pyfunc.load_model(
    model_uri=f"models:/{model_name}/{stage}")

# Predict on a Pandas DataFrame.
data = [[
    1.0,
    0.0,
    0.0,
    0.0,
    0.0,
    4.987654,
    360.0,
    1.0, 2.0,
    8.696
]]
print("Prediction: ", loaded_model.predict(pd.DataFrame(data)))
