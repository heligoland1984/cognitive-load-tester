# Cognitive Load Tester

Aplikacja do analizy obciazenia poznawczego interfejsow uzytkownika, zbudowana z uzyciem Streamlit i lokalnego modelu AI (Ollama).

## Co robi?

Wklejasz opis interfejsu uzytkownika, a aplikacja analizuje go pod katem cognitive load i zwraca:
- Ocena ogolna (skala 1-10)
- Glowne problemy (elementy konkurujace o uwage)
- Niejasne elementy
- Rekomendacje uproszczenia

Na koncu mozesz wypelnic uproszczony kwestionariusz NASA-TLX.

## Technologie

- Python
- Streamlit
- Ollama (llama3.2)

## Uruchomienie lokalne

1. Zainstaluj zaleznosci:
pip install streamlit requests

2. Zainstaluj i uruchom Ollama: ollama.com
ollama pull llama3.2
ollama serve

3. Uruchom aplikacje:
streamlit run app.py

## Autor

Karol Bontron - projekt portfolio z zakresu kognitywistyki i AI UX
