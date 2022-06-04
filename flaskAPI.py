from flask import Flask,request,jsonify
import numpy as np
import pickle
model = pickle.load(open('module.pkl','rb'))
app = Flask(__name__)
@app.route('/')
def index():
    return "Hello world"
@app.route('/predict',methods=['POST'])
def predict():
    st = 'Badday'
    input_query = np.array([st])
    result = model.predict(input_query)[0]
    return jsonify({'Result':str(result)})
if __name__ == '__main__':
    app.run(debug=True)