import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Streamlit Config
st.set_page_config(page_title="🏀 NBA vs WNBA Salary Analysis", layout="wide")

# Title and Introduction
st.title("🚨🏀 Gender Pay Gap in Professional Basketball")
st.markdown("""
Welcome! This interactive app explores the **gender pay gap** in professional basketball  
using salary data from **NBA** and **WNBA** players.

### 🔍 What You Can Do:
- Analyze salary differences between men and women players  
- Upload your own basketball salary data  
- Search specific players to compare earnings  
- Share insights on gender equity in sports  
""")

# Sidebar Instructions
st.sidebar.header("📄 How to Use This App")
st.sidebar.markdown("""
1. Review the built-in analysis from our dataset  
2. Optionally upload your own Excel file (must include columns: Rank, Player, Salary, Gender)  
3. Use the search bar to find specific player salaries  
""")

# File upload (optional)
uploaded_file = st.file_uploader("Upload your own Excel file (Rank, Player, Salary, Gender)", type=["xlsx"])

st.markdown("""
Don't have a file? Download this one to practice uploading or figure out data formatting!
            """)

# Allow download of default dataset (Excel format)
with open("StreamlitAppFinal/NBAvsWNBA1.xlsx", "rb") as f:
    st.download_button(
        label="📥 Download Example NBA/WNBA Dataset",
        data=f,
        file_name="NBAvsWNBA1.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

# Load default or uploaded data
@st.cache_data
def load_data(file):
    if file:
        df = pd.read_excel(file)
        st.write("Data loaded from the uploaded file.")
    else:
        df = pd.read_excel("StreamlitAppFinal/NBAvsWNBA1.xlsx")  # Local or hosted file
        st.write("Using the default dataset.")
    
    df.columns = df.columns.str.strip()  # Clean column names
    df['Salary'] = df['Salary'].replace('[\$,]', '', regex=True)
    df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')  # Coerce errors into NaN values
    return df

data = load_data(uploaded_file)

# Search functionality
search_player = st.text_input("🔎 Search for a player by name (case-insensitive):")
if search_player:
    result = data[data['Player'].str.contains(search_player, case=False)]
    if not result.empty:
        st.subheader("Player Search Results")
        st.dataframe(result)
    else:
        st.warning("No player found with that name.")

# Summary Stats
st.subheader("📊 Summary Statistics")
summary = data.groupby('Gender')['Salary'].agg(['count', 'mean', 'max', 'min']).reset_index()
summary.columns = ['Gender', 'Number of Players', 'Average Salary', 'Max Salary', 'Min Salary']
summary['Average Salary'] = summary['Average Salary'].map("${:,.2f}".format)
summary['Max Salary'] = summary['Max Salary'].map("${:,.2f}".format)
summary['Min Salary'] = summary['Min Salary'].map("${:,.2f}".format)
st.dataframe(summary)

# Boxplot
st.subheader("📦 Salary Distribution by Gender")
col1, _ = st.columns([1, 1])  # Half-width column
with col1:
    fig, ax = plt.subplots()
    sns.boxplot(data=data, x='Gender', y='Salary', palette='Set2', ax=ax)
    ax.set_title('NBA vs WNBA Salary Distribution')
    ax.set_ylabel("Salary ($)")
    st.pyplot(fig)

# Add Histogram of Salary Distribution
st.subheader("📊 Salary Distribution (Histogram)")
col2, _ = st.columns([1, 1])
with col2:
    fig2, ax2 = plt.subplots()
    sns.histplot(data['Salary'], bins=30, kde=True, ax=ax2)
    ax2.set_title('Salary Distribution for NBA/WNBA Players')
    ax2.set_xlabel("Salary ($)")
    ax2.set_ylabel("Frequency")
    st.pyplot(fig2)

# Gender Pay Gap Visualization (Pie Chart)
st.subheader("📊 Gender Pay Gap Overview")
gender_counts = data['Gender'].value_counts()
gender_salary_avg = data.groupby('Gender')['Salary'].mean()

col3, _ = st.columns([1, 1])
with col3:
    fig3, ax3 = plt.subplots(1, 2, figsize=(10, 5))
    ax3[0].pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90, colors=["#FF9999", "#66B2FF"])
    ax3[0].set_title('Player Gender Distribution')

    sns.barplot(x=gender_salary_avg.index, y=gender_salary_avg.values, ax=ax3[1], palette='Set2')
    ax3[1].set_title('Average Salary by Gender')
    ax3[1].set_ylabel("Average Salary ($)")
    st.pyplot(fig3)



# Top Earners
st.subheader("🏅 Top 10 Highest Paid Players")
top_players = data.sort_values(by='Salary', ascending=False).head(10)
top_players['Salary'] = top_players['Salary'].map("${:,.2f}".format)
st.dataframe(top_players)

