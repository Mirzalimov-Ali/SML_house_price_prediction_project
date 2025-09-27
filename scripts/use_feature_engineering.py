import pandas as pd
import os
from src.feature_engineering import FeatureCreation
from src.preprocessing import Preprocessing

df = pd.read_csv('data/preprocessed/preprocessed_house_price_prediction.csv')

# Feature creation
feature_creation = FeatureCreation(df)
df = (
    feature_creation.createFeatures().getDataset()
)

# Save engineered dataset
output_folder = 'data/engineered'
os.makedirs(output_folder, exist_ok=True)

output_path = os.path.join(output_folder, 'engineered_House_price_dataset.csv')
df.to_csv(output_path, index=False)

print(df.head(10))



# Encoding & Scaling & Transformation
preprocessing = Preprocessing(df)
df = (
    preprocessing.scale()
    .logTransformation()
    .getDataset()
)


# Save final dataset
folder = 'data/final'
os.makedirs(folder, exist_ok=True)

path = os.path.join(folder, 'final_dataset.csv')
df.to_csv(path, index=False)