
# Harry Potter Named Entity Recognition (NER) App 📚⚡

🔗 Link to web app: ([https://hanson-python-portfolio-ev34yf2jhxjcpfcbuuyymc.streamlit.app/])

## Project Overview
Welcome to the **Harry Potter Named Entity Recognition (NER) App**!  
This app demonstrates how Named Entity Recognition (NER) works using the first chapter of *Harry Potter and the Sorcerer’s Stone*. NER is a task in Natural Language Processing (NLP) that identifies and classifies entities (like names, locations, dates) in text.

We use **spaCy**, a powerful NLP library, to process the text and detect named entities like characters' names, places, and other important entities. The app lets you explore the entities in the text and learn more about them!

### What's NER? 🤔
NER stands for **Named Entity Recognition**, which is a part of Natural Language Processing (NLP). It helps identify words or phrases that represent specific things like:
- **PERSON**: Names of people (e.g., Harry Potter)
- **GPE**: Geopolitical entities (e.g., countries, cities)
- **DATE**: Dates or time references
- **ORG**: Organizations (e.g., Hogwarts)

This app helps you understand how spaCy processes text and identifies these entities!

---

## Instructions 🚀

### Running the App Locally

1. **Clone this repository** to your local machine:
   ```bash
   git clone [https://github.com/ahanson-3/HANSON-Python-Portfolio/blob/c0e918a377f893f25675426c9f674ceeadade0b3/NERStreamlitApp/HarryPotter_NERapp.py]
      ```

#### Navigate to the project folder:

   ```bash
cd ner-harrypotter
   ```

#### Install required libraries:

*If you don't have the libraries already, install them using pip:*
   ```bash
pip install -r requirements.txt
   ```

#### Download the spaCy model:

*We’re using the en_core_web_sm spaCy model. Run this command to download it:*
   ```bash
python -m spacy download en_core_web_sm
   ```

#### Run the app:

*Start the Streamlit app with the following command:*
   ```bash
streamlit run app.py
   ```


---

## Required Libraries 📦

**spaCy:** For NLP tasks, particularly Named Entity Recognition.

**Streamlit:** For building interactive web apps.

**pandas:** For handling and displaying data.

**matplotlib/plotly:** Optional, for visualizations.

*To install all dependencies, run:*
pip install -r requirements.txt

---

## App Features ✨

**Named Entity Recognition:** The app processes the first chapter of Harry Potter and the Sorcerer’s Stone using spaCy and highlights named entities like characters, places, and dates.

**Interactive Text Upload:** You can upload your own text to see how NER works with different content.

**Entity Label Explanation:** A dropdown lets you choose an entity label (e.g., PERSON, GPE, DATE) and get a detailed explanation of that label.

**Visualize Entities:** The app uses spaCy's displaCy visualizer to highlight and color-code the entities in the text.

*Example Usage*
* Upload your own text or use the pre-loaded chapter from Harry Potter.
* View entities detected in the text (e.g., "Harry Potter" as PERSON, "Hogwarts" as GPE).
* Visualize entities with an interactive graph.

---

## References 📚

* spaCy Documentation
* spaCy Named Entity Recognition (NER) Tutorial
* EntityRuler Documentation
