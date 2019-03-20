# Knapsack case
Genetic algorithm case for workshop with CogitoNTNU

### Requirements
- python 3.7 (should also work with python 2.7)
- matplotlib
- requests

Run `pip install -r requirements.txt` in a terminal, and you should
 be able to run the code.


### Problem definition: what to do?
Your task is to find a set of buildings that cover the largest possible
area of the site without overlapping.

You are given a polygon defining the building site, and a set of 
predefined buildings in the file `data.json`. This data
is parsed by the helper function `read_problem_from_json()`, and returned as
the `site_polygon` and the list `building_vector` which together serve as
the problem definition. 

The `building_vector` contains 3000 buildings, far more than you will be able to fit on
the building site. The polygon defining the footprint of each building is
found at `building_vector[building_index]["coordinates"]` 

### Code overview: where to start?
To solve the case, it should suffice to work with the two files main.py 
and GA_helpers.py. 
The other files are supporting functions that need not be changed.

The example solution uses a representation where the genome is a binary string
of the same length as the building vector. Each True/False value in the genome
defines whether the corresponding building in the `building_vector` if 
included (True) in the solution or not (False). 

Other representations than this can be used, as long as the solution
genome is converted to such a binary string before submission to the score board.

#### main.py
This file contains the top level definition of the working
(but pretty poorly preforming) implementation of a 
GA solution to the problem. Here parameters of the algorithm are defined,
and the choices of which methods to use for parent selection, crossover, 
mutation, survivor selection etc. are made.

Here you should implement your top-level strategy for solving the problem.

#### GA_helpers.py
This file contains the implementation of some helper functions and
various simple genetic algorithm operators, including tournament
selection methods and simple mutation and crossover operations 
for binary string genomes.

Here you should implement the specific operators and helper functions you 
need to support your strategy for solving the problem.

### Submission to the score bord
When you are ready to submit, you may use of one of two functions provided. In `GA_helpers.py` there is a function
named `post_best_solution_to_highscore`. It takes your population (with the assumption that you have used the provides Individual class)
and your name as input and posts the best solution to the scoreboard. You may also use `post_genome_to_highscore` in `data_client.py`
which takes the genome you want to post to the scoreboard, and your name as arguments. 

