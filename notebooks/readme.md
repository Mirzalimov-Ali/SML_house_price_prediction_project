# 📒 Notebooks Folder

`notebooks/` folderida projectning **modelni tekshirish va analysis qilish** uchun Jupyter Notebook kurinishida yozilgan.  
Bu notebooklar orqali datasetni urganish, feature engineering, preprocessing, va model training qilingan.  

---

## 📁 Notebooklar tuzilishi

- `data_analysis.ipynb`  
- `preprocessing.ipynb`  
- `feature_engineering.ipynb`  
- `train.ipynb`  

---

## 📊 data_analysis.ipynb

🔎 **Exploratory Data Analysis (EDA)**  
Ushbu notebookda dataset ustida **vizualization va tahlil** ishlari qilingan.  

- `seaborn`, `matplotlib`, va `plotly.express` yordamida grafikalar:
  - **Scatterplot**: Price vs Living Area  
  - **Lineplot**: Average Price by Year Built  
  - **Boxplot**: Prices by Grade  
  - **Boxplot**: Renovated vs Not Renovated  
  - **Barplot**: Average Price by Bedrooms  
  - **Barplot**: Average Price by Floors  
  - **Barplot**: Waterfront vs Non-Waterfront  
  - **Interactive Scatterplot** (plotly-express): Price vs Living Area (Grade buyicha ranglangan)

📂 Grafiklar saqlangan folder: `visuals/`  
- `Price_vs_LivingArea.png`  
- `price_by_yearbuilt.png`  
- `price_by_grade.png`  
- `renovated_vs_notrenovated.png`  
- `price_by_bedrooms.png`  
- `price_by_floors.png`  
- `Price_by_Waterfront.png`  

---

## 🤖 train.ipynb

🧠 **Machine Learning modellari ustida training va evaluation (baholash)**  

### ✨ Feature Selection
- `FeatureSelection` class orqali **Correlation asosida feature tanlash**.  
- Filter Method
- Tanlangan featurelar list qilib chiqariladi.  

### 📌 Train-Test Split va K-Fold
- `train_test_split` bilan 80/20 split  
- `KFold` (5 splits, shuffle=True, random_state=42)  

### 🏗 Modellar
Quyidagi regression modellari solishtirilgan:  

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
- `XGBoost` (`XGBRegressor`)  
- `AdaBoostRegressor`  

### 📊 Nima bilan baholaymiz?
- `r2_score`  
- `mean_absolute_error`  
- `cross_val_score` (K-Fold mean va std)  

### 📋 Natijalar
- Natijalar `tabulate` orqali **table** kurinishida chiqariladi  
- **Eng yaxshi model yashil**, **eng yomon model qizil** bilan ajratiladi  

📂 Table jadval:  
+------------------------+--------------+-----------------------+
| Algorithm              |     r2_score |   mean_absolute_error |
+========================+==============+=======================+
| Linear Regression      | 0.7301693343 |          0.2126874839 |
+------------------------+--------------+-----------------------+
| Lasso                  | 0.7302675797 |          0.2132109342 |
+------------------------+--------------+-----------------------+
| Ridge                  | 0.7301555722 |          0.2126943250 |
+------------------------+--------------+-----------------------+
| ElasticNet             | 0.7299917816 |          0.7299917816 |
+------------------------+--------------+-----------------------+
| Decision Tree          | 0.7005376992 |          0.2137661003 |
+------------------------+--------------+-----------------------+
| Random Forest          | 0.8395371570 |          0.1549535657 |
+------------------------+--------------+-----------------------+
| Gradient Boosting      | 0.8431809155 |          0.1556232897 |
+------------------------+--------------+-----------------------+
| Extra Trees            | 0.8350939834 |          0.1553868609 |
+------------------------+--------------+-----------------------+
| Hist Gradient Boosting | 0.8460028493 |          0.1538798721 |
+------------------------+--------------+-----------------------+
| SVM                    | 0.8296088437 |          0.1609522148 |
+------------------------+--------------+-----------------------+
| KNN                    | 0.8158230832 |          0.1662507093 |
+------------------------+--------------+-----------------------+
| XGBoost                | 0.8376814810 |          0.1569496670 |
+------------------------+--------------+-----------------------+
| AdoBoost               | 0.7422633256 |          0.2131679344 |
+------------------------+--------------+-----------------------+


### 🏆 Eng yaxshi model
- **HistGradientBoostingRegressor** (R² ≈ 0.906, MAE ≈ 0.118)