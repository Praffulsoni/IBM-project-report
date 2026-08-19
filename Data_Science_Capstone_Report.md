# Data Science Capstone Project Report

## Executive Summary
The project analyzes SpaceX Falcon 9 launch data and predicts first-stage landing success. The workflow covers REST API collection, Wikipedia scraping, data wrangling, exploratory visualization, SQL analysis, Folium mapping, Plotly Dash and supervised classification.

## Introduction
Reusable first stages can reduce launch cost and increase launch cadence. The analytical objective is to understand which launch characteristics are associated with successful landing and to build a binary classifier for landing outcome.

## Data Collection and Wrangling
SpaceX REST API records are retrieved with `requests` and normalized with pandas. Supplementary launch history is collected from the Wikipedia launch table with BeautifulSoup. The prepared dataset is cleaned and the landing outcome is represented as a binary `Class` target.

## EDA and Visualization
Exploratory analysis examines flight number, launch site, payload mass, orbit and yearly landing success. Seaborn/Matplotlib/Plotly visualizations are paired with analytical interpretations.

## SQL
SQL is used for distinct launch sites, payload aggregation, minimum payload, average payload, mission-outcome counts, maximum-payload booster versions and date/outcome filters.

## Folium
Folium maps launch-site coordinates and supports marker clustering and geographic interpretation.

## Plotly Dash
The dashboard uses dropdown filtering and callback-driven Plotly figures to explore launch-site and payload relationships interactively.

## Predictive Analysis
A scikit-learn pipeline preprocesses numerical and categorical features. Classification models are evaluated using a train/test split, cross-validation, accuracy and a confusion matrix.

## Conclusion
Landing reliability is associated with multiple factors rather than a single threshold. Flight experience, launch site, orbit and payload are useful together, motivating a multi-feature predictive model.

## Author
Prafful Soni
