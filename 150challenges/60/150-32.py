
from typing import List


class Solution:
    # simulation, O(n*m*k), n is len(s), m is len(words),k is len(words[0])
    # def findSubstring(self, s: str, words: List[str]) -> List[int]:
    #     ans = []
    #     dictionary = {}
    #     for item in words:
    #         if item in dictionary:
    #             dictionary[item] += 1
    #         else:
    #             dictionary[item] = 1
    #     length = len(s)
    #     wordLength = len(words[0])
    #     wordCnt = len(words)
    #     for i in range(length-wordCnt*wordLength+1):
    #         check = dictionary.copy()
    #         start = i
    #         flag = True
    #         while len(check) != 0:
    #             if start+wordLength > length:
    #                 flag = False
    #                 break
    #             elif s[start:start+wordLength] in check:
    #                 if check[s[start:start+wordLength]] == 1:
    #                     del check[s[start:start+wordLength]]
    #                 else:
    #                     check[s[start:start+wordLength]] -= 1
    #                 start += wordLength
    #             else:
    #                 flag = False
    #                 break
    #         if flag:
    #             ans.append(i)
    #     return ans


    # two pointer,  O(n*k), n is len(s),k is len(words[0])
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ans = []
        dictionary = {}
        for item in words:
            if item in dictionary:
                dictionary[item] += 1
            else:
                dictionary[item] = 1
        length = len(s)
        wordLength = len(words[0])
        for left in range(wordLength):
            check = dictionary.copy()
            for right in range(left,length-wordLength+1,wordLength):
                rightWord = s[right:right+wordLength]
                if rightWord in check:
                    if check[rightWord] == 1:
                        del check[rightWord]
                        if len(check) == 0:
                            ans.append(left)
                            leftWord = s[left:left+wordLength]
                            check[leftWord] = 1
                            left += wordLength
                    else:
                        check[rightWord] -= 1
                else:
                    if rightWord in dictionary:
                        while s[left:left+wordLength] != rightWord:
                            leftWord = s[left:left+wordLength]
                            check[leftWord] = check.get(leftWord, 0) + 1
                            left += wordLength
                        # why dont update 'check': now leftword = rightword, just move leftword(delete 1), and rightword already be counted
                        left += wordLength
                    else:
                        left = right+wordLength
                        check = dictionary.copy()
                
        return ans
s = Solution()
print(s.findSubstring("barfoofoobarthefoobarman",["bar","foo","the"]))
