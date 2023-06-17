import pygame
import random
class Enemy:
    def __init__(self,image):
        self.x = random.randint(0, 1000)
        self.y =random.randint(0, 1000)
        self.image = image
        self.width = 250
        self.height = 250
        self.hp =50
        self. damage = 10
def loadimage(path):
    image = pygame. image.load(path)
    image = pygame.transform.scale(image, (250, 250))
    return image

def iscolliding(thing):
    if thing.y > (y + height):
        return False
    elif (thing.y + thing.height) < y:
        return False
    if thing.x > (x + width):
        return False
    elif (thing.x + thing.width) < x:
        return False
    return True
pygame.init()
window = pygame.display.set_mode((1000,1000))
pygame.display.set_caption('FRANKS GAME!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
clock = pygame.time.Clock()
standinganimation = pygame.image.load("first game/left ONE.png")
standinganimation = pygame.transform.scale(standinganimation, (250, 250))
walkingleft = [loadimage("first game/left ONE.png"), loadimage("first game/left TWO.png"),loadimage("first game/left THREE.png"), loadimage("first game/Left FOUR .png")]
walkingright =[loadimage("first game/right ONE.png"), loadimage("first game/right TWO.png"),loadimage("first game/right THREE.png"),loadimage("first game/right FOUR.png")]
attackleft =[loadimage("first game/left killing 1.png"), loadimage("first game/left killing 2.png")]
attackright =[loadimage("first game/right killing 1.png"), loadimage("first game/right killing 2.png")]
deathleft =[loadimage("first game/left death 1.png"), loadimage("first game/left death 2.png"),loadimage("first game/left death 3.png"), loadimage("first game/left death 4.png"), loadimage("first game/left death 5.png")]
deathright =[loadimage("first game/right death 1.png"), loadimage ("first game/right death 2.png"), loadimage("first game/right death 3.png"), loadimage("first game/right death 5.png")]
chrisdeathleft =[loadimage("first game/cdl 1.png"), loadimage("first game/cdl 2.png"), loadimage("first game/cdl 3.png"), loadimage("first game/cdl 4.png"), loadimage("first game/cdl 5.png"), loadimage("first game/cdl 6.png"), loadimage ("first game/cdl 7.png")]
chrisdeathright =[loadimage("first game/cdr 1.png")]
chrisstanding = loadimage("first game/chris 1.png")
standingleft = loadimage("first game/left ONE.png")
standingright = loadimage("first game/right ONE.png") 
# x is left and right
x = 0
# y is left and right 
y = 0 
width = 250
height = 250
speed = 5                           
hp = 1000
damage = 25
direction = "left"
framenumber = 0
enemies =[]
attacking = False 
run = True
death = False
while run:
    clock.tick(60)
    if death:
        window.fill((56, 73, 24))
        window.blit(deathright[framenumber//15], (x, y))
        pygame.display.update()
        if framenumber == 59:
            pygame.time.delay(100)
            break
        else:
            framenumber += 1
            continue
    
    framenumber += 1
    if framenumber == 1:
        enemy = Enemy(chrisstanding)
        enemies. append(enemy)
    if framenumber == 23:
        framenumber = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
    keys = pygame.key.get_pressed()
    attacking = False
    if direction == "right":
        direction = "stand right"
    elif direction == "left":
        direction = "stand left"
    if keys [pygame.K_UP]:
        y -= speed
        if direction == "stand right":
            direction = "right"
        elif direction == "stand left":
            direction = "left"
        
    if keys [pygame.K_DOWN]:
        y += speed
        if direction == "stand right":
            direction = "right"
        elif direction == "stand left":
            direction = "left"
    if keys[pygame.K_RIGHT]:
        x += speed 
        direction = "right"

    if keys [pygame.K_LEFT]:
        x -= speed
        direction = "left"
    if keys [pygame.K_SPACE]:
        attacking = True
   
    window.fill((56, 73, 24))
    #pygame.draw.rect(window, (0, 255, 0), (x, y, width, hieght))
    if attacking == True:
        if direction == "left" or direction == "stand left":
            window.blit(attackleft[framenumber // 12], (x, y))
        if direction == "right" or direction == "stand right":
            window.blit(attackright[framenumber// 12], (x, y))
    elif direction == "left":
        window.blit(walkingleft[framenumber // 6], (x, y))
    elif direction == "right":
        window.blit(walkingright[framenumber // 6], (x, y))
    elif direction == "stand left":
        window.blit(standingleft,(x, y))
    elif direction == "stand right":
        window.blit(standingright,(x, y))

    for enemy in enemies:
        window.blit (enemy.image, (enemy.x, enemy.y))
        if iscolliding(enemy):
            if attacking:
                enemy.hp -= damage
                if enemy.hp < 1:
                    enemies.remove(enemy)
            else:
                hp -= enemy.damage
                if hp < 1:
                    death = True
                    framenumber = 0
                    

    pygame.display.update()

pygame.quit()