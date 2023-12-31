# Numbers-Station Simplified Guide

If you're fascinated by numbers stations on shortwave radio and want to create your own coded messages using a one-time pad, you've come to the right place. This tool has been generated with the help of ChatGPT.

---

**Please note: This readme is a work in progress and will be updated later.**

**How to Use:**

1. Start by installing three essential Python libraries using pip: `pyperclip`, `random`, and `string`.

2. Run the "generate-numbers.py" script. It will generate a file named "one_time_pad.txt."

3. Run the "encode-message.py" script and input your message. This script reads from the "one_time_pad.txt" file and encodes your message into numbers. Be sure to copy the numbers into the clipboard before starting the next step.

4. If you plan to use text-to-speech software to read the numbers, run the "group-numbers-for-tts.py" script. If you prefer to read the numbers aloud, use the "group-numbers.py" script instead.

5. Execute the "create-human-readable-otp.py" script. It will transform the "one_time_pad.txt" into a human-readable text file. Share this newly generated file with your intended recipient; it will be named "sorted_formatted_one_time_pad.txt," but feel free to rename it before sharing.

6. Should you wish to change your one-time pad, repeat the steps from 2 above to generate a new "one_time_pad.txt." Ensure that your one-time pad remains secure and confidential, as it's a critical component of encoding and decoding messages. Make sure you backup your old one-time pad before doing this (this is optional).

**Important Tips:**

If the "encode-message.py" script generates a group of numbers with less than 5 digits, follow these steps:

- Open the "sorted_formatted_one_time_pad.txt" file.
- Locate the number that corresponds to an empty space and use it to complete the string of numbers.
- Add another string of numbers below if needed.

For example, if your output is like this:

2, 9, 3, 9, 0.
3, 3, 9, 1, 4.
1, 9, 4, 5, 4.
0, 2, 9, 2, 9.
4, 2, 1, 9, 4.
5, 2, 1, 0, 3.
3, 9, 1, 9, 2.
0, 4, 0, 4, 8.
1, 9, 4, 8, 3.
4, 3, 5.


And the number for an empty space is "19," edit your output as follows:

2, 9, 3, 9, 0.
3, 3, 9, 1, 4.
1, 9, 4, 5, 4.
0, 2, 9, 2, 9.
4, 2, 1, 9, 4.
5, 2, 1, 0, 3.
3, 9, 1, 9, 2.
0, 4, 0, 4, 8.
1, 9, 4, 8, 3.
4, 3, 5, 1, 9


This ensures your numbers station maintains the correct format.

It's also recommended to duplicate each line if you want to mimic the Lincolnshire Poacher format, like this:

2, 9, 3, 9, 0.
2, 9, 3, 9, 0.
3, 3, 9, 1, 4.
3, 3, 9, 1, 4.
1, 9, 4, 5, 4.
1, 9, 4, 5, 4.
0, 2, 9, 2, 9.
0, 2, 9, 2, 9.
4, 2, 1, 9, 4.
4, 2, 1, 9, 4.
5, 2, 1, 0, 3.
5, 2, 1, 0, 3.
3, 9, 1, 9, 2.
3, 9, 1, 9, 2.
0, 4, 0, 4, 8.
0, 4, 0, 4, 8.
1, 9, 4, 8, 3.
1, 9, 4, 8, 3.
4, 3, 5, 1, 9
4, 3, 5, 1, 9


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

**Important Caution and Legal Disclaimer:**

We strongly discourage transmitting the encoded messages created using this tool over any radio frequencies, including but not limited to ham radio, CB radio, GMRS, MURS, or any other radio service. The use of radio frequencies for transmitting encoded messages without proper authorization may be subject to severe legal consequences.

Before considering any transmission over the airwaves, it is essential to research and fully understand the relevant local, regional, and national laws governing radio communications. Make sure you comply with all legal requirements and obtain any necessary licenses or permissions. We do not endorse or support any unauthorized radio transmissions, and users who choose to transmit messages in this manner do so at their own risk.

Please be aware that the use of radio frequencies without the proper authorization can lead to legal penalties, including fines and possible imprisonment. It is crucial to respect the rules and regulations that govern radio communications in your area.

By using this tool, you acknowledge that the creator of this software is not responsible for any actions you may take, including any legal consequences that may arise from transmitting messages over radio frequencies. Users are solely responsible for their own actions and should exercise caution and legal compliance when considering radio transmissions.
