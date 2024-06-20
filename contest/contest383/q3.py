class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        rowCnt = len(image)
        colCnt = len(image[0])
        ans = [[0]*colCnt for _ in range(rowCnt)]
        index2ans = {}
        def checkGood(r,c,r1,r2,c1,c2):
            r_ = [0,0,1,-1]
            c_ = [1,-1,0,0]
            for i in range(4):
                newR = r+r_[i]
                newC = c+c_[i]
                if r1<=newR<=r2 and c1<=newC<=c2:
                    if abs(image[r][c]-image[newR][newC]) > threshold:
                        return False
            return True
        
        # travel throuth each region
                
        for i in range(rowCnt-2):
            for j in range(colCnt-2):
                flag = True
                avg = 0
                for i_ in range(3):
                    for j_ in range(3):
                        avg += image[i+i_][j+j_]
                        if not checkGood(i+i_,j+j_,i,i+2,j,j+2):
                            flag = False
                if flag:
                    for i_ in range(3):
                        for j_ in range(3):
                            if (i+i_,j+j_) in index2ans:
                                index2ans[(i+i_,j+j_)].append(avg//9)
                            else:
                                index2ans[(i+i_,j+j_)] = [avg//9]
        
        # calculate each ans
        for i in range(rowCnt):
            for j in range(colCnt):
                if (i,j) not in index2ans:
                    ans[i][j] = image[i][j]
                else:
                    ans[i][j] = sum(index2ans[(i,j)])//len(index2ans[(i,j)])
        
        return ans
                            
                            
