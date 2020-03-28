class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        a = []
        ans = []
        def generate_parenthesis(ope, close):
            print(a)
            if(ope ==  0 and close == 0):
                s = ''
                for i in range(len(a)):
                    if(a[i] == 1):
                        s = s+'('
                    else:
                        s = s+')'
                ans.append(s)
                return
                    
            if(ope == 0):
                a.append(0)
                generate_parenthesis(ope, close-1)
                a.pop(len(a)-1)
                
            elif(ope == close):
                a.append(1)
                generate_parenthesis(ope-1, close)
                a.pop(len(a)-1)
            
            elif(ope < close):
                a.append(1)
                generate_parenthesis(ope-1, close)
                a.pop(len(a)-1)
                a.append(0)
                generate_parenthesis(ope, close-1)
                a.pop(len(a)-1)
            
        generate_parenthesis(n, n)
        return ans
            
