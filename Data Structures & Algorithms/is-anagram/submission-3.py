class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            count_s = {}
            count_t = {}
            for c in s:
                count_s[c] = count_s.get(c, 0) + 1
            print(count_s)
            for r in t:
                count_t[r] = count_t.get(r, 0) + 1
            print(count_t)

            if count_s == count_t:
                return True
            else:
                return False
