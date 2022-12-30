# link: https://leetcode.com/problems/car-fleet/

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        sorted_cars = sorted(list(range(n)), key=lambda i: position[i]) # sort car index by position

        count = 0
        prev_position, prev_speed = target, float('inf')
        while sorted_cars:
            index = sorted_cars.pop()
            if speed[index] <= prev_speed or (prev_position-position[index])/(speed[index]-prev_speed) * prev_speed + prev_position > target:
                print(index)
                count += 1
                prev_position, prev_speed = position[index], speed[index]
            else:
                pass

        return count
