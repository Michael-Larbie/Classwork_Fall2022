def interface():
    print("My Program")
    print("Options:")
    print("9 - Quit")
    keep_running = True
    while keep_running:
        choice = input("Enter your choice: ")
        if choice=='9':
            return
            
def input_HDL():
    HDL_input = input("Enter the HDL value:")
    return int(HDL_input)
    
def check_HDL():
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
    
    
interface() 