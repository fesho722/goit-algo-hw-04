import random

def get_numbers_ticket(min, max, quantity):
    if not (1 <= min <= max <= 1000) or not (1 <= quantity <= max - min + 1):
        return []
    
    result = []
    result_no_repeat = set()
    while len(result_no_repeat) < quantity:
        result_no_repeat.add(random.randint(min, max))
    return result_no_repeat




    
