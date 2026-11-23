from labpgm6 import employee_details

def test_employee_details():
    result = employee_details("Tejashwini", "EMP101", "IT", "25000")

    expected = "Name: Tejashwini\nEmployee ID: EMP101\nDepartment: IT\nSalary: 25000"

    assert result == expected