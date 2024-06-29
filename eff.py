
file = open("eff_large_wordlist.txt", "r")
passphrases = []

# Loop to process the wordlist and append to a Py list (passphrases)
# Using for loop means that you don't need f.close() as the loop closes it

for x in file:
    s = x.split()
    words = s[1]
    passphrases.append(words)
    #print(passphrases)



# import urllib.request

# url = "https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt"
# data = urllib.request.urlopen(url)

# for line in data:
#     ...
