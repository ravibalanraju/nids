from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
from preprocess import preprocess_data

def train_model():
    X_train, X_test, y_train, y_test = preprocess_data('data/dataset.csv')
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    print(f'Accuracy: {accuracy_score(y_test, y_pred)}')
    print(classification_report(y_test, y_pred))
    
    joblib.dump(model, 'models/trained_model.pkl')

if __name__ == "__main__":
    train_model()
