# link: https://leetcode.com/problems/longest-valid-parentheses/

'''
This is a modified version of LeetCode official solution 3.
I don't want to push the closing parentheses' index into the stack, so I keep track of the last unmatched closing parenthesis instead.

```last_unmatched_open```  and  ```last_unmatched_end``` is for tracking the start of the substring and update the length.

```last_unmatched_open``` will be updated when there's a new match and the stack is popped,
or ```(``` is pushed into the stack.
```last_unmatched_end``` will be updated when the stack is empty and a ```)``` is encountered.

```last_unmatched_open``` is always larger than ```last_unmatched_end```.
```i - last_unmatched_end``` is only valid when all parentheses are closed after ```last_unmatched_end```. (stack is empty)
If there is unclosed parentheses, we update the length using ```i - last_unmatched_open``` instead.

By the way, when there's an unmatched closing parenthesis ```index=i```, we don't need to consider ```s[:i]``` anymore. That's why each time ```last_unmatched_end``` is updated, the stack is empty.
'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [] 
        max_len = 0
        last_unmatched_end = -1
        # last_unmatched_open: the last unmatched '('
        # last_unmatched_end: the last unmatched ')'

        for i, p in enumerate(s):
            if p == '(':
                stack.append(i)
            else:
                # for every s[i] == '(':
                # case 1: s[i-1] == '('
                # i-1 is in the stack
                # case 2: s[i-1] == ')'
                # unmatched_end <= i-1
                if stack:
                    # remove the matched parenthesis
                    stack.pop()
                    # get the element before the first matched '(' of the current substring
                    # and update the length
                    if stack: # there is a unmatched opened parenthesis 
                        last_unmatched_open = stack[-1]
                        max_len = max(max_len, i - last_unmatched_open)
                    else:
                        max_len = max(max_len, i - last_unmatched_end)
                else:
                    last_unmatched_end = i
        return max_len

    # Leet Code officail solution 3
    # def longestValidParentheses(self, s: str) -> int:
    #     stack = [-1] # index i-1: start of substring=0
    #     max_len = 0
        
    #     for i, p in enumerate(s):
    #         if p == '(':
    #             stack.append(i)
    #         else:
    #             stack.pop()
    #             if stack:
    #                 max_len = max(max_len, i - stack[-1]) # stack[-1]: one index before the popped '('
    #             else: # no matching '(', refresh potential start of substring to i+1
    #                 stack.append(i) 
    #     return max_len


        # ")))"
        # stack = [-1] -> [0] -> [1] -> [2]

        # "(()"
        # stack = [-1] -> [-1, 0] -> [-1, 0, 1] -> [-1, 0]

        # "()()"
        # stack = [-1] -> [-1, 0] -> [-1] -> [-1, 1] -> [-1]
