import pandas as pd

from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, ExtraTreesRegressor, HistGradientBoostingRegressor, AdaBoostRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
import xgboost

from tabulate import tabulate
from joblib import dump
import os
from src.train import Trainer

# ____________________________________________ Single Split __________________________________________________

df = pd.read_csv('data/engineered/engineered_House_price_dataset.csv')

x = df.drop('price', axis=1)
y = df['price']

# _____________________________________________ train model __________________________________________________

models = [
    LinearRegression(),
    Lasso(alpha=0.001),
    Ridge(alpha=0.1),
    ElasticNet(alpha=0.0001),
    DecisionTreeRegressor(random_state=42),
    RandomForestRegressor(random_state=42, n_estimators=200),
    GradientBoostingRegressor(random_state=42, learning_rate=0.1, max_depth=5),
    ExtraTreesRegressor(random_state=42),
    HistGradientBoostingRegressor(random_state=42),
    SVR(kernel='rbf', C=20.0),
    KNeighborsRegressor(n_neighbors=5),
    xgboost.XGBRegressor(),
    AdaBoostRegressor()
]

results = []

for model in models:
    trainer = Trainer(model, x, y)
    trainer.train().evaluate()

    results.append([model.__class__.__name__, trainer.r2, trainer.mae, trainer.kfold.mean(), trainer.kfold.std()])

# ______________________________________________ tabulate ____________________________________________________

headers = ["Algorithm", "r2_score", "mean_absolute_error", "K-Fold Mean", "K-Fold Std"]
best_model = max(results, key=lambda x: x[1])
worst_model = min(results, key=lambda x: x[1])

green = "\033[92m"
red = "\033[91m"
reset = "\033[0m"

for row in results:
    if row == best_model:
        row[:] = [green + str(i) + reset for i in row]
    elif row == worst_model:
        row[:] = [red + str(i) + reset for i in row]

table = tabulate(results, headers=headers, tablefmt="grid", floatfmt=".6f")

print(table)

# _______________________________________ save compare algorithms _____________________________________________

def SaveComparison(table):
    with open('results/all_model_compare.txt', 'w') as f:
        f.write(table)

SaveComparison(table)

# ___________________________________________ save best model _________________________________________________

os.makedirs('model', exist_ok=True)
dump(HistGradientBoostingRegressor, 'model/HistGradientBoostingRegressor.joblib')