from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:


        #Use the counter Hashmap

        counter = collections.Counter(arr)
        # use most_common() to show the first n element, but in this case, n not define, so it will be all the element
        # and return type will be 2d list
        counter = counter.most_common()
        unique = len(counter)
        while k>0 and unique>0:
            # if the value k is enough to remove the least common element
            if k>=counter[-1][1]:
                # remove the needed amount to pop the least common element
                k -= counter[-1][1]
                # pop the last element in the list
                counter.pop()
                # decrement the unique since the last element poped
                unique -= 1
            # if the value k is not enough to remove the least common element
            else:
                return unique
        return unique   