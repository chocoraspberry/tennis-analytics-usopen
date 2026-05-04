# Tennis Match Analysis & Prediction

This project analyzes the factors influencing singles tennis match outcomes on hard court and evaluates machine learning models for match prediction using ATP and WTA US Open dataset (2019-2024). A set of difference-based features are engineered to capture relative player performance, including rally consistency, serve performance, return performance and performance under pressure.

## Data Source
Data is sourced from Jeff Sackmann's repository:

[https://github.com/JeffSackmann](https://github.com/JeffSackmann/tennis_slam_pointbypoint)

Use the US Open point-by-point datasets from 2019–204; also use US Open matches datasets to create the tour column which indicates its a ATP or WTA match.

## Key Findings

- **Consistency matters more than power**  
  Players with lower unforced error rates are significantly more likely to win.

- **Controlled aggression is critical**  
  Higher winner rates strongly correlate with match success.

- **Performance under pressure matters**  
  Break point win percentage is a key factor, especially in WTA matches.

- **ATP vs WTA differences**  
  - ATP: net play has stronger impact  
  - WTA: break points and return quality are more important  

## Model Performance
- ATP best model: Random Forest (F1 ≈ 0.86)  
- WTA best model: XGBoost (F1 ≈ 0.92)

## Full Report

A detailed report including methodology, analysis, and conclusions is available here:

[Read the full report](report/final-report.pdf)

## License
Code in this repository is licensed under the MIT License.

The data is licensed separately under Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0). Non-commercial use only.
