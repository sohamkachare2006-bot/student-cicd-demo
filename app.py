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