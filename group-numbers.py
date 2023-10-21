import pyperclip

def group_numbers_into_fives(input_string):
    # Remove any non-numeric characters from the input string
    input_string = ''.join(filter(str.isdigit, input_string))

    # Split the string into groups of 5
    groups_of_fives = [input_string[i:i+5] for i in range(0, len(input_string), 5)]

    return groups_of_fives

# Read the input string from the clipboard
input_string = pyperclip.paste()

if input_string:
    result = group_numbers_into_fives(input_string)
    for group in result:
        print(group)
else:
    print("No valid input found in the clipboard.")
