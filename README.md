# 🛡️ InternShield — Fake Internship Detector

> Built for Indian students who deserve better than getting scammed.

🔗 **Live Demo → [internshield-a1yq.onrender.com](https://internshield-a1yq.onrender.com)**

---

## The Problem

1 in 5 college students get targeted by fake internship scams. Platforms like Internshala and LinkedIn are flooded with fraudulent postings promising unrealistic stipends, requiring no qualifications, and asking for personal details upfront.

There was no simple tool a student could just *use* to verify a posting. So I built one.

---

## What It Does

Paste any internship or job posting — title, company profile, description, requirements — and InternShield gives you:

- A **risk score** (0–100%)
- A **verdict** — Likely Fraudulent or Appears Legitimate
- A breakdown of exactly which **red flags** were detected

---

## How It Works

User pastes job posting
↓
Text preprocessing + TF-IDF vectorization (5,000 features)
↓
Logistic Regression classifier (class_weight='balanced')
↓
Risk score + red flag detection
↓
Full-page result overlay

---

## Model Performance

| Metric | Score |
|---|---|
| Accuracy | 96% |
| Recall (Fake) | 87% |
| Precision (Fake) | 58% |
| Training Data | 17,880 job postings |

> High recall is prioritised over precision — missing a fake internship is worse than a false alarm.

---

## Red Flags Detected

- Suspicious earning claims
- Personal email domains (gmail, yahoo, hotmail)
- Artificial urgency language
- No qualifications required
- Missing or thin company profile
- Unusually short description

---

## Tech Stack

| Layer | Technology |
|---|---|
| ML Model | scikit-learn (TF-IDF + Logistic Regression) |
| Backend | Python, Flask |
| Frontend | HTML, CSS, JavaScript |
| Deployment | Render |

---

## Project Structure
internshield/
├── app.py                  # Flask backend + prediction API
├── model.pkl               # Trained ML model
├── vectorizer.pkl          # TF-IDF vectorizer
├── templates/
│   ├── index.html          # Home page
│   ├── analyze.html        # Analysis page
│   └── intro.html          # Intro animation
├── static/                 # Audio assets
├── requirements.txt
└── Procfile

---

## Run Locally

```bash
git clone https://github.com/Nandini-Chauhan/internshield.git
cd internshield
pip install -r requirements.txt
python app.py
```

Then open `http://127.0.0.1:5000`

---

## Dataset

[Real or Fake Job Postings](https://www.kaggle.com/datasets/shivamb/real-or-fake-fake-jobposting-prediction) — Kaggle

17,880 job postings, 866 fraudulent (4.8%)

---

## Author

**Nandini Chauhan**
B.Tech CSE (AI & ML) — MIET, Meerut | Batch of 2028

[LinkedIn](https://linkedin.com/in/your-linkedin) · [GitHub](https://github.com/Nandini-Chauhan)