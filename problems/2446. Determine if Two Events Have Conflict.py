class Solution:
    def haveConflict(self, event1: list[str], event2: list[str]) -> bool:
        def convert(time):
            hour, minute = time.split(':')
            return int(hour)*60 + int(minute)
        
        e1_start = convert(event1[0])
        e1_end = convert(event1[1])
        e2_start = convert(event2[0])
        e2_end = convert(event2[1])
        
        if e1_start > e2_end or e2_start > e1_end:
            return False
        else:
            return True