class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anams = {}
        for word in strs:
            key = "".join(sorted(word))

            if key not in anams:
                anams[key] = []

            anams[key].append(word)
        return list(anams.values())



        