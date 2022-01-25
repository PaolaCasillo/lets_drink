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

### •	Add a new cocktail (-a)

```bash
python main.py "my Drink" -a
```
This argument allows to insert a new drink to the database. The `-a` activates the 
`add_element` function which first checks if the drink already exists in our database 
and then generate a sequence of questions to insert all the necessary data, such as the ones below:
```bash
Now enter the ingridients of the drink->1
Now enter the intruction to do it -> 2
Now enter the Alcohol_type -> 3
Now enter the type of glass to use to serve it->4
Now enter the basic taste of the drink->5
Now enter the category of the drink->6
Thank you for your contribution!
```

### •	Find manually if the drink is present in the database (-d)

```bash
python main.py "Spritz" -d
```
fter being called, the argument `-d` allows to get the database relation 
between all drink and ingridients as follows:

```bash
Now you can see by yourself which cocktails you can do with your availale ingridients
After sex : Orange Juice and vodka
1                Bloody Mary  : Vodka and tomato juice 
2        Spritz : Aperol, Prosecco and Sparkling Water 
3                      Gin Tonic : Gin and tonic water 
4     Cosmopolitan : Vodka, Triple Sec, Lemon Juice,...
5              Cuba Libre : White Rum, Lime Juice, Cola
6     Long Island : Gin, Tequila, Vodka, White Rum, ...
7     Sex on the beach : Vodka, Peach schnapps, Oran...
8     Negroni : Campari, Gin, sweet vermouth, organz...
9     Americano : Campari, Sweet Vermouth, Soda wate...
10        Moscow Mule : Vodka, lime juice, ginger beer 
11    Margarita : Cazadores Tequila, triple sec liqu...
```


It's possible to see them separated with the following commands:

- `python main.py "Drinks" -drk` which allows to see the entire list of cocktails
- `python main.py "gin" -p`, to have access to the entire list of alcholics

that's an example of -drk output:
```bash
0            After sex
1         Bloody Mary 
2               Spritz
3            Gin Tonic
4         Cosmopolitan
5           Cuba Libre
6          Long Island
7     Sex on the beach
8              Negroni
9            Americano
10         Moscow Mule
11           Margarita
12             Mojito 
```
 
### •	Print all characteristics of the given drink (-chr)
 
 