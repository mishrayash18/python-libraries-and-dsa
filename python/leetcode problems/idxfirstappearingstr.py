"index of the first appearance of a string"
def strstr(heystack:str, needle:str):
    if needle in heystack:
        return heystack.index(needle)
    else:
        return -1

print(strstr("bdbdbsad", "sad"))