#runtime beats 22.76% of python submissions

def canConstruct(ransomNote: str, magazine: str) -> bool:
        magazine_list = list(magazine)
        in_magazine = 0
        for x in range(len(ransomNote)):
            if ransomNote[x] in magazine_list:
                if magazine_list.index(ransomNote[x]) != None:
                    index = magazine_list.index(ransomNote[x])
                    magazine_list.pop(index)
                    in_magazine +=1
        if in_magazine == len(ransomNote):
            return True 
        return False

#testing 
ransomNote = "aa"
magazine = "ab"
print(canConstruct(ransomNote,magazine))
