import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

# Load processed training data
train_data = pd.read_csv('train_data.csv')
X_train = train_data.iloc[:, :-1]
y_train = train_data.iloc[:, -1]

# Load processed test data
test_data = pd.read_csv('test_data.csv')
X_test = test_data.iloc[:, :-1]
y_test = test_data.iloc[:, -1]

# Train the logistic regression model
model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Save the trained model
joblib.dump(model, 'diabetes_model.joblib')
print("\nModel saved as 'diabetes_model.joblib'")
