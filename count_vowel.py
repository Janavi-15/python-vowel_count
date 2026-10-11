def count_vowel(word):
    count = 0
    for letter in word.lower():
        if letter in "aeiou":
            count = count + 1
    print(count)

a = input("Enter any word:")
count_vowel(a)