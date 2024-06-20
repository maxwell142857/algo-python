class Solution:
    # o(n^3)
    def maxPoints(self, points: List[List[int]]) -> int:
        def check(point1,point2,point3):
            if point1[0]==point2[0]==point3[0]:
                return True
            elif point1[0]==point2[0] or point2[0]==point3[0]:
                return False
            else:
                k1 = (point1[1]-point2[1])/(point1[0]-point2[0])
                k2 = (point3[1]-point2[1])/(point3[0]-point2[0])
                return abs(k1-k2) < 0.0000000001
            
        
        n = len(points)
        if n == 1:
            return 1
        ans = 0
        for index1 in range(n):
            for index2 in range(index1+1,n):
                cnt = 2
                for index3 in range(index2+1,n):
                    if check(points[index1],points[index2],points[index3]):
                        cnt += 1
                ans = max(ans,cnt)
        return ans
    
    # o(n^2)
    def maxPoints(self, points: List[List[int]]) -> int:
        def getK(point1,point2):
            if point1[0] == point2[0]:
                return (True,point2[0])
            else:
                return (False,(point1[1]-point2[1])/(point1[0]-point2[0]))
            
        
        ans = 1
        for i in range(len(points)):
            infiniteK = {} # x value: times
            normalK = {} # k value: times
            for j in range(len(points)):
                if i == j:
                    continue

                result = getK(points[i],points[j])
                if result[0]:
                    infiniteK[result[1]] = infiniteK.get(result[1],0)+1
                else:
                    normalK[result[1]] = normalK.get(result[1],0)+1

            if len(infiniteK) == 0 and len(normalK) == 0:
                continue
            elif len(infiniteK) == 0:
                tmpMax = max(normalK.values())
            elif len(normalK) == 0:
                tmpMax = max(infiniteK.values())
            else:
                tmpMax= max(max(infiniteK.values()),max(normalK.values()))
            ans = max(ans,tmpMax+1)
        return ans

