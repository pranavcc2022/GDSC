def length_of_last_word(s):
    s = s.strip()

    if not s or len(s) <= 1 or len(s) >= 104:
        print("Input length must be greater than 1 and less than 104 characters.")
        return 0

    words = s.split()
    last_word = words[-1]

    return len(last_word)

user_input = input("Enter a string: ")

if len(user_input) > 1 and len(user_input) < 104:
    result = length_of_last_word(user_input)
    print("Length of the last word is:", result)
else:
    print("Input length must be greater than 1 and less than 104 characters.")