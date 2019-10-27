class Solution(object):
    def letterCombinations(self, digits):
        sols = []
        d = {'2':["a", "b", "c"], '3':["d", "e", "f"], '4':["g", "h", "i"], '5':["j", "k", "l"], '6':["m", "n", "o"], '7': ["p", "q", "r", "s"], '8': ["t", "u", "v"], '9':["w", "x", "y", "z"]}
        if(digits == ""):
            return []
        def solution(letter, phone):
            if (len(letter) == 0):
                sols.append(phone)
                return
            for i in range(len(d[letter[0]])):
                solution(letter[1:], phone+d[letter[0]][i])
        solution(digits, "")
        return sols
