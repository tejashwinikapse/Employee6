from labpgm6 import employee_details

def test_employee_details():
    result = employee_details("Tejashwini", 101, "IT", 25000)

    expected = "Employee Name: Tejashwini," " Employee ID: 101, " "Department: IT, " "Salary: 25000"

    assert result == expected