# Step 1: Read the one-time pad from a text file
def read_one_time_pad(filename):
    pad = {}
    with open(filename, 'r') as file:
        for line in file:
            char, number = line.strip().split(':')  # Strip leading/trailing whitespaces
            if char.strip() == '':
                pad[' '] = int(number)  # Map whitespace to space character
            else:
                pad[char] = int(number)
    return pad

# Step 2: Create a function to encode a message using the one-time pad
def encode_message(message, one_time_pad):
    encoded_message = []
    message = message.upper()  # Convert the message to uppercase
    for char in message:
        if char in one_time_pad:
            number = one_time_pad[char]
            # Format single-digit numbers with a leading "0"
            if number < 10:
                encoded_message.append(f'0{number}')
            else:
                encoded_message.append(str(number))
        elif char == ' ':
            encoded_message.append(f'0{one_time_pad[" "]}')  # Use the number associated with the space character
        else:
            encoded_message.append(char)  # Leave non-alphabet characters as-is
    return ' '.join(encoded_message)

# Step 3: Allow the user to input a message and encode it
if __name__ == "__main__":
    pad_filename = "one_time_pad.txt"  # Replace with your one-time pad file
    one_time_pad = read_one_time_pad(pad_filename)

    message = input("Enter the message you want to encode: ")
    encoded_message = encode_message(message, one_time_pad)

    print("Encoded message:", encoded_message)
