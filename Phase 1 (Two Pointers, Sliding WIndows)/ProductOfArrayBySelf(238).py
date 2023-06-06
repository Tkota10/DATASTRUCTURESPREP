#solution 1

def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        answer = []
        first = 0
        while first < len(nums):
            element = 1
            for k in range(len(nums)):
                if k != first:
                    element *= nums[k]
            answer.append(element)
            first += 1
        return answer

#Solution 2

def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        n = len(nums)
        left_product = [1] * n  # Precomputed product from the left side
        right_product = [1] * n  # Precomputed product from the right side

        # Calculate the product from the left side
        for i in range(1, n):
            left_product[i] = left_product[i - 1] * nums[i - 1]

        # Calculate the product from the right side
        for i in range(n - 2, -1, -1):
            right_product[i] = right_product[i + 1] * nums[i + 1]

        # Calculate the product except self
        answer = []
        for i in range(n):
            answer.append(left_product[i] * right_product[i])

        return answer
