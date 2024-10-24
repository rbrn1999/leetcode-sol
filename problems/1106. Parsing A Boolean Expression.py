# link: https://leetcode.com/problems/parsing-a-boolean-expression/

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def __parse(i: int) -> tuple[bool, int]:
            if expression[i] == 't':
                return (True, i+1)
            if expression[i] == 'f':
                return (False, i+1)

            operator = expression[i]
            i += 2 # skip '('

            if operator == '!':
                value, i = __parse(i)
                i += 1 # skip ')'
                return (not value, i)

            # case: '&' and '|'
            values = []
            while expression[i] != ')':
                if expression[i] != ',':
                    value, i = __parse(i)
                    values.append(value)
                else:
                    i += 1 # skip comma

            i += 1 # skip ')'
            if operator == '&':
                return (all(values), i)
            if operator == '|':
                return (any(values), i)

            print('Error')
            return (False, 10000)

        return __parse(0)[0]
