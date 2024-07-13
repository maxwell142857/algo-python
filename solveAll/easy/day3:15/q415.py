class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        val1 = [int(c) for c in num1]
        val2 = [int(c) for c in num2]
        val1 = val1[::-1]
        val2 = val2[::-1]
        ans = []
        n1,n2 = len(val1),len(val2)
        carry = 0
        p1,p2 = 0,0
        while p1<n1 or p2<n2:

            result = carry
            if p1<n1:
                result += val1[p1]
            if p2<n2:
                result += val2[p2]

            if result>=10:
                result %= 10
                carry = 1
            else:
                carry = 0
            ans.append(str(result))

            p1 += 1
            p2 += 1
        
        if carry:
            ans.append('1')
            
        ans = ans[::-1]
        return ''.join(ans)
        
        
        

                
