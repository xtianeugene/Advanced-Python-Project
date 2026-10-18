from surprise import Dataset, Reader, SVD
from surprise.model_selection import cross_validate

data = Dataset.load_builtin("ml-100k")
algo = SVD()
cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=3)