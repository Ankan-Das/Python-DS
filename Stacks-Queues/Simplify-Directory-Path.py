#######################################################
#######################################################
Given an absolute path for a file (Unix-style), simplify it.

Examples:

path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
Note that absolute path always begin with ‘/’ ( root directory )
Path will not have whitespace characters.
#######################################################
######################################################


class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):
        dirs = A.split('/')
        result = []
        for c in dirs:
            if c == '' or c == '.': continue
            elif c == '..':
                if len(result)>0: result.pop()
            else:
                result.append(c)
        return '/'+'/'.join(result)
