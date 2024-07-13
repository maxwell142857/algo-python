class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def generateH(val):
            if val == 0:
                return [0]
            elif val == 1:
                return [8,4,2,1]
            elif val == 2:
                return [3,5,9,6,10]
            elif val == 3:
                return [7,11]
            else:
                return []
        
        def generateM(val):

            candidates = [32,16,8,4,2,1]
            result = []
            for i in range(64):
                cnt = 0
                tmp = 0
                for j in range(6):
                    if i &pow(2,j):
                        cnt += 1
                        tmp += candidates[j]
                if cnt == val and tmp<60:
                    result.append(tmp)
            return result
        
        def combine(h,m):
            result = []
            for a in h:
                for b in m:
                    if b <10:
                        result.append(str(a)+':0'+str(b))
                    else:
                        result.append(str(a)+':'+str(b))
            return result

        ans = []
        for i in range(turnedOn+1):
            h = generateH(i)
            m = generateM(turnedOn-i)
            if h and m:
                ans.extend(combine(h,m))
        return ans



                    

            
