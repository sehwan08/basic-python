# class Unit: #클래스 선언
#     def __init__(self, name, hp, damage): #생성자
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} Unit is ready.".format(self.name))
#         print("HP:{0}, Attack:{1}".format(self.hp, self.damage))

# # marine1 = Unit("Marine", 40, 5)
# # marine2 = Unit("Marine", 40, 5)
# # tank = Unit("Tank", 150, 35)

# # unit1 = Unit("Zealot", 70, 20)
# # print("Name:{0}, Damage:{1}".format(unit1.name, unit1.damage))

# # unit1.upgrade = True
# # if unit1.upgrade == True:
# #     print("{0} has been upgraded".format(unit1.name))

# class AttackUnit:
#     def __init__(self, name, hp, damage): #생성자
#         self.name = name
#         self.hp = hp
#         self.damage = damage

#     def attack(self, location):
#         print("{0} is attacking to {1} location. [Damege {2}]".format(self.name, location, self.damage))


#     def damaged(self, damaged):
#         print("{0} is under attack [{1} damaged]".format(self.name, damaged))
#         self.hp -= damaged
#         print("{0} : HP:{1}".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} is dead".format(self.name))

# #공격
# firebat1 = AttackUnit("Firebat", 50, 16)
# firebat1.attack("South")

# #공격 받음
# firebat1.damaged(25)
# firebat1.damaged(25)


class Unit: #클래스 선언
    def __init__(self, name, hp, speed): #생성자
        self.name = name
        self.hp = hp
        self.speed = speed
    
    def move(self, location):
        print("Unit is movig")
        print("{0} : is heading to {1} [속도 {2}]".format(self.name, location, self.speed))

class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage): #생성자
        Unit.__init__(self, name, hp, speed) #상속받는 클래스에서 파라미터를 받음
        self.damage = damage

    def attack(self, location):
        print("{0} is attacking to {1} location. [Damege {2}]".format(self.name, location, self.damage))

    def damaged(self, damaged):
        print("{0} is under attack [{1} damaged]".format(self.name, damaged))
        self.hp -= damaged
        print("{0} : HP:{1}".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} is dead".format(self.name))

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


class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        super().__init__(name,hp,0)
        self.location = location

supply_depot = BuildingUnit("SupplyDepot", 500, "South")