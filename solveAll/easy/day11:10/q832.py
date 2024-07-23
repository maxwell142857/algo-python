class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        rowCnt = len(image)
        colCnt =len(image)
        for r in range(rowCnt):
            image[r] = image[r][::-1]
        for r in range(rowCnt):
            for c in range(colCnt):
                image[r][c]  = (image[r][c]+1)%2
        return image