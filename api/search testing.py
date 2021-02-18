import string
line = 'string FOR searching Terms'

userInput = input("search term:")
userInputlow = userInput.casefold()
lineLow = line.casefold()
if userInputlow in lineLow:
    string = string.capwords(lineLow)
    print(line)
    print(string)

    # author = author.casefold()
    # print(author)
    # author = string.capwords(author)
    # print(author)