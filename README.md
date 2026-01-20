# Health Data Analysis with Python  
**Report**

## Question 1: Recursive Health Index Computation

### What was done
A recursive function was implemented to compute a Health Index \( H(x) \) defined by a recurrence relation with a base case \( H(0) = 0 \).

### How it was done
The recurrence relation was simplified so that each call computes the value using the previous result \( H(x-1) \). Input validation ensures that only non-negative integers are accepted; invalid inputs raise an error.

### Verification
Small values of \( x \) were computed manually and compared with the function output. The values matched exactly, confirming correctness.

---

## Question 2: Class-Based Patient Records

### What was done
A `PatientRecord` class was created to store patient information and health measurements and to compute averages for specific measurements.

### How it was done
The class constructor stores the patient name, age, and measurement dictionary. A static validation method checks that:
- Measurements are stored in a dictionary
- Each measurement value is a list
- All elements in the lists are numeric

The `average_measurement` method computes the mean of a selected measurement and raises an error if the measurement does not exist.

### Verification
Test data for blood pressure and heart rate were used. The computed averages matched hand-calculated values.

---

## Question 3: Lambda-Based BMI Classification

### What was done
A function was implemented to classify BMI values into standard categories such as Underweight, Normal, Overweight, and Obesity.

### How it was done
A lambda function was used internally to map BMI values to categories based on threshold comparisons. The function processes a list of BMI values and returns a dictionary mapping each value to its category.

### Verification
Known BMI examples were tested, and each value was assigned the correct category according to standard definitions.

---

## Question 4: Health Data Matrix Analysis

### 4.1 Row and Column Analysis

#### What was done
A function was written to analyze a 2D NumPy matrix by computing:
- The average of the second row
- The maximum value of the fourth column

If the matrix does not meet the required size, an informative message is printed.

#### How it was done
NumPy’s built-in mean and max functions were used. The function first checks the matrix dimensions before performing calculations.

#### Verification
The results were verified by manually inspecting the matrix values and confirming the calculations.

---

### 4.2 Row Transformation

#### What was done
A function was implemented to apply a user-defined transformation to a specific row of a matrix.

#### How it was done
The function accepts a callable transformation and applies it to all elements in the selected row. A lambda function was used to normalize a row by subtracting its mean and dividing by its standard deviation.

#### Verification
After transformation, the normalized row has a mean close to zero and a standard deviation close to one, confirming correct behavior.

---

## Question 5: Visualization of COVID-19 Data

### What was done
Real COVID-19 data from *Our World in Data* were used to create:
1. A scatter plot of daily new cases for a single country
2. A bar chart comparing total cases across three countries

### How it was done
The dataset was loaded locally using pandas. Matplotlib was used to generate the plots, with appropriate titles, axis labels, and legends. Input validation ensures that exactly three countries are provided for comparison.

### Verification
Plots were visually inspected to confirm that:
- The correct countries were selected
- Axis labels and titles were accurate
- Trends matched known COVID-19 patterns

---

## Errors and Issues Encountered

While loading the dataset, a warning about mixed data types appeared. This was resolved by adjusting the data-loading settings. The warning did not affect the correctness of the results.

---

## Conclusion

This assignment reinforced key Python concepts, including recursion, object-oriented design, functional programming, numerical analysis, and data visualization. Each result was validated through manual checks, logical reasoning, and visual inspection. The final solutions are correct, reusable, and maintainable.

---

## Files Included

- `answers.py` — Contains all implemented functions and classes  
- `report.md` — This report explaining methods, results, and verification
