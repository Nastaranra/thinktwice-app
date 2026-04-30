%%writefile app.py

import streamlit as st

# Page setup
st.set_page_config(
    page_title="ThinkTwice",
    page_icon="🔮",
    layout="centered"
)

# Title
st.title("🔮 ThinkTwice")
st.subheader("See your future before you decide")

st.write("Before making a decision, check your regret risk.")

st.markdown("---")

# Inputs
amount = st.slider("💰 Purchase Amount ($)", 0, 1000, 200)
sleep = st.slider("😴 Sleep Hours", 0, 10, 7)
stress = st.slider("😰 Stress Level", 1, 10, 5)
urgency = st.selectbox("⚡ Urgency", ["Low", "Medium", "High"])
mood = st.selectbox("😊 Mood", ["Happy", "Neutral", "Sad", "Angry"])

# Button
if st.button("🔮 Predict My Future"):

    score = 0
    reasons = []

    if stress >= 7:
        score += 20
        reasons.append("High stress")

    if sleep < 6:
        score += 15
        reasons.append("Low sleep")

    if amount > 300:
        score += 30
        reasons.append("High spending")

    if urgency == "High":
        score += 20
        reasons.append("Impulsive decision")

    if mood in ["Sad", "Angry"]:
        score += 15
        reasons.append("Emotional state")

    st.markdown("---")
    st.subheader(f"🔴 Regret Score: {score}%")

    if score > 60:
        st.error("High Risk of Regret")
        st.write("💡 Wait 24 hours before deciding")
    elif score > 30:
        st.warning("Medium Risk")
        st.write("💡 Think carefully")
    else:
        st.success("Low Risk")
        st.write("💡 Decision looks okay")

    st.write("### Why?")
    for r in reasons:
        st.write("-", r)

# Footer (FIXED — no error)
st.caption("ThinkTwice is a decision-support tool, not financial, medical, or legal advice.")