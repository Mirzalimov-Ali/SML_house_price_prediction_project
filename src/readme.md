# 📂 src Folder Structure

`src/` folderi projectning **asosiy Python codelari** saqlanadigan folder.
Bu yerda har bir file alohida module sifatida yozilgan, va ichida turli **class** lar mavjud.  
Ular malumotlarni tayyorlash, Feature Engineering va Model Training qilish jarayonlarini boshqaradi.

---

## 📁 feature_engineering.py
🔹 **FeatureCreate class** – yangi featurelar yasash uchun,
🔹 **FeatureSelection class** – muhim featurelarni tanlash uchun.  (※lekin bu faqatkina notebooks da ishlatilgan※)

---

## 📁 model_training.py
🤖 **Trainer class** – modelni uqitish va baholash uchun:  
- `train_test_split` – datasetni bulish  
- `KFold`, `cross_val_score` – cross-validation  
- `r2_score`, `mean_absolute_error` – model sifatini baholash  

---

## 📁 preprocessing.py
⚙️ **Preprocessing class** – datasetni oldindan tayyorlash uchun:  
- Fill missing values
- Encoding 
- Scaling  
- Log transformation  