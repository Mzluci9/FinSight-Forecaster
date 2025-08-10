# Portfolio Forecasting Project

## Overview
This project implements Tasks 1 and 2 of the Week 11 10 Academy challenge, focusing on preprocessing, EDA, and time series forecasting for TSLA.

## Folder Structure
- `data/raw/`: Raw YFinance data.
- `data/processed/`: Cleaned data.
- `notebooks/`: Jupyter notebooks for exploration and modeling.
- `scripts/`: Python scripts for data fetching, preprocessing, EDA, and modeling.
- `outputs/plots/`: Visualizations (including modeling/ for forecasts).
- `outputs/reports/`: Insights and reports.

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Run data fetching: `python scripts/data_fetch.py`
3. Run preprocessing: `python scripts/preprocess.py`
4. Run EDA: `python scripts/eda.py`
5. Run modeling: `python scripts/modeling.py`

## Outputs
- Cleaned data in `data/processed/`.
- Plots in `outputs/plots/` and `outputs/plots/modeling/`.
- Insights in `outputs/reports/insights.md` and `outputs/reports/task2_report.md`.