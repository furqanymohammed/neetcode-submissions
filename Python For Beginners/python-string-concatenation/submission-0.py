def concatenate(s1: str, s2: str) -> str:
    concats = s1 + s2
    if len(concats) > 10:
        return "Too long!"
    else:
        return concats




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
