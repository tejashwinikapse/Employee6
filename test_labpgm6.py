from labpgm6 import employee_details


def test_employee_details():
    result = employee_details("Tejashwini", "164", "IT", "30000")

    expected = "Employee Name: Tejashwini, Employee ID: 164, Department: IT, Salary: 30000"

    assert result == expected