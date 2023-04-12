# link: https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:

        dirs = [d for d in path.split('/') if d not in ['.', '']]

        output = []
        for d in dirs:
            if d == '..':
                if output:
                    output.pop()
            else:
                output.append(d)

        return '/' + '/'.join(output)

