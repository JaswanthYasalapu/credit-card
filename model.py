import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

def load_and_preprocess_data(filepath):
    print("[1/5] Loading data...")
    df = pd.read_csv(filepath)
    
    print(f"Dataset loaded. Shape: {df.shape}")
    print(f"Class distribution:\n{df['Class'].value_counts(normalize=True) * 100}\n")
    
    # Scale the 'Amount' feature
    scaler = StandardScaler()
    df['scaled_amount'] = scaler.fit_transform(df['Amount'].values.reshape(-1, 1))
    joblib.dump(scaler, 'scaler.pkl')
    
    # Drop unnecessary columns for modeling
    df = df.drop(['Time', 'Amount'], axis=1)
    
    X = df.drop('Class', axis=1)
    y = df['Class']
    
    return train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

def handle_imbalance(X_train, y_train):
    print("[2/5] Balancing data via under-sampling...")
    # Get indices of both classes
    fraud_indices = np.array(y_train[y_train == 1].index)
    normal_indices = np.array(y_train[y_train == 0].index)
    
    # Randomly select normal indices to match the number of fraud cases
    random_normal_indices = np.random.choice(normal_indices, len(fraud_indices), replace=False)
    
    # Combine indices and extract subset
    balanced_indices = np.concatenate([fraud_indices, random_normal_indices])
    X_balanced = X_train.loc[balanced_indices]
    y_balanced = y_train.loc[balanced_indices]
    
    print(f"Balanced training set size: {len(y_balanced)} samples.\n")
    return X_balanced, y_balanced

def train_model(X_train, y_train):
    print("[3/5] Training Random Forest Classifier...")
    model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    print("[4/5] Evaluating model performance...")
    predictions = model.predict(X_test)
    probabilities = model.predict_proba(X_test)[:, 1]
    
    # Print metrics to terminal
    print("\n================ EVALUATION METRICS ================")
    print("\nConfusion Matrix:")
    cm = confusion_matrix(y_test, predictions)
    print(cm)
    
    print("\nClassification Report:")
    print(classification_report(y_test, predictions))
    
    auc_score = roc_auc_score(y_test, probabilities)
    print(f"ROC-AUC Score: {auc_score:.4f}")
    print("====================================================\n")
    
    return cm

def save_confusion_matrix_plot(cm):
    print("[5/5] Generating and saving evaluation plot...")
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=['Legit', 'Fraud'], 
                yticklabels=['Legit', 'Fraud'])
    plt.title('Confusion Matrix')
    plt.ylabel('True Class')
    plt.xlabel('Predicted Class')
    
    # Save chart as an image in the project directory
    output_filename = 'confusion_matrix.png'
    plt.savefig(output_filename, dpi=300, bbox_inches='tight')
    print(f"Success! Confusion matrix visualization saved as '{output_filename}'.")

if __name__ == "__main__":
    # Execute the entire pipeline end-to-end
    X_train, X_test, y_train, y_test = load_and_preprocess_data('creditcard.csv.zip')
    X_train_bal, y_train_bal = handle_imbalance(X_train, y_train)
    clf = train_model(X_train_bal, y_train_bal)
    joblib.dump(clf, 'fraud_model.pkl') 
    matrix = evaluate_model(clf, X_test, y_test)
    save_confusion_matrix_plot(matrix)