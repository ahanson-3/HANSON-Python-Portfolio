import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="NBA vs WNBA Salary Gap", layout="wide")

st.title("🏀 Gender Pay Gap in Professional Basketball")
st.markdown("""
This app highlights the **dramatic pay disparities** between **NBA** and **WNBA** players using real salary data.  
Explore how **gender inequality** persists in professional sports — and what the numbers really show.
""")

# Load data
uploaded_file = st.file_uploader("Upload your Excel file with Salary Data", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    
    # Basic cleaning
    df = df.dropna(subset=["Player", "Salary", "Gender"])
    df["Gender"] = df["Gender"].str.upper()
    
    # Summary
    st.subheader("📋 Summary Statistics")
    stats = df.groupby("Gender")["Salary"].describe().T
    st.dataframe(stats)

    # Gender comparison bar
    st.subheader("💰 Average Salary by Gender")
    avg_salaries = df.groupby("Gender")["Salary"].mean().reset_index()
    fig1, ax1 = plt.subplots()
    sns.barplot(data=avg_salaries, x="Gender", y="Salary", palette="pastel", ax=ax1)
    ax1.set_title("Average Salary: NBA vs WNBA")
    st.pyplot(fig1)

    # Salary distribution
    st.subheader("📊 Salary Distribution")
    fig2, ax2 = plt.subplots()
    sns.boxplot(data=df, x="Gender", y="Salary", palette="Set2", ax=ax2)
    ax2.set_title("Salary Distribution by Gender")
    st.pyplot(fig2)

    # Top player comparison
    st.subheader("🏆 Top Paid Players by Gender")
    top_n = st.slider("How many top-ranked players to show per gender?", min_value=5, max_value=30, value=10)
    top_male = df[df["Gender"] == "M"].nsmallest(top_n, "Rank")
    top_female = df[df["Gender"] == "F"].nsmallest(top_n, "Rank")

    st.markdown("#### 🔝 Top NBA Salaries")
    st.dataframe(top_male[["Rank", "Player", "Salary"]].reset_index(drop=True))

    st.markdown("#### 🔝 Top WNBA Salaries")
    st.dataframe(top_female[["Rank", "Player", "Salary"]].reset_index(drop=True))

    # Ratio visualization
    st.subheader("⚖️ Salary Ratio (WNBA to NBA)")
    if "M" in df["Gender"].unique() and "F" in df["Gender"].unique():
        male_avg = df[df["Gender"] == "M"]["Salary"].mean()
        female_avg = df[df["Gender"] == "F"]["Salary"].mean()
        ratio = female_avg / male_avg

        st.metric("WNBA Salary as % of NBA Salary", f"{ratio*100:.2f}%", delta=f"{(ratio-1)*100:.2f}%")

    st.markdown("""
    ---
    📢 **Why It Matters:**  
    Despite similar levels of training, competition, and commitment, women basketball players earn **a fraction** of what their male counterparts do.  
    Raising awareness is the first step toward **equity and change**.
    """)

else:
    st.info("👈 Upload an Excel file to begin. Expected columns: Rank, Player, Salary, Gender.")

