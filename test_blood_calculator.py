import pytest

@pytest.mark.parametrize("input_one,input_two", 
    [(85,"Normal"),
     (45,"Borderline low"),
     (20, "Low")])

def test_check_HDL_Normal(input_one, input_two):
    from blood_calculator import check_HDL
    answer = check_HDL(input_one)
    assert answer == input_two
    
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
