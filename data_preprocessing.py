import pandas as pd
import numpy as np  # <-- Add this line
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

# Load dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.csv"
df = pd.read_csv(url, header=None, names=[
    'Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
    'Insulin', 'BMI', 'DiabetesPedigree', 'Age', 'Outcome'
])

# Handle missing values (encoded as 0)
zero_columns = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
df[zero_columns] = df[zero_columns].replace(0, np.nan)  # <-- Use np.nan instead of pd.NA
imputer = SimpleImputer(strategy='mean')
df[zero_columns] = imputer.fit_transform(df[zero_columns])
# ... previous code ...
# Split data
X = df.drop('Outcome', axis=1)
y = df['Outcome']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Save processed data and scaler
pd.concat([pd.DataFrame(X_train_scaled), y_train.reset_index(drop=True)], axis=1).to_csv('train_data.csv', index=False)
pd.concat([pd.DataFrame(X_test_scaled), y_test.reset_index(drop=True)], axis=1).to_csv('test_data.csv', index=False)
import joblib
joblib.dump(scaler, 'scaler.joblib')


