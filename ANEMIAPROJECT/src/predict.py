import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load trained model
model = joblib.load("MODELS/anemia_model.pkl")

# ---- USER INPUT VALUES ----
data = {
    "Age": [25],
    "Sex": ["M"],             # M or F
    "Hemoglobin": [12.5],
    "Hematocrit": [38],
    "RBC_count": [4.5],
    "MCV": [82],
    "MCH": [27],
    "MCHC": [32],
    "RDW": [12.5],
    "WBC": [6000],
    "Platelets": [250]
}

df = pd.DataFrame(data)

# ---- FIX: Convert all string columns into numbers ----
label_encoder = LabelEncoder()

for column in df.columns:
    if df[column].dtype == "object":
        df[column] = label_encoder.fit_transform(df[column])

# ---- Predict ----
prediction = model.predict(df)[0]

if prediction == 1:
    print("⚠️ Patient is ANEMIC")
else:
    print("✅ Patient is NOT anemic")
