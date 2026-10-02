class Solution:
    '''2 х 2 указателя 0_0'''
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        m = len(matrix)
        n = len(matrix[0])
        answer = []
        top, bot = 0, m - 1
        left, right = 0, n - 1

        while top <= bot and left <= right:
            for index in range(left, right + 1):
                answer.append(matrix[top][index])
            top += 1

            for index in range(top, bot + 1):
                answer.append(matrix[index][right])
            right -= 1
            if top <= bot:
                for index in range(right, left - 1, -1):
                    answer.append(matrix[bot][index])
                bot -= 1
            if left <= right:
                for index in range(bot, top - 1, -1):
                    answer.append(matrix[index][left])
                left += 1

        return answer
