import pytest

@pytest.mark.parametrize("input_one,expected", 
    [(85,"Normal"),
     (45,"Borderline low"),
     (20, "Low")])

def test_check_HDL_Normal(input_one, expected):
    from blood_calculator import check_HDL
    answer = check_HDL(input_one)
    assert answer == expected
    
@pytest.mark.parametrize("input_one, expected",
    [(120,"Normal"),
     (140,"Borderline high"),
     (170,"High")])

def test_check_LDL_Normal(input_one, expected):
    from blood_calculator import check_LDL
    answer = check_LDL(input_one)
    assert answer == expected
    
@pytest.mark.parametrize("input_one, expected",
    [(150,"Normal"),
     (220,"Borderline high"),
     (260,"High")])

def test_check_Cholesterol_Normal(input_one, expected):
    from blood_calculator import check_Cholesterol
    answer = check_Cholesterol(input_one)
    assert answer == expected  
'''   
def test_check_HDL_BorderlineLow():
    from blood_calculator import check_HDL
    answer = check_HDL(45)
    expected = "Borderline low"
    assert answer == expected
    
def test_check_HDL_low():
    from blood_calculator import check_HDL
    answer = check_HDL(25)
    expected = "Low"
    assert answer == expected
 '''
