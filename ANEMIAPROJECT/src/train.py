import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
import joblib

# 1. Load processed file
df = pd.read_csv("DATA/processed.csv")

# 2. Convert ALL string columns to numbers
label_encoder = LabelEncoder()

for column in df.columns:
    if df[column].dtype == 'object':   # If column is text
        df[column] = label_encoder.fit_transform(df[column])

# 3. Select features (X) and target (y)
X = df.drop("Anemia_Label", axis=1)
y = df["Anemia_Label"]

# 4. Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 5. Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# 6. Predict
preds = model.predict(X_test)

# 7. Report results
print("Accuracy:", accuracy_score(y_test, preds))
print(classification_report(y_test, preds))

# 8. Save model
joblib.dump(model, "MODELS/anemia_model.pkl")
print("Model saved successfully!")