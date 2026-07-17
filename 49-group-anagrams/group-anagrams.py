class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap=defaultdict(list)
        for i in strs:
            chars=list(i)
            chars.sort()
            key="".join(chars)
            hashmap[key].append(i)
        return list(hashmap.values())