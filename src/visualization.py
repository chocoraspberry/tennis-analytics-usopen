"""Plotting helpers for EDA notebooks."""

from __future__ import annotations

import math
import matplotlib.pyplot as plt
import seaborn as sns


def plot_hist(df, columns, n_cols=3, kde=True):
    """Plot histograms for multiple columns."""
    n_rows = math.ceil(len(columns) / n_cols)
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, n_rows * 5))
    axes = axes.flatten() if hasattr(axes, 'flatten') else [axes]

    for i, col in enumerate(columns):
        sns.histplot(df[col], kde=kde, ax=axes[i])
        axes[i].set_title(f'Distribution of {col}')
        axes[i].set_xlabel('')

    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()


def plot_box(df, columns, x='match_winner', hue=None, n_cols=3, figsize=(15, 5)):
    """Plot boxplots for multiple columns."""
    n_rows = math.ceil(len(columns) / n_cols)
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(figsize[0], figsize[1] * n_rows))
    axes = axes.flatten() if hasattr(axes, 'flatten') else [axes]

    for i, col in enumerate(columns):
        sns.boxplot(data=df, x=x, y=col, hue=hue, ax=axes[i])
        axes[i].set_title(col)
        if hue and i != 0 and axes[i].get_legend() is not None:
            axes[i].get_legend().remove()

    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()
