def predict_performance(study_hours, attendance, assignment_score):

    score = (
        study_hours * 5
        + attendance * 0.3
        + assignment_score * 0.4
    )

    if score >= 80:
        return "EXCELLENT"
    elif score >= 60:
        return "GOOD"
    else:
        return "NEEDS IMPROVEMENT"


if __name__ == "__main__":
    study_hours = 10
    attendance = 95
    assignment_score = 90

    result = predict_performance(
        study_hours,
        attendance,
        assignment_score
    )

    print("Study Hours:", study_hours)
    print("Attendance:", attendance)
    print("Assignment Score:", assignment_score)
    print("Predicted Performance:", result)