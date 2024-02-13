The code implements a rudimentary One Time Pad
The code takes in plain English text message as input, then XORs it with a Hexadecimal key to create an encrypted text which is also hexadedcimal
To use this code, a help menu is given as well. Please find below two test cases where a single word and multiple words are encrypted then decrypted using the right key
Then in the final test case, wrong key is  given to decrypt a text.
____________________________________________________________________________________________

Case 1: Single word encryption
┌──(root㉿kali)-[~/cryptography/programming2]
└─# python3 rajpal-one_time_pad.py                                                          
Error: Please specify either -e for encryption or -d for decryption.

┌──(root㉿kali)-[~/cryptography/programming2]
└─# python3 rajpal-one_time_pad.py -e HELLOHELLO
Encrypted Text: 240be99e0616bb31d3a5
Key: 6c4ea5d2495efe7d9fea
                                                                                                   

┌──(root㉿kali)-[~/cryptography/programming2]
└─# python3 rajpal-one_time_pad.py -d --text 240be99e0616bb31d3a5 --key 6c4ea5d2495efe7d9fea
Decrypted Text: HELLOHELLO

____________________________________________________________________________________________
Case 2: Sentence encryption and decryption
For a sentence, message is to be encrypted in quotation marks
┌──(root㉿kali)-[~/cryptography/programming2]
└─# python3 rajpal-one_time_pad.py -e "Hello TAs, this is Harshit."                         
Encrypted Text: 7b31a8ae0b78944d176029d79fee655ed9430da2dae74f8d2b2d00
Key: 3354c4c26458c00c644c09a3f787167eb0302deabb953ce542592e

┌──(root㉿kali)-[~/cryptography/programming2]
└─# python3 rajpal-one_time_pad.py -d --text 7b31a8ae0b78944d176029d79fee655ed9430da2dae74f8d2b2d00 --key 3354c4c26458c00c644c09a3f787167eb0302deabb953ce542592e
Decrypted Text: Hello TAs, this is Harshit.
____________________________________________________________________________________________
Case 3: Wrong key used
The program gives an error in this case. See how I have changed the correct key.
┌──(root㉿kali)-[~/cryptography/programming2]
└─# python3 rajpal-one_time_pad.py -e HELLOHELLO                                            
Encrypted Text: 2e399e1e0470095c28bb
Key: 667cd2524b384c1064f4

┌──(root㉿kali)-[~/cryptography/programming2]
└─# python3 rajpal-one_time_pad.py -d --text 240be99e0616bb31d3a5 --key 557ab2524b989f5678c4
Traceback (most recent call last):
  File "/root/cryptography/programming2/rajpal-one_time_pad.py", line 67, in <module>
    main()
  File "/root/cryptography/programming2/rajpal-one_time_pad.py", line 60, in main
    print(f"Decrypted Text: {decrypted.decode('utf-8')}")
                             ^^^^^^^^^^^^^^^^^^^^^^^^^
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xcc in position 3: invalid continuation byte
