#1. Write a function  count_vowels(word) that takes a word as an argument and returns the number of vowels in the word

def count_vowels(word) :
    count = 0
    vowels = ["a", "e", "i", "o", "u"]
    for letter in word.lower():
        if letter in vowels:
            count+=1
    return count

words = ["Sanyukta", "Naman", "Arsh", "Shivangi", "Shruti", ""]

for i in words:
    count = count_vowels(i)
    print("Number of vowels in words", count)