import pathlib
import os
import prediction_model

PACKAGE_ROOT = pathlib.Path(prediction_model.__file__).resolve().parent

DATAPATH = os.path.join(PACKAGE_ROOT, 'datasets')

TRAIN_FILE = os.path.join(DATAPATH, 'train.csv')
TEST_FILE = os.path.join(DATAPATH,'test.csv')

MODEL_NAME = 'classificaton.pkl'
SAVE_MODEL_PATH = os.path.join(PACKAGE_ROOT, 'trained_models')

TARGET = "Loan_Status"

# Final featurs used in the model
FEATURE = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
           'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
           'Loan_Amount_Term', 'Credit_History', 'Property_Area']
NUM_FEATURES = ['ApplicantIncome', 'LoanAmount', 'Loan_Amount_Term']

CAT_FEATURES = ['Gender', 'Married', 'Dependents', 'Education',
                'Self_Employed', 'Credit_History', 'Property_Area']

FEATURE_TO_ENCODE = ['Gender', 'Married', 'Dependents', 'Education',
                     'Self_Employed', 'Credit_History', 'Property_Area']

FEATURE_TO_MODIFY = ["ApplicantIncome"]
FEATURE_TO_ADD = 'CoapplicantIncome'

DROP_FEATURE = ['CoapplicantIncome']
LOG_FEATURE = ['ApplicantIncome', 'LoanAmount']
