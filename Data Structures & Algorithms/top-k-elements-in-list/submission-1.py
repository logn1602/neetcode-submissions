class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts_x = {}
        for x in nums:
            if x in counts_x:
                counts_x[x] += 1
            else:
                counts_x[x] = 1
        # return counts_x.items()
        sorted_counts = sorted(counts_x.items(), key=lambda s: s[1], reverse=True)
        
        sliced_counts = sorted_counts[:k]
        output_d = []
        for pair in sliced_counts:
             output_d.append(pair[0])
        return output_d  
        

