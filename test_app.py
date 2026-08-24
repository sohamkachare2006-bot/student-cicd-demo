from app import predict_performance


def test_excellent_student():
    assert predict_performance(10, 95, 90) == "No EXCELLENT"


def test_good_student():
    assert predict_performance(5, 70, 65) == "GOOD"


def test_needs_improvement():
    assert predict_performance(2, 50, 40) == "NEEDS IMPROVEMENT"