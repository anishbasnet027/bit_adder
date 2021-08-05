import ApplicationDesign  #impoting the other modules
import ExceptionHandle
import binaryConvertAdd
import Reverse

loop_continue=True       
while loop_continue==True:   #this loop is to run program again   
    ApplicationDesign.design_top() #calling function from ApplicationDesign module
    loop=True
    first_number=0 
    second_number=0
    while loop==True:        #this loop is to check 9 bit numbers
        first_number=ExceptionHandle.exception_handle(first_number)     #passing number in different functions string check for 1st number
        first_number1=ExceptionHandle.number_validation(first_number)    #number between 0 to 255 check for 1st number

        second_number=ExceptionHandle.exception_handle_b(second_number)   #Strig check for 2nd number
        second_number1=ExceptionHandle.number_validation_b(second_number) #number between 0 to 255 check for 2st number
        
        if first_number1+second_number1>255:             #checking if the sum of number is greater than 8 bit or not
            print("\n")
            print("!!!!!!!!!!!!!!!!!!!! Error  !!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("      The sum of two numbers is greater than 8 bit   ")
            print("\n")
            print("   The sum of two numbers should be less than 9 bit   ")
            print("---------------------------------------------------------")
            print("\n")
        else:
            break
        
    
    first_binary=binaryConvertAdd.binary_to_decimal(first_number1)     #converting to binary for 1st number
    first_binary_reversed=Reverse.binary_reverse(first_binary)         #Reversing the converted list


    second_binary=binaryConvertAdd.binary_to_decimal(second_number1)    #converting to binary for 2nd number
    second_binary_reversed=Reverse.binary_reverse(second_binary)        #Reversing the converted list

    binary_addition=binaryConvertAdd.binary_adiition(first_binary_reversed,second_binary_reversed)   #adding 
    print("       Sum of given numbers in the binary form = ",binary_addition)     #displaying sum or output
    print("-------------------------------------------------------------------")
    print("\n")

    
    print("Do you want to perform more addition?")                          #asking user to continue or not
    print("-------------------------------------------------------------------")
    ask_user=input("If yes press any key else type 'No' ").lower()
    print("\n")
    
    if ask_user=="no" :
        loop_continue=False     #if answer is no then program will end
        
ApplicationDesign.design_bottom()   #calling other function to display message
