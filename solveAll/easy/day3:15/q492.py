class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        ans = [area,1] # 1*area
        base = 2
        while base*base<=area:
            if area%base==0:
                ans = [area//base,base]
            base += 1
        return ans
