# 🏀 NBA vs WNBA Salary Analysis App

## Overview

This interactive Streamlit app explores the **gender pay gap** in professional basketball using salary data from **NBA** and **WNBA** players. It allows users to visualize salary distributions, search for specific athletes, upload their own datasets, and compare top male and female earners.

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
