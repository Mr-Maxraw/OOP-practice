class Duck:
    def swim_quak(self):
        print("i am a duck. can swim can quack")

class RoboDuck:
    def swim_quak(self):
        print("i am a robo duck. can swim can quack")

class Log:
    def swim(self):
        print("i am log. can swim")

def duck_testing(a):
    a.swim_quak()

duck_testing(Duck())
duck_testing(RoboDuck())
duck_testing(Log())
