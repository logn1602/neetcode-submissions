class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for words in strs:
            count = [0] * 26
            for i in words:
                count[ord(i)- ord('a')] += 1
            key = tuple(count)
            
            result[key].append(words)
        return list(result.values())



        