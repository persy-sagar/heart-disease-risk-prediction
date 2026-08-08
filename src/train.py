import joblib
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
# pyrefly: ignore [missing-import]
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, recall_score, roc_auc_score

from preprocess import load_and_preprocess

X_train, X_test, y_train, y_test, encoders = load_and_preprocess()

models = {
    "LogisticRegression": LogisticRegression(max_iter=1000),
    "RandomForest": RandomForestClassifier(random_state=42),
    "XGBoost": XGBClassifier(eval_metric='logloss', random_state=42)
}

best_model = None
best_score = 0

for name, model in models.items():
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    recall = recall_score(y_test, preds)
    auc = roc_auc_score(y_test, preds)
    print(f"{name} -> Accuracy: {acc:.3f}, Recall: {recall:.3f}, ROC-AUC: {auc:.3f}")

    if recall > best_score:   # prioritizing recall since missing disease is worse than a false alarm
        best_score = recall
        best_model = model
        best_name = name

print(f"\nBest model: {best_name}")

os.makedirs('models', exist_ok=True)
joblib.dump(best_model, 'models/model.pkl')
joblib.dump(encoders, 'models/encoders.pkl')
print("Saved model to models/model.pkl")