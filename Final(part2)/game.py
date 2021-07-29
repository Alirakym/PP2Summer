import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

# Initialzing
pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Font
font_small = pygame.font.SysFont("Verdana", 20)

# Other Variables for use in the program
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0

# Create a white screen
screen = pygame.display.set_mode((600, 600))
screen.fill(WHITE)
pygame.display.set_caption("Hungry Lion")

enemyDelay = 500
friendDelay = 1000
enemySpeed = 4
friendSpeed = 3

class Player:
    def __init__(self):
        super().__init__()
        self.x = 350
        self.y = 350
        self.width = 20
        self.height = 20
        self.surf = pygame.Surface((40, 40))

    def draw(self):
        pygame.draw.rect(screen, BLUE, [self.x, self.y, self.height, self.width])

    def update(self):
        global SCORE
        pressed_keys = pygame.key.get_pressed()
        if self.y > 0:
            if pressed_keys[K_UP]:
                self.y -= 7
        if self.y + self.height < SCREEN_HEIGHT:
            if pressed_keys[K_DOWN]:
                self.y += 7

        if self.x > 0:
            if pressed_keys[K_LEFT]:
                self.x -= 5
        if self.x + self.width < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.x += 5

        playerRect = pygame.Rect((self.x, self.y),(self.width, self.height))
        for enemy in enemyList:
            enemyRect = pygame.Rect((enemy.x, enemy.y),(enemy.width, enemy.height))
            if playerRect.colliderect(enemyRect):
                enemyList.remove(enemy)
                SCORE -= 1
                pygame.mixer.Sound('beep-02.wav').play()
                

        for friend in friendList:
            friendRect = pygame.Rect((friend.x, friend.y),(friend.width, friend.height))
            if playerRect.colliderect(friendRect):
                friendList.remove(friend)
                SCORE += 1
                pygame.mixer.Sound('coin.wav').play()
        print(SCORE)

class Friend:
    def __init__(self):
        super().__init__()
        self.x = random.randint(0, 600)
        self.y = 600
        self.width = 20
        self.height = 20
        self.surf = pygame.Surface((40, 40))
        self.rect = self.surf.get_rect(center=(random.randint(40, SCREEN_WIDTH - 40), 0))

    def draw(self):
        pygame.draw.rect(screen, GREEN, [self.x, self.y, self.height, self.width])

    def update(self):
        self.y -= friendSpeed


class Enemy:
    def __init__(self):
        super().__init__()
        self.x = random.randint(0, 600)
        self.y = 0
        self.width = 20
        self.height = 20
        self.surf = pygame.Surface((40, 40))
        self.rect = self.surf.get_rect(center=(random.randint(40, SCREEN_WIDTH - 40), 0))

    def draw(self):
        pygame.draw.rect(screen, RED, [self.x, self.y, self.height, self.width])

    def update(self):
        self.y += enemySpeed


enemyList = []
friendList = []


def checkFriend():
    for friend in friendList:
        if friend.y < 0:
            friendList.remove(friend)


def checkEnemy():
    for enemy in enemyList:
        if enemy.y > 600:
            enemyList.remove(enemy)




enemyTime = 0


def createEnemy(delay):
    global enemyTime
    enemyTime += delay
    if enemyTime > enemyDelay:
        enemyList.append(Enemy())
        enemyTime = 0


friendTime = 0


def createFriend(delay):
    global friendTime
    friendTime += delay
    if friendTime > friendDelay:
        friendList.append(Friend())
        friendTime = 0



player=Player()
delay = 0
while True:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            print('Quit')
            sys.exit()
        
    screen.fill(WHITE)
    

    for enemy in enemyList:
        enemy.update()
    for friend in friendList:
        friend.update()
    player.update()
    checkEnemy()
    checkFriend()
    createEnemy(delay)
    createFriend(delay)
    player.draw()
    for friend in friendList:
        friend.draw()

    for enemy in enemyList:
        enemy.draw()

    

    scores = font_small.render(str(SCORE), True, (255,215,0))
    screen.blit(scores, (580,10))

    

    pygame.display.update()
    delay = FramePerSec.tick(60)

