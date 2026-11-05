#Write a program to overload the less than (&lt;) and equal to (==) operators.
# For example, create objects - ob1 and ob2 with values 3 and 4 to 
#compare values, respectively. 
# You can additionally create more objects to try different values.
class Numbers:
    def __init__(self, num):
        self.num = num
    def __lt__(self, other):
        print(self.num<other.num)
    def __eq__(self,other):
        print(self.num==other.num)
ob1 = Numbers(3)
ob2 = Numbers(4)
ob1 < ob2
ob1 == ob2