import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load dataset
data = pd.read_csv("waste_dataset.csv")

wet_keywords = ["food", "fruit", "vegetable", "peel", "tea", "coffee", "egg"]
dry_keywords = ["plastic", "paper", "cardboard", "glass", "metal", "tin", "foil"]
ewaste_keywords = ["battery", "mobile", "charger", "laptop", "earphone",
                   "keyboard", "mouse", "power", "circuit"]

def classify_rule_based(item):
    item = item.lower()

    wet_score = sum(word in item for word in wet_keywords)
    dry_score = sum(word in item for word in dry_keywords)
    ewaste_score = sum(word in item for word in ewaste_keywords)

    if wet_score > dry_score and wet_score > ewaste_score:
        return "wet"
    elif dry_score > wet_score and dry_score > ewaste_score:
        return "dry"
    elif ewaste_score > wet_score and ewaste_score > dry_score:
        return "e-waste"
    else:
        return "unknown"

# Predictions
y_true = data["category"]
y_pred = data["item_name"].apply(classify_rule_based)

# Remove unknown predictions (optional but recommended)
mask = y_pred != "unknown"
y_true = y_true[mask]
y_pred = y_pred[mask]

# Evaluation
print("\nMethod 1: Rule-Based Semantic Classification\n")
print("Accuracy:", round(accuracy_score(y_true, y_pred) * 100, 2), "%")

print("\nClassification Report:\n")
print(classification_report(y_true, y_pred))

print("\nConfusion Matrix:\n")
print(confusion_matrix(y_true, y_pred))
