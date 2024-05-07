FIRST_CHAR_CODE = ord("A")
LAST_CHAR_CODE =ord("Z")
CHAR_RANGE = FIRST_CHAR_CODE - LAST_CHAR_CODE + 1

def caeser_shift(message, shift):
    result=""

    for char in message.upper():
        if char.isalpha():
            char_code=ord(char)
            new_char_code=char_code + shift

            if new_char_code > LAST_CHAR_CODE:
                new_char_code -= CHAR_RANGE 

            if new_char_code < FIRST_CHAR_CODE:
                new_char_code += CHAR_RANGE 

            new_char=chr(new_char_code)
            result+=new_char

        else:
            result+= char

    print(result)

user_input= input("ENTER THE MESSAGE TO BE ENCRYPT/DECRYPT: ")
user_shift= int(input("ENTER SHIFT VALUE: "))
 
caeser_shift(user_input,user_shift)

