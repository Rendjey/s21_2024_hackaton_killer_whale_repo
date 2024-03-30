import random

def base_controller():
    student = True
    random_number = random.randint(1, 20)
    if(random_number == 9):
        student = False
    return student