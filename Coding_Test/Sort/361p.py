"""
https://school.programmers.co.kr/learn/courses/30/lessons/42889?language=python3
"""

def solution(N, stages):
    answer = []
    stage_num = len(stages)

    for i in range(1, N+1):
        count = stages.count(i)

        if stage_num == 0:
            fail = 0
        else:
            fail = count/stage_num

        answer.append((i, fail))
        stage_num -= count

    answer = sorted(answer, key=lambda t: t[1], reverse=True)

    answer = [i[0] for i in answer]
    return answer

solution(5, [2, 1, 2, 6, 2, 4, 3, 3])