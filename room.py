from bangtal import *


# door_object : 문 객체
# door_name : 문 이름
# callback : 열린 문을 클릭했을 때 행동
def make_door_onMouseAction(door_object, door_name, callback):
    def onMouseAction(x, y, action):
        if door_object.closed == True:
            door_object.setImage(f"Images/문-{door_name}-열림.png")
            door_object.closed = False
        else:
            callback()

    return onMouseAction


scene1 = Scene("방1", "Images/배경-1.png")
scene2 = Scene("방2", "Images/배경-2.png")
scene3 = Scene("방3", "Images/하늘.jpg")

door1 = Object("Images/문-왼쪽-닫힘.png")
door1.locate(scene1, 150, 270)
door1.show()
door1.closed = True
door1.onMouseAction = make_door_onMouseAction(door1, "왼쪽", scene2.enter)

door2 = Object("Images/문-오른쪽-닫힘.png")
door2.locate(scene1, 800, 270)
door2.show()
door2.closed = True
door2.onMouseAction = make_door_onMouseAction(door2, "오른쪽", scene3.enter)

door3 = Object("Images/문-오른쪽-닫힘.png")
door3.locate(scene2, 900, 270)
door3.show()
door3.closed = True
door3.onMouseAction = make_door_onMouseAction(door3, "오른쪽", scene1.enter)

door4 = Object("Images/문-왼쪽-닫힘.png")
door4.locate(scene3, 150, 270)
door4.show()
door4.closed = True
door4.onMouseAction = make_door_onMouseAction(door4, "왼쪽", scene1.enter)

door5 = Object("Images/문-오른쪽-닫힘.png")
door5.locate(scene3, 800, 270)
door5.show()
door5.closed = True
door5.onMouseAction = make_door_onMouseAction(door5, "오른쪽", endGame)

startGame(scene1)

