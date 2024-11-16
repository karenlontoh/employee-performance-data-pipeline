# **Employee Performance Analysis Pipeline 👔📊**

An end-to-end data pipeline for analyzing employee performance using PostgreSQL, Apache Airflow, Elasticsearch, and Kibana.

## **Introduction 🏢**

Kahn (2018), in his study on Psychological Conditions of Personal Engagement and Disengagement at Work, demonstrated a strong connection between high employee performance and positive business outcomes. To foster a productive workforce that maximizes potential, ABC Company conducts employee performance analysis to identify areas for improvement and growth.

## **Project Objectives 🎯**

The goal of this project is to understand the factors influencing employee productivity, enabling the HR team to develop policies that enhance both performance and job satisfaction.

## **Problem Breakdown 🔍**

1. What is the distribution of employee performance scores across different ranges?
2. How does performance vary across different departments?
3. What is the relationship between employee satisfaction and performance scores?
4. How does gender impact performance scores?
5. How do work hours per week influence performance scores?
6. How does salary range affect performance scores?

## **Dataset Overview 📂**

Sourced from [Kaggle](https://www.kaggle.com/datasets/mexwell/employee-performance-and-productivity-data), the dataset contains comprehensive employee performance information.

### **Table Overview**

| No | Column Name                | Description                                              |
|----|----------------------------|----------------------------------------------------------|
| 1  | Employee_ID                | Unique identifier for each employee                      |
| 2  | Department                 | Department of the employee (e.g., Sales, HR, IT)         |
| 3  | Gender                     | Gender of the employee (Male, Female, Other)             |
| 4  | Age                        | Age of the employee (22-60)                              |
| 5  | Job_Title                  | Job role (e.g., Manager, Analyst, Developer)             |
| 6  | Hire_Date                  | Date the employee was hired                              |
| 7  | Years_At_Company           | Number of years with the company                         |
| 8  | Education_Level            | Highest education attained (e.g., Bachelor, Master)      |
| 9  | Performance_Score          | Performance rating (1 to 5 scale)                        |
| 10 | Monthly_Salary             | Monthly salary (USD)                                     |
| 11 | Work_Hours_Per_Week        | Weekly work hours                                        |
| 12 | Projects_Handled           | Total projects handled                                   |
| 13 | Overtime_Hours             | Overtime hours in the last year                          |
| 14 | Sick_Days                  | Sick days taken                                          |
| 15 | Remote_Work_Frequency      | % of time worked remotely (0% - 100%)                    |
| 16 | Team_Size                  | Number of team members                                   |
| 17 | Training_Hours             | Training hours completed                                 |
| 18 | Promotions                 | Number of promotions received                            |
| 19 | Employee_Satisfaction_Score| Satisfaction score (1.0 to 5.0 scale)                    |
| 20 | Resigned                   | Boolean indicating if the employee resigned              |

## **Methodology 🔧**

1. **Input Data to PostgreSQL**: Initial data storage in PostgreSQL for structured management.
2. **ETL with Apache Airflow**: Airflow DAGs handle data extraction, transformation, and loading processes.
3. **Data Cleaning**: Essential cleaning performed within Airflow with validation checks.
4. **Loading to Elasticsearch**: Cleaned data is pushed to Elasticsearch for indexing.
5. **Visualization with Kibana**: Dashboards created in Kibana for data exploration and analysis.

## **Conclusion 📊**

- **Department Performance**: Engineering and Operations departments perform the best, while IT, HR, and Customer Support need targeted improvements.
- **Employee Satisfaction**: Higher satisfaction correlates with better performance, though not universally significant.
- **Salary Impact**: Employees earning $6,000-$10,000/month perform better.
- **Performance Distribution**: Most employees score between 1-3, highlighting a need to support underperformers.
- **Gender Analysis**: No significant difference across genders.
- **Work Hours**: Optimal performance peaks at 30 hours/week; declines with excessive hours.

## **Recommendations 💡**

1. **Review Salaries and Incentives**: Increase incentives for lower salary brackets to enhance productivity.
2. **Support for Underperformers**: Provide training and mentorship programs.
3. **Promote Work-Life Balance**: Avoid excessive work hours to maintain peak productivity.
4. **Apply Best Practices**: Share successful strategies from Engineering/Operations with other departments.
5. **Enhance Satisfaction**: Introduce employee recognition programs and growth opportunities.

## **Dependencies 📚**

- **Database**: PostgreSQL
- **ETL Tool**: Apache Airflow
- **Search Engine**: Elasticsearch
- **Visualization Tool**: Kibana

### **Libraries Used 🛠️**

- Pandas
- GreatExpectation
- Elasticsearch
- Apache Airflow

## Author 👩‍💻
Karen Lontoh  
LinkedIn: [Karmenia Ditabaya Lontoh](https://www.linkedin.com/in/karmenia-lontoh/)
