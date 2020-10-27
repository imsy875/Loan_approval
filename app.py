from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
app = Flask(__name__)
model = pickle.load(open('Last_Model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Dependents=int(request.form['dependents'])
        ApplicantIncome=int(request.form['income'])	
        CoapplicantIncome=int(request.form['coincome'])
        LoanAmount=int(request.form['loan_amount'])
        Loan_Amount_Term=int(request.form['loan_amount_term'])
        Credit_History=request.form['credit']
        if(Credit_History=='1.0'):
            Credit_History=1.0
        else:
            Credit_History=0.0
        Gender_Male=request.form['gender']
        if(Gender_Male=='male'):
            Gender_Male=1
        else:
            Gender_Male=0
        Married_Yes=request.form['married']
        if(Married_Yes=='yes'):
            Married_Yes=1
        else:
            Married_yes=0
        Education_not_graduate=request.form['graduate']
        if(Education_not_graduate=='not_graduate'):
             Education_not_graduate=1
        else:
             Education_not_graduate=0
        Self_Employed_Yes=request.form['self_employed']
        if(Self_Employed_Yes=='yes'):
             Self_Employed_Yes=1
        else:
             Self_Employed_Yes=0
        Property_Area_Semiurban=request.form['living']
        if(Property_Area_Semiurban=='semi_urban'):
                Property_Area_Semiurban=1
                Property_Area_Urban=0
        elif(Property_Area_Semiurban=='urban'):
                Property_Area_Semiurban=0
                Property_Area_Urban=1
        else:
            Property_Area_Semiurban=0
            Property_Area_Urban=0
        prediction=model.predict([[Dependents,ApplicantIncome,CoapplicantIncome,
                                   LoanAmount, Loan_Amount_Term,
                                   Credit_History, Gender_Male, Self_Employed_Yes, 
                                   Married_yes,Property_Area_Semiurban, Property_Area_Urban,
                                   Education_not_graduate]])
        output=prediction()
        if output==0:
            return render_template('index.html',prediction_texts="Sorry you are not eligible for the loan")
        else:
            return render_template('index.html',prediction_text="Congratulations, You are eligible for the loan")
    else:
        return render_template('index.html')
if __name__=="__main__":
    app.run(debug=True)
