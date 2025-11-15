import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import joblib

# Load data
df = pd.read_csv('data/NY-House-Dataset.csv')

# Select features
features = [
    'TYPE', 'BEDS', 'BATH', 'PROPERTYSQFT', 'ADMINISTRATIVE_AREA_LEVEL_2',
    'LOCALITY', 'SUBLOCALITY', 'STREET_NAME', 'LATITUDE', 'LONGITUDE'
]
target = 'PRICE'

# Drop rows with missing target
df = df.dropna(subset=[target])

# Fill missing values for features
for col in features:
    if df[col].dtype == 'object':
        df[col] = df[col].fillna('Unknown')
    else:
        df[col] = df[col].fillna(df[col].median())

X = df[features]
y = df[target]

# Categorical and numerical features
categorical = ['TYPE', 'ADMINISTRATIVE_AREA_LEVEL_2', 'LOCALITY', 'SUBLOCALITY', 'STREET_NAME']
numerical = ['BEDS', 'BATH', 'PROPERTYSQFT', 'LATITUDE', 'LONGITUDE']

# Preprocessing
preprocessor = ColumnTransformer([
    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical),
    ('num', SimpleImputer(strategy='median'), numerical)
])

# Model pipeline
model = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', GradientBoostingRegressor(n_estimators=200, random_state=42))
])

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train
model.fit(X_train, y_train)

# Evaluate
score = model.score(X_test, y_test)
print(f'Model R^2 score: {score:.3f}')

# Save model
joblib.dump(model, 'models/advanced_house_price_model.joblib')
print('Model saved as models/advanced_house_price_model.joblib')

# Simple appreciation projection
def project_future_price(current_price, years, annual_rate=0.04):
    """
    Project future price using compound annual growth rate.
    annual_rate: expected annual appreciation (default 4%)
    """
    return current_price * ((1 + annual_rate) ** years)

# Example usage:
# future_price = project_future_price(1000000, 5)
# print(f"Projected price in 5 years: ${future_price:,.2f}")
