# pwdhelper
This utility is designed to be a simple password generator, which works offline. 


## Overview
Right now, the script carries out the following functions: 
1. Prompts the user for the number of passwords required, and the character length.
2. Once provided the script will spit out these passwords, with 3 digits and 2 punctuation characters.

There will eventually be a "Passphrase" function which allows the user to generate passphrases with the use of the [Electronic Frontier Foundations' Dice-Generated Passphrases](https://www.eff.org/dice) [list](https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt). This is a list that is created by Joseph Bonneau. And he has written a [deep dive](https://www.eff.org/deeplinks/2016/07/new-wordlists-random-passphrases) about passphrase security, and the methodology and criteria he used to create these EFF wordlists. Currently this wordlist sits in the directory for ease of access.


## Known Issues
There are a few bits that I need to figure out on my own to make this a bit nicer, and I will get round to these. They are:

1. Add in my work with the passphrase function.
2. Allow the user to specify how many digits and punctuation characters they want in their password.
3. Add a menu option to integrate everything together and make it easier to read and navigate through for the user. 
4. Allow the user to copy any of those passwords generated to the clipboard.
