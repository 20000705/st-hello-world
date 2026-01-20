# Lab 2 Report

## Personal Details
**Name:** Yifan Wang  
**Date:** 01/20/2026  

---

## Report Requirements Checklist
- [x] Self-contained and convincing  
- [x] Validated and verified results  
- [x] Explained "What" and "How" for each answer  
- [x] Used figures and plots with captions  
- [x] Code included only where necessary  
- [x] Explained errors and issues encountered  

---

## Homework Questions and Answers

### Answer to Question 1: Recursive Health Index Computation

#### What was done  
A recursive function was implemented to compute a Health Index \( H(x) \) defined by a recurrence relation with a base case \( H(0) = 0 \).

#### How it was done  
The recurrence relation was simplified so that each recursive call computes the value using the previous result \( H(x-1) \). Input validation was added to ensure that only non-negative integers are accepted; invalid inputs raise a `ValueError`. 

**Result:**  
`health_index(3) = 12`

---

### Answer to Question 2: Class-Based Patient Records

#### What was done  
A `PatientRecord` class was created to store patient information and associated health measurements and to compute averages for specific measurements.

#### How it was done  
The class constructor stores the patient’s name, age, and a dictionary of measurements. A static validation method ensures that:
- Measurements are provided as a dictionary  
- Each measurement value is stored as a list  
- All values in the lists are numeric  

The `average_measurement` method computes the mean of a requested measurement and raises an error if the measurement does not exist.

**Result:**  
`Average BP = 122.33`

---

### Answer to Question 3: Lambda-Based BMI Classification

#### What was done  
A function was implemented to classify BMI values into standard health categories: Underweight, Normal, Overweight, and Obesity.

#### How it was done  
A lambda function was used internally to apply threshold-based classification rules. The function processes a list of BMI values and returns a dictionary mapping each value to its category.

**Result:**  
`{16.5: 'Underweight', 22.4: 'Normal', 27.3: 'Overweight', 31.8: 'Obesity'}`

---

### Answer to Question 4: Health Data Matrix Analysis

#### 4.1 Row and Column Analysis

##### What was done  
A function was written to analyze a 2D NumPy matrix by computing the average of the second row  and the maximum value of the fourth column.

If the matrix does not meet the required size, an informative message is printed.

##### How it was done  
NumPy’s built-in `mean` and `max` functions were used for clarity and numerical stability. Matrix dimensions are checked before accessing rows and columns.

**Result:**  
`[59.125, 130.0]`

---

#### 4.2 Row Transformation

##### What was done  
A function was implemented to apply a user-defined transformation to a specific row of a matrix.

##### How it was done  
The function accepts a callable transformation and applies it element-wise to the selected row. A lambda function was used to normalize the row by subtracting its mean and dividing by its standard deviation.

**Result:** 
`row_transform (row 1 normalized):
 [[ 70.           1.75        22.9        120.        ]
 [  0.41896332  -1.15051844  -0.69091317   1.42246829]
 [ 65.           1.6         25.4        110.        ]]`
 
---

### Answer to Question 5: Visualization of COVID-19 Data

#### What was done  
Real COVID-19 data were used to create a scatter plot showing daily new cases for a selected country and a bar chart comparing total cases across three countries. 

#### How it was done  
The dataset was loaded locally using pandas. Matplotlib was used to generate the plots with clear titles, axis labels, and legends. Input validation ensures that exactly three countries are provided for comparison.

**Figures:**  

*Figure 1:* Daily new COVID-19 cases for Germany  
![Scatter Plot of Daily Cases](Figure_1.png)  

*Figure 2:* Total COVID-19 cases for France, Spain, and Italy  
![Bar Chart of Total Cases](Figure_2.png)

---

## Errors and Issues Encountered

Several minor issues were encountered during implementation. When loading the COVID-19 dataset, a warning appeared due to mixed data types across columns. This occurred because the dataset contains numeric values, missing entries, and text fields. The issue was resolved by adjusting the data-loading settings and did not affect the correctness of the analysis.

In the matrix analysis section, an early version of the code did not check matrix dimensions before accessing rows and columns, which caused index errors for small test cases. Adding dimension validation resolved this issue.

Finally, when normalizing matrix rows, integer arrays caused unintended truncation of floating-point values. Converting the matrix to floating-point format before transformation fixed this problem.


---

## References
- Our World in Data COVID-19 Dataset  
- NumPy Documentation  
- Pandas Documentation  
- Matplotlib Documentation  


