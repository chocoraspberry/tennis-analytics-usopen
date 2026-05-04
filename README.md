# Tennis Match Analysis & Prediction

This project analyzes the factors influencing singles tennis match outcomes on hard court and evaluates machine learning models for match prediction using ATP and WTA US Open dataset (2019-2024). A set of difference-based features are engineered to capture relative player performance, including rally consistency, serve performance, return performance and performance under pressure. Logistic Regression, Random Forest, and XGBoost models are trained and compared with cross validation and test F1 score. 

All models achieved strong performance, with F1 score above 0.84 for ATP and 0.90 for WTA matches.Random Forest and XGBoost have the best results for ATP and WTA datasets respectively. Feature importance analysis shows that winner rate and unforced errors are the primary factors for match outcome. Break point performance is particularly important in WTA matches. Net point performance is particularly important in ATP matches. These findings prove the importance of rally consistency, controlled aggression, and performance under pressure for amateur players. 

## Data Source
Data is sourced from Jeff Sackmann's Tennis Abstract repository:

https://github.com/JeffSackmann

Use the US Open point-by-point datasets from 2019–204.

## Key Findings
- Consistency matters more than raw power.
- Higher winner rate is strongly associated with match success.
- Break point performance is important, especially in WTA matches.
- Net play appears more impactful in ATP matches.

## Project Structure
```text
notebooks/
  01_data_cleaning.ipynb
  02_eda.ipynb
  03_modeling.ipynb
src/
  data_processing.py
  feature_engineering.py
  modeling.py
  visualization.py
report/
  tennis_analysis_report.pdf
```

## License
Code in this repository is licensed under the MIT License.

The data is licensed separately under Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0). Non-commercial use only.
