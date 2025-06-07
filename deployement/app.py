from flask import Flask, render_template, request, jsonify
from .utils import make_prediction

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    email_text = request.form['email_content']
    prediction = make_prediction(email_text)
    return render_template('index.html', prediction=prediction, email_text=email_text)

@app.route('/api/predict', methods=['POST'])
def api_predict():
    data = request.get_json(force = True)
    email_text = data['email_content']
    prediction = make_prediction(email_text[0])
    return jsonify({'prediction': prediction, 'email_text': email_text})  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)