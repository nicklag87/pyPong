import pygame, sys, random, time


# initialize pygame
pygame.init()

test = 1


# set up screen, paddles, and ball variables
playerBlack = (0, 0, 0)
enemBlack = (0, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
pause = False

screen = pygame.display.set_mode((400, 250))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

paddle = pygame.Rect(10, 100, 10, 40)
enemyPaddle = pygame.Rect(380, 100, 10, 40)
ball = pygame.Rect(200, 125, 10, 10)

speed = 2



enemyPaddleSpeed = 2

ballDirX = random.randint(-1, 4)
ballDirY = random.randint(-1, 4)

# check for ball's existence
ballExist = False

# text
pygame.font.init()
score = 0

def createScore():
    scoreText = str(score)

    myfont = pygame.font.SysFont(None, 40)
    mytext = myfont.render(scoreText, 1, (255, 100, 100))
    playerScoreTextPos = (100, 10)
    # blit score
    screen.blit(mytext, playerScoreTextPos)


enemyScore = 0

def createEnemScore():
    eScoreText = str(enemyScore)

    myfont = pygame.font.SysFont(None, 40)
    mytext = myfont.render(eScoreText, 1, (255, 100, 100))
    playerScoreTextPos = (300, 10)
    # blit score
    screen.blit(mytext, playerScoreTextPos)


# functions
def drawBall(ball):
    pygame.draw.rect(screen, playerBlack, ball)

def moveBall(ball, ballDirX, ballDirY):
    if ballDirX == 0:
        ballDirX = 1
        ball.y += ballDirX
    if ballDirY == 0:
        ballDirY = 1
        ball.y += ballDirY
    ball.x += ballDirX
    ball.y += ballDirY

    return ball


def enemPaddleAI(paddle2, ball, ballDirx):
    if ballDirX > 0:
        if ball.y < paddle2.y:
            paddle2.y -= enemyPaddleSpeed
        elif ball.y > paddle2.y:
            paddle2.y += enemyPaddleSpeed


    return paddle2





def key(key):
    return pygame.key.get_pressed()[eval("pygame.K_"+ key)]

def addOne(ballDirX):
    if ballDirX < 0:
        ballDirX -= 1
    if ballDirX > 0:
        ballDirX += 1
    return ballDirX


while True:
    if pygame.event.get(pygame.QUIT) or key("ESCAPE"):
        pygame.quit()
        sys.exit()

    if key("UP"):
        if paddle.top <= 0:
            print(paddle.top)
        else:
            paddle.y -= speed
    if key("DOWN"):
        if paddle.top >= 250 - paddle.height:
            print(paddle.top)
        else:
            paddle.y += speed






    screen.fill(white)


    # blit scores
    createScore()
    createEnemScore()


    pygame.draw.rect(screen, playerBlack, paddle)
    pygame.draw.rect(screen, enemBlack, enemyPaddle)

    if ball.left >= 400 - ball.height:
        print("player 2 missed")
        ballExist = False
        score = score + 1
        ball = pygame.Rect(200, 125, 10, 10)
        ballDirX = random.randint(-1, 2)
        ballDirY = random.randint(-1, 2)
        if ballDirX == 0:
            ballDirX = 1
            ball.y += ballDirX
        if ballDirY == 0:
            ballDirY = 1
            ball.y += ballDirY
    elif ball.right <= 0:
        print("player 1 missed")
        enemyScore = enemyScore + 1
        ball = pygame.Rect(200, 125, 10, 10)
        ballDirX = random.randint(-1, 2)
        ballDirY = random.randint(-1, 2)
        if ballDirX == 0:
            ballDirX = 1
            ball.y += ballDirX
        if ballDirY == 0:
            ballDirY = 1
            ball.y += ballDirY
    else:
        drawBall(ball)
        moveBall(ball, ballDirX, ballDirY)
        ballExist = True



    enemPaddleAI(enemyPaddle, ball, ballDirX)




    pygame.display.flip()


    # paddle collision
    collision = paddle.colliderect(ball)
    if collision == True:
        ballDirX = addOne(ballDirX)
        print(ballDirX)
        print collision
        playerBlack = (255, 0, 0)
        ballDirX = -ballDirX
    elif collision == False:
        playerBlack = (0, 0, 0)

    # enemy paddle collision
    enemCollision = enemyPaddle.colliderect(ball)
    if enemCollision == True:
        ballDirX = addOne(ballDirX)
        print(ballDirX)
        enemBlack = (255, 0, 0)
        ballDirX = -ballDirX
    elif enemCollision == False:
        enemBlack = (0, 0, 0)




    # wall collision
    if ball.bottom >= 250:
        ballDirY = -ballDirY
    if ball.top <= 0:
        ballDirY = -ballDirY



