class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # stack = []
        # for a in asteroids:
        #     if not stack:
        #         stack.append(a)
        #     elif not (stack[-1] > 0 and a < 0):
        #         stack.append(a)
        #     elif -a == stack[-1]:
        #         stack.pop()
        #     else:
        #         while stack and a * stack[-1] < 0 and abs(a) > abs(stack[-1]):
        #             stack.pop()
        #         if not stack and a * stack[-1] > 0:
        #             stack.append(a)
        # return stack
        stack = []
        for a in asteroids:
            while stack and stack[-1] > 0 and a < 0 and abs(stack[-1]) < abs(a):
                stack.pop()
            if stack and (stack[-1] > 0 and a < 0):
                if abs(a) == abs(stack[-1]):
                    stack.pop()
            else:
                stack.append(a)
        return stack