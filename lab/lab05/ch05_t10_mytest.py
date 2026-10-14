pyg = "ay"

original = input("Enter a word: ")

if len(original) > 0 and original.isalpha():
    # Convert the word to lowercase and get its first letter.
    word = original.lower()
    first = word[0]

    # Add the first letter and suffix, then remove the original first letter.
    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)]

    # Display the translation.
    print(new_word)
else:
    print("empty")