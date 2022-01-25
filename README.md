# lets_drink


Lets_Drink is a software development project that allows users to 
obtain information about their favourite cocktails. 
In addition, it allows to get information about cocktails of the same category 
or with same alchool type and return all the characteristics available
in order to create and serve the requested drink.



If the name of the cocktail given as input is not present or
not available you can also insert it. 
All of this can be managed directly from the user's machine terminal.

In the following paragraphs you'll find a general overview about the original CSV file from
which we have taken the initial data, as well as a short explanation of how the software 
works and the outputs the user can obtain.

# CSV file 
In order to store all the paintings and authors, we created a CSV file called
 `cocktails_data.csv`, defined by the following properties:
 -Drink Name
 -Glass
 -Instruction
 -Basic_taste
 -Category
 -Ingridients
 -Alcohol_type
 
 
The original database contained tons of raws with repetitions and useful and very ofte empty cells, so we decided to restructure the csv file.
All the information is needed by the software to work properly and to perform the functions
we created.
 
# How to start

The first thing to do in order to develop the main functionalities just described
is to clone the remote directory. 

To do this, the user can type:

`git clone https://github.com/PaolaCasillo/lets_drink.git

This will automatically download all the files the user needs to run the program.

# Functionalities

In order to develop a suitable structure for our project according to the intended goals,
we created 4 main functions and stored them into different modules:

-  `add_element` function;
-  `check_drink function;
-  `return_chr` function;
-  `similarities` function.

All these functions are called by argparse from the `main.py` module by the corresponding
optional arguments.

This means that if the user wants to get some insights from our functions, he/she
doesn't need to point to the specific module that contains the function, but in general 
it's enough to type:

```bash
python main.py "name of the drink" -optional argument
```

The name of the drink is indeed a positional argument that should always 
be included. 

No optional argument is required if the user only wants to know if the cocktail
is present in our database..

For example, if we want to know if the classic "Spritz" is present, we only neeed to write:

```bash
python main.py "Spritz"
```

And the output will be:

```bash
In order to do  Spritz  you need:  Aperol, Prosecco and Sparkling Water  
Instruction:  Mix one third of Prosecco, one third of Aperol and one third of Sparkling Water, add ice.
```

Instead, for more complicated queries, we can recall some optional arguments. 

Here follow some examples:
 
 
 
 
 
 
 
 
 
 
 