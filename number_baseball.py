import random


direction_message = "Please enter 4 numbers from 0 to 9 without duplicates, separated by spaces"

class Opponent:
    def __init__(self):
        self._nums = self._choice_nums()
        self.count = 0
    
    def _choice_nums(self):
        candidate = [i for i in range(0,10)]
        nums = []

        for _ in range(4):
            num = random.choice(candidate)
            nums.append(num)
            candidate.remove(num)
        
        return nums
    
    def compute_result(self, called_nums):
        score = {"strike":0, "ball":0}
        for answer, user_num in zip(self._nums, called_nums):
            if answer==user_num:
                score["strike"] += 1
                continue
            if user_num in self._nums:
                score["ball"] += 1

        self.count += 1
        return score


def validate_input(called_nums):
    if len(set(called_nums)) != 4:
        raise ValueError(direction_message)
    
    for called_num in called_nums:
        if not called_num.isdigit() or int(called_num)>9:
            raise ValueError(direction_message)


def parse_input(user_input):
    called_nums = user_input.strip(" ").split(" ")
    try:
        validate_input(called_nums)
        return [int(called_num) for called_num in called_nums]
    except ValueError as e:
        raise e
        

def start():
    opponent = Opponent()
    print(direction_message)
    while 1:
        try:
            called_nums = parse_input(input())
            result = opponent.compute_result(called_nums)
            print("-"*100)
            if result["strike"]==4:
                print("You Win!🎉")
                print("Count: {}".format(opponent.count))
                break
            print("Strikes: {}".format(result["strike"]))
            print("Balls: {}".format(result["ball"]))
            print("-"*100)
        except ValueError as e:
            print("-"*100)
            print(e)
    
        
if __name__=="__main__":
    start()