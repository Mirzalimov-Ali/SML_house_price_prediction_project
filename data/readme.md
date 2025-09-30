# 📂 Data Folder Structure

Bu folderda projectda ishlatiladigan barcha malumotrlar saqlanadi.  
Datasetlar raw(hom) holatidan boshlab, tayyorlangan final versiyasigacha shu yerda bo‘ladi.

---

## 📁 [raw]

🗂 **Original dataset** (Kaggle yoki boshqa platformdan yuklab olingan).  
🚫 Hali ishlov berilmagan

---

## 📁 [preprocessed]

✨ **Tozalangan dataset**:

-   Fill missing values
-   Encoding qilingan (One-Hot, Label)

---

## 📁 [engineered]

🛠 **Feature engineering qilingan dataset**:

-   Yangi featurelar yasalgan - house_age, renovated, bath_per_bed, rooms_per_floor    
-   Scaling qilingan (MinMaxScaler)
-   Log transformation qilingan

> 🔎 Bu bosqichdagi dataset model sifatini oshirishga yordam beradi. 
-   R2 ↑

---

## 📁 [final]

🏁 **Tayyor dataset** – modelni training va test qilishda ishlatiladigan **Final dataset** shu yerda buladi.
