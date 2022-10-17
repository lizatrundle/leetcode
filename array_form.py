
# runtime: 329 MS
#faster than 86.75% of python3 submissions 


#return the array form of the integer num + k 

def addToArrayForm(num: list[int], k: int) -> list[int]:
    array_string = "".join(str(x) for x in num)
    answer = int(array_string) + k
    new_list = []
    for x in str(answer):
        new_list.append(int(x))
        
    return new_list
