from enum import Enum
class vp(Enum):
    YELL=1
    gree=2
    treea=3
    halou=1
class Common():
    YELL=2
    print(YELL)
print(vp.YELL.name)
print(vp.YELL.value)
print(vp.YELL)

print("hahaahha")
print(vp.halou)
for v in vp:
    print(v.value)

