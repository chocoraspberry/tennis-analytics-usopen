"""Reusable modeling helpers."""

from __future__ import annotations

import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, classification_report
from sklearn.model_selection import cross_validate


def cross_validate_model(model, X_train, y_train, cv, scoring=('accuracy', 'f1')):
    """Return mean cross-validation accuracy and F1."""
    results = cross_validate(model, X_train, y_train, cv=cv, scoring=list(scoring))
    return {
        'cv_accuracy': results['test_accuracy'].mean(),
        'cv_f1': results['test_f1'].mean(),
    }


def evaluate_classifier(model, X_train, X_test, y_train, y_test, model_name):
    """Fit a classifier and return predictions plus common metrics."""
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    metrics = {
        'model': model_name,
        'test_accuracy': accuracy_score(y_test, y_pred),
        'test_f1': f1_score(y_test, y_pred),
        'confusion_matrix': confusion_matrix(y_test, y_pred),
        'classification_report': classification_report(y_test, y_pred),
    }
    return y_pred, metrics


def append_result(results_list, model_name, cv_metrics, y_test, y_pred):
    """Append a compact model result row to a list."""
    results_list.append({
        'model': model_name,
        'cv_accuracy': cv_metrics['cv_accuracy'],
        'cv_f1': cv_metrics['cv_f1'],
        'test_accuracy': accuracy_score(y_test, y_pred),
        'test_f1': f1_score(y_test, y_pred),
    })
    return results_list


def results_table(results_list):
    """Convert model result dictionaries into a rounded DataFrame."""
    return pd.DataFrame(results_list).round(3)
