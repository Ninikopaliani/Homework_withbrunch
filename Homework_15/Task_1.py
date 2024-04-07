def main(t):
    if switch == "f":
        print(f"{t}℃ is >> {t * 9/5 + 35}℉")
    elif switch == "c":
        print(f"{t}℉ is >> {(t-32) * 5/9}℃")
    else:
        print("please enter correct symbol")


n = 5
switch = input(" please enter c -> for switch celsius or f -> for switch fahrenheit: ")
print("-"*80)
print("example_1: ")
main(n)
print("-"*80)

print("example_2:")
n = 22
main(n)
print("-"*80)






