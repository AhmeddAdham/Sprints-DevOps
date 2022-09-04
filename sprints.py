import statistics

def myFunc(list):
   even_numbers= []
   float_numbers=[]

   for i in list:   #Base Condition
    if type(i) != int and type(i) != float:
        return 0

    for j in list:      
        if type(j)== int and j%2 ==0:   # Even and Integer check
            even_numbers.append(j)

        if type(j) == float:
            float_numbers.append(j)

        

    mean=statistics.mean(even_numbers)
    max_float= max(float_numbers)
    
    return mean , max_float



 # Small test     
 # 1,2,3,4 ---> 2,4 ---> 2+4 / 2 ---> 6/2=3 correct
 # 1.3 > 1.2 correct   
print("Mean and maximum values are ",myFunc([1,2,3,4,1.2,1.3]))





