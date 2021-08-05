def exception_handle(num1):   #this function is to check 1st input value is string or not if it is string then it displays error message and again to input 
	process=False
	while process==False:    #loop to check again and again
	    try:
	        num1=int(input("        Enter the first decimal number :: "))
	        print("\n")
	        print("-----------------------------------------------------------------")
	        process=True
	    except:
	        print("\n")
	        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!  ERROR   !!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	        print("         String input found please input integer value ")
	        print("-----------------------------------------------------------------")
	        print("\n")
	return num1    #returing the checked value


def exception_handle_b(num2):  #this function is to check 1st input value is string or not if it is string then it displays error message and again to input 
	process=False
	while process==False:   #loop to check again
	    try:
	        num2=int(input("        Enter the second decimal number :: "))
	        print("\n")
	        print("-------------------------------------------------------------------")
	        process=True
	    except:
	        print("\n")
	        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!   ERROR     !!!!!!!!!!!!!!!!!!!!!!!!!!!")
	        print("         String input found please input integer value ")
	        print("-------------------------------------------------------------------")
	        print("\n")
	return num2   #returing the checked value

def number_validation(number):
    while number<0 or number>255:  #loop runs if it not in the range
        print("\n")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!  ERROR   !!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("          Please enter a value between 0 to 255 ")
        print("----------------------------------------------------------")
        print("\n")
        number=exception_handle(number) # calling function to check the string input
    return number




def number_validation_b(number):  #this function is to check if the user 2nd input is between 0 to 255 or not if it is not in the range then it display message and ask again to input right value    
    while number<0 or number>255:  #loop runs if it not in the range
        print("\n")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!  ERROR   !!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("          Please enter a value between 0 to 255 ")
        print("----------------------------------------------------------")
        print("\n")
        number=exception_handle(number) # calling function to check the string input
    return number



       
    
