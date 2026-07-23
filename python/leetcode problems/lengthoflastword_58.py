def lengthOfLastWord(s: str) -> int:
    words = s.split()
    last_word = words[-1]
    return len(last_word)

print(lengthOfLastWord("hello world  from   python"))