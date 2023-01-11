# link: https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ips = []
        n = len(s)
        def helper(start, end, ip_segments):
            if end >= n:
                return
            if len(ip_segments) == 3:
                if int(s[start:]) > 255 or n - start > 1 and s[start] == '0':
                    return
                ip_segments.append(int(s[start:]))
                ips.append('.'.join([str(seg) for seg in ip_segments]))
                ip_segments.pop()
                return
            if int(s[start:end+1]) > 255:
                return
            if s[start] != '0':
                helper(start, end+1, ip_segments)
            ip_segments.append(int(s[start:end+1]))
            start = end + 1
            end = start
            helper(start, end, ip_segments)
            ip_segments.pop()

        helper(0, 0, [])
        return ips
