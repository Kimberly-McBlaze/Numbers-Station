# Numbers-Station
Inspired by numbers stations heard on shortwave radio, this will create a one-time-pad and encode your message into numbers. These scripts were generated using ChatGPT.
-------------

**How to use:**

1: Execute the "generate-numbers.py" file, it will create a "one_time_pad.txt" file.


2: Execute the "encode-message.py" file and type whatever message you want. It will read from the above file and generate some numbers according to the file above.


3: If you're using text-to-speech software to read the numbers, execute the "group-numbers-for-tts.py" file. If you prefer to read the numbers yourself, execute the "group-numbers.py" file instead.


4: Execute the "create-human-readable-otp.py" file, which will generate a human-readable text file from the "one_time_pad.txt" file, give this newly generated file to your intended recipient, the new file will be called "sorted_formatted_one_time_pad.txt", you can rename this file if you want before sending it to your recipient.


**Some things you should know about:**

If the "encode-message.py" script generates a group of numbers that is less than 5 digits, open the sorted_formatted file and look for the number that corresponds with an empty space and use that to fill in the rest of the string of numbers to complete the string, adding another string of numbers below that if necessary. For example, if your output is this:

2, 3, 2, 9, 0.

6, 1, 3, 0, 6.

1, 3, 2, 8, 2.

3, 1, 1, 1, 3.

2, 3.

and the number for an empty space is "16", edit your putout so that it reads the following:

2, 3, 2, 9, 0.

6, 1, 3, 0, 6.

1, 3, 2, 8, 2.

3, 1, 1, 1, 3.

2, 3, 1, 6, 1.

6, 1, 6, 1, 6.

This adds some extra padding so that your numbers station can maintain the correct format.

It is also highly recommended to duplicate each line if you want to be true to the Lincolnshire Poacher format, like this:

2, 3, 2, 9, 0.

2, 3, 2, 9, 0.

6, 1, 3, 0, 6.

6, 1, 3, 0, 6.

1, 3, 2, 8, 2.

1, 3, 2, 8, 2.

3, 1, 1, 1, 3.

3, 1, 1, 1, 3.

2, 3, 1, 6, 1.

2, 3, 1, 6, 1.

6, 1, 6, 1, 6.

6, 1, 6, 1, 6.
