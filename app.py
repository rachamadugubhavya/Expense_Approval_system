# app.py

import streamlit as st
from prompt import prompt
from parser import parser
from model import get_model

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="Expense Categorizer",
    page_icon="💰",
    layout="centered"
)

# -------------------------------
# Custom CSS
# -------------------------------
st.markdown("""
<style>

body {
    background-color: #0f172a;
}

.main {
    background-color: #0f172a;
}

.title {
    font-size: 40px;
    font-weight: bold;
    text-align: center;
    color: #38bdf8;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    color: #cbd5f5;
    margin-bottom: 30px;
}

.input-box {
    background-color: #1e293b;
    padding: 15px;
    border-radius: 10px;
}

.result-card {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 12px;
    margin-top: 20px;
    border: 1px solid #334155;
}

.label {
    color: #94a3b8;
    font-size: 14px;
}

.value {
    font-size: 20px;
    font-weight: bold;
    color: #22c55e;
}

.note {
    color: #e2e8f0;
    font-size: 15px;
    margin-top: 10px;
}

button[kind="primary"] {
    background-color: #38bdf8;
    color: black;
    font-weight: bold;
    border-radius: 8px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# Title Section
# -------------------------------
st.markdown('<div class="title">💰 Expense Categorizer</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Classify your expenses using GenAI (Groq + LangChain)</div>', unsafe_allow_html=True)

# -------------------------------
# Input
# -------------------------------
st.markdown('<div class="input-box">', unsafe_allow_html=True)

expense_input = st.text_input(
    "Enter your expense description:",
    placeholder="e.g., Paid electricity bill, Uber ride, bought groceries..."
)

st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# Button
# -------------------------------
if st.button("Categorize Expense"):

    if not expense_input.strip():
        st.warning("Please enter an expense description.")
    else:
        try:
            model = get_model()
            chain = prompt | model | parser

            result = chain.invoke({
                "expense_description": expense_input
            })

            # -------------------------------
            # Output Display
            # -------------------------------
            st.markdown('<div class="result-card">', unsafe_allow_html=True)

            st.markdown(f"""
            <div class="label">Category</div>
            <div class="value">{result.expense_category}</div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div class="label">Type</div>
            <div class="value">{result.expense_type}</div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div class="label">Confidence</div>
            <div class="note">{result.confidence_note}</div>
            """, unsafe_allow_html=True)

            st.markdown('</div>', unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Error: {str(e)}")

# -------------------------------
# Footer
# -------------------------------
st.markdown("""
<br><br>
<center style="color: #64748b;">
Built with  using LangChain + Groq
</center>
""", unsafe_allow_html=True)