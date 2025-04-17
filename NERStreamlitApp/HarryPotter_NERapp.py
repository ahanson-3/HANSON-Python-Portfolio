# Import the necessary libraries for Streamlit
import streamlit as st
import spacy
from spacy.pipeline import EntityRuler
import pandas as pd
from spacy import displacy

#title image
st.image(
        "https://imageservice.disco.peacocktv.com/uuid/e80c1e3c-2d93-3d94-8f5c-2c6e66e8cc09/TITLE_TREATMENT?language=eng&territory=US&proposition=NBCUOTT&version=8eb13517-eee5-354d-aa2f-9b77d006a2d5", width = 800
    )


import subprocess
import importlib.util

# Check if the model is installed; if not, download it
model_name = "en_core_web_sm"
if importlib.util.find_spec(model_name) is None:
    subprocess.run(["python", "-m", "spacy", "download", model_name])

nlp = spacy.load(model_name)

# Create the Streamlit UI components
st.title("🧙📖 Harry Potter Named Entity Recognition")

st.markdown("""
*This is a streamlit app to teach you about Named Entity Recognition (NER) through using the first chapter of Harry Potter using spaCy.*  
**Afterwards you can scroll to the bottom to try it with your own custom text!**

# **What is NER?**
            
Name Entity Recognition (NER) is a task in Natural Language Processing (NLP) that identifies and classifies entities in text into predefined categories like person, organization, location, date, time, and more. Essentially, NER helps computers understand the "who," "what," "where," and "when" of a piece of text. 

*The subject of the NER NLP will be the first chapter of Harry Potter*            
                       
# 📚 **What is Harry Potter?**

*Author:* J.K. Rowling  
*Genre:* Fantasy  
*Main Character:* Harry Potter  

---

## 📖 Book Series

1. *Harry Potter and the Sorcerer’s Stone* (aka *Philosopher’s Stone*)
            * This is where the first chapter we are analyzing is extracted from!
2. *Harry Potter and the Chamber of Secrets*
3. *Harry Potter and the Prisoner of Azkaban*
4. *Harry Potter and the Goblet of Fire*
5. *Harry Potter and the Order of the Phoenix*
6. *Harry Potter and the Half-Blood Prince*
7. *Harry Potter and the Deathly Hallows*

---

## 🎬 Movies

The movies follow the same storyline as the books, with the final book split into two films.

---         

            """)

st.subheader("**Let's get started on analyzing chapter 1 of Sorcerer's Stone with NER!**")

# Define the file path 
hp_chapter1 = ('NERStreamlitApp/Harry_Potter_Chapter1.txt')

# Read the file content
with open(hp_chapter1, 'r', encoding='utf-8') as f:
    text = f.read()

# Adjust the maximum allowed length for the NLP model to process the full text
nlp.max_length = len(text)

# Process the text with the spaCy model
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
st.markdown("**What is a Named Entity?** A named entity is any word or phrase in the text that represents a specific object, person, place, date, or event. NER entities are typically classified into different categories, and these categories help the model or system understand and organize information in a way that’s useful for further analysis.")
st.markdown("Here's a table of all named entities detected in the text, along with their classification labels.")

st.dataframe(ent_df)

st.markdown("""
----
""")

    # Show top 15 entity texts and labels
st.subheader("Top 15 Most Common Entity Texts:")
st.markdown("These are the most frequently mentioned names, places, dates, or other entities in the first chapter.")

st.write(ent_df['text'].value_counts()[:15])

st.subheader("👤 Characters in Chapter 1")

st.markdown("""
The first chapter of *Harry Potter and the Sorcerer’s Stone* introduces several key characters who play important roles in the story. 
Below are some of the most commonly mentioned character names, along with images of a few central figures.
""")

# Define a list of filtered character names based on most common entity texts
chapter1_characters = [
    "Dursley", "Dumbledore", "McGonagall", "Hagrid", 
    "Harry", "Dudley", "Dursleys", "Voldemort", 
    "Harry Potter", "Potters", "Potter"
]