# Add interactive Salary Filter
st.subheader("🔍 Filter Players by Salary")
min_salary, max_salary = st.slider("Select salary range", 
                                   min_value=int(data['Salary'].min()), 
                                   max_value=int(data['Salary'].max()), 
                                   value=(int(data['Salary'].min()), int(data['Salary'].max())))
filtered_data = data[(data['Salary'] >= min_salary) & (data['Salary'] <= max_salary)]
st.write(f"Displaying players with salaries between ${min_salary:,.2f}",f" and ${max_salary:,.2f}")
st.dataframe(filtered_data)

# Allow download of processed data
if not data.empty:
    st.download_button("Download Cleaned Data", data.to_csv(index=False), file_name="Cleaned_Salary_Data.csv")
else:
    st.warning("No data available to download.")

import requests
from PIL import Image
from io import BytesIO
import urllib.parse

# --- Player Comparison Section ---
st.subheader("👥 Compare a WNBA Player vs an NBA Player")

# Filter by gender
female_players = data[data['Gender'] == 'F']['Player'].unique()
male_players = data[data['Gender'] == 'M']['Player'].unique()

col1, col2 = st.columns(2)

with col1:
    selected_female = st.selectbox("Select WNBA Player", sorted(female_players))
with col2:
    selected_male = st.selectbox("Select NBA Player", sorted(male_players))

# Function to fetch Wikipedia image
def get_wikipedia_image_url(player_name):
    search = urllib.parse.quote(player_name)
    wiki_api_url = f"https://en.wikipedia.org/w/api.php?action=query&titles={search}&prop=pageimages&format=json&pithumbsize=300"
    response = requests.get(wiki_api_url).json()
    pages = response.get("query", {}).get("pages", {})
    for page in pages.values():
        if "thumbnail" in page:
            return page["thumbnail"]["source"]
    return None

# Retrieve info
female_info = data[data['Player'] == selected_female].iloc[0]
male_info = data[data['Player'] == selected_male].iloc[0]

# Layout results
st.markdown("### 📋 Player Comparison")
comp1, comp2 = st.columns(2)

with comp1:
    st.markdown(f"**{female_info['Player']}** (WNBA)")
    st.write(f"**Salary:** ${female_info['Salary']:,.2f}")
    image_url = get_wikipedia_image_url(female_info['Player'])
    if image_url:
        st.image(image_url, caption=female_info['Player'], use_container_width=True)
    else:
        st.info("No image found on Wikipedia.")

with comp2:
    st.markdown(f"**{male_info['Player']}** (NBA)")
    st.write(f"**Salary:** ${male_info['Salary']:,.2f}")
    image_url = get_wikipedia_image_url(male_info['Player'])
    if image_url:
        st.image(image_url, caption=male_info['Player'], use_container_width=True)
    else:
        st.info("No image found on Wikipedia.")

st.subheader("""💡 Why This Matters: Bridging the Gender Gap in Pro Basketball""")
st.markdown("""
While this app analyzes salary disparities between NBA and WNBA players, the numbers tell only part of the story. Women's basketball is experiencing a cultural breakthrough—from record-breaking viewership to viral social media moments—yet equity in pay, coverage, and representation remains a pressing challenge. These snapshots below help contextualize the data you’ve seen, grounding it in the real momentum and barriers facing women in professional sports today.
         

📺 Only 15% of National Sports Coverage Goes to Women
Despite their achievements, women’s sports made up just 15% of national coverage in 2023.
            
🏀 18.7 Million Viewers Watched the 2024 Women’s NCAA Championship
It was the most-watched basketball game (college or professional, men's or women’s) since 2019.

🏆 Boston Has No WNBA Team
Despite being a massive sports hub, Boston—home to iconic teams—still lacks a WNBA franchise.
            
💸 WNBA Salaries Lag Behind Men’s
Professional women’s players earn only a fraction of what their male counterparts make—an issue fans hope will shift with more visibility.
            
🌍 Women’s Basketball is Driving Cultural Change
The surge in viewership is reshaping perceptions of women’s sports and offering real representation for young girls.
            
🎥 Social Media is a Game-Changer
Platforms like TikTok and Instagram helped amplify players like Angel Reese and JuJu Watkins, increasing engagement with the sport.
            
🤝 Community Drives Viewership
Sports fandom isn’t just about gameplay—it’s about connection. Women’s basketball is finally building that same loyal community.

💥 Rising Stars are Helping Make Change: Caitlin Clark Broke Records & Social Media
She became the all-time NCAA scoring leader, surpassing both men's and women’s records. Her highlights went viral across TikTok and Instagram.

Sources:
            
- https://herhoopstats.com/salary-cap-sheet/wnba/players/salary_2024/stats_2023/

- https://hoopshype.com/salaries/players/

- https://therearview.org/the-growing-popularity-of-womens-basketball-and-why-it-matters/ 
            
            """)
