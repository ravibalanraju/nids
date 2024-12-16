import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

def preprocess_data(filepath):
    data = pd.read_csv(filepath)
    data = data.dropna()
    X = data.drop('label', axis=1)
    y = data['label']
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)
    
    joblib.dump(scaler, 'models/scaler.pkl')
    
    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    X_train, X_test, y_train, y_test = preprocess_data('data/dataset.csv')
    print("Preprocessing completed.")
