# Tennis Match Analysis & Prediction

This repository contains an exploratory data analysis (EDA) and machine learning project using professional tennis point data.

## Project Structure

```text
notebooks/
  01_data_cleaning.ipynb   # raw data loading, cleaning, aggregation, feature engineering
  02_eda.ipynb             # distributions, ATP/WTA comparisons, correlations
  03_modeling.ipynb        # logistic regression, random forest, XGBoost modeling
src/
  data_processing.py       # reusable cleaning and aggregation helpers
  visualization.py         # reusable plotting helpers
  modeling.py              # reusable model evaluation helpers
data/processed/            # generated processed files, ignored by git
images/                    # plots for README or reports
```

## How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run notebooks in order:

```text
01_data_cleaning.ipynb
02_eda.ipynb
03_modeling.ipynb
```

`01_data_cleaning.ipynb` creates `data/processed/analysis_df.csv`, which is loaded by the EDA and modeling notebooks.

## Data Source & License

This project uses tennis data from Jeff Sackmann / Tennis Abstract:

- Source: https://github.com/JeffSackmann
- License: Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)
- License text: https://creativecommons.org/licenses/by-nc-sa/4.0/

The data is used for non-commercial analysis. Any reuse of the data or derived data must comply with the original CC BY-NC-SA 4.0 license.

## Repository License

Code in this repository can be licensed separately from the dataset. If you choose MIT for the code, keep the data license notice above in the README.
