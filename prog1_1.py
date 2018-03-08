#Mouse game
class Pointer(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def moveUp(self):
        self.y += 1

    def moveDown(self):
        self.y -= 1

    def moveLeft(self):
        self.x -= 1

    def moveRight(self):
        self.x +=  1

    def checkPosition(self):
        x = self.x
        y = self.y
        return x, y

c = Pointer(10, 20)
c.moveUp()
print(c.checkPosition())

#I have changed to check in the git repository
