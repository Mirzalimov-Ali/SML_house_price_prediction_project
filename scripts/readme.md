# 📂 Scripts Folder Structure

`scripts/` folderi projectning **asosiy jarayonlarini bajaradigan scriptlar** saqlanadigan joy.  
Bu scriptlar `src/` ichidagi classlardan foydalanib, **real ish jarayonini avtomatlashtiradi**.  
Har bir scriptda **logging** (`src/logger.py`) orqali jarayonlar log qilinadi.

---
## 📁 use_preprocessing.py

⚙️ **Datasetni Preprocess qilish (Preprocessing)**

- `Preprocessing` class yordamida:
  - Missing valuelarni tulldirish
  - Encoding qilish

- Natijani saqlaydi:
  - `data/preprocessed/preprocessed_house_price_dataset.csv`

- Datasetdan namunaviy qatorlarni (`head(10)`) chiqarib beradi

---
## 📁 use_feature_engineering.py

🛠 **Feature Engineering va Preprocessing jarayonlari**

- `FeatureCreation` class yordamida yangi featurelar yasaydi:
  - House Age  
  - Renovated  
  - Living-to-Lot Ratio  
  - Bath per Bed  
  - Rooms per Floor  
  - va boshqalar

- `Preprocessing` class yordamida:
  - Scaling  
  - Log Transformation  

- Tayyor datasetlarni saqlaydi:
  - `data/engineered/engineered_house_price_dataset.csv`
  - `data/final/final_dataset.csv`

---

## 📁 model_training.py

🤖 **Model Training va Comparison**

- Turli xil ML algoritmlari ustida training va baholash ishlari:
  - `LinearRegression`
  - `Lasso`
  - `Ridge`
  - `ElasticNet`
  - `DecisionTreeRegressor`
  - `RandomForestRegressor`
  - `GradientBoostingRegressor`
  - `ExtraTreesRegressor`
  - `HistGradientBoostingRegressor`
  - `SVR`
  - `KNeighborsRegressor`
  - `XGBoost (XGBRegressor)`
  - `AdaBoostRegressor`

- `Trainer` class yordamida:
  - `train_test_split`, `KFold`, `cross_val_score` orqali modelni training qilish
  - `r2_score` va `mean_absolute_error` orqali modelni baholash (evaluate)

- Natijalarni **tabulate** kutubxonasi bilan **table** kurinishda chiqaradi
- Natijalarni `results/all_model_compare.txt` filega saqlaydi
- Modelni `joblib` yordamida `model/` folderiga saqlaydi

---


