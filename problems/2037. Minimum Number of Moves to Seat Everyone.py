# link: https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

# Sorting
class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        return sum(abs(seat-student) for seat, student in zip(sorted(seats), sorted(students)))

# Counting Sort
class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        max_position = max(max(seats), max(students))
        count = [0] * max_position
        for seat in seats:
            count[seat-1] += 1
        for student in students:
            count[student-1] -= 1

        unmatched = 0
        moves = 0

        for c in count:
            unmatched += c
            moves += abs(unmatched)

        return moves
