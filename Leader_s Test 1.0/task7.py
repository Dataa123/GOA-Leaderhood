def replace(word):
    output = ""
    for i in word[:]:
        if word.count(i.lower()) >= 2:
            output += ")"
        else:
            output += "("
    return output
print(replace("recede"))
print(replace("Success"))

#completed