# Show these in a bullet list
st.markdown("### 📜 Mentioned Characters:")
for name in chapter1_characters:
    st.markdown(f"- {name}")

# Visuals for selected characters (in two columns)
st.markdown("### 🖼️ Character Highlights:")

col1, col2 = st.columns(2)

with col1:
    st.image(
        "https://upload.wikimedia.org/wikipedia/en/d/d7/Harry_Potter_character_poster.jpg",
        caption="Harry Potter", width =250
    )
    st.image(
        "https://upload.wikimedia.org/wikipedia/en/e/e8/Dumbledore_-_Prisoner_of_Azkaban.jpg",
        caption="Albus Dumbledore", width=250
    )

with col2:
    st.image(
        "https://upload.wikimedia.org/wikipedia/en/1/10/RubeusHagrid.jpg",
        caption="Rubeus Hagrid", width=250
    )
    st.image(
        "https://upload.wikimedia.org/wikipedia/en/e/ea/McGonagall_%28screenshot%29.jpg",
        caption="Minerva McGonagall", width=250
    )

st.markdown("""
----
""")

st.subheader("Top 15 Entity Labels:")
st.markdown("This shows which types of entities (like PERSON, DATE, GPE) appear most often in the text.")

st.write(ent_df['label'].value_counts()[:15])

st.markdown("""
----
""")
st.subheader("Explore Entity Label Explanations")

st.markdown("""
Use the dropdown below to select an entity label and learn what it means.  
These labels are assigned by spaCy's Named Entity Recognizer to help categorize text elements like people, places, dates, and more.
""")

# Get unique labels from the data
unique_labels = ent_df["label"].unique().tolist()
unique_labels.sort()  # Sort alphabetically for better UX

# Selectbox for choosing a label
selected_label = st.selectbox("Select an entity label to learn more:", unique_labels)

# Get explanation using spaCy
explanation = spacy.explain(selected_label)

# Display the explanation
if explanation:
    st.write(f"**{selected_label}**: {explanation}")
else:
    st.write(f"**{selected_label}**: No explanation found in spaCy's built-in descriptions.")

st.markdown("""
----
""")

    # Display combinations of text and label counts
st.subheader("Top 20 Text and Label Combinations:")
st.markdown("A breakdown of the most common entity + label pairs, showing how often specific names are classified in certain ways.")

st.write(ent_df[['text', 'label']].value_counts()[:20])

st.markdown("""
----
""")

    # List unique labels in the dataset
st.subheader("Unique Entity Labels:")
st.markdown("A full list of all the different entity types that were found in the chapter.")

st.write(ent_df["label"].unique())

st.markdown("""
----
""")

    # Visualize Entities using DisplaCy
st.subheader("Visualize Named Entities:")
st.markdown("Below is a visual highlight of all entities in the text, color-coded by type using spaCy's DisplaCy visualizer.")

displacy.render(doc, style="ent", jupyter=False)


# Streamlit doesn't visualize displaCy naturally so I'm going to use HTML to show the visualization
import streamlit.components.v1 as components
# Generate HTML
html = displacy.render(doc, style="ent", page=True)

# Show in Streamlit
components.html(html, height=800, scrolling=True)

st.markdown("""
----
""")

st.subheader("Try Your Own Text")
st.markdown("Want to test it out yourself? Enter any text you like and see the named entities appear below.")

# User input
user_input = st.text_area("Enter your own text for NER:", "Mr. and Mrs. Dursley, of number four, Privet Drive...")

# If there's input, process it
if user_input:
    # Run spaCy NLP pipeline
    user_doc = nlp(user_input)
    
    # Extract entities
    user_entities = [{'text': ent.text, 'label': ent.label_} for ent in user_doc.ents]
    
    if user_entities:
        user_ent_df = pd.DataFrame(user_entities)
        
        st.markdown("#### Entities in Your Text:")
        st.dataframe(user_ent_df)

        # Visualize using DisplaCy
        st.markdown("#### Visual Highlight of Your Entities:")
        user_html = displacy.render(user_doc, style="ent", page=True)
        components.html(user_html, height=300, scrolling=True)
    else:
        st.info("No named entities found in the input text.")
