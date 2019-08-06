#############################################################################
#############################################################################
#For Given Number N find if its COLORFUL number or not
#
#Return 0/1
#
#COLORFUL number:
#
#A number can be broken into different contiguous sub-subsequence parts. 
#Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245. 
#And this number is a COLORFUL number, since product of every digit of a contiguous subsequence is different
#Example:
#
#N = 23
#2 3 23
#2 -> 2
#3 -> 3
#23 -> 6
#this number is a COLORFUL number since product of every digit of a sub-sequence are different. 
#
#Output : 1
##############################################################################
##############################################################################

class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        Hello = []
        while A!=0:
            temp = A%10
            Hello.append(temp)
            copy = int(A/10)
            while copy!=0:
                Hello.append(Hello[-1]*(copy%10))
                copy = int(copy/10)
            A = int(A/10)
        
        Hello.sort()
        for i in range(len(Hello)-1):
            if Hello[i]==Hello[i+1]:
                return 0
        return 1
        #print(Hello)
