################################################################
################################################################
#Given a limited range array contains both positive and non-positive numbers, i.e., elements are in the range from -MAX to +MAX. Our task is to search if some number is present in the array or not in O(1) time.
#
#Since range is limited, we can use index mapping (or trivial hashing). We use values as the index in a big array. Therefore we can search and insert elements in O(1) time.
#
#How to handle negative numbers?
#The idea is to use a 2D array of size hash[MAX+1][2]
#
#Algorithm:
#
#Assign all the values of the hash matrix as 0.
#Traverse the given array:
#    If the element ele is non negative assign 
#        hash[ele][0] as 1.
#    Else take the absolute value of ele and 
#         assign hash[ele][1] as 1.
#To search any element x in the array.
#
#If X is non-negative check if hash[X][0] is 1 or not. If hash[X][0] is one then the number is present else not present.
#If X is negative take absolute value of X and then check if hash[X][1] is 1 or not. If hash[X][1] is one then the number is present
#################################################################
#################################################################


def search(X): 
  
    if X >= 0: 
        if has[X][0] == 1: 
            return True
        else: 
            return False
  
    # if X is negative take the absolute 
    # value of X. 
    X = abs(X) 
    if has[X][1] == 1: 
        return True
  
    return False
  
def insert(a, n): 
  
    for i in range(0, n): 
        if a[i] >= 0: 
            has[a[i]][0] = 1
        else: 
            has[abs(a[i])][1] = 1
  
# Driver code 
if __name__ == "__main__": 
  
    a = [-1, 9, -5, -8, -5, -2] 
    n = len(a) 
  
    MAX = 1000
      
    # Since array is global, it is 
    # initialized as 0. 
    has = [[0 for i in range(2)]  
              for j in range(MAX + 1)] 
    insert(a, n) 
  
    X = -5
    if search(X) == True: 
        print("Present") 
    else: 
        print("Not Present") 
