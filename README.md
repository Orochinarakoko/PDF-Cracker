# PDF-Cracker
A simple , terminal based python script that uses the pikepdf module in order to run a wordlist attack against a password-protected PDF file.

# How it works
1) The user inputs the wordlist they want to use , the target PDF file , and the number of threads they want to spawn.
2) The program opens the wordlist , and append the word on each line to a queue from the queue module.
3) Then , the program spawns the desired umber of threads - this increases the speed at which the program can crack the password.
4) Each thread gets a word from the queue and uses it as the password to try and open the PDF file using the word as the password.
5) If the thread can open the file using that particular password , then we tell the user that the word is the password.
6) If the thread cannot open the file using that particular password , then we can determine that the password is not that particular word , and the thread will then get another word from the queue
7) This is repeated untill the password is found , or the entire wordlist has been used


# Troubleshooting

If you recieve "ERROR OPENING [WORDLIST]":
 - Check that the wordlist you have passed is not password protected
 - Check that the wordlist you have passed is not corrupted
 - If all else fails , use a different wordlist or re-download the wordlist you were going to use

If the program freezes after completing the attack , you may have used too many threads - I recommend NO MORE THAN 500 THREADS

If you receive "NO FILE IN DIRECTORY CALLED [FILE]":
 - Check you have inputted then name of the file correctly
 - Check that you are running the script from the correct directory
 - Check , just in case , to see if the file is actually in your directory
 - If all else fails , re-download the file


If you find any other errors or bugs whilst using this script , please feel free to contact me and I will try to amend it.
