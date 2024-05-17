# link: https://leetcode.com/problems/next-closest-time/

class Solution:
    def nextClosestTime(self, time: str) -> str:
        digits = [time[0], time[1], time[3], time[4]]

        # find larger minutes
        next_minutes = 60
        for i in range(len(digits)):
            if int(digits[i]) >= 6:
                continue
            for j in range(len(digits)):
                cur_minutes = int(digits[i] + digits[j])
                if cur_minutes > int(time[-2:]) and cur_minutes < next_minutes:
                    next_minutes = cur_minutes

        if next_minutes < 60:
            return time[:3] + str(next_minutes).zfill(2)

        # find the cloest hour
        min_digit = min(int(digit) for digit in digits)
        minutes = min_digit * 10 + min_digit
        hour = int(time[:2])
        diff = 24
        for i in range(len(digits)):
            if int(digits[i]) > 2:
                continue
            for j in range(len(digits)):
                cur_hour = int(digits[i] + digits[j])
                if cur_hour >= 24:
                    continue
                if cur_hour > int(time[:2]) and cur_hour - int(time[:2]) < diff:
                    hour = cur_hour
                    diff = cur_hour - int(time[:2])
                elif cur_hour < int(time[:2]) and cur_hour + 24 - int(time[:2]) < diff:
                    hour = cur_hour
                    diff = cur_hour + 24 - int(time[:2])

        return str(hour).zfill(2) + ':' + str(minutes).zfill(2)
