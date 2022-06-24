expected_str = "apa"
expected_str2 = "hehe"
str = input("The string to check is: ").lower()
# assert str == expected_str
# assert str == expected_str2
if str[0] == str[-1]:
    print("equal")
else:
    print("Not equal")
