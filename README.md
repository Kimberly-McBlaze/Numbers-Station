# Numbers-Station Simplified Guide

If you're fascinated by numbers stations on shortwave radio and want to create your own coded messages using a one-time pad, you've come to the right place. This tool has been generated with the help of ChatGPT.

---

**Please note: This readme is a work in progress and will be updated later.**

**How to Use:**

1. Start by installing three essential Python libraries using pip: `pyperclip`, `random`, and `string`.

2. Run the "generate-numbers.py" script. It will generate a file named "one_time_pad.txt."

3. Run the "encode-message.py" script and input your message. This script reads from the "one_time_pad.txt" file and encodes your message into numbers.

4. If you plan to use text-to-speech software to read the numbers, run the "group-numbers-for-tts.py" script. If you prefer to read the numbers aloud, use the "group-numbers.py" script instead.

5. Execute the "create-human-readable-otp.py" script. It will transform the "one_time_pad.txt" into a human-readable text file. Share this newly generated file with your intended recipient; it will be named "sorted_formatted_one_time_pad.txt," but feel free to rename it before sharing.

**Important Tips:**

If the "encode-message.py" script generates a group of numbers with less than 5 digits, follow these steps:

- Open the "sorted_formatted_one_time_pad.txt" file.
- Locate the number that corresponds to an empty space and use it to complete the string of numbers.
- Add another string of numbers below if needed.

For example, if your output is like this:

2, 3, 2, 9, 0.
6, 1, 3, 0, 6.
1, 3, 2, 8, 2.
3, 1, 1, 1, 3.
2, 3.

And the number for an empty space is "16," edit your output as follows:

2, 3, 2, 9, 0.
6, 1, 3, 0, 6.
1, 3, 2, 8, 2.
3, 1, 1, 1, 3.
2, 3, 1, 6, 1.
6, 1, 6, 1, 6.

This ensures your numbers station maintains the correct format.

It's also recommended to duplicate each line if you want to mimic the Lincolnshire Poacher format, like this:

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

**The Lincolnshire Poacher Format:**

In case you want to follow the Lincolnshire Poacher format, here's how it works:

1. Start with a 1-minute interval signal.
2. Follow it with 1 to 2 seconds of silence.
3. Announce a 5-digit ID spoken 5 times.
4. Add 4 seconds of silence.
5. Repeat the same 5-digit ID spoken 5 times.
6. Insert a 12-second chime signal.
7. Share your message, which consists of numbers grouped into strings of 5. Each group of 5 numbers is sent twice.
8. After the message, include 4 seconds of silence.
9. Follow up with the 12-second chime signal.
10. Add 4 seconds of silence.
11. Conclude with a 1-minute interval signal before going off the air.
