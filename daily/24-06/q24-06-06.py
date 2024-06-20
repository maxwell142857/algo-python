class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        val2cnt = Counter(hand)
        arr = []
        for k,v in val2cnt.items():
            arr.append([k,v])
        arr.sort()
        cnt = len(hand)
        if cnt%groupSize != 0:
            return False
        p = 0
        n = len(arr)
        while cnt > 0:
            while p<n and arr[p][1] == 0:
                p += 1
            if p+groupSize-1<n:
                arr[p][1] -= 1
                for i in range(p+1,p+groupSize):
                    if arr[i][0] == arr[i-1][0]+1 and arr[i][1] != 0:
                        arr[i][1] -= 1
                    else:
                        return False
                cnt -= groupSize
            else:
                return False
        return cnt == 0

