from cmu_graphics import*
import math
import random

#seperate into class file
class block:
    def __init__(self, color, centerX, centerY, sideLength, angle):
        self.color = color
        self.centerX = centerX
        self.centerY = centerY
        self.sideLength = sideLength
        self.angle = angle

playerBlock =  block('purple', 150, 225, 50, 0)

#seperate into class file
class obstacle:
    def __init__(self, shape, width, centerY, topY):
        self.shape = shape
        self.width = width
        self.centerY = centerY
        self.topY = topY


floor = obstacle('rectangle', 150, 225, 200)
spike = obstacle('triangle', 30, 237.5, 224.5)
#doubleSpike = obstacle 


def onAppStart(app):
    app.width = 800
    app.height = 400
    app.titleScreen = True
    app.difficultySetting = False
    app.stepsPerSecond = 30
    app.obstacleX = 800
    app.obstacleY = 200
    app.jumping = False
    app.falling = False
    app.blockAngle = 0
    app.obstacles = ['floor','spike']#doubleSpike,tripleSpike}
    app.backgroundX = 0
    app.trail = True
    app.mapSpeed = 0
    app.jumpMax = 125
    app.countdown = 3
    app.relativeCount = 0
    app.playScreen = False
    app.mainFloorY = 250
    app.floorObstacle = False
    app.currentObstacle = app.obstacles[random.randrange(0,2)]
    app.floorY = 250



def redrawAll(app):
    #title screen 
    if app.titleScreen == True:
        drawTitleScreen(app)
    #speed/difficulty screen
    elif app.difficultySetting == True and app.titleScreen == False:
        drawDifficultyScreen(app)
    #play screen 
    elif app.titleScreen == False and app.difficultySetting == False:
        drawPlayScreen(app)



def drawDifficultyScreen(app):
    #background color
    drawRect(0,0,800,400,fill = 'lightblue', opacity = 80)
    #different speeds
    drawRect(150, 200, 200, 100, align = 'center', fill = 'cyan', border = 'black')
    drawRect(400, 200, 200, 100, align = 'center', fill = 'cyan', border = 'black')
    drawRect(650, 200, 200, 100, align = 'center', fill = 'cyan', border = 'black')
    drawLabel('Slow', 150, 200, fill = 'lightgreen', border = 'black', font = 'orbitron', size = 45)
    drawLabel('Moderate', 400, 200, fill = 'lightgreen', border = 'black', font = 'orbitron', size = 45)
    drawLabel('Fast', 650, 200, fill = 'lightgreen', border = 'black', font = 'orbitron', size = 45)

def drawTitleScreen(app):
    #background color
    for i in range(-800, app.width, 50):
        drawRect(app.backgroundX + i, 0, 800, app.height, fill='lightblue', opacity=80)
        drawRect(app.backgroundX + i, 0, 50, 50, fill='blue', opacity=10, border='white')
        drawRect(app.backgroundX + i, 50, 50, 50, fill='blue', opacity=10, border='white')
        drawRect(app.backgroundX + i, 100, 50, 50, fill='blue', opacity=10, border='white')
        drawRect(app.backgroundX + i, 150, 50, 50, fill='blue', opacity=10, border='white')
        drawRect(app.backgroundX + i, 200, 50, 50, fill='blue', opacity=10, border='white')
        drawRect(app.backgroundX + i, 250, 50, 50, fill='blue', opacity=10, border='white')
        drawRect(app.backgroundX + i, 300, 50, 50, fill='blue', opacity=10, border='white')
        drawRect(app.backgroundX + i, 350, 50, 50, fill='blue', opacity=10, border='white')
    #drawing for the title screen
    drawLabel('Geometry Dash Mini', 400, 50, size=50, font='orbitron', bold=True, fill='lightgreen', border= 'black', borderWidth=2,opacity=100)
    #play button
    drawRect(400, 200, 100, 100, fill='cyan', align = 'center', border = 'black')
    drawRegularPolygon(395,200, 50, 3, fill = 'yellow', border = 'black', rotateAngle = 90, align = 'center')
    #speed/difficulty setting
    drawRect(400, 325, 200, 100, fill = 'cyan', align = 'center', border = 'black')
    drawLabel('Select Difficulty', 400, 325, fill = 'lightgreen', font = 'orbitron', size = 27.5, border = 'black')


