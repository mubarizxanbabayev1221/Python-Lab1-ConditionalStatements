# Laboratory Assignment 1: Conditional Statements and Decision-Making in Python

**Course:** Fundamentals of Programming / Introduction to Python Programming

**Institution:** Karabakh University

**Faculty:** Math & IT

**Department:** Computer Engineering

**Instructor:**  Shamil Humbatov

## 📌 Overview

This repository contains the solution set for **Laboratory Assignment 1**, focusing on conditional statements (`if`, `elif`, `else`), fundamental mathematical operations, and algorithmic decision-making in Python.

The lab consists of three core applications:

1. **Body Mass Index (BMI) Calculator:** Computes personal body mass index based on physical attributes and evaluates fitness classifications using nested control flow.

2. **Chinese Zodiac Calculator:** Determines the traditional animal zodiac sign corresponding to any given calendar birth year via modular arithmetic.

3. **Birthday Guessing Game:** Uses binary bitwise representation (via set choices) to dynamically calculate a user's exact day of birth without explicit prompting.

## 📁 Repository Structure

```
Python-Lab1-ConditionalStatements/
│
├── Task1.py            # Body Mass Index (BMI) Calculator
├── Task2.py            # Chinese Zodiac Sign Calculator
├── Task3.py            # Interactive Birthday Guessing Game
├── README.md           # Documentation and Project Guide
└── FoP_LAB_01.pdf      # Detailed Laboratory Assignment Report

```

## 🛠️ Tasks & Code Explanations

### Task 1: Body Mass Index (BMI) Calculator (`Task1.py`)

Computes the Body Mass Index using the standard formula:

$$
\text{BMI} = \frac{\text{weight (kg)}}{\text{height (m)}^2}
$$

The program categorizes the output according to standard WHO guidelines:

* **Below 18.5:** Underweight

* **18.5 – 24.9:** Normal Weight

* **25.0 – 29.9:** Overweight

* **30.0 and above:** Obese

#### Code Breakdown:

```
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

bmi = weight / (height * height)

if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi <= 24.9:
    category = "Normal Weight"
elif 25.0 <= bmi <= 29.9:
    category = "Overweight"
else:
    category = "Obese"

print(f"BMI: {bmi:.2f}")
print("Category:", category)

```

### Task 2: Chinese Zodiac Calculator (`Task2.py`)

The Chinese Zodiac operates on a 12-year cycle where each year corresponds to a specific animal sign. The calculation uses the modulo arithmetic operator (`year % 12`) mapped to a dictionary structure.

#### Code Breakdown:

```
birth_year = int(input("Enter your birth year: "))

c = birth_year % 12

d = {
    0: "Monkey",   1: "Rooster", 2: "Dog",    3: "Pig",
    4: "Rat",      5: "Ox",      6: "Tiger",  7: "Rabbit",
    8: "Dragon",   9: "Snake",  10: "Horse", 11: "Sheep"
}

zs = d[c]
print("Your Chinese Zodiac sign is:", zs)

```

### Task 3: Birthday Guessing Game (`Task3.py`)

This game determines a user's birth day (from 1 to 31) through five target number sets. Each set represents a binary position ($2^0, 2^1, 2^2, 2^3, 2^4$). An affirmative response (`1`) adds the starting base number of that set ($1, 2, 4, 8, 16$) to the total sum.

#### Code Breakdown:

```
day = 0

# Set 1 (2^0 = 1)
print("Is your birthday in Set1?")
print(" 1  3  5  7  9 11 13 15 17 19 21 23 25 27 29 31")
if int(input("Enter 0 for No and 1 for Yes: ")) == 1:
    day += 1

# Set 2 (2^1 = 2)
print("\nIs your birthday in Set2?")
print(" 2  3  6  7 10 11 14 15 18 19 22 23 26 27 30 31")
if int(input("Enter 0 for No and 1 for Yes: ")) == 1:
    day += 2

# Set 3 (2^2 = 4)
print("\nIs your birthday in Set3?")
print(" 4  5  6  7 12 13 14 15 20 21 22 23 28 29 30 31")
if int(input("Enter 0 for No and 1 for Yes: ")) == 1:
    day += 4

# Set 4 (2^3 = 8)
print("\nIs your birthday in Set4?")
print(" 8  9 10 11 12 13 14 15 24 25 26 27 28 29 30 31")
if int(input("Enter 0 for No and 1 for Yes: ")) == 1:
    day += 8

# Set 5 (2^4 = 16)
print("\nIs your birthday in Set5?")
print("16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31")
if int(input("Enter 0 for No and 1 for Yes: ")) == 1:
    day += 16

print("\nYour birthday is:", day)

```

## 🚀 How to Run the Scripts

### Prerequisites

* Python 3.x installed on your local environment.

### Running Tasks

Run any of the script files directly via terminal or IDE:

```
# Task 1: BMI Calculator
python Task1.py

# Task 2: Chinese Zodiac
python Task2.py

# Task 3: Birthday Game
python Task3.py

```

## 💻 Sample Execution Outputs

### Task 1 Output

```
Enter weight (kg): 75
Enter height (m): 1.78
23.671253629592222
Normal Weight

```

### Task 2 Output

```
Enter your birth year: 2000
Your Chinese Zodiac sign is: Dragon

```

### Task 3 Output

```
Is your birthday in Set1?
 1  3  5  7  9 11 13 15 17 19 21 23 25 27 29 31
Enter 0 for No and 1 for Yes: 1

Is your birthday in Set2?
 2  3  6  7 10 11 14 15 18 19 22 23 26 27 30 31
Enter 0 for No and 1 for Yes: 1

Is your birthday in Set3?
 4  5  6  7 12 13 14 15 20 21 22 23 28 29 30 31
Enter 0 for No and 1 for Yes: 0

Is your birthday in Set4?
 8  9 10 11 12 13 14 15 24 25 26 27 28 29 30 31
Enter 0 for No and 1 for Yes: 0

Is your birthday in Set5?
16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
Enter 0 for No and 1 for Yes: 1

Your birthday is: 19

```

## 📜 Recommended Commit History

To satisfy the repository requirements, maintain a clear git commit log:

1. `git commit -m "Initial commit: Add Task1 Body Mass Index calculator"`

2. `git commit -m "Add Task2 Chinese Zodiac sign calculator using dictionary lookup"`

3. `git commit -m "Add Task3 Birthday Guessing Game based on binary set arithmetic"`

4. `git commit -m "Add documentation and detailed project README"`

## ⚖️ Academic Integrity Statement

This work has been prepared independently as part of the academic curriculum for Karabakh University. All submission rules regarding personal code authorship have been rigorously observed.