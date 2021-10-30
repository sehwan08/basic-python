from random import *

class Unit: #클래스 선언
    def __init__(self, name, hp, speed): #생성자
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} is ready".format(name))
    
    def move(self, location):
        print("Unit is movig")
        print("{0} : is heading to {1} [속도 {2}]".format(self.name, location, self.speed))

    def damaged(self, damaged):
        print("{0} is under attack [{1} damaged]".format(self.name, damaged))
        self.hp -= damaged
        print("{0} : HP:{1}".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} is dead".format(self.name))

class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage): #생성자
        Unit.__init__(self, name, hp, speed) #상속받는 클래스에서 파라미터를 받음
        self.damage = damage

    def attack(self, location):
        print("{0} is attacking to {1} location. [Damege {2}]".format(self.name, location, self.damage))

class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "Marine", 40, 1, 5)
    
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : Stimpack! (Used 10 HP)".format(self.name))
        else:
            print("{0} : Not enough HP".format(self.name))

class Tank(AttackUnit):

    seize_mode = False

    def __init__(self):
        AttackUnit.__init__(self,"Tank", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_mode == False:
            return
        
        if self.seize_mode == False:
            print("{0} : on Seize-Mode".format(self.name))
            self.damage *= 2
            self.seize_mode = True

        else:
            print("{0} : back to normal".format(self.name))
            self.damage /= 2
            self.seize_mode = False


class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} is flying to {1}. [Speed {2}]".format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("Moving")
        self.fly(self.name, location)


class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "Wraith", 80, 20, 5)
        self.clocked = False

    def clocking(self):
        if self.clocked == True:
            print("{0} : back to normal".format(self.name))
            self.clocked = False
        else:
            print("{0} : on Clocking".format(self.name))
            self.clocked = True


def game_start():
    print("Game is starting")

def game_over():
    print("Player : GG")
    print("[Player] left the game")

game_start()

m1 = Marine()
m2 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

#유닛 일괄 관리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

#전군 이동
for unit in attack_units:
    unit.move("South")

#시즈모드 개발
Tank.seize_mode = True
print("Seize-Mode upgraded")

#공격 모드
for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

#전군 공격
for unit in attack_units:
    unit.attack("South")

#전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 20))

#게임 종료
game_over()
