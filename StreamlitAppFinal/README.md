# 🏀 NBA vs WNBA Salary Analysis App

## Overview

This interactive Streamlit app explores the **gender pay gap** in professional basketball using salary data from **NBA** and **WNBA** players. It allows users to visualize salary distributions, search for specific athletes, upload their own datasets, and compare top male and female earners.

## 🔗 Link to App: 
["https://hanson-python-portfolio-pkcafb3sbrmbhdvpapxk9v.streamlit.app/"]

## 🌟 Features

- 📊 Summary statistics comparing NBA vs WNBA salaries  
- 📦 Boxplots and histograms of salary distribution  
- 🔍 Player search and comparison (with Wikipedia profile images)  
- 📥 Upload your own Excel data  
- 📤 Download cleaned data  
- 💬 Contextual insights into gender equity in sports

## 🎯 Purpose

To raise awareness and encourage discussion around the pay gap and gender equity in professional basketball. This tool is both educational and interactive, designed for students, fans, and advocates of women’s sports.

## 📂 File Requirements

Uploaded files must be Excel (`.xlsx`) format with these columns:
- `Rank`
- `Player`
- `Salary`
- `Gender` (as "M" or "F")

## 🚀 Deployment

You can deploy this app using [Streamlit Community Cloud](https://streamlit.io/cloud).  
Make sure your folder contains:
- `StreamlitAppFinal.py` (or `app.py`)
- `NBAvsWNBA1.xlsx`
- `README.md`
- `requirements.txt` (include `pandas`, `matplotlib`, `seaborn`, `streamlit`, `openpyxl`, and `wikipedia`)

## 🔧 Setup Instructions

```bash
pip install -r requirements.txt
streamlit run StreamlitAppFinal.py
```

## 📸 Sneakpeak

Below is an example of the first visualization and the summary statistics that can either be the default dataset or your own:
<img width="1388" alt="Screenshot 2025-05-07 at 12 53 24 AM" src="https://github.com/user-attachments/assets/bcc67f9f-b941-451a-8a8a-269defae2cc8" />

Below displays how you can select different female and male players to compare salaries and alongside their visuals sourced from Wikapedia:
<img width="1403" alt="Screenshot 2025-05-07 at 12 52 49 AM" src="https://github.com/user-attachments/assets/d58a95c3-094e-4694-b333-a3c0a9baa195" />


## 🔗 Resources used:

- https://herhoopstats.com/salary-cap-sheet/wnba/players/salary_2024/stats_2023/

- https://hoopshype.com/salaries/players/

- https://therearview.org/the-growing-popularity-of-womens-basketball-and-why-it-matters/
