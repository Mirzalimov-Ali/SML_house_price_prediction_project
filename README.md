# 🏠 House Price Prediction

![Python Version](https://img.shields.io/badge/Python-3.10-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## 📖 Projectning tavsifi
Ushbu project King County (Washington), US uylarning narxini bashorat qilishga moslangan.  
Maqsad: datalarni urganish, yangi featurelar yasash, data analysis qilish va turli regressor modellarini urgatib narhni aniqlik bilan predict qilish.

## 🔹 Future Vision
1. [Dataset](#-dataset)
2. [Yangi featurelar](#-yangi-featurelar)
3. [Data analysis & Visualization](#-Visualization)
4. [Modellar va natijalar](#-modellar-va-natijalar)
5. [Result](#-xulosa)
6. [Urnatish](#-Urnatish)
7. [License](#-License)

---

## 📊 Dataset
Datasetda uylar buyicha sotuv datalarni mavjud va quyidagi ustunlarni uz ichiga oladi:

|-------------------------------------------------------------------------|
| Columns        | Type     | desc                                        |
|----------------|----------|---------------------------------------------|
| id             | int      | Uyning unique ID si                         |
| date           | object   | Sotuv kuni                                  |
| price          | int      | Uy narxi (dollar)                           |
| bedrooms       | int      | Yotoq xonalar soni                          |
| bathrooms      | float    | Bathroom soni                               |
| sqft_living    | int      | Uyning maydoni (kv. fut)                    |
| sqft_lot       | int      | Tashqarri maydoni (kv. fut)                 |
| floors         | float    | Etajlar soni                                |
| waterfront     | int      | Suv manzarasi (0 = yo‘q, 1 = bor)           |
| view           | int      | Manzara ratingi (0-4)                       |
| condition      | int      | Uy holati (1-5)                             |
| grade          | int      | Uy sifati (1-13)                            |
| sqft_above     | int      | Yerdan yuqoridagi maydon                    |
| sqft_basement  | int      | Podval maydoni                              |
| yr_built       | int      | Uy qurilgan yili                            |
| yr_renovated   | int      | Oxirgi remont yili                          |
| zipcode        | int      | Pochta indeksi                              |
| lat            | float    | Kenglik                                     |
| long           | float    | Uzunlik                                     |
| sqft_living15  | int      | Atrofdagi uylarning urtacha yashash maydoni |
| sqft_lot15     | int      | Atrofdagi hovlilarning urtacha maydoni      |
| ----------------------------------------------------------------------- |


## 🔹 Yangi Featurelar
Projectda yangi Featurelar yasaladi, ular narxni yaxshiroq bashorat qilishga yordam beradi:

|----------------------------------------------------------------------------|
| Xususiyat           | Tavsif                                               |
|---------------------|------------------------------------------------------|
| house_age           | Uy yoshi (2025 yilga nisbatan)                       |    
| renovated           | Remont bulgani (1/0)                                 |
| living_to_lot_ratio | Yashash maydoni va hovli maydoni nisbati             |
| bath_per_bed        | Har bir yotoq xonaga tugri keluvchi bathroomlar soni |
| rooms_per_floor     | Har bir etajdagi xonalar soni                        |
| -------------------------------------------------------------------------- |

## 📈 Visualization (Data Anaylysis)
Barcha grafiklar `/visuals/` papkada saqlandi:

- Qurilgan yil buyicha urtacha narh
- Yashash maydoni vs narh
- Yotoq xonalar soni buyicha urtacha narh
- Etajlar soni buyicha urtacha narh
- Suv manzarasi buyicha urtacha narh
- Uy sifati (grade) buyicha narh
- Remontlangan va Remontlanmagan uylar
- Interaktiv scatter plot (plotly-express)

![Misol grafik](visuals/Price_vs_LivingArea.png)

---

## 🤖 Modellar va natijalar

| Algoritm                        | r2_score | mean_absolute_error | K-Fold Mean | K-Fold Std |
|---------------------------------|----------|---------------------|-------------|------------|
| LinearRegression                | 0.7786   | 0.1929              | 0.7775      | 0.0047     |
| Lasso                           | 0.7711   | 0.1957              | 0.7710      | 0.0036     |
| Ridge                           | 0.7783   | 0.1930              | 0.7770      | 0.0045     |
| ElasticNet                      | 0.7778   | 0.1933              | 0.7766      | 0.0044     |
| DecisionTreeRegressor           | 0.7790   | 0.1798              | 0.7699      | 0.0128     |
| RandomForestRegressor           | 0.8907   | 0.1256              | 0.8891      | 0.0035     |
| GradientBoostingRegressor       | 0.9038   | 0.1209              | 0.8996      | 0.0029     |
| ExtraTreesRegressor             | 0.8931   | 0.1232              | 0.8909      | 0.0028     |
| HistGradientBoostingRegressor   | 0.9061   | 0.1182              | 0.9032      | 0.0023     | ✅ Eng yaxshi model
| SVR                             | 0.8813   | 0.1325              | 0.8762      | 0.0047     |
| KNeighborsRegressor             | 0.7877   | 0.1783              | 0.7878      | 0.0024     |
| XGBRegressor                    | 0.9047   | 0.1190              | 0.8995      | 0.0036     |
| AdaBoostRegressor               | 0.7607   | 0.2049              | 0.7642      | 0.0079     | ❌ Eng yomon model

---

## 🔹 Xulosa
- Uy narxiga eng katta tasir qiluvchi faktorlar: **yashash maydoni, grade va suv manzarasi**.  
- Yangi va remont bulingan uylar qimmatroq.  
- Yasalgan yangi Featurelar (`house_age`, `living_to_lot_ratio`, `rooms_per_floor`) model aniqligini oshirdi.  
- Eng yaxshi model: **HistGradientBoostingRegressor** (R2 ≈ 0.906, MAE ≈ 0.118).

---

## ⚙️ O‘rnatish
```bash
git clone https://github.com/Mirzalimov-Ali/SML_house_price_prediction_project.git
cd SML_house_price_prediction_project
pip install -r requirements.txt