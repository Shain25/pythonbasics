def longest_word (words: list[str]):
    longest=""
    for word in words:
       if len(word) > len(longest):
            longest = word
    return longest
print(longest_word(["orange", "banana", "blueberry", "kiwi"]))