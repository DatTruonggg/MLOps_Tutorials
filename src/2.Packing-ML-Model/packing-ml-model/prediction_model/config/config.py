import pathlib
import os
import prediction_model

PACKAGE_ROOT = pathlib.Path(prediction_model.__file__).resolve().parent

DATAPATH = os.path.join(PACKAGE_ROOT, 'datasets')
TRAIN_FILE = 'train.csv'
TEST_FILE = 'test.csv'

SAVE_MODEL_PATH = os.path.join(PACKAGE_ROOT, 'trained_models')

TARGET = ["Loan_Status"]

# Final featurs used in the model
FEATURE = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
           'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
           'Loan_Amount_Term', 'Credit_History', 'Property_Area']
NUM_FEATURES = ['ApplicantIncome', 'LoanAmount', 'Loan_Amount_Term']
