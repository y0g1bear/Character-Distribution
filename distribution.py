"""
distribution.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
we = input("Please enter a string of text (the bigger the better): ")
harambe = ('The ditribution of characters in "'  + we +  '" is:')
print(harambe)
letters = []
wesplit = we.split()
alph = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
for e in alph:
    school = we.count(e)
    if not school == 0:
        letters.append(e*we.count(e))
for x in letters:
    print(x)
letters.
for l in range(26):
    jum = 0 
    while jum < len(letters)-1:
        wax = letters[jum]
        letters[jum]= letters[jum+1]
        letters[jum+1] = wax
    jum +=1
    
for g in letters:
    print(c)