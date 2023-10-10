'''movie guesser'''

#more hints for longer names? done btw
# just adding comments AND FFS delete unnecessary ones b4 putting in git xD
# already on git, still havent fixed above 
# a LOT of comments to fix :(
# putting in git and backing up at github(as private tho), will check it out some other time

import random as rd

#--variables--

y,yes='y','y'

movie_list = ['Twilight', 'Extraction', 'inception', 'republic', 'Godzilla',
         'Hotel Transylvania', 'Jurassic World', 'The Pursuit of Happyness',
         '2012', 'The Suicide Squad', 'Now You See Me', 'The Conjuring',
         'Jurassic world', 'Superman', 'Venom', 'Aquaman', 'Annabelle',
         'Dumbo', 'The Avengers', 'Interstellar', 'Cars', 'Despicable Me',
         'Captain America', 'Fast and Furious','inception','cindrella',
         'dangal','Fantastic Beasts']

score_brd = dict() #show scoreboard

#--functions--

# display score of player
def dscore(name,score = 0):
    name = name.lower()
    if name in score_brd.keys():
        score_brd[name] = score_brd[name] + score
    else:
        score_brd.update({name:score})
        
def show_score():
    for i,j in score_brd.items():
        print(i,j)

# to add space to movie name while displaying it
def insert_spaces(movie_title, dashed_title):
    """
    Generate a new list by inserting spaces in a given list at the positions where there are spaces in a movie title.

    Parameters:
    - movie_title (list): A list representing a movie title.
    - dashed_title (list): A list representing a dashed version of the movie title with spaces to be inserted.

    Returns:
    - list: A new list with spaces inserted at the positions where there are spaces in the movie title.
    """
    space_positions = []  # position of spaces
    for i in range(len(movie_title)):
        if movie_title[i] == ' ':
            space_positions.append(i)
            dashed_title[i] = ' '

    return dashed_title

# to remove spaces from movie name to ease processing
def remove_spaces(input_string):
    """
    Removes all occurrences of spaces in the given string.

    Parameters:
        string (str): The input string from which spaces will be removed.

    Returns:
        str: The modified string with all spaces removed.
    """
    return input_string.replace(" ","")
    
def generate_hint(x):
    """
    Generates a hint for the game based on the given condition.

    Parameters:
    - x (str): The condition to generate the hint. If `x` is equal to 'y', a hint will be generated.

    Global Variables:
    - a (unknown type): Global variable used in the function.
    - r_movie_list (list): Global variable representing a list of movies.
    - dashed (list): Global variable representing a list of characters with hidden letters.

    Returns:
    None
    """
    global a,r_movie_list,dashed
    if x == 'y' :
        if dashed.count('_')>2 :
            while True:
                #random index from movie list to give hint
                rr = rd.randrange(len(r_movie_list)) 
                #checking if to be hinted spot is empty 
                if dashed[rr] == '_' :
                    break
                else:
                    continue
            #putting hint in dashed list
            dashed[rr] = r_movie_list.copy()[rr] 
            #replacing elements from r movie list so they dont get used again 
            r_movie_list[rr] = 0

def play(number_of_turns, hint = None ) :
    """
    Plays a game of guessing a movie name.

    Args:
        number_of_turns (int): The number of turns the player has to guess the movie name.
        hint ('y', optional): Option to enable hints. Enter 'y' to enable hints. Defaults to None.

    Returns:
        None
    """
    global a,r_movie_list,dashed,movie_list
    
    random_movie = rd.choice(movie_list)
    mod_movie = remove_spaces(random_movie).lower() #modifing randomly chosen movie to make it easier to play

    r_movie_list = list(mod_movie) #list of letters of chosen movie name

    rcopy = r_movie_list.copy() #copy of above list, to check is user has given correct answer
    
    dashed = ['_' for i in range(len(mod_movie))] #dashed list to show to player
    
    dashed[0] = r_movie_list.copy()[0] #putting 1st compulsory hint in dashed list
    if len(r_movie_list) > 7:
        for i in range(3):
            generate_hint('y')
    if len(r_movie_list) > 13:
        for i in range(3):
            generate_hint('y')
    
    r_movie_list[0] = 0 #replacing elements from r movie list so they dont get used again
    
    mod_dashed = insert_spaces (list(random_movie),dashed.copy())
    for j in mod_dashed :    
        print(j,end = ' ')
    print()
    print()
    print(f'The movie has {len(mod_movie)} letters')
    print()
    if (hint == 'y') :
        print('''Hints option is enabled.
Hints will be given only after first turn and if more than two blanks are present. ''','\n')
    else:
        print('Hints option is disabled')
    a = 1
    score = 10
    
    while a <= (number_of_turns) :
        
        user_guess = remove_spaces(input('Guess the name : '))
        if len(user_guess) > len(r_movie_list):
            print("please do not enter input longer than the movie",'\n')
            continue
        print()
        list_guess = list(user_guess)
        
        for i in list_guess:  #looping elements of list guess
            if i in r_movie_list :  #checking if element is present in elemts/letters of *list* of chosen movie
                x = r_movie_list.index(i)  #finding index of element in r movie list
                
                r_movie_list[x] = 0 #replacing elements from r movie list so they dont get used again
                dashed[x] = i #putting valid element in correct position of dashed list 
                
        generate_hint(hint)
        mod_dashed = insert_spaces (list(random_movie),dashed.copy())
        for j in mod_dashed :    #printing dashed list
            print(j,end = ' ')
        
        print()
        if dashed == rcopy :
            print(f'Congratulations you won and your score is {score}!!')
            print(f"The right answer was : {random_movie}")
            break
        elif a == (number_of_turns) :
            print("Better luck next time")
            print(f"The right answer was : {random_movie}")
            break
        else:
            a = a+1
            if (hint == 'y') :
                score = score - 2
            else:
                score = score - 1
            continue

play(4)