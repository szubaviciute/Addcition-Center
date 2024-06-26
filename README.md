# Addiction center

### Overview

This data analysis project aims to provide insights into the admissions of Lithuanian addiction center from 2016. By analyzing various aspects of the patient's data I aimed to identify trends and gain a deeper understanding of the severity of drug abuse (including alcohol, tobacco and narcotics) in Lithuania 

![Addiction_center-1](https://github.com/szubaviciute/Addcition-Center/assets/159541216/7595be9e-b48c-4f50-a806-d4e19ab238db)

### Data sources

The primary dataset used for this analysis is the "center.csv" file, containing detailed information about each patient admission to Lithuania's Addiction center. The data were collected from Lithuania's official data site https://data.gov.lt/datasets/2381/

### Tools

- Python - Data cleaning and analysis
- Power BI Desktop - visualization

### Data Cleaning/Preparation

The initial data preparation phase included following tasks:

- Data loading and inspection
- Removing not useful columns and duplicates
- Handling null values
- Renaming columns from Lithuanian to English
- Data cleaning and formatting

### Exploratory Data Analysis

EDA involved exploring the admission data to answer key questions, such as:

1. What are average years of addiction by acquired education
2. How old are most of the patients by admission number and what is their occupation 
3. Is there an increase in patient admission during the years

### Data Analysis snippet

Extracting only year from the date

``` py
df6['date'] = pd.to_datetime(df5['visit_date'])
print(df6)

df6['date'] = pd.to_datetime(df6['date'])
df6['year'], df6['month'] = df6['date'].dt.year, df6['date'].dt.month
df6
```

### Results

The analysis results are summarized as follows:

1. Most of the patients did not provide data for their acquired education, however the next group that finished only primary school topped period of addiction with 26 years
2. Most of the addmited patients are in 35-39 age bracket, while most of them are registered in the Labor Services
3. There is no increase in patient admission to addiction center overall (skipping COVID years 2019-2020), however repeated visits increased right after pandemic (2019-2020 shutdown)

### Recommendations

Based on the performed analysis, it seems that:

1. Most of the admitted patients have only finished primary school, while the least admitted patients have finished university. Thus, acquired education might play a role in the drug abuse 
2. Since there is no increase in the number of admissions during the years from 2016, it might mean the people are less and less afftected by addiction (including alcohol, tobacco and narcotics)
   
### Limitations

The Vilnius Addiction Center is the biggest center specialising in ambulatory services, however other cities might also have data on patient's admission. Thus having more datasets from other Lithuanian cities would be an advantage for future analysis to gather more insights on addiction severity in Lithuania

### References

- https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html
