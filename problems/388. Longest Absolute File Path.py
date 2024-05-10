# link: https://leetcode.com/problems/longest-absolute-file-path/

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        path_lengths = []
        pure_length = 0 # sum of path_lengths
        result = 0
        lines = input.split('\n')

        for line in lines:
            i = 0
            while line[i] == '\t':
                i += 1

            while len(path_lengths) > i:
                pure_length -= path_lengths.pop()

            path_lengths.append(len(line)-i)
            pure_length += len(line)-i
            if '.' in line:
                final_path_length = pure_length + (len(path_lengths) - 1)
                result = max(result, final_path_length)
                pure_length -= path_lengths.pop()

        return result
