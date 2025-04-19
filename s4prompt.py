class Quokka:
    def __init__(self, arm_length, leg_length, num_eyes, has_tail, is_furry):
        self.arm_length = arm_length
        self.leg_length = leg_length
        self.num_eyes = num_eyes
        self.has_tail = has_tail
        self.is_furry = is_furry

    def about(self):
        print("Quokka:")
        print(f"Arm Length: {self.arm_length}")
        print(f"Leg Length: {self.leg_length}")
        print(f"Number of Eyes: {self.num_eyes}")
        print(f"Has Tail: {'Yes' if self.has_tail else 'No'}")
        print(f"Is Furry: {'Yes' if self.is_furry else 'No'}")


my_fave = Quokka(arm_length=3.5, leg_length=4.5, num_eyes=2, has_tail=True, is_furry=True)
my_fave.about()
