class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = {}
        for string in strs :
            stringSorted = ''.join(sorted(string))
            if stringSorted not in str_dict:
                str_dict[stringSorted] = []
            str_dict[stringSorted].append(string)

        return list(str_dict.values())