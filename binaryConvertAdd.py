def binary_to_decimal(number):     # this function converts the user input decimal number into the 8 bit binary form
    binary_list=[] 
    step=0
    while step!=8:    #running 8 times for making 8 bit number
        remainder=number%2  
        binary_list.append(remainder)   # adding value to the list
        number=number//2
        step+=1
    return binary_list  #returning the result


import LogicGates   # importing the mudule LogicGates to perform addition using it
def binary_adiition(x,y):  #this function adds the convertes binary number and reversed binary number sing the concept of full bit adder
    sum_value=[]
    Binary_list=[]
    Binary_sum=""
    crayyIn=0
    for j in range(len(x)-1,-1,-1):
        num1=int(x[j])
        num2=int(y[j])
        Storing_Sum1=LogicGates.XOR_gate(num1,num2) #sum of the numbers sending to the function of LogicGated to add the numbers 
        Total_Sum=LogicGates.XOR_gate(Storing_Sum1,crayyIn)

        #carry Out
        Carry_Out_1=LogicGates.AND_gate(num1,num2)   #carry out of the numbers sending to the function of LogicGated to add the numbers 
        Carry_Out_2=LogicGates.AND_gate(Storing_Sum1,crayyIn)
        Total_Carry_Out=LogicGates.OR_gate(Carry_Out_1,Carry_Out_2)
        crayyIn=Total_Carry_Out
        sum_value.append(Total_Sum)
        
    for x in range(len(sum_value)-1,-1,-1):  #Since the output is in list form and it has (,) between its items to remove it, the output is converted in the list 
        Binary_list.append(sum_value[x])   
        Binary_sum=Binary_sum+str(sum_value[x])  #string concadination
    return Binary_sum



	


	
