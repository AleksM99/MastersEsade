# MastersEsade Python Assignments

This repository contains the Python assignments completed as part of the coursework for my Master's degree at Esade. These assignments cover a variety of exercises aimed at reinforcing Python programming concepts.

## Contents

1. **Session1**  
   This file contains foundational exercises on Python programming, covering topics such as:
   - Print statements and basic arithmetic
   - Conditional statements
   - Loops and iteration
   - Functions and input handling

2. **Session2**  
   This script contains more complex exercises, including:
   - FizzBuzz implementation
   - Filtering data types from a list
   - Simple to-do list implementation
   - Celsius to Fahrenheit conversion

Both scripts provide hands-on experience in implementing key Python concepts.

3. **Session3**

The Student Course Registration System is a Python-based application designed to manage students, courses, enrollments, and grades. The system allows students to enroll in courses, assign grades, and calculate GPAs. The project utilizes object-oriented programming principles like inheritance, encapsulation, and abstraction.

- Add and manage students and courses.
- Enroll students in courses and assign grades.
- Calculate GPA based on the enrolled courses and assigned grades.
- View all registered students and courses.

4. **Session4**
This notebook provides solutions to analyze and organize satellite annotation files. Each file follows a specific naming convention.

Structure:
{DATE}_{TIME}_SN{SATELLITE_NUMBER}_QUICKVIEW_VISUAL_{VERSION}_{UNIQUE_REGION}.txt

where: 
DATE: Formatted as YYYYMMDD (e.g., 20241201 for December 1, 2024).
TIME: Formatted as HHMMSS (e.g., 213430 for 21:34:30).
SATELLITE_NUMBER: An integer indicating the satellite number.
VERSION: The pipeline version, e.g., 0_1_2 or 1_3_1.
UNIQUE_REGION: A unique location identifier, e.g., SATL-2KM-10N_552_4164.

Requirements
Python 3.x
Jupyter Notebook
Standard libraries: glob, re, os

Within notebook:
1. Count Total Files
Counts the total number of .txt files in the annotations folder using glob.
2. Validate Filename Format
Checks how many files follow the specified naming convention by using regular expressions.
3. Annotations by Month and Year
Calculates the number of annotations per month and year and identifies the month with the highest count.
4. Organize Files by Month
Creates a new annotations folder structure where files are organized into subfolders named by month (YYYYMM).
5. Sort Annotations by Date
Sorts and prints all annotations from the most recent to the oldest based on date and time in the filename.
6. Satellite Analysis
Counts unique satellite numbers.
Determines the number of annotations per satellite.
Identifies the satellite used in the most recent annotation.
7. Count Unique Regions
Calculates the number of unique regions across all annotation files.

5. **Session5**

   Similar to session 4 however introduced more concepts that are simplifying the code. Those include imports of:
   glob for file management, regen for better syntax recovery, and systematic checks.


6. **Session6**

Data Analysis Homework Exercises with pandas

Requirements
To run the code and complete the exercises, you'll need the following:

Python 3.x
pandas library
Install pandas with:
pip install pandas

Dataset Descriptions:

Movies Dataset
Contains information on movies and series, including columns like release_year, country, and duration.

Titanic Dataset
Contains data on Titanic passengers with columns such as sex and survived.

Exercises
Check for Missing Values in Rating Column - We use the isnull() function to check for missing entries, helping ensure data integrity.

Count Films from Poland Released in 2021 - This is achieved by filtering rows where the release_year is 2021 and country is Poland.
Movies from 2020 with No Missing Values

Objective: Identify movies from 2020 that contain no missing values - This is accomplished by filtering for the year 2020 and ensuring all columns are complete.

Year with the Most Title - We use grouping and counting functions to identify the year with the highest number of entries.

Calculate Average Duration for Movies and Series in 2010 - Since movies are measured in minutes and series in seasons (e.g., "5 seasons"), we split and convert the duration as needed, then calculate the average separately for each type.


Titanic Dataset Exercises
Calculate Gender-Based Survival Percentage - By grouping data by sex and averaging the survived column, we find the percentage of survivors among men and women.

Calculate Survival Percentage Grouped by Gender and Class - Grouping by both sex and class allows us to see survival percentages across these categories, providing deeper insights into survival factors.

7.**Session 7**


Overview

File Structure
Assignment7.ipynb:
The primary Jupyter Notebook containing all relevant code, instructions, and analysis. 

Prerequisites
To run this assignment, ensure you have the following:

Python Environment: Install Python 3.7 or later.
Jupyter Notebook: Ensure Jupyter is installed. 
Required Libraries: Install the dependencies listed below:

pip install pandas

The notebook includes exercises focusing on Pandas II, specifically:

Handling Missing Data:
Potential transformations or imputations to manage gaps in datasets; often using other data.

Data Transformation:
Methods to reshape and manipulate data for analysis, such as pivoting, merging, or grouping; as well as creating new columns based on other ones; merging and joining two data frames.





