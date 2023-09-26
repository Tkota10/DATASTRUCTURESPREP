class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        '''
        Skill array, even length. Index, refers to index

        #Num of Teams


        #Methodology:

        Sort the array:

        Two Pointers:

        l = 0
        r = len(skill) - 1

        '''

        skill.sort()

        l = 0
        r = len(skill) - 1

        p = []
        a = []

        while l < (len(skill) / 2):
            p.append(skill[l] * skill[r])
            a.append(skill[l] + skill[r])

            l += 1
            r -= 1
        
        if len(set(a)) == 1:
            return (sum(p))
        else:
            return -1