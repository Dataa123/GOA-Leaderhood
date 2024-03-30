def popout(word):
    word = word.lower()
    new_word = ""
    for i in word[:]:
        if word.count(i) < 2:
                new_word += i
                break
    return new_word

print(popout("Traqtori"))
print(popout("sTreSS"))
print(popout(" .mmeerraabi"))
print(popout("aabb"))

# half completed