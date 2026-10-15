import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('diabetes-dataset.csv')

print(f"This dataset has {df.shape[0]} rows and {df.shape[1]} columns")

#inspecting the first five rows
print(f"First five rows: {df.head()}")

#data types of each column
print("Data Types:")
print(df.dtypes)



#check unique values in categorical columns
print("\nCategorical Columns:\n")

categorical_columns = [
    "gender",
    "ethnicity",
    "education_level",
    "income_level",
    "employment_status",
    "smoking_status",
    "diabetes_stage"
]

for column in categorical_columns:
    print(f"{column} : {df[column].unique()}")

print('\nBinary Columns:\n')

binary_columns = [
    "family_history_diabetes",
    "hypertension_history",
    "cardiovascular_history",
    "diagnosed_diabetes"
]

for column in binary_columns:
    print(f"{column} : {df[column].unique()}\n")

#check whether the numerical columns contain suspicious values
#print(df.describe().loc[['min','max']]) or
print(df.describe().T[['min','max']])

#check for missing cells/duplicated rows
print(f"\nNumber of duplicated rows: {df.duplicated().sum()}")
print(f"\nNumber of empty cells: \n{df.isnull().sum()}")

#Check diabetes diagnosis consistency
print(f"\n {pd.crosstab(df['diabetes_stage'], df['diagnosed_diabetes'],margins=True)}")

#Observations:
#Type 2: Every person has diagnosed_diabetes = 1
#No Diabetes and Pre-Diabetes: Every person has diagnosed_diabetes = 0
#Gestational and Type 1: The diagnosis flag is mixed. Some people have 0, while others have 1

#the percentage of people in each diabetes stage who have diagnosed_diabetes = 1
print(f"\n {pd.crosstab(df['diabetes_stage'], df['diagnosed_diabetes'], normalize="index").round(2)*100}")

#Observations:
#Gestational: 57% have diagnosis value 1, while 43% have 0
#No Diabetes: 100% have diagnosis value 0
#Pre-Diabetes: 100% have diagnosis value 0
#Type 1: 54% have diagnosis value 1, while 46% have 0
#Type 2: 100% have diagnosis value 1


#Number people in the dataset that have been diagnosed with diabetes
diagnosis_count =df['diagnosed_diabetes'].value_counts()
diagnosis_percentage= df['diagnosed_diabetes'].value_counts(normalize=True)
print(f"\nNumber of people with diabetes: {diagnosis_count[1]} ({diagnosis_percentage[1]:.2f})")
print(f"Number of people without diabetes: {diagnosis_count[0]} ({diagnosis_percentage[0]:.2f})")

print(f"Total records: {len(df)}")

# Group people by age and compare their diabetes diagnosis
df['age_group'] = pd.cut(
                    df['age'],
                 bins=[17,29,39,49,59,69,79,90],
                    labels=["18-29", "30-39", "40-49", "50-59", "60-69","70-79", "80-90"]
)

print(pd.crosstab(df['age_group'],df['diagnosed_diabetes'], normalize="index").round(2) *100)
#Diabetes diagnosis proportions increased across the age groups in the dataset, from 48% among people aged 18–29 to 72% among those aged 80–90.

print(df.groupby('diagnosed_diabetes')['bmi'].mean().round(2))
#higher BMI =/ diabetes
print()

print(df.groupby('diagnosed_diabetes')['glucose_fasting'].mean().round(2))
#suggests that people with a diabetes diagnosis have higher average fasting glucose in your dataset.
# It is an association, not proof that one factor caused the other.

print()
print(df.groupby("diagnosed_diabetes")["hba1c"].mean().round(2))

print()
print(df.groupby("diagnosed_diabetes")["systolic_bp"].mean().round(2))

print()
print(df.groupby("diagnosed_diabetes")["physical_activity_minutes_per_week"].mean().round(2))

print()
print(df.groupby("diagnosed_diabetes")["sleep_hours_per_day"].mean().round(2))

#bar charts

#distribution of people
num_diagnoses= df.groupby('diagnosed_diabetes')['diagnosed_diabetes'].count()
num_diagnoses.index= ["No diabetes", "Has diabetes"]
num_diagnoses.plot(kind='bar')
plt.title('Diabetes diagnosis distribution')
plt.xlabel('Diabetes Diagnosis')
plt.ylabel('Number of people')
plt.xticks(rotation=0)
plt.show()

#Age distribution
age_distribution= df['age_group'].value_counts().sort_index()
age_distribution.plot(kind='bar')
plt.title('Age group distribution')
plt.xlabel('Age Group')
plt.ylabel('Number of people')
plt.show()

#percentage diagnosed with diabetes by age group
age_diabetes= pd.crosstab(df['age_group'], df['diagnosed_diabetes'], normalize="index")*100
age_diabetes[1].plot(kind='bar')
plt.title('Diabetes positive by age distribution')
plt.xlabel('Age Group')
plt.ylabel('Percentage of people (%)')
plt.show()

#fasting glucose
fasting_glucose =df.groupby('diagnosed_diabetes')['glucose_fasting'].mean().round(2)
fasting_glucose.index=['No Diabetes', 'Has Diabetes']
fasting_glucose.plot(kind='bar')
plt.title('Average glucose fasting levels by diabetes diagnosis')
plt.xlabel('Diabetes Diagnosis')
plt.ylabel('Average glucose fasting levels')
plt.xticks(rotation=0)
plt.show()

#bmi
bmi_avg = df.groupby('diagnosed_diabetes')['bmi'].mean().round(2)
bmi_avg.index= ["No diabetes", "Has diabetes"]

bmi_avg.plot(kind='bar')
plt.title("Average Body Mass Index (BMI) by Diabetes Diagnosis")
plt.xlabel("Diabetes Diagnosis")
plt.ylabel("Average BMI")

plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

#HbA1c
hba1c =df.groupby('diagnosed_diabetes')['hba1c'].mean().round(2)
hba1c.index=['No Diabetes', 'Has Diabetes']
hba1c.plot(kind='bar')
plt.title('Average HbA1c levels by diabetes diagnosis')
plt.xlabel('Diabetes Diagnosis')
plt.ylabel('Average HbA1c levels')
plt.xticks(rotation=0)
plt.show()

#Systolic BP
systolic_bp = df.groupby('diagnosed_diabetes')['systolic_bp'].mean().round(2)
systolic_bp.index=['No Diabetes', 'Has Diabetes']
systolic_bp.plot(kind='bar')
plt.title('Average Systolic BP levels by diabetes diagnosis')
plt.xlabel('Diabetes Diagnosis')
plt.ylabel('Average Systolic BP levels')
plt.xticks(rotation=0)
plt.show()

#Physical Activity
physical_activity = df.groupby('diagnosed_diabetes')['physical_activity_minutes_per_week'].mean().round(2)
physical_activity.index=['No Diabetes', 'Has Diabetes']
physical_activity.plot(kind='bar')
plt.title('Average physical activity minutes per week by diabetes diagnosis')
plt.xlabel('Diabetes Diagnosis')
plt.ylabel('Average physical activity minutes per week')
plt.xticks(rotation=0)
plt.show()


# Percentage diagnosed with diabetes by smoking status
smoking_status = pd.crosstab(
    df["smoking_status"],
    df["diagnosed_diabetes"],
    normalize="index"
) * 100

smoking_status[1].plot(kind="bar")

plt.title("Percentage Diagnosed with Diabetes by Smoking Status")
plt.xlabel("Smoking Status")
plt.ylabel("People Diagnosed with Diabetes (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

