# Read the "one_time_pad.txt" file
with open("one_time_pad.txt", "r") as input_file:
    lines = input_file.readlines()

# Create a list to store the mappings
otp_list = []
for line in lines:
    key, value = line.strip().split(":")
    otp_list.append((int(value), key))

# Sort the list by the numeric values
otp_list.sort()

# Create the second text file with sorted content
with open("sorted_formatted_one_time_pad.txt", "w") as output_file:
    for i, (value, key) in enumerate(otp_list):
        formatted_value = f"{i:02d}"
        output_line = f"{formatted_value} - {key}\n"
        output_file.write(output_line)

print("Sorted formatted one_time_pad.txt created.")
