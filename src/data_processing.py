"""Data processing helpers for tennis point and match data."""

from __future__ import annotations

import numpy as np
import pandas as pd


def safe_divide(numerator, denominator):
    """Divide safely, returning 0 where the denominator is 0 or missing."""
    denominator = np.asarray(denominator)
    return np.where(denominator > 0, numerator / denominator, 0)


def get_categorical_counts(df: pd.DataFrame, col_name: str):
    """Aggregate categorical point-level values by match and serving player."""
    dummies = pd.get_dummies(df[col_name], prefix=col_name)
    temp_df = pd.concat([df[['match_id', 'ServeIndicator']], dummies], axis=1)

    p1_counts = (
        temp_df[temp_df['ServeIndicator'] == 1]
        .groupby('match_id')
        .sum()
        .drop(columns='ServeIndicator', errors='ignore')
        .add_prefix('p1_')
    )
    p2_counts = (
        temp_df[temp_df['ServeIndicator'] == 2]
        .groupby('match_id')
        .sum()
        .drop(columns='ServeIndicator', errors='ignore')
        .add_prefix('p2_')
    )
    return p1_counts, p2_counts


def impute_zero_with_mean(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """Replace zero values with the non-zero mean for selected columns."""
    df = df.copy()
    for col in columns:
        non_zero_mean = df.loc[df[col] != 0, col].mean()
        df.loc[df[col] == 0, col] = non_zero_mean
    return df
