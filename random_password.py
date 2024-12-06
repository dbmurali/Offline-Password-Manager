import random
from random import shuffle


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



def ran():
    print("Welcome to the PyPassword Generator!")
    nr_letters = random.randint(3, 5)
    nr_symbols = random.randint(1, 3)
    nr_numbers = random.randint(3, 5)


    pass_words=[random.choice(letters) for _ in range(nr_letters)]
    pass_symbols=[random.choice(symbols) for _ in range(nr_symbols)]
    pass_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    my_pass=pass_words+pass_symbols+pass_numbers
    shuffle(my_pass)
    my_pass="".join(my_pass)
    return my_pass

