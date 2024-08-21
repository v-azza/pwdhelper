# pwdhelper
This utility is designed to be a simple password generator, which works offline. 


## Overview
This script has been created to help users generate passwords without being connected to the internet. This makes use of the in-built Python modules 'random' and 'string'. 

There is a "Passphrase" function which allows the user to generate passphrases with the use of the [Electronic Frontier Foundations' Dice-Generated Passphrases](https://www.eff.org/dice) [list](https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt). This is a list that is created by Joseph Bonneau. And he has written a [deep dive](https://www.eff.org/deeplinks/2016/07/new-wordlists-random-passphrases) about passphrase security, and the methodology and criteria he used to create these EFF wordlists. Currently this wordlist sits in the directory for ease of access.


## Dependencies
### Python3 modules:
- random (Built-in)
- string (Built-in)
- [pyperclip](https://pypi.org/project/pyperclip/)


## Known Issues
There are a few bits that I need to figure out on my own to make this a bit nicer, and I will get round to these. They are:

1. ~~Add in my work with the passphrase function.~~
2. ~~Allow the user to specify how many digits and punctuation characters they want in their password.~~
3. ~~Add a menu option to integrate everything together and make it easier to read and navigate through for the user.~~ 
4. ~~Allow the user to copy any of those passwords generated to the clipboard.~~
5. ~~Allow the user to re-print the last passwords generated in the terminal using the tool.~~
6. Improve error checking and checks to see whether the script is being run directly.
