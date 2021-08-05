def binary_reverse(binary_num):   #this function reverse the converted binary list because the answer we need is in reversed form
    reversed_list=[]      
    for i in range(len(binary_num)-1,-1,-1):
        reversed_list.append(binary_num[i])   # adding the value to the created list
    return reversed_list #returung the value 

