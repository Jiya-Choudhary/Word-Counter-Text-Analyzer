print("Word_Counter")
para = input("Enter Paragraph: ")
words_list=para.split()
word_count = len(words_list)
print("Number of words:", word_count)
longest_word =""
vowels ="aeiouAEIOU"
found_vowels =[]
for word in words_list:
    if len(word)>len(longest_word):
        longest_word=word
for char in para:
    if char in vowels and char not in found_vowels:
        found_vowels.append(char)
print("Longest word:", longest_word)
print("Vowels found:", found_vowels)

