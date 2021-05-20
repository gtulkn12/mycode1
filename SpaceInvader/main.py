import pygame
import random
import math

#initialize the pygame / always in game
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('.\\Udemy\\SpaceInvader\\bg.jpg')

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('.\\Udemy\\SpaceInvader\\ufo.png')
pygame.display.set_icon(icon)

### PLAYER
playerImg = pygame.image.load('.\\Udemy\\SpaceInvader\\battleship.png')
playerX = 370
playerY = 510
playerX_change = 0

### ENEMY
enemyImg= []
enemyX= []
enemyY = []
enemyX_change = []
enemyy_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
        enemyImg.append(pygame.image.load('.\\Udemy\\SpaceInvader\\enemy.png'))
        enemyX.append(random.randint(0, 736)) # places the enemy at random location on the x axis
        enemyY.append(random.randint(50, 150)) # places enemy at random location on the y axis
        enemyX_change.append(0.3)
        enemyy_change.append(40)

        # enemyImg = pygame.image.load('.\\Udemy\\SpaceInvader\\enemy.png')
        # enemyX = random.randint(0, 736) # places the enemy at random location on the x axis
        # enemyY = random.randint(50, 150) # places enemy at random location on the y axis
        # enemyX_change = 0.3
        # enemyy_change = 40

### BULLET
bulletImg = pygame.image.load('.\\Udemy\\SpaceInvader\\bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bullety_change = .7
bullet_state = 'ready'

### SCORE
score_value = 0
font= pygame.font.Font('freesansbold.ttf', 32)

textX= 10
textY= 10

def show_score(x,y):
        score = font.render("Score :" + str(score_value), True, (255, 255, 255) )
        screen.blit(score, (x, y))

def player(x, y):
        #Draws player on screen
        screen.blit(playerImg, (x, y))

def enemy(x, y, i):
        #Draws enemy on screen
        screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
        global bullet_state
        bullet_state = "fire"
        screen.blit(bulletImg, (x + 16 , y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
        # Distance between two points and the midpoint ---> D=^((x2−x1)2+(y2−y1)2)
        distance = math.sqrt(math.pow(enemyX-bulletX, 2) + math.pow(enemyY-bulletY, 2))
        if distance < 27:
                return True
        else:
                return False

### Game Loop
running = True
while running:
        # RGB - Red, Green, Blue - 0-55
        screen.fill((0, 0, 0))
        # background image
        screen.blit(background, (0, 0))
        #moves player right with every pass of the while loop
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False

        # if keystroke is passed check wheeter its right or left
                if event.type == pygame.KEYDOWN:
                        print("A keystroke is pressed")
                        if event.key == pygame.K_LEFT:
                                print("Left arrow is pressed.")
                                #controls distance moved/speed of object to the Left
                                playerX_change = -0.3
                        if event.key == pygame.K_RIGHT:
                                print("Right arrow is pressed")
                                #controls distance moved/speed of object to the Right
                                playerX_change = 0.3
                        if event.key == pygame.K_SPACE:
                                print("Space bar is pressed")
                                if bullet_state is "ready":
                                        bulletX = playerX
                                #controls distance moved/speed of object to the Right
                                        fire_bullet(bulletX,bulletY)

                if event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                                print("Keystroke has been released")
                                #stops the object after each key release
                                playerX_change = 0
        
        playerX += playerX_change
        #Create Boundary and Border / Prevents object from going beyond the L / R limits of the screen
        if playerX <= 0:
                playerX = 0
        elif playerX > 736:
                playerX = 736

### Enemy Movement
        for i in range(num_of_enemies):
                enemyX[i] += enemyX_change[i]
                if enemyX[i] <= 0:
                        enemyX_change[i] = 0.3
                        enemyY[i] += enemyy_change[i]
                elif enemyX[i] > 736:
                        enemyX_change[i] = -0.3
                        enemyY[i] += enemyy_change[i]

### Collision
                collision = isCollision (enemyX[i], enemyY[i], bulletX, bulletY)
                if collision:
                        bulletY = 480
                        bullet_state = "ready"
                        score_value += 1
                        print(score_value)
                        enemyX[i] = random.randint(0, 736)
                        enemyY[i] = random.randint(50, 150)
                enemy(enemyX[i], enemyY[i], i)

### Bullet Movement
        if bulletY < 0:
                bulletY = 480
                bullet_state = "ready"
        if bullet_state is "fire":
                fire_bullet(bulletX, bulletY )
                bulletY -= bullety_change
                
        #call method to draw player on the screen
        player(playerX, playerY)

        show_score(textX, textY)
        #Updates screen / always included in game
        pygame.display.update()        