import random

# TOTAL OF PLACES BY FLOORS
PLACES = 27
FLOORS = 3

# CODES
LETTERS = ['A', 'B', 'C', 'D']

def generate_code(i):
    code = ""
    for _ in range(4):
        code += random.choice(LETTERS)
    code += "-"
    for _ in range(4):
        code += str(random.randint(0,9))
    if i < 9:
        code += f"-0{i+1}"
    else:
        code += f"-{i+1}"
    return code

class Floor():

    def __init__(self):
        self.all_places = [{"status": "D", "code": generate_code(i)} for i in range(PLACES)]

    def add_car(self, place):
        if self.all_places[place-1]["status"] == "D":
            self.all_places[place-1]["status"] = "V"
            return True
        else:
            return False

    def remove_car(self, place, code):
        if self.all_places[place-1]["status"] == "V":
            if self.all_places[place-1]["code"] == code:
                self.all_places[place-1]["status"] = "D"
                return True
        else:
            return False

    def get_free_places(self):
        free_places = [i+1 for i in range(PLACES) if self.all_places[i]["status"] == "D"]
        return free_places

    def get_taken_places(self):
        free_places = self.get_free_places()
        taken_places = []
        for i in range(PLACES):
            i+= 1
            if i not in free_places:
                taken_places.append(i)
        return taken_places


class Parking():

    def __init__(self, floors):
        self.parking = [Floor() for _ in range(floors)]
    

parking = Parking(3)

while True:
    print("********************************")
    #Ask for floor
    valid = False
    while not valid:
        user_floor = input(f'At which floor are you? 1-{FLOORS} : ')
        try:
            if int(user_floor) in range(1, FLOORS+1):
                floor = parking.parking[int(user_floor)-1]
                valid = True
                break
        except:
            print("Please try again.")
    
    #Ask for enter/exit
    valid = False
    while not valid:
        enter_or_exit = input('Do you want to enter or exit? Enter/Exit : ').lower()
        try:
            if str(enter_or_exit) == "enter" or str(enter_or_exit) == "exit":
                valid = True
        except:
            print("Please try again")

    #Enter
    if enter_or_exit == "enter":
        valid = False
        free_places = floor.get_free_places()
        while not valid:
            place_choice = input(f'Which place do you want ? {free_places} : ')
            try:
                #If place is free
                if int(place_choice) in free_places:
                    if floor.add_car(int(place_choice)) is True:
                        print(f"Valid ✔\nKeep your code in your mind, you'll need it to exit : {floor.all_places[int(place_choice)-1]['code']}")
                        valid = True
            except:
                print("Please try again.")

    #Exit
    elif enter_or_exit == "exit":
        valid = False
        try_ = 1
        while not valid:
            taken_places = floor.get_taken_places()
            user_code = input("Enter your code please : ").upper()
            try:
                user_place = int(user_code.split("-")[-1])
                if floor.remove_car(user_place, user_code) is True:
                    print(f"Valid ✔\nSee you later !")
                    valid = True
            except:
                if try_ == 3:
                    valid = True
                    print("Too many mistakes. Please do all again.")
                else:
                    print(f"Please try again, you still have {3-try_} chances.")
                try_ += 1