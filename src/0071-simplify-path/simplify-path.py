# Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.
#
# In a UNIX-style file system, a period '.' refers to the current directory. Furthermore, a double period '..' moves the directory up a level.
#
# Note that the returned canonical path must always begin with a slash '/', and there must be only a single slash '/' between two directory names. The last directory name (if it exists) must not end with a trailing '/'. Also, the canonical path must be the shortest string representing the absolute path.
#
#  
# Example 1:
#
#
# Input: path = "/home/"
# Output: "/home"
# Explanation: Note that there is no trailing slash after the last directory name.
#
#
# Example 2:
#
#
# Input: path = "/../"
# Output: "/"
# Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
#
#
# Example 3:
#
#
# Input: path = "/home//foo/"
# Output: "/home/foo"
# Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
#
#
# Example 4:
#
#
# Input: path = "/a/./b/../../c/"
# Output: "/c"
#
#
#  
# Constraints:
#
#
# 	1 <= path.length <= 3000
# 	path consists of English letters, digits, period '.', slash '/' or '_'.
# 	path is a valid Unix path.
#
#


"""
class Solution:
    def simplifyPath(self, path):
        """
        #:type path: str
        #:rtype: str
"""(if not be here, than will )
        path.replace('//', '/')
        list = path.split('/')
        res = '/'
        num = []
        for i in range(len(list)):
            if list[i] == '..' and len(res) > 1:
                res = res[:len(res) - num[-1] - 1]
                num=num[:-1]
            elif list[i] != '' and list[i] != '.' and list[i] != '..':
                res = res + list[i] + '/'
                num.append(len(list[i]))
        return res[:-1] if len(res) > 1 else res

"""    
class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path.replace('//', '/')
        list = path.split('/')
        res =[]
        for i in range(len(list)):
            if list[i] == '..' and len(res) > 0:
                res = res[:-1]
            elif list[i] != '' and list[i] != '.' and list[i] != '..':
                res.append(list[i])
        return '/'+'/'.join(res)
    
"""1\ general solution 2\boundray solution"""
