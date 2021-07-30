"""Write a function that gets a list of integers as an input and returns the
 sum f all even numbers minus the sum of all odd numbers."
"""
#%% by jumman

list_1=[77, 25, 1, 29, 6, 8, 44, 9, 11, 26, 36, 7]

def even_odd_diff(lista):
    even_number = 0
    odd_number = 0
    final_sum = 0
    try:
        for element in lista:
            if(element % 2 == 0):
                even_number += element
            else:
                odd_number += element
                
        final_sum = (even_number - odd_number)
        return final_sum
    except:
        print("Invalid data type")
        
#if __name__ ==  '__main__':
#    even_odd_diff(list_1)
        
#%% by nata