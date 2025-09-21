# Olist Sales Analytics Platform

**Company Dataset:** Olist (Brazilian E-commerce)  
**Role:** Data Analyst – Sales Analytics Division  

---

## Project Overview
This project analyzes the **Olist E-commerce dataset** to provide insights into **sales performance, customer behavior, product categories, and seller efficiency**.  
The platform combines **PostgreSQL for database management, Python for analysis, and visualization tools** to deliver data-driven insights for business stakeholders.

---

## Key Analytics Areas
- **Sales Performance Analysis** – Order volume, revenue tracking, and transaction trends  
- **Customer Segmentation** – Demographic and behavioral analytics from customer dataset  
- **Product Category Analysis** – Performance of categories across marketplaces  
- **Geographic Sales Distribution** – Regional sales heatmaps across Brazil  
- **Seller Performance** – Seller ratings, delivery efficiency, and revenue generation  
- **Payment Analysis** – Payment methods, installments, and transaction behavior  
- **Review Analysis** – Customer feedback trends and satisfaction metrics  
- **Logistics & Delivery** – Delivery time, delays, and carrier performance  
- **Seasonal Trends** – Sales during holidays, Black Friday, and seasonal peaks  

---

## Tech Stack
- **Database:** PostgreSQL (via pgAdmin)  
- **Programming:** Python (pandas, psycopg2, matplotlib)  
- **Visualization:** Matplotlib, Seaborn, Plotly  
- **Data Source:** Olist E-commerce Dataset (Kaggle)  

---

## Features
- Normalized **relational database schema** for Olist datasets  
- ETL pipeline to load CSV data into PostgreSQL  
- **SQL queries** for KPIs and sales insights  
- Python scripts for **data analysis and visualization**  
- Schema diagram (**ER Diagram**) in pgAdmin  

---

## ERD of the data base
<img width="948" height="818" alt="image" src="https://github.com/user-attachments/assets/250407f2-4c4e-4856-8c10-602d925c0c69" />

---

## Screenshots

<img width="805" height="805" alt="image" src="https://github.com/user-attachments/assets/df9efe5b-a334-4521-b4c7-4d6e1c8f2571" />
<img width="749" height="338" alt="image" src="https://github.com/user-attachments/assets/acfe07ef-3ab7-4bc4-8e6d-5eee321e0729" />
<img width="958" height="934" alt="image" src="https://github.com/user-attachments/assets/6036549e-2cc6-451f-893a-6c1ec8f75a21" />

---

## Tools

- **Python 3.11** – Data analysis and ETL scripting  
- **PostgreSQL** – Database for Olist datasets  
- **pgAdmin 4** – Database management and schema visualization  
- **psycopg2** – PostgreSQL adapter for Python  
- **pandas** – Data manipulation and cleaning  
- **NumPy** – Numerical computations  
- **Matplotlib & Seaborn** – Data visualization  
- **Plotly (optional)** – Interactive dashboards  
- **Olist E-commerce Dataset** – Source data (from Kaggle)  

---

## Prerequisites

- **Python 3.8+** – for running scripts and data analysis  
- **PostgreSQL 13+** – database for storing Olist datasets  
- **pgAdmin 4** – (optional) for managing PostgreSQL visually  
- **pip** – Python package manager for installing dependencies  
- **Olist E-commerce Dataset** – source CSV files (from Kaggle)  

---

## Create a .env file and write there:

DB_HOST=localhost

DB_NAME=your_database_name

DB_USER=your_username

DB_PASSWORD=your_password

DB_PORT=5432

---

## To run the script:

python main.py

---
