### Building a Translator that converts all vowels to "g"
def tranlate(phrase):
    result = ""
    for letter in phrase:
        #if letter in "AEIOUaeiou":
        if letter.lower() in "aeiou":
            if letter.islower():
                result += "g"
            else:
                result += "G"
        else:
            result += letter
    return result







###
###
### Main codes:

print(tranlate(input("Enter a phrase: ")))











