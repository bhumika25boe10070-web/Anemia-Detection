import pandas as pd

df = pd.read_csv("DATA/raw.csv")

# Create anemia label
def create_label(row):
    hb = row['Hemoglobin']
    sex = row['Sex']

    if sex == 'M':
        return 1 if hb < 13 else 0
    else:
        return 1 if hb < 12 else 0

df['Anemia_Label'] = df.apply(create_label, axis=1)

# Save processed file
df.to_csv("DATA/processed.csv", index=False)

print("Processed dataset saved with Anemia_Label column!")
