from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import pickle

app = Flask(__name__)

@app.route('/', methods=['GET'])
@cross_origin()
def homepage():
    return  render_template('index.html')

@app.route('/predict',methods=['POST','GET'])
@cross_origin()
def prediction():
    if request.method == 'POST':
        try:
            processTemperature = float(request.form['processTemperature'])
            rotationalSpeed = float(request.form['rotationalSpeed'])
            torque = float(request.form['torque'])
            toolWear = float(request.form['toolWear'])
            twf = request.form['twf']
            hdf = request.form['hdf']
            pwf = request.form['pwf']
            osf = request.form['osf']
            rnf = request.form['rnf']
            filename = 'ai4i_lgr_model.pickle'
            loaded_model = pickle.load(open(filename, 'rb'))
            prediction = loaded_model.predict([[processTemperature, rotationalSpeed, torque, toolWear, twf, hdf, pwf, osf, rnf]])
            print("Prediction is ", prediction)
            return render_template('result.html', prediction=prediction[0])
        except Exception as ex:
            print("The Exception message is ", ex)
            return "Something is wrong"
    else:
        return render_template('index.html')

if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
    #return render_template('result.html')
	app.run(debug=True) # running the app