name = input("Enter the name:")
vowel = ['a', 'e', 'i', 'o', 'u']
for char in name:
    if char in vowel:
        print(char, '-It is a vowel')
    else:
        print(char, '-It is a constrant')
