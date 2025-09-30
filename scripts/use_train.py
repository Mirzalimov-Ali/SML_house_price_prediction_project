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
from src.feature_engineering import FeatureSelection



import logging
import src.logger

logger = logging.getLogger('src.use_train')

# ____________________________________________ Single Split __________________________________________________

df = pd.read_csv('data/final/final_dataset.csv')

fs = FeatureSelection(df, target='price')
fs.filter_by_correlation()
selected_features = fs.get_selected_features()

# x = df[selected_features]
x = df.drop('price', axis=1)
y = df['price']

logger.info("Dataset loaded with shape %s", df.shape)

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
best_r2 = -float("inf") # eng kichkina mumkun bulgan infinity son
best_trained_model = None
best_model_name = ""

for model in models:
    trainer = Trainer(model, x, y)
    trainer.train().evaluate()

    results.append([model.__class__.__name__, trainer.r2, trainer.mae, trainer.kfold.mean(), trainer.kfold.std()])

    if trainer.r2 > best_r2:
        best_r2 = trainer.r2
        best_trained_model = trainer.model
        best_model_name = model.__class__.__name__

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

logger.info("\n%s", table)

# ___________________________________________ save comparison _________________________________________________

def SaveComparison(table):
    with open('results/all_model_compare.txt', 'w') as f:
        f.write(table)


SaveComparison(table)
logger.info("Comparison table saved at results/all_model_compare.txt")

# ___________________________________________ save best model _________________________________________________

if best_trained_model is not None:
    os.makedirs('model', exist_ok=True)
    save_path = f'model/{best_model_name}.joblib'
    dump(best_trained_model, save_path)
    logger.info("Best model '%s' saved successfully at '%s' with r2=%.6f", best_model_name, save_path, best_r2)
else:
    logger.error("No model was selected to save. Check the training loop.")