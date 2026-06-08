import pickle

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/home')
def home_direct():
    return render_template('index.html')

@app.route('/analyze')
def analyze():
    return render_template('analyze.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    title = data.get('title', '')
    company = data.get('company', '')
    description = data.get('description', '')
    requirements = data.get('requirements', '')

    text = title + ' ' + company + ' ' + description + ' ' + requirements
    vec = vectorizer.transform([text])
    prediction = int(model.predict(vec)[0])
    probability = model.predict_proba(vec)[0]
    fake_score = round(float(probability[1]) * 100, 1)
    real_score = round(float(probability[0]) * 100, 1)

    red_flags = []
    text_lower = text.lower()
    if any(w in text_lower for w in ['earn from home', 'no experience needed', 'anyone can apply']):
        red_flags.append("Suspicious earning claims")
    if any(w in text_lower for w in ['gmail.com', 'yahoo.com', 'hotmail.com']):
        red_flags.append("Personal email domain used")
    if any(w in text_lower for w in ['urgent hiring', 'immediate joining']):
        red_flags.append("Artificial urgency language")
    if any(w in text_lower for w in ['no qualification', 'no degree', 'no skills required']):
        red_flags.append("No qualifications required")
    if len(description) < 100:
        red_flags.append("Unusually short description")
    if not company or len(company) < 30:
        red_flags.append("Missing or thin company profile")

    return jsonify({
        'prediction': prediction,
        'fake_score': fake_score,
        'real_score': real_score,
        'red_flags': red_flags
    })

if __name__ == '__main__':
    app.run(debug=True)