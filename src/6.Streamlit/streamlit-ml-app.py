import joblib 
import streamlit as st
import numpy as np

model_name = "RF_Loan_model.joblib"
model = joblib.load(model_name)


def prediction(Gender, Married, Dependents, Education, Employed,
                            ApplicantIncome, CoapplicantIncome, LoanAmount,
                            Loan_Amount_Term, Credit_History, PropertyArea):
    if Gender =="Male":
        Gender = 1 
    else: 
        Gender = 0
    
    if Married == "Yes":
        Married = 1
    else:
        Married = 0

    if Education == "Graduate":
        Education = 1
    else:
        Education = 0

    if Employed == "Yes":
        Employed = 1
    else:
        Employed = 0
    
    if Credit_History == "Outstanding Loan":
        Credit_History = 1
    else:
        Credit_History = 0
        
    if PropertyArea == "Rural":
        PropertyArea = 1
    elif PropertyArea == "Urban":
        PropertyArea = 1 
    else:
        PropertyArea = 2

    Total_Income = np.log(ApplicantIncome + CoapplicantIncome)
    prediction = model.predict([[Gender, Married, Dependents, Education, 
                                 Employed, LoanAmount, Loan_Amount_Term, Credit_History, 
                                 PropertyArea,Total_Income]])
    print(prediction)
    if prediction == 0:
        pred = "Rejected"
    else: 
        pred = "Approved"

    return pred


def main():
    # front end
    st.title("Welcome to Loan Application")
    st.header("Please enter your details to proceed with your application")
    Gender = st.selectbox("Your gender",("Male","Female"))
    Married = st.selectbox("Married",("Yes","No"))
    Dependents = st.number_input("Number of dependents")
    Education = st.selectbox("Education", ("Graduate", "Not graduate"))
    Employed = st.selectbox("Self Employed", ("Yes", "No"))
    ApplicantIncome = st.number_input("Applicant Income")
    CoapplicantIncome = st.number_input("Coapplicant Income")
    LoanAmount = st.number_input("Loan Amount")
    Loan_Amount_Term = st.number_input("Loan Amount Term")
    Credit_History = st.checkbox("Credit History", ("Outstanding Loan", "No Outstanding Loan"))
    PropertyArea = st.selectbox("Property Area", ("Rural", "Urban", "Semi-Urban"))
    
    if st.button("Predict"):
        result = prediction(Gender, Married, Dependents, Education, Employed,
                            ApplicantIncome, CoapplicantIncome, LoanAmount,
                            Loan_Amount_Term, Credit_History, PropertyArea)

        if result == "Approved":
            st.success("Ur loan application is Approved")
        else: 
            st.error("Pls check ur loan application")

if __name__ == "__main__":
    main()

