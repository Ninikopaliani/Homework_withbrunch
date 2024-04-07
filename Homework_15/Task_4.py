def vowel_counter(word, vowel="aeiou"):
    counter = 0
    for i in word:
        for j in vowel:
            if i == j:
                counter += 1
            continue
    print(counter)


text = "test"
print("a. ", text, "->", end=" ")
vowel_counter(text)
print("-"*80)
text = "Python"
print("b. ", text, "->", end=" ")
vowel_counter(text)
print("-"*80)
text = "Kvaratskhelia"
print("c. ", text, "->", end=" ")
vowel_counter(text)




