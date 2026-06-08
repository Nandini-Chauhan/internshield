import pickle
import time

import streamlit as st

model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

st.set_page_config(
    page_title="InternShield",
    page_icon="🛡️",
    layout="centered"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=IBM+Plex+Mono:wght@400;600&family=Inter:wght@400;500;600&display=swap');

html, body, .stApp {
    background: #FAFAF8 !important;
}

.block-container {
    padding-top: 3rem !important;
    max-width: 720px !important;
}

.masthead {
    border-top: 3px solid #111;
    border-bottom: 1px solid #111;
    padding: 1.2rem 0;
    margin-bottom: 2.5rem;
    display: flex;
    align-items: baseline;
    justify-content: space-between;
}

.masthead-title {
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 2.4rem;
    font-weight: 900;
    color: #111;
    letter-spacing: -1px;
    line-height: 1;
}

.masthead-tag {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.65rem;
    color: #888;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.section-label {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.65rem;
    color: #888;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 0.5rem;
    margin-top: 1.5rem;
}

div[data-testid="stTextInput"] label,
div[data-testid="stTextArea"] label {
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 0.65rem !important;
    color: #888 !important;
    letter-spacing: 3px !important;
    text-transform: uppercase !important;
}

div[data-testid="stTextInput"] input {
    background: #fff !important;
    border: 1px solid #ddd !important;
    border-radius: 4px !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.95rem !important;
    color: #111 !important;
    padding: 0.75rem !important;
    transition: border 0.2s !important;
}

div[data-testid="stTextInput"] input:focus {
    border: 1px solid #111 !important;
    box-shadow: none !important;
}

div[data-testid="stTextArea"] textarea {
    background: #fff !important;
    border: 1px solid #ddd !important;
    border-radius: 4px !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.9rem !important;
    color: #111 !important;
    line-height: 1.6 !important;
    transition: border 0.2s !important;
}

div[data-testid="stTextArea"] textarea:focus {
    border: 1px solid #111 !important;
    box-shadow: none !important;
}

div[data-testid="stButton"] button {
    background: #111 !important;
    color: #FAFAF8 !important;
    border: none !important;
    border-radius: 4px !important;
    font-family: 'IBM Plex Mono', monospace !important;
    font-weight: 600 !important;
    font-size: 0.85rem !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    padding: 0.8rem 2rem !important;
    width: 100% !important;
    margin-top: 1rem !important;
    transition: background 0.2s !important;
    cursor: pointer !important;
}

div[data-testid="stButton"] button:hover {
    background: #333 !important;
}

.result-card {
    background: #fff;
    border: 1px solid #e0e0e0;
    border-radius: 6px;
    padding: 2rem;
    margin-top: 2rem;
    animation: slideUp 0.4s ease;
}

@keyframes slideUp {
    from { opacity: 0; transform: translateY(16px); }
    to   { opacity: 1; transform: translateY(0); }
}

.result-verdict {
    font-family: 'Playfair Display', serif;
    font-size: 1.6rem;
    font-weight: 700;
    margin-bottom: 0.3rem;
}

.result-verdict.fake { color: #C8102E; }
.result-verdict.real { color: #0A6E3F; }

.result-sub {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.75rem;
    color: #888;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 1.5rem;
}

.risk-bar-wrap {
    background: #f0f0ee;
    border-radius: 2px;
    height: 6px;
    margin-bottom: 0.4rem;
    overflow: hidden;
}

.risk-bar-fill {
    height: 100%;
    border-radius: 2px;
    transition: width 0.8s cubic-bezier(.4,0,.2,1);
}

.risk-bar-fill.fake { background: #C8102E; }
.risk-bar-fill.real { background: #0A6E3F; }

.score-row {
    display: flex;
    justify-content: space-between;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.75rem;
    color: #888;
    margin-bottom: 1.5rem;
}

.big-score {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 3.5rem;
    font-weight: 600;
    line-height: 1;
    margin-bottom: 0.2rem;
}

.big-score.fake { color: #C8102E; }
.big-score.real { color: #0A6E3F; }

.flags-section {
    border-top: 1px solid #eee;
    padding-top: 1.2rem;
    margin-top: 0.5rem;
}

.flags-label {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #aaa;
    margin-bottom: 0.8rem;
}

.flag-pill {
    display: inline-block;
    background: #FFF0F1;
    color: #8B0000;
    border: 1px solid #F5C6CA;
    border-radius: 3px;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.72rem;
    padding: 0.3rem 0.7rem;
    margin: 0.2rem 0.2rem 0.2rem 0;
}

.clean-pill {
    display: inline-block;
    background: #F0FFF6;
    color: #0A6E3F;
    border: 1px solid #B7E8C8;
    border-radius: 3px;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.72rem;
    padding: 0.3rem 0.7rem;
    margin: 0.2rem 0.2rem 0.2rem 0;
}

.divider {
    border: none;
    border-top: 1px solid #e8e8e8;
    margin: 2rem 0;
}

.stWarning {
    background: #FFFBF0 !important;
    border: 1px solid #F5DDA0 !important;
    color: #7A5800 !important;
    border-radius: 4px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="masthead">
    <div class="masthead-title">InternShield</div>
    <div class="masthead-tag">Fraud Detection Engine &nbsp;·&nbsp; v1.0</div>
</div>
""", unsafe_allow_html=True)

title = st.text_input("Job Title")
company = st.text_area("Company Profile", height=90)
description = st.text_area("Job Description", height=140)
requirements = st.text_area("Requirements", height=90)

if st.button("Run Analysis"):
    if not description:
        st.warning("Paste at least the job description to analyse.")
    else:
        with st.spinner("Scanning posting..."):
            time.sleep(0.8)

        text = title + ' ' + company + ' ' + description + ' ' + requirements
        vec = vectorizer.transform([text])
        prediction = model.predict(vec)[0]
        probability = model.predict_proba(vec)[0]

        fake_score = round(probability[1] * 100, 1)
        real_score = round(probability[0] * 100, 1)

        # Red flags
        red_flags = []
        text_lower = text.lower()
        if any(w in text_lower for w in ['earn from home', 'work from home and earn', 'no experience needed', 'anyone can apply']):
            red_flags.append("Suspicious earning claims")
        if any(w in text_lower for w in ['gmail.com', 'yahoo.com', 'hotmail.com']):
            red_flags.append("Personal email domain")
        if any(w in text_lower for w in ['urgent hiring', 'immediate joining']):
            red_flags.append("Artificial urgency language")
        if any(w in text_lower for w in ['no qualification', 'no degree', 'no skills required']):
            red_flags.append("No qualifications required")
        if len(description) < 100:
            red_flags.append("Unusually short description")
        if not company or len(company) < 30:
            red_flags.append("Missing or thin company profile")

        verdict_class = "fake" if prediction == 1 else "real"
        verdict_text = "Likely Fraudulent" if prediction == 1 else "Appears Legitimate"
        verdict_sub = "High risk — treat with caution" if prediction == 1 else "Low risk — signals look normal"

        flags_html = ""
        if red_flags:
            pills = "".join([f'<span class="flag-pill">{f}</span>' for f in red_flags])
            flags_html = f"""
            <div class="flags-section">
                <div class="flags-label">Signals Detected</div>
                {pills}
            </div>
            """
        else:
            flags_html = """
            <div class="flags-section">
                <div class="flags-label">Signals Detected</div>
                <span class="clean-pill">No obvious red flags found</span>
            </div>
            """

        st.markdown(f"""
        <div class="result-card">
            <div class="big-score {verdict_class}">{fake_score}%</div>
            <div class="result-verdict {verdict_class}">{verdict_text}</div>
            <div class="result-sub">{verdict_sub}</div>

            <div class="risk-bar-wrap">
                <div class="risk-bar-fill {verdict_class}" style="width: {fake_score}%"></div>
            </div>
            <div class="score-row">
                <span>Risk Score</span>
                <span>{fake_score}% fake &nbsp;·&nbsp; {real_score}% real</span>
            </div>

            {flags_html}
        </div>
        """, unsafe_allow_html=True)