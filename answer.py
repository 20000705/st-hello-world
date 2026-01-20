import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Q1. Recursive Health Index Computation
def health_index(x):
    if not isinstance(x, int) or x < 0:
        raise ValueError("x must be a non-negative integer")

    if x == 0:
        return 0

    return 3 * x + x**2 - health_index(x - 1)

# Q2. Class-Based Patient Records
class PatientRecord:
    def __init__(self, name, age, measurements):
        self.name = name
        self.age = age

        PatientRecord.validate_measurements(measurements)
        self.measurements = measurements

    def average_measurement(self, measurement_name):
        if measurement_name not in self.measurements:
            raise KeyError(f"Measurement '{measurement_name}' not found")

        values = self.measurements[measurement_name]
        if len(values) == 0:
            raise ValueError(f"Measurement '{measurement_name}' has no values")

        return sum(values) / len(values)

    @staticmethod
    def validate_measurements(data):
        if not isinstance(data, dict):
            raise ValueError("Measurements must be a dictionary")

        for metric, series in data.items():
            if not isinstance(series, list):
                raise ValueError(f"Measurement '{metric}' must be a list")

            for v in series:
                if not isinstance(v, (int, float)):
                    raise ValueError(f"All values in '{metric}' must be numbers")


# Q3. Lambda-Based BMI Classifier
def classify_bmi(bmi_values):
    if not isinstance(bmi_values, list):
        raise ValueError("bmi_values must be a list")

    bmi_category = lambda bmi: (
        "Underweight" if bmi < 18.5 else
        "Normal" if bmi < 24.9 else
        "Overweight" if bmi < 29.9 else
        "Obesity"
    )

    result = {}
    for bmi in bmi_values:
        if not isinstance(bmi, (int, float)):
            raise ValueError("All BMI values must be numeric")
        result[bmi] = bmi_category(bmi)

    return result

# Q4. Health Data Matrix Analysis
# 4.1 Row and Column Analysis
def analyze_matrix(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        raise ValueError("matrix must be a 2D NumPy array")

    rows, cols = matrix.shape
    if rows < 2 or cols < 4:
        print("Invalid matrix size")
        return None

    avg_second_row = np.mean(matrix[1, :])
    max_fourth_col = np.max(matrix[:, 3])

    return np.array([avg_second_row, max_fourth_col])


# 4.2 Row Transformation
def row_transform(matrix, row, transform_fn):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        raise ValueError("matrix must be a 2D NumPy array")
    if not isinstance(row, int):
        raise ValueError("row must be an integer")
    if row < 0 or row >= matrix.shape[0]:
        raise IndexError("row index out of range")
    if not callable(transform_fn):
        raise ValueError("transform_fn must be callable")

    new_matrix = matrix.astype(float).copy()
    new_matrix[row, :] = transform_fn(new_matrix[row, :])
    return new_matrix


# Normalization lambda
normalize_row = lambda r: (r - np.mean(r)) / np.std(r) if np.std(r) != 0 else (r - np.mean(r))


# Q5. Visualization of COVID-19 Data
def plot_country_cases(country_name: str) -> None:
    df = pd.read_csv(
        "/home/yw24k/Downloads/owid-covid-data.csv",
        parse_dates=["date"],
        low_memory=False
    )

    country_data = df[df["location"] == country_name]

    if country_data.empty:
        raise ValueError(f"No data found for country: {country_name}")

    plt.figure(figsize=(10, 5))
    plt.scatter(
        country_data["date"],
        country_data["new_cases"],
        alpha=0.6,
        label=country_name
    )

    plt.title(f"Daily New COVID-19 Cases in {country_name}")
    plt.xlabel("Date")
    plt.ylabel("New Cases")
    plt.legend()
    plt.tight_layout()
    plt.show()


def compare_countries(countries: list[str]) -> None:
    if len(countries) != 3:
        raise ValueError("Exactly three countries must be provided")

    df = pd.read_csv(
        "/home/yw24k/Downloads/owid-covid-data.csv",
        low_memory=False
    )

    totals = []
    for country in countries:
        country_data = df[df["location"] == country]

        if country_data.empty:
            raise ValueError(f"No data found for country: {country}")

        totals.append(country_data["total_cases"].max())

    plt.figure(figsize=(8, 5))
    plt.bar(countries, totals, label="Total cases")

    plt.title("Total COVID-19 Cases Comparison")
    plt.xlabel("Country")
    plt.ylabel("Total Cases")
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Q1
    print("health_index(3) =", health_index(3))

    # Q2
    p = PatientRecord("John Doe",45,{"blood_pressure": [120, 125, 122],"heart_rate": [72, 75, 73]})
    print("Average BP =", round(p.average_measurement("blood_pressure"),2))

    # Q3
    bmi_values = [16.5, 22.4, 27.3, 31.8]
    print("BMI categories:", classify_bmi(bmi_values))

    # Q4
    mat = np.array([
        [70, 1.75, 22.9, 120],
        [80, 1.80, 24.7, 130],
        [65, 1.60, 25.4, 110]
    ], dtype=float)

    print("analyze_matrix:", analyze_matrix(mat))
    print("row_transform (row 1 normalized):\n", row_transform(mat, 1, normalize_row))

    # Q5
    plot_country_cases("Germany")
    compare_countries(["France", "Spain", "Italy"])