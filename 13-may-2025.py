# You are given a string s and an integer t, representing the number of transformations to perform. In one transformation, every character in s is replaced according to the following rules:

# If the character is 'z', replace it with the string "ab".
# Otherwise, replace it with the next character in the alphabet. For example, 'a' is replaced with 'b', 'b' is replaced with 'c', and so on.
# Return the length of the resulting string after exactly t transformations.

# Since the answer may be very large, return it modulo 109 + 7.

class Solution(object):
    def lengthAfterTransformations(self, s, t):
        """
        :type s: str
        :type t: int
        :rtype: int
        """
        strcnt = [0]*26
        for i in s:
            strcnt [ord(i)-ord('a')]+=1
        for i in range(t):
            num = strcnt[25]
            for k in range(25,0,-1): 
                strcnt [k] = strcnt [k-1]
            strcnt[0] = num
            strcnt[1] += num
        return sum(strcnt)%((10**9)+7)
    
# so the question is clear 
# i maintained a list of 26 elements and used the count to itrate the list everytime and update the values in the list
# i used the ord function to get the ascii value of the character and then substracted it with the ascii value of 'a' to get the index of the list

# points to remember:
# ord('a') = 97
# chr(97) = 'a'


            