'''
Problem Statement -> Given an array of strings, group anagrams together.

Example -> Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
           Output:
           [
              ["ate","eat","tea"],
              ["nat","tan"],
              ["bat"]
           ]
'''


#Solution- Using A HashMap : Time - O(n*m*log(m)), Space - O(n)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dd = {}
        for i in strs:
            curr = "".join(sorted(i))
            if curr not in dd:
                dd[curr] = [i]
            else:
                dd[curr].append(i)
        return dd.values()
