## Introduction, Outline of Section
- Self inteiduction
- Logistics:
	* Office hour Monday 11:30-12:30
	* Email: minjiaz@uchicago.edu
	* Mac User

## Possible Installation Expectations
- Tell them that we expect them to have everything installed/signed up by the first week, and that they should attend section and office hours if they need any help...installation support will not be guaranteed after the first week — checklist below:
    * (Windows only) install cygwin
    * Sign up for Github
    * Download Git for command line
    * Download a Text Editor (Atom)
    * Install Python
        * 1. Make sure its the latest Python 3 version
        * 2. Make sure its the anaconda distribution (it comes with many packages and jupyter and makes life much easier)
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
	* more to be insallted ....

## CLI (Command Line Interface)
Why? - Compare to GUI (Graphical User Interface)
---"when you are a child you use a computer by looking at the pictures. When you grow up, you learn to read and write."

- Navigation
	* pwd (print working directory)
	* cd (change directory)

	```
    $ cd complete-pathname # General cd command
    $ cd ./relative-pathname
    $ cd .. 		    # Change to parent directoy
    $ cd / 				# Change to root directory
    $ cd 				# Change to home (defualt) directory
    ```

 - Inspecting Files
 	* ls (list files and directories)

    ```

    ```
 	* less (view text files)
 	* file (calssfiy a file's contents)


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
```
You can also add ALL file to staging area
```
$ git add -A
```
5) Commit (save) staged file
```
$ git commit
```
