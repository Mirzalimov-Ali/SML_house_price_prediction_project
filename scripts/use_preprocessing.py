import pandas as pd
import os
import logging
import src.logger
from src.preprocessing import Preprocessing

logger = logging.getLogger("scripts.use_preprocessing")  # fileni nomi yani scripts.use_preprocessing

df = pd.read_csv('data/raw/house_price_prediction.csv')
logger.info('Dataset loaded with shape %s', df.shape)

preprocessing = Preprocessing(df)
df = preprocessing.fillMissingValues().encode().getDataset()


# save dataset
output_folder = 'data/preprocessed'
os.makedirs(output_folder, exist_ok=True)

output_path = os.path.join(output_folder, 'preprocessed_house_price_prediction.csv')
df.to_csv(output_path, index=False)

logger.info("Preprocessed dataset saved at %s", output_path)

print(df.head(10))