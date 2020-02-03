'''
Given an array of characters with repeats, compress it in place. 
The length after compression should be less than or equal to the original array.

Example:
Input: ['a', 'a', 'b', 'c', 'c', 'c']
Output: ['a', '2', 'b', 'c', '3']
'''

class Solution(object):
    def compress(self, chars):
        count = 1
        out = []
        ch = chars[0]
        for i in range(1, len(chars)):
            if ch == chars[i]:
                count+=1
            else:
                if count == 1:
                    out.append(ch)
                else:
                    out.append(ch)
                    out.append(count)
                count = 1
            ch = chars[i]
        if count > 1:
            out.append(ch)
            out.append(count)    
        else:
            out.append(ch)
        return out

print(Solution().compress(['a', 'a', 'b', 'c', 'c', 'c']))
# ['a', '2', 'b', 'c', '3']