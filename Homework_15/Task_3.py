def inverse_word(string):
    if len(string) <= 1:
        return string
    else:
        return string[-1] + inverse_word(string[:-1])


input_string = "test"
inverse = inverse_word(input_string)
print("a. ", input_string, "->:", inverse)
print("-"*80)
input_string = "Abc"
inverse = inverse_word(input_string)
print("b. ", input_string, "->:", inverse)

