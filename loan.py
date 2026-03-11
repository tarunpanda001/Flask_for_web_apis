from flask import Flask,request
import pickle

app = Flask(__name__)
with open("classifier.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return "<h1>Welcome to the Loan Application Service</h1>"

@app.route("/predict",methods=["GET"])
def predict():
    return "<h1>Here I will predict the loan approval status</h1> \
    <p>To make a prediction, send a POST request with required data.</p>"

@app.route("/predict",methods=["POST"])
def make_prediction():
    loan_req = request.get_json()
    if loan_req["Gender"] == "Male":
        Gender = 0
    else:
        Gender = 1
    if loan_req["Married"] == "No":
        Married = 0
    else:
        Married = 1
    
    ApplicantIncome = loan_req["ApplicantIncome"]
    CreditHistory = loan_req["CreditHistory"]
    LoanAmount = loan_req["LoanAmount"]

    input_data = [Gender, Married, ApplicantIncome, LoanAmount, CreditHistory]
    
    pred = model.predict([input_data])
    print(pred)
    
    if pred[0] == 0:
        pred = "Loan Approved"
    else:
        pred = "Loan Rejected"

    return {"Loan Status": pred}

if __name__ =="__main__":
    app.run(debug=True)