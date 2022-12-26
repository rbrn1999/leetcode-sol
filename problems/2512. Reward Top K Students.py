# link: https://leetcode.com/problems/reward-top-k-students/

class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        scores = [] # (score, id)
        positive_set = set(positive_feedback)
        negative_set = set(negative_feedback)

        for i in range(len(student_id)):
            score = 0
            for word in report[i].split():
                if word in positive_set:
                    score += 3
                elif word in negative_set:
                    score -= 1
                else:
                    pass
            scores.append((score, student_id[i]))

        scores.sort(key=lambda x: (x[0], -x[1]), reverse=True)
        return [x[1] for x in scores[:k]]
