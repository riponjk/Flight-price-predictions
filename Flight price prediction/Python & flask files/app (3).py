import flask
from flask import Flask, render_template, request
import pickle
import numpy as np
import sklearn

app = Flask(__name__)

model = pickle.load(open('flightprice.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/getdata', methods=['POST'])
def pred():
    Airline = request.form['airline']
    print(Airline)
    Source = request.form['Source']
    print(Source)
    Destination = request.form['Destination']
    print(Destination)
    Date = request.form['date']
    print(Date)
    Month = request.form['month']
    print(Month)
    Year = request.form['year']
    print(Year)
    Dep_Time_Hour = request.form['Dep_Time_Hour']
    print(Dep_Time_Hour)
    Dep_Time_Mins = request.form['Dep_Time_Mins']
    print(Dep_Time_Mins)
    Arrival_Time_Hour = request.form['Arrival_Time_Hour']
    print(Arrival_Time_Hour)
    Arrival_TimeMins = request.form['Arrival_Time_Mins']
    print(Arrival_TimeMins)
    Arrival_Day = request.form['Arrival_Day']
    print(Arrival_Day)



    inp_features = [[int(Airline), int(Source), int(Destination) ,int(Date),int(Month), int(Year), int(Dep_Time_Hour),
                     int(Dep_Time_Mins),
                     int(Arrival_Time_Hour),int(Arrival_TimeMins),int(Arrival_Day)]]
    print(inp_features)
    prediction = model.predict(inp_features)
    print(type(prediction))
    t = prediction[0]
    print(t)
    if t > 0.5:
        prediction_text = 'No change in price'
    else:
        prediction_text = 'Price will increase'
    print(prediction_text)
    return render_template('prediction.html', prediction_results=prediction_text)


if __name__ == "__main__":
    app.run()