# Character Distribution

The purpose of this challenge is to gain proficiency with looping, decision making and lists.

Write and submit a Python program that computes and displays the distribution of characters 
in a given sample of text.

Output of your program should look like this:

```Please enter a string of text (the bigger the better): <em>The rain in Spain stays mainly in the plain.</em>
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
```

Notice about this example:

* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. For example, 
  in the printout above, the letters e, h, l, p and y both occur twice in the text and they are 
  listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.

There are a few techniques or tricks that you may find handy when working on this challenge. 
If you see something here that sounds useful, feel free to learn more about it!

* ```python
  'a string has several characters'.count('a')``` will return 5, which is the number 
  of times the character 'a' appears in the string.
* ```python
  zip([1,4,2],['a','z','q'])``` will return an iterator for generating a list of *tuples* 
  (another type of list) like this: ```[(1, 'a'), (4, 'z'), (2, 'q')]```
* If ```mylist``` is a list like ```[435, 2, 45, 2]``` then
  ```python
  mylist.sort()``` will change it to: ```[2, 2, 45, 435]```
  
  
            <li>If <code>mylist</code> is a list like [435, 2, 45, 2]</code> then
                <code class="prettyprint lang-py">mylist.append(99)</code> will change it to: [435, 2, 45, 2, 99]</li>
            <li>If <code>mylist</code> is a list like [435, 2, 45, 2]</code> then mylist[-1] will return 2, the last
            element in the list.</li>
            <li>You can get the length of a string, or number of elements in a list using the builtin
            <code class="prettyprint lang-py">len()</code> function. For example:
            <code class="prettyprint lang-py">len([435, 2, 45, 2])</code> will return 4.</li>
            <li>If you <code class="prettyprint lang-py">import string</code> then use
            <code class="prettyprint lang-py">string.ascii_lowercase</code> to get a string with the letters a-z in it.</li>
        </ul>
