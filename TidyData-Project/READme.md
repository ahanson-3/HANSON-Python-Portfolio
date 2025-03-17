# 📊 Tidy Data Project 🧹

## Project Overview 💡

This project applies the principles of tidy data to clean and visualize a dataset using Python. The goal is to ensure that the dataset adheres to tidy data principles, such as:

* Each variable in its own column
* Each observation in its own row
* Each type of observational unit in its own table

In this project, a Jupyter Notebook is used to clean the data, transform it, and perform basic exploratory data analysis.

## Dataset Description 📊

This project uses 2008 Summer Olympics data given for this project. The dataset contains Olympians, their gender, their events, and their medals.

### Pre-processing steps:
* Cleaned missing data and handled incorrect entries.
* Reshaped the data into a tidy format.
* Applied transformations like splitting columns or cleaning strings where necessary.

## 🧹 Data Cleaning & Tidy Process

The data was cleaned and transformed following the tidy data principles:
* **Reshaping**: Melting and pivoting the dataset as needed.
* **Splitting columns**: Using string functions to separate combined columns.
* **Cleaning**: Removing unwanted characters or handling missing values.

## 📈 Visualizations

Various visualizations were created to explore the cleaned data. These visualizations help to better understand the insights from the dataset.

## 🧑‍💻 Pivot-Table & Aggregation

The cleaned dataset was analyzed using pivot tables to aggregate the data and compute summary statistics.

## 📚 References

- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
- [Tidy Data Principles](https://vita.had.co.nz/papers/tidy-data.pdf)

## 🏆 Conclusion

*This notebook performed data cleaning and visualization on a dataset of Olympic medalists.*

### Key takeaways:

1. **Data Transformation**: The original wide-format data was successfully converted into a tidy long format, where each variable had its own column, each observation its own row, and relevant observations were retained, removing empty medal entries and NaN values.

2. **Visualizations**: Visualizations like countplots and barplots helped identify trends in medal distribution by gender and sport. Heatmaps provided a concise overview of medal counts across various sports, highlighting gender disparities and dominant sports.

3. **Aggregation**: Pivot tables and grouped counts provided quantitative summaries of the data, allowing further insights into medal distributions based on gender and sport.

4. **Key Findings**: The analysis revealed dominant sports (athletics, swimming, gymnastics), gender disparities in some sports, and sports with more balanced participation. The visualizations offered a clear and accessible way to understand the data, enabling a deeper understanding of the medal distribution amongst male and female participants.
