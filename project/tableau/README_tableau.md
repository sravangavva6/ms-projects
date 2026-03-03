# Tableau Dashboards – HIGGS Dataset Analysis

This document describes the Tableau dashboards developed to complement the Apache Spark–based machine learning analysis of the HIGGS dataset. The dashboards are designed to provide intuitive visual insights into data quality, model behavior, business interpretation, and scalability considerations.

---

## Tools Used
- **Tableau Desktop / Tableau Public**
- **Dataset:** HIGGS_small.csv (processed output from Spark pipeline)
- **Visualization Type:** Static and interactive dashboards

---

## Dashboard 1: Data Quality & Pipeline Monitoring

**Objective:**  
To monitor dataset integrity and preprocessing stability.

**Visualizations Included:**
1. Total number of records processed  
2. Class distribution (signal vs background)  
3. Zero-value presence in selected features  
4. Average feature values for sanity checking  

**Insight:**  
Ensures data consistency and validates preprocessing steps before model training.

---

## Dashboard 2: Model Performance & Feature Importance

**Objective:**  
To visually compare model performance and understand feature behavior.

**Visualizations Included:**
1. Model performance summary (ROC–AUC comparison)  
2. Bar chart comparing classification models  
3. Average values of selected key features  
4. Feature behavior across class labels  

**Insight:**  
Highlights the effectiveness of ensemble models and the relevance of selected features.

---

## Dashboard 3: Business Insights & Recommendations

**Objective:**  
To translate analytical results into domain-relevant insights.

**Visualizations Included:**
1. Signal vs background event volume  
2. Average feature values by class  
3. Feature stability indicators  
4. Text-based recommendation summary  

**Insight:**  
Supports decision-making by connecting data patterns to high-energy physics objectives.

---

## Dashboard 4: Scalability & Cost Analysis

**Objective:**  
To justify the use of distributed computing for large-scale analytics.

**Visualizations Included:**
1. Data volume distribution by class  
2. Feature dimensionality overview  
3. Feature magnitude comparison  
4. Scalability and cost recommendation summary  

**Insight:**  
Demonstrates how data size and dimensionality motivate the use of Apache Spark.

---

## How to Use
1. Open Tableau Desktop or Tableau Public  
2. Connect to the provided CSV dataset  
3. Load the dashboards from the Tableau workbook file  
4. Interact with filters and views to explore insights  

---

## Notes
- Dashboards intentionally use simple visualizations for clarity and interpretability.
- No advanced calculations or binning techniques are used.
- The dashboards are designed to complement, not replace, the Spark-based analysis.

---

## Author
Project developed as part of a Big Data Analytics and Machine Learning study using the HIGGS dataset.