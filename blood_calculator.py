print("This is the blood_calculator.py module. ")
print("Python thinks this called {}".format(__name__))

def interface():
    print("My Program")
    print("Options:")
    print("1 - Analyze HDL")
    print("2 - Analyze LDL")
    print("3 - Analyze Cholesterol")
    print("9 - Quit")
    keep_running = True
    while keep_running:
        choice = input("Enter your choice: ")
        if choice=='9':
            return
        elif choice == "1":
            HDL_driver()
        elif choice == "2":
            LDL_driver()
        elif choice == "3":
            Cholesterol_driver()
            
def input_HDL():
    HDL_input = input("Enter the HDL value:")
    return int(HDL_input)
    
def check_HDL(HDL_value):
    if HDL_value >= 60:
        return "Normal"
    elif 40 <= HDL_value < 60:
        return "Borderline low"
    else:
        return "Low"
        
def HDL_driver():
    hdl_value = input_HDL()
    answer = check_HDL(hdl_value)
    output_HDL_result(hdl_value, answer)

def output_HDL_result(hdl_value, charac):
    print("The results for an HDL value {} is {}".format(hdl_value, charac))
    
def input_LDL():
    LDL_input = input("Enter the LDL value:")
    return int(LDL_input)

def check_LDL(LDL_value):
    if LDL_value < 130:
        return "Normal"
    elif 130 <= LDL_value <= 159:
        return "Borderline high"
    elif 160 <= LDL_value <= 189:
        return "High"
    else:
        return "Very High"
  
def LDL_driver():
    ldl_value = input_LDL()
    answer = check_LDL(ldl_value)
    output_LDL_result(ldl_value, answer)

def output_LDL_result(ldl_value, charac):
    print("The results for an LDL value {} is {}".format(ldl_value, charac))

def input_Cholesterol():
    Cholesterol_input = input("Enter the Cholesterol value:")
    return int(Cholesterol_input)

def check_Cholesterol(Cholesterol_value):
    if Cholesterol_value < 200:
        return "Normal"
    elif 200 <= Cholesterol_value <= 239:
        return "Borderline high"
    else:
        return "High"
  
def Cholesterol_driver():
    Cholesterol_value = input_Cholesterol()
    answer = check_Cholesterol(Cholesterol_value)
    output_Cholesterol_result(Cholesterol_value, answer)

def output_Cholesterol_result(Cholesterol_value, charac):
    print("The results for an Cholesterol value {} is {}".format(Cholesterol_value, charac))

if __name__ == "__main__":
    interface() 