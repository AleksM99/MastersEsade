# MastersEsade Python Assignments

This repository contains the Python assignments completed as part of the coursework for my Master's degree at Esade. These assignments cover a variety of exercises aimed at reinforcing Python programming concepts.

## Contents

1. **PFDS1.py**  
   This file contains foundational exercises on Python programming, covering topics such as:
   - Print statements and basic arithmetic
   - Conditional statements
   - Loops and iteration
   - Functions and input handling

2. **Lesson2.py**  
   This script contains more complex exercises, including:
   - FizzBuzz implementation
   - Filtering data types from a list
   - Simple to-do list implementation
   - Celsius to Fahrenheit conversion

Both scripts provide hands-on experience in implementing key Python concepts.

3. Project 3

The Student Course Registration System is a Python-based application designed to manage students, courses, enrollments, and grades. The system allows students to enroll in courses, assign grades, and calculate GPAs. The project utilizes object-oriented programming principles like inheritance, encapsulation, and abstraction.

- Add and manage students and courses.
- Enroll students in courses and assign grades.
- Calculate GPA based on the enrolled courses and assigned grades.
- View all registered students and courses.

Session 4
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

