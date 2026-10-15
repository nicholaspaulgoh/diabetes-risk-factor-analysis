
# Diabetes Risk Factor Analysis

## Project Overview

This project explores a dataset containing 100,000 records to investigate patterns and associations between diabetes diagnosis status, demographic characteristics, lifestyle factors, and health measurements.

Using Python, Pandas, and Matplotlib, I performed exploratory data analysis (EDA), examined data quality, calculated descriptive statistics, and created visualisations to compare people with and without a recorded diabetes diagnosis.

The objective was to practise data analysis techniques and communicate meaningful findings through data-driven observations.

## Tools and Technologies

- **Python** — data analysis and scripting
- **Pandas** — data manipulation, grouping, aggregation, and cross-tabulation
- **Matplotlib** — data visualisation
- **CSV** — dataset input and handling

## Dataset Overview

The dataset contains 100,000 records and 31 original columns covering:

- **Demographics:** age, gender, ethnicity, education level, income level, and employment status
- **Lifestyle factors:** smoking status, alcohol consumption, physical activity, diet, sleep, and screen time
- **Medical history:** family history of diabetes, hypertension, and cardiovascular history
- **Health measurements:** BMI, waist-to-hip ratio, blood pressure, heart rate, cholesterol, glucose, insulin, and HbA1c
- **Diabetes information:** diabetes stage and recorded diagnosis status

I also created an age-group variable to compare diagnosis percentages across different age ranges.

## Data Quality Assessment

Before analysing the data, I:

- Inspected the dataset's dimensions, sample records, and column data types.
- Examined unique values in categorical columns and checked binary variables.
- Reviewed numerical minimum and maximum values for potentially suspicious measurements.
- Checked for missing values and duplicated rows.
- Compared `diabetes_stage` with `diagnosed_diabetes` to investigate label consistency.

The initial checks identified no missing cells or duplicated rows. However, I identified combinations of diabetes stage and diagnosis status that require further investigation, particularly for Type 1 and Gestational records.

## Exploratory Data Analysis

I performed the following analyses and created visualisations:

1. Diabetes diagnosis distribution
2. Age-group distribution
3. Percentage diagnosed with diabetes by age group
4. Average BMI by diagnosis status
5. Average fasting glucose by diagnosis status
6. Average HbA1c by diagnosis status
7. Average systolic blood pressure by diagnosis status
8. Average physical activity minutes per week by diagnosis status
9. Percentage diagnosed with diabetes by smoking status

I used `groupby()` to calculate group averages and `pd.crosstab()` to compare categorical variables and calculate within-group percentages.

## Key Findings

### 1. Diabetes Diagnosis Distribution

- 59,998 records (59.998%) were labelled as diagnosed with diabetes.
- 40,002 records (40.002%) were labelled as not diagnosed with diabetes.

The dataset therefore contains a higher proportion of diagnosed records. This describes the dataset's composition and should not be interpreted as diabetes prevalence in the general population.

### 2. Age-Group Patterns

The percentage of records labelled as diagnosed with diabetes increased across the age groups in my initial analysis:

- Ages 18–29: 48%
- Ages 30–39: 54%
- Ages 40–49: 57%
- Ages 50–59: 62%
- Ages 60–69: 66%
- Ages 70–79: 70%
- Ages 80–90: 72%

This suggests an association between age group and diagnosis status within the dataset. These results should be regenerated after validating the age-group boundaries.

### 3. BMI

- Average BMI without a recorded diagnosis: 25.19
- Average BMI with a recorded diagnosis: 25.90

The diagnosed group had a slightly higher average BMI, with a difference of 0.71 BMI units.

### 4. Fasting Glucose

- Average fasting glucose without a recorded diagnosis: 102.61
- Average fasting glucose with a recorded diagnosis: 116.79

The diagnosed group had a higher average fasting glucose level, with a difference of 14.18 recorded units.

### 5. HbA1c

- Average HbA1c without a recorded diagnosis: 5.84
- Average HbA1c with a recorded diagnosis: 6.97

The diagnosed group had a higher average HbA1c, with a difference of 1.13 recorded units.

### 6. Systolic Blood Pressure

- Average systolic blood pressure without a recorded diagnosis: 114.13
- Average systolic blood pressure with a recorded diagnosis: 116.91

The diagnosed group had a slightly higher average systolic blood pressure, with a difference of 2.78 recorded units.

### 7. Physical Activity

- Average physical activity without a recorded diagnosis: 129.33 minutes per week
- Average physical activity with a recorded diagnosis: 111.97 minutes per week

The diagnosed group reported approximately 17.36 fewer average physical activity minutes per week.

### 8. Sleep Duration

Both groups had an average reported sleep duration of 7.0 hours per day when rounded to one decimal place. Equal rounded averages do not necessarily mean the underlying distributions are identical.

### 9. Smoking Status

I compared the percentage diagnosed with diabetes across Never, Former, and Current smoking categories. The purpose was to examine whether diagnosis percentages differed between these groups. The exact percentages require verification against the calculated results before drawing conclusions.

## Limitations

- The dataset's source, sampling method, and representativeness have not yet been established.
- The findings describe associations and group differences; they do not demonstrate causation.
- Statistical significance has not been tested.
- The consistency of diabetes-stage and diagnosis labels requires further investigation.
- Measurement units and dataset definitions should be verified before clinical interpretations are made.
- The analysis is exploratory and does not provide medical diagnoses or individual risk predictions.

## Conclusion

This project demonstrates a practical exploratory data analysis workflow using Python, Pandas, and Matplotlib.

The analysis identified differences in fasting glucose, HbA1c, BMI, systolic blood pressure, and physical activity between records with and without a recorded diabetes diagnosis. It also identified an increasing proportion of diagnosed records across age groups in the initial analysis.

The project strengthened my skills in data inspection, data-quality assessment, aggregation, categorical analysis, and visualisation. Further validation and analysis would be needed before drawing broader conclusions.

## Future Improvements

- Validate the age-group boundaries and regenerate the affected results.
- Investigate the consistency of diabetes-stage and diagnosis labels.
- Add a correlation heatmap to explore relationships between numerical variables.
- Examine distributions and outliers in addition to group averages.
- Improve the visual presentation of charts and save them in a dedicated folder.


