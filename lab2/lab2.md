## Introduction, Outline of Section
- Self Introduction
- Logistics:
	* Lab: Monday 10:30-11:30
	* Office hour:  Monday 11:30-12:30
	* Email: minjiaz@uchicago.edu
	* Mac User

## Some typo to fix in case you haven't done so

1. Under #2 in the salaries.sh file, the hint should state:
```
Hint: grep for ',F,' then use wc
```

2. In cell1 of the test_suite.ipynb file, change the second line to:
```
import matplotlib.pyplot as plt
```

3. In cell2 of the test_suite.ipynb file, change the second line to:
```
salaries = pd.read_csv('salaries.csv')
```

## Possible Installation Expectations
- Tell them that we expect them to have everything installed/signed up by the first week, and that they should attend section and office hours if they need any help...installation support will not be guaranteed after the first week — checklist below:
    * (Windows only) install cygwin
    * Sign up for Github
    * Download Git for command line
    * Download a Text Editor (Atom)
    * Install Python
        1. Make sure its the latest Python 3 version
        2. Make sure its the anaconda distribution (it comes with many packages and jupyter and makes life much easier)
    * Spend a bit of time to show them the website links and where they can download stuff... make sure everyone has stuff installed and help them debug/answer their questions

## ATOM Configuration
After install ATOM, it is almost ready to go, but there is a couple of things we need to do in setting, just to get everything working perfectly for programming in python

Hit command + , to bring the setting tab
- Editor Setting
	* Check __Show Indent Guide__ and __Show Invisible__ boxes. (To nevigate through your code showing the indentation. This is very helpful when you are working with html file in week 6 web scraping
	* Change Tab length from 2(defualt) to 4.
- Packages
	* Enable __autosave__
- Install
	* __autocomplete-python__ : python auto completion for variable, function
	* __Hydrogen__ : run code interactively, inspect data and plot
	* more to be installed ....

## CLI (Command Line Interface)
Why? - Compare to GUI (Graphical User Interface)
---"when you are a child you use a computer by looking at the pictures. When you grow up, you learn to read and write."

- Navigation
	* pwd (print working directory)
	* cd (change directory)
	```
    $ cd complete-pathname # General cd command
    $ cd ./relative-pathname
    $ cd .. 		    # Change to parent directory
    $ cd / 				# Change to root directory
    $ cd 				# Change to home (defualt) directory
    ```

 - Inspecting Files
 	* ls (list files and directories)
    ```
	$ ls -l # in long format
	$ ls -lh # in human readable format
	$ ls *.csv # filter for csv format file
    ```
 	* less (view text files)
	```
	$ less filename

 - Manipulating Files
 	* cp (copy files and directories)
 	* mv (move or reanme files and diretories)
 	* rm (remove file and diretories)
 	* mkdir (create new diretories)
 	* touch (create new file)
 	Explore these commands in http://linuxcommand.org/lc3_lts0050.php,
 	http://linuxcommand.org/lc3_lts0060.php

  - More advanced commands
    * curl
    ```
    $ curl data.cityofchicago.org/api/views/xzkq-xp2w/rows.csv -s -o salaries.csv
    ```
    * cat, less, head, tail, wc
    ```
    $ cat salaries.csv
    $ less salaries.csv
    $ head -n salaries.csv
    $ tail -n salaries.csv
    $ wc -l salaries.csv
    ```
    * grep with RegEx:
    __Standard RegEx w/o backslash__
	Reference: https://www.icewarp.com/support/online_help/203030104.htm
        * ^' and '$': the start and the end of a string
        ```
        "^abc"  # matches any string that starts with "abc".
        "abc$"  # matches a string that ends in with "abc".
        "^abc$" # a string that starts and ends with "abc" - effectively an exact match comparison.
        "abc"   # a string that has the text "abc" in it.
        ```
        * '*', '+', and '?': the number of times a character or a sequence of characters may occur. What they mean is: "zero or more", "one or more", and "zero or one."
        ```
        "ab*"   # matches a string that has an a followed by zero or more b's ("ac", "abc", "abbc", etc.)
        "ab+"   # same, but there's at least one b ("abc", "abbc", etc., but not "ac")
        "ab?"   # there might be a single b or not ("ac", "abc" but not "abbc").
        "a?b+$" # a possible 'a' followed by one or more 'b's at the end of the string: Matches any string ending with "ab", "abb", "abbb" etc. or "b", "bb" etc. but not "aab", "aabb" etc.
        ```
        * Braces { }: indicate ranges in the number of occurrences
        ```
        "ab{2}"   # matches a string that has an a followed by exactly two b's ("abb")
        "ab{2,}"  # there are at least two b's ("abb", "abbbb", etc.)
        "ab{3,5}" # from three to five b's ("abbb", "abbbb", or "abbbbb")
        ```
        Note that you must always specify the first number of a range (i.e., "{0,2}", not "{,2}"). Also, as you might have noticed, the symbols '*', '+', and '?' have the same effect as using the bounds "{0,}", "{1,}", and "{0,1}", respectively.

        To quantify a sequence of characters, put them inside parentheses:
        ```
        "a(bc)*"     # matches a string that has an a followed by zero or more copies of the sequence "bc"
        "a(bc){1,5}" # one through five copies of "bc."
        ```
        * Period .: any single character:
        ```
        "a.[0-9]" # matches a string that has an a followed by one character and a digit
        "^.{3}$"  # a string with exactly 3 characters
        ```
        * Bracket expressions: which characters are allowed in a single position of a string:
        ```
        "[ab]"           # matches a string that has either an a or a b (that's the same as "a|b")
        "[a-d]"          # a string that has lowercase letters 'a' through 'd' (that's equal to "a|b|c|d" and even "[abcd]")
        "^[a-zA-Z]"      # a string that starts with a letter
        ",[a-zA-Z0- 9]$" # a string that ends in a comma followed by an alphanumeric character
        ```
    * Program composition
        * Redirect >
        ```
        $ grep command > newfilename
        ```
        * Pipe |
        ```
        $ grep command | wc -l
        ```

## Scripts
Executation command
```
$ sh script.sh
```
Selfexplain your code using __echo__ (= print() in python)
```
$ echo "tell me about what does youe output means:"
```

## Git Commands
- Basic  
Check if your github accout is linked to your terminal
```
$ git config --global user.email
$ git config --global user.name
```

If not
```
$ git config --global user.email "you@example.com"
$ git config --global user.name "Your Name"
```

View the status of repo (whether the branch is up-to-date)
```
$ git status
```
Show history
```
$ git log
```

- HW git workflow
1) Accept the assignment on Github
2) Download your HW locally
```
$ git clone https://github.com/harris-ippp/s18-a01-username.git
```
3) Modify/Add the file in HW dir
4) Add the file to staging area
```
$ git add filename
$ git add -A # add ALL files
```

5) Commit (save) staged file
```
$ git commit filename -m 'commit message'
```
6) Push to Github
```
$ git push
```
7) go on your Github repo and check that everything is updated
