import time
import copy
import random


direction_message = "Please enter 4 numbers from 0 to 9 without duplicates, separated by spaces"

class Opponent:
    def __init__(self):
        self._nums = self._choice_nums()
        self.count = 0
        self.all_candi = []
        self.make_candi(4)
        self.player_answer = []


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
    

    def make_candi(self, d, i=0, lst = []):
        if i==d:
            self.all_candi.append(copy.deepcopy(lst))
            return

        for n in range(10):
            if n in lst:
                continue
            else:
                lst.append(n)
                self.make_candi(d, i+1, lst)
                lst.pop()
    

    def compute_possible_answer(self, s, b, post_answer):
        while True:
            pre_n = len(self.all_candi)

            if s+b == 0:
                i = 0
                while i != len(self.all_candi):
                    for num in post_answer:
                        if num in self.all_candi[i]:
                            self.all_candi.remove(self.all_candi[i])
                            break
                    else:
                        i+=1
            else:
                i = 0
                while i != len(self.all_candi):
                    st, ba = 0, 0
                    for j in range(4):
                        if post_answer[j] == self.all_candi[i][j]:
                            st += 1
                        elif post_answer[j] in self.all_candi[i]:
                            ba += 1
                    
                    if st!=s or ba!=b:
                        self.all_candi.remove(self.all_candi[i])
                        continue

                    i += 1
            
            if pre_n == len(self.all_candi):
                break
        print(self.all_candi)
    

    def choice_answer(self):
        try:
            return random.choice(self.all_candi)
        except IndexError:
            raise IndexError
    

    def validate_user_answer(self, answer):
        try:
            str_and_ball = answer.split()
            answer = list(map(int, str_and_ball))
            for i in answer:
                if i>4:
                    raise ValueError
            return answer
        except ValueError:
            raise ValueError


class Player:
    def __init__(self):
        self.nums = []


    def validate_numbers(self, called_nums):
        if len(set(called_nums)) != 4:
            raise ValueError(direction_message)
        
        for called_num in called_nums:
            if not called_num.isdigit() or int(called_num)>9:
                raise ValueError(direction_message)
    
    def parse_input(self, user_input):
        called_nums = user_input.strip(" ").split(" ")
        try:
            self.validate_numbers(called_nums)
            return [int(called_num) for called_num in called_nums]
        except ValueError as e:
            raise e



def start():
    opponent = Opponent()
    player = Player()
    print(opponent._nums)

    print(direction_message)
    while 1:
        try:
            player_nums = player.parse_input(input())
            player.nums = player_nums
            print("-"*100)
            print("Great! Your numbers are {}, please remember it.".format(player.nums))
            for i in range(5, -1, -1):
                print(i, end="\r")
                time.sleep(1)
            print("Then, let's start!")
            time.sleep(2)
            print("-"*100)
            break
        except Exception as e:
            print("-"*100)
            print(e)

    
    while 1:
        # print("Your turn")
        # print(direction_message)
        # try:
        #     called_nums = player.parse_input(input())
        #     result = opponent.compute_result(called_nums)
        #     print("-"*100)
        #     if result["strike"]==4:
        #         print("You Win!🎉")
        #         print("Count: {}".format(opponent.count))  
        #         break
                          
        #     print("Strikes: {}".format(result["strike"]))
        #     print("Balls: {}".format(result["ball"]))
        #     print("-"*100)
        
        # except ValueError as e:
        #     print("-"*100)
            # print(e)

        print("CPU turn")
        try:
            answer = opponent.choice_answer()
        except IndexError:
            print("Wait!, I think you give me wrong answer.")
            print("Please check your answers!")
            for i in opponent.player_answer:
                print("Numbers:", i["cpu_answer"])
                print("Your answer:", i["player_answer"])
                print("-"*100)
            break

        print("CPU's answer:", answer)
        print("Please enter number of strikes and balls.")
        print("For example, If 3 stirkes and 1 ball, enter '3 1'")
        while 1:
            try:
                s, b = opponent.validate_user_answer(input())
                player_answer = {"cpu_answer":answer, "player_answer":{"strikes":s, "balls":b}}
                opponent.player_answer.append(player_answer)
                break
            except ValueError:
                print("Please enter correct format.")
        
        if s==4 and b==0:
            print("CPU WIN!!!")
            break
        
        opponent.compute_possible_answer(s, b, answer)
        print("-"*100)


def validate_input(char):
    if char not in ["y", "n", "Y", "N"]:
        raise ValueError
    else:
        return char


def is_next_game(char):
    if char in ["y", "Y"]:
        return True
    
    print("Bye! Thank you for playing.")
    time.sleep(1)
    return False


def want_next():
    while 1:
        print("-"*100)
        print("Do you want to play one more? (y/n)")
        try:
            char = validate_input(input())
            return is_next_game(char)
        except ValueError:
            print("Please enter y or n.")


if __name__=="__main__":
    is_continue = True
    while is_continue:
        start()
        is_continue = want_next()