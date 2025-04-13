# Import the necessary libraries for Streamlit
import streamlit as st
import spacy
from spacy.pipeline import EntityRuler
import pandas as pd
import plotly.express as px
from spacy import displacy

# Install the libraries if not already installed
# %pip install spacy plotly pandas streamlit

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Create the Streamlit UI components
st.title("Harry Potter Named Entity Recognition")

st.markdown("""
This is a demo app for performing Named Entity Recognition (NER) on the first chapter of Harry Potter using spaCy.
""")

# Upload text file
uploaded_file = st.file_uploader(NERStreamlitApp/Harry_Potter_Chapter1.txt, type=["txt"])

if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")
    nlp.max_length = len(text)
    
    # Process the document with spayC
    doc = nlp(text)

    # Named Entity Recognition (NER)
    entities_data = []

    # Extract each entity and its label
    for ent in doc.ents:
        entities_data.append({
            'text': ent.text,
            'label': ent.label_
        })

    # Convert to DataFrame for better display
    ent_df = pd.DataFrame(entities_data)
    
    st.subheader("Entities Found:")
    st.dataframe(ent_df)

    # Show top 15 entity texts and labels
    st.subheader("Top 15 Most Common Entity Texts:")
    st.write(ent_df['text'].value_counts()[:15])

    st.subheader("Top 15 Entity Labels:")
    st.write(ent_df['label'].value_counts()[:15])

    st.subheader("Explanation for 'FAC' label:")
    st.write(spacy.explain("FAC"))

    st.subheader("Explanation for 'GPE' label:")
    st.write(spacy.explain("GPE"))

    # Display combinations of text and label counts
    st.subheader("Top 20 Text and Label Combinations:")
    st.write(ent_df[['text', 'label']].value_counts()[:20])

    # List unique labels in the dataset
    st.subheader("Unique Entity Labels:")
    st.write(ent_df["label"].unique())

    # Visualize Entities using DisplaCy
    st.subheader("Visualize Named Entities:")
    displacy.render(doc, style="ent", jupyter=False)

else:
    st.warning("Please upload a text file to analyze.")