def drawPlayScreen(app):
    #background color and background sqaures
    for i in range(-800, app.width, 50):
        drawRect(app.backgroundX + i, 0, 800, app.height, fill='lightblue', opacity=80)
        drawRect(app.backgroundX + i, 0, 50, 50, fill='blue', opacity=10, border='white')
        drawRect(app.backgroundX + i, 50, 50, 50, fill='blue', opacity=10, border='white')
        drawRect(app.backgroundX + i, 100, 50, 50, fill='blue', opacity=10, border='white')
        drawRect(app.backgroundX + i, 150, 50, 50, fill='blue', opacity=10, border='white')
        drawRect(app.backgroundX + i, 200, 50, 50, fill='blue', opacity=10, border='white')
    #floor
    drawRect(0,250,800, 250, fill = 'blue', border = 'black', opacity = 50, borderWidth = 5)
    #Countdown
    #obstacle load
    if app.countdown != 0:
        drawLabel(f'{app.countdown}', 400, 200, size=50, font='orbitron', bold=True, fill='lightgreen', border= 'black', borderWidth=2,opacity=100)
    else:
        if app.currentObstacle == 'floor':
            drawRect(app.obstacleX,app.obstacleY,150, 50, fill = 'blue', border = 'black', opacity = 50, borderWidth = 5)
        elif app.currentObstacle == 'spike':
            drawRegularPolygon(app.obstacleX, 237.5, 30, 3, fill='red', border = 'black', borderWidth = 2) 
    #player block
    drawRect(playerBlock.centerX, playerBlock.centerY, playerBlock.sideLength, playerBlock.sideLength, fill = 'purple', border = 'white', align = 'center', rotateAngle = playerBlock.angle)
    drawRect(playerBlock.centerX, playerBlock.centerY, playerBlock.sideLength-10, playerBlock.sideLength-10, fill = 'blue', border = 'white', align = 'center', rotateAngle = playerBlock.angle)
    drawRect(playerBlock.centerX, playerBlock.centerY, playerBlock.sideLength-20, playerBlock.sideLength-20, fill = 'purple', border = 'white', align = 'center', rotateAngle = playerBlock.angle)
    drawRect(playerBlock.centerX, playerBlock.centerY, playerBlock.sideLength-30, playerBlock.sideLength-30, fill = 'black', border = 'white', align = 'center', rotateAngle = playerBlock.angle)
    #player block trail
    if app.trail == True:
        for i in range(playerBlock.centerX - 75, playerBlock.centerX-25, 5):
            drawCircle(i, playerBlock.centerY + 25 - random.randrange(0,15), 2, fill = 'purple')
            drawCircle(i-5, playerBlock.centerY + 25 - random.randrange(0,15), 2, fill = 'white')
            drawCircle(i-10, playerBlock.centerY + 25 - random.randrange(0,15), 2, fill = 'blue')



def onKeyPress(app, key):
    #jump mechanics
    if key == 'space' and playerBlock.centerY == 225:
        app.jumping = True




def onStep(app):
    #Count screen 
    if app.difficultySetting == False and app.titleScreen == False and app.playScreen == False:
        app.relativeCount += 30
    if app.relativeCount == 900:
        app.countdown = 2
    elif app.relativeCount == 1800:
        app.countdown = 1
    elif app.relativeCount == 2700:
        app.countdown = 0
    #making sure that the map speed is different from the block jump speed so it runs smoother
    if app.countdown == 0:
        app.obstacleX -= (10 + app.mapSpeed)
        if app.obstacleX + 150 <= 0:
            app.obstacleX = 800 #move obstacle back to the beginning
            app.currentObstacle = app.obstacles[random.randrange(0,2)]
    app.backgroundX -= 2 
    if app.backgroundX <= 0:
        app.backgroundX = 800
    #changing app.floorY for the block to land on the floor obstacle
    if app.currentObstacle == 'floor' and (playerBlock.centerX >= app.obstacleX and playerBlock.centerX <= app.obstacleX + floor.width):
        app.floorY = floor.topY
    else:
        app.floorY = app.mainFloorY
        app.falling = True
    #jumping and falling animation
    addAngle = (90/((100)/10))/2
    if app.jumping == True and playerBlock.centerY >= app.jumpMax:
        app.falling = False
        playerBlock.centerY -= 10
        playerBlock.angle += addAngle
        app.trail = False
        if playerBlock.centerY == app.jumpMax:
            app.jumping = False
            app.falling = True
    if app.falling == True and playerBlock.centerY+25 <= app.floorY:
        if playerBlock.centerY+25 < app.floorY:
            playerBlock.centerY += 10
            playerBlock.angle += addAngle
        if playerBlock.centerY + 25 == app.floorY:
            playerBlock.angle = 0
            app.falling = False
            app.trail = True




def onMousePress(app, mouseX, mouseY):
    #title screen options
    if app.titleScreen == True and (mouseX >= 350 and mouseX <= 450) and (mouseY >= 150 and mouseY <= 250):
        app.titleScreen = False
    elif app.titleScreen == True and (mouseX >=200 and mouseX <= 600) and (mouseY >= 225 and mouseY <= 425):
        app.titleScreen = False
        app.difficultySetting = True
    #difficulty options
    if app.difficultySetting == True and (mouseX >= 50 and mouseX <= 250) and (mouseY >= 150 and mouseY <= 250):
        app.mapSpeed = -5
        app.difficultySetting = False
        app.titleScreen = True
    elif app.difficultySetting == True and (mouseX >= 300 and mouseX <= 500) and (mouseY >= 150 and mouseY <= 250):
        app.difficultySetting = False
        app.titleScreen = True
        app.mapSpeed = 5
    elif app.difficultySetting == True and (mouseX >= 550 and mouseX <= 750) and (mouseY >= 150 and mouseY <= 250):
        app.difficultySetting = False
        app.titleScreen = True
        app.mapSpeed = 10
    



def distance(x1, y1, x2, y2):
    distance = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2) )
    return distance


#def isValid(app, playerBlock, obstacle):
    #if distance(playerBlock.centerX, playerBlock.centerY, )

def main():
    runApp()

main()