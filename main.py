from pathlib import Path

import numpy as np
import pandas as pd


DATA_FILE = Path(__file__).with_name("students.csv")
SUBJECT_COLUMNS = ["Mathematics", "Python", "Artificial_Intelligence", "English"]


def load_student_data(file_path: Path) -> pd.DataFrame:
    """Load student records and check that all required columns are present."""
    data = pd.read_csv(file_path)
    required_columns = [
        "Student_ID", "Name", "Department", "Attendance_Percentage", *SUBJECT_COLUMNS
    ]
    missing_columns = [column for column in required_columns if column not in data.columns]
    if missing_columns:
        raise ValueError(f"Dataset is missing required columns: {', '.join(missing_columns)}")
    return data


def assign_grade(average: float) -> str:
    """Return a letter grade using the thresholds documented in README.md."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    elif average >= 40:
        return "E"
    return "F"


def process_student_data(data: pd.DataFrame) -> pd.DataFrame:
    """Add total, average, grade, and pass/fail columns to a copy of the data."""
    results = data.copy()
    marks = results[SUBJECT_COLUMNS].to_numpy(dtype=float)
    results["Total_Marks"] = np.sum(marks, axis=1)
    results["Average_Marks"] = np.round(np.mean(marks, axis=1), 2)

    grades = []
    pass_statuses = []
    for row in results.itertuples(index=False):
        grades.append(assign_grade(row.Average_Marks))
        subject_marks = [getattr(row, subject) for subject in SUBJECT_COLUMNS]
        passed_subjects = all(mark >= 40 for mark in subject_marks)
        attendance_ok = row.Attendance_Percentage >= 75
        pass_statuses.append("Pass" if passed_subjects and attendance_ok else "Fail")

    results["Grade"] = grades
    results["Result"] = pass_statuses
    return results


def print_student_summary(results: pd.DataFrame) -> None:
    """Print student-wise totals, averages, grades, and results."""
    columns = ["Student_ID", "Name", "Total_Marks", "Average_Marks", "Grade", "Result"]
    print("\nSTUDENT PERFORMANCE SUMMARY")
    print(results[columns].to_string(index=False))


def print_class_summary(results: pd.DataFrame) -> None:
    """Print class statistics and the top-performing students."""
    overall_average = np.mean(results["Average_Marks"].to_numpy())
    pass_count = int((results["Result"] == "Pass").sum())
    fail_count = len(results) - pass_count
    highest = results.loc[results["Average_Marks"].idxmax()]
    lowest = results.loc[results["Average_Marks"].idxmin()]
    top_students = results.sort_values(
        by=["Average_Marks", "Name"], ascending=[False, True]
    ).head(3)

    print("\nCLASS SUMMARY")
    print(f"Number of students: {len(results)}")
    print(f"Overall class average: {overall_average:.2f}")
    print(f"Passed: {pass_count} | Failed: {fail_count}")
    print(
        f"Highest average: {highest['Name']} ({highest['Average_Marks']:.2f})"
    )
    print(f"Lowest average: {lowest['Name']} ({lowest['Average_Marks']:.2f})")
    print("\nTOP 3 PERFORMERS")
    for position, (_, student) in enumerate(top_students.iterrows(), start=1):
        print(f"{position}. {student['Name']} — {student['Average_Marks']:.2f} ({student['Grade']})")


def print_subject_analysis(data: pd.DataFrame) -> None:
    """Print each subject's average, highest mark, and lowest mark."""
    subject_averages = data[SUBJECT_COLUMNS].mean()
    best_subject = subject_averages.idxmax()
    print("\nSUBJECT-WISE PERFORMANCE")
    for subject in SUBJECT_COLUMNS:
        marks = data[subject].to_numpy(dtype=float)
        print(
            f"{subject.replace('_', ' ')}: average {np.mean(marks):.2f}, "
            f"highest {np.max(marks):.0f}, lowest {np.min(marks):.0f}"
        )
    print(f"Best average subject: {best_subject.replace('_', ' ')} ({subject_averages[best_subject]:.2f})")


def main() -> None:
    """Run the complete analytics workflow."""
    data = load_student_data(DATA_FILE)
    print("STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print(f"Loaded {len(data)} student records from {DATA_FILE.name}.")
    print("Columns:", ", ".join(data.columns))
    print("\nDATA PREVIEW")
    print(data.head().to_string(index=False))

    results = process_student_data(data)
    print_student_summary(results)
    print_class_summary(results)
    print_subject_analysis(data)


if __name__ == "__main__":
    main()
