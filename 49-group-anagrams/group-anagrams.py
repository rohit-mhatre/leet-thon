class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = {}

        for string in strs:
            sortedString = ''.join(sorted(string))

            if sortedString not in str_dict:
                str_dict[sortedString] = []
            
            str_dict[sortedString].append(string)

        return list(str_dict.values())