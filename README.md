# Interactive_dataset_analyzer


# Project Goal: 

The goal of this project was to build an interactive dataset analyzer program that would
allow the user to enter a file containing a list of books (with the book's information) upon which
the user is then prompted to enter a command. Once the command has been entered, the dataset
analyzer would analyze the file and return the analyzed data to the user.

# The Project Design:

__The program will behave as described in the following steps:__

1) A user interface will prompt the user to enter a command however if the user inputs a
command other than “L” to load the data file, the user interface will prompt the user to
load a file.

2) Once the user loads a file, the program will ask to enter another command at which this
point the user can input a command to perform an action on the data using the analyzer (file named analyzer).

3) The program will then analyze the data and perform an action (like add a book or remove
a book etc.) and return the analyzed data to the user

4) The program will continue to the prompt the user until the user enters “Q” to exit the
program

With Python installed, run this command:

``` >>>python ```

The interactive user interface will run:

```
The available commands are:
1- L)oad data
2 -A)dd book
3- R) emove book
4- G)et books T)itle R)ate P)ublisher A)uthor
5- GCT)Get all Categories for book Title
6- S)ort books T)itle R)ate p)ublisher A)uthor
7- Q)uit
Please type your command:
```


When prompted, enter a command to execute the desired function. Some functions will ask for the file name or book title. To utilize commands 2-6, the dataset must be loaded or the messageor the message _"File not loaded"_ will be returned. To load the dataset, eneter L when prompted to enter a command. 
