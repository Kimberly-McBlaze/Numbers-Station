import random
import string

# Generate a one-time pad with shuffled numbers
def generate_one_time_pad():
    characters = list(string.ascii_uppercase + "1234567890.,!?@'-+$€£¥=* ")  # Uppercase alphabet and common punctuation marks
    random.shuffle(characters)
    shuffled_numbers = list(range(len(characters)))
    random.shuffle(shuffled_numbers)
    one_time_pad = {char: str(num) for char, num in zip(characters, shuffled_numbers)}
    return one_time_pad

# Save the one-time pad to a text file
def save_one_time_pad(one_time_pad, filename):
    with open(filename, "w") as file:
        for char, num in one_time_pad.items():
            file.write(f"{char}:{num}\n")

# Encode a message using the one-time pad
def encode_message(message, one_time_pad):
    encoded_message = ""
    for char in message:
        if char in one_time_pad:
            encoded_message += one_time_pad[char] + " "
    return encoded_message

# Decode an encoded message using the one-time pad
def decode_message(encoded_message, one_time_pad):
    reverse_pad = {v: k for k, v in one_time_pad.items()}
    encoded_chars = encoded_message.split()
    decoded_message = ""
    for char in encoded_chars:
        if char in reverse_pad:
            decoded_message += reverse_pad[char]
    return decoded_message

# Main program
if __name__ == "__main__":
    message = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.,!?@'-+$€£¥=* "
    
    # Generate a one-time pad
    one_time_pad = generate_one_time_pad()
    
    # Save the one-time pad to a text file
    save_one_time_pad(one_time_pad, "one_time_pad.txt")
    print("One-time pad saved to 'one_time_pad.txt'")
    
    # Encode the message
    encoded_message = encode_message(message, one_time_pad)
    print("Encoded Message: ", encoded_message)
    
    # Decode the message
    decoded_message = decode_message(encoded_message, one_time_pad)
    print("Decoded Message: ", decoded_message)