import streamlit as st
import requests
import json

SYSTEM_PROMPT = """
Jestes ekspertem UX i kognitywistyki. Analizujesz opisy interfejsow
pod katem obciazenia poznawczego. Twoja analiza zawiera:
1. OCENA OGOLNA (skala 1-10)
2. GLOWNE PROBLEMY (max 5 elementow)
3. NIEJASNE ELEMENTY
4. REKOMENDACJE
Odpowiadaj po polsku.
"""

def ask_ollama(prompt):
    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "llama3.2:latest",
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            "stream": False
        }
    )
    return response.json()["message"]["content"]

st.set_page_config(page_title="Cognitive Load Tester")
st.title("Cognitive Load Tester")

ui_description = st.text_area("Opis interfejsu", height=200)

if st.button("Analizuj") and ui_description:
    with st.spinner("Analizowanie..."):
        analysis = ask_ollama(ui_description)
    st.subheader("Wynik analizy")
    st.markdown(analysis)
    st.divider()
    st.subheader("NASA-TLX")
    mental = st.slider("Wysilek mentalny", 1, 10, 5)
    frustration = st.slider("Frustracja", 1, 10, 5)
    time_pressure = st.slider("Presja czasu", 1, 10, 5)
    if st.button("Zapisz ocene"):
        avg = round((mental + frustration + time_pressure) / 3, 1)
        st.success(f"Srednie obciazenie: {avg}/10")
