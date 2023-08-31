class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            # When a positive asteroid moves to the right, just add it to the stack
            if asteroid > 0:
                stack.append(asteroid)
            else:
                # While there are asteroids in the stack and the current asteroid
                # is negative and bigger than the positive asteroid on the stack, and the top asteroid in the stack is positive
                while stack and stack[-1] > 0 and stack[-1] < abs(asteroid):
                    stack.pop()  # The positive asteroid explodes
                # Check if the current negative asteroid survives; Essentially otherwise add a negative asteroid
                if not stack or stack[-1] < 0:
                    stack.append(asteroid)
                # If the current negative asteroid collides with an equal size positive asteroid
                elif stack[-1] == abs(asteroid):
                    stack.pop()  # Both asteroids explode

        return stack