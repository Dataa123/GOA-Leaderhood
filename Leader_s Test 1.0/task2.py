def replace(word_list):
    word = ""
    for i in word_list:
        if i == int:
            word += "N"
        elif i == "0" or i == 0:
            word += "Z"
        else:
            word += "L"
    return word


print(replace([0, "m", "m", 123, "0", "m", 1]))