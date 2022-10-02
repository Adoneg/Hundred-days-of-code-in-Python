
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
# 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
# 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
#
# # if direction == "encode":
# def caesar(text, shift_num, cipher_direction):
#     shifted_letter = ''
#     if cipher_direction == "decode":
#         shift_num *= -1
#     for char in text:
#         if char in alphabet:
#             index = alphabet.index(char)
#             current_index = index + shift_num
#             shifted_letter += alphabet[current_index]
#         else:
#             shifted_letter += char
#     print(f"the {cipher_direction}d word is {shifted_letter}")
#
# should_continue = True
# while should_continue:
#     direction = input("Enter 'decode' decrypt and 'encode' to encrypt:\n").lower()
#     text = input("Type your text:\n").lower()
#     shift_num = int(input("Enter the shift number:\n"))
#
#     shift_num = shift_num % 26
#     caesar(text, shift_num, direction)
#
#     replay = input("Do you want to go again? enter 'yes' or 'no':\n").lower()
#     if replay == 'no':
#         should_continue = False
#
