def remove_fourth_character(word: str) -> str:
    beforeword = word[:3]
    afterword = word[4:]
    combinedword = beforeword + afterword
    return combinedword


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
