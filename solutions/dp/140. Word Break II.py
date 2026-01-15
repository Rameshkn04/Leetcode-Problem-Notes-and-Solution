from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        wordSet = set(wordDict)
        n = len(s)

        @lru_cache(None)
        def dfs(start):
            if start == n:
                return [""]

            res = []
            for end in range(start + 1, n + 1):
                word = s[start:end]
                if word in wordSet:
                    for sub in dfs(end):
                        if sub:
                            res.append(word + " " + sub)
                        else:
                            res.append(word)
            return res

        return dfs(0)
