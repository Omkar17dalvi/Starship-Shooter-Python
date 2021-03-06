import pygame
import os
pygame.font.init()
pygame.mixer.init()

WIDTH,HEIGHT = 900,500

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Starship Shooter")

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

FPS = 60
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 45
VEL = 5
BULLET_VEL = 7
BORDER = pygame.Rect(WIDTH/2-5,0,10,HEIGHT)

BULLET_NUM = 3

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans',100)

BULLET_FIRE = pygame.mixer.Sound('Assets/Silencer.mp3')

BULLET_HIT = pygame.mixer.Sound('Assets/Grenade.mp3')


YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')),(WIDTH,HEIGHT))

YELLOW_HIT = pygame.USEREVENT + 1 
RED_HIT = pygame.USEREVENT + 2




def draw_window(yellow, red, yellow_bullets, red_bullets, yellow_health, red_health):
    WIN.blit(SPACE,(0,0))
    pygame.draw.rect(WIN,BLACK, BORDER)

    yellow_health_text = HEALTH_FONT.render("Health :"+str(yellow_health), 1 , WHITE)
    red_health_text = HEALTH_FONT.render("Health :"+str(red_health), 1 , WHITE)
    WIN.blit(yellow_health_text, (10,10))
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10,10))
    WIN.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y))
    WIN.blit(RED_SPACESHIP,(red.x,red.y))

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN,YELLOW,bullet)
    for bullet in red_bullets:
        pygame.draw.rect(WIN,RED,bullet)
    pygame.display.update()


def yellow_handle_movement(key_pressed,yellow):
    if key_pressed[pygame.K_a] and yellow.x - VEL > 0:
            yellow.x-=VEL
    if key_pressed[pygame.K_d] and yellow.x + VEL + SPACESHIP_HEIGHT < WIDTH/2 -5:
            yellow.x+=VEL
    if key_pressed[pygame.K_w] and yellow.y - VEL > 0:
            yellow.y-=VEL
    if key_pressed[pygame.K_s] and yellow.y + VEL + SPACESHIP_WIDTH < HEIGHT:
            yellow.y+=VEL  

def red_handle_movement(key_pressed,red):
    if key_pressed[pygame.K_LEFT] and red.x - VEL > WIDTH/2 +5:
            red.x-=VEL
    if key_pressed[pygame.K_RIGHT] and red.x + VEL + SPACESHIP_HEIGHT< WIDTH:
            red.x+=VEL
    if key_pressed[pygame.K_UP] and red.y - VEL > 0:
            red.y-=VEL
    if key_pressed[pygame.K_DOWN] and red.y + VEL + SPACESHIP_WIDTH < HEIGHT:
            red.y+=VEL  

def handle_bullets(yellow_bullets, red_bullets, yellow, red):

    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)

def win_condition(winner_text):
    final_text = WINNER_FONT.render(winner_text,1,WHITE)
    WIN.blit(final_text,(WIDTH//2-final_text.get_width()//2,HEIGHT//2-final_text.get_height()//2 ))
    pygame.display.update()
    pygame.time.delay(3000)

def main():
    """main function with main game loop"""
    clock = pygame.time.Clock()
    run = True
    yellow = pygame.Rect(200,250,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    red = pygame.Rect(600,250,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)

    yellow_health = 10
    red_health = 10
    winner_text = ""
    yellow_bullets = []
    red_bullets=[]
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < BULLET_NUM:
                    bullet = pygame.Rect(yellow.x + yellow.height, yellow.y + yellow.width//2 -2, 10,5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE.play()
                if event.key == pygame.K_RCTRL and len(red_bullets) < BULLET_NUM:
                    bullet = pygame.Rect(red.x, red.y + red.width//2 -2, 10,5)
                    red_bullets.append(bullet)
                    BULLET_FIRE.play()
            if event.type == RED_HIT:
                    red_health-=1
                    BULLET_HIT.play()
            if event.type == YELLOW_HIT:
                    yellow_health-=1
                    BULLET_HIT.play()

        if yellow_health <= 0:
            winner_text = "Red Wins !"
        if red_health <= 0:
            winner_text = "Yellow Wins"
        if winner_text!="":
            win_condition(winner_text) #win condition
            break

        key_pressed = pygame.key.get_pressed()

        yellow_handle_movement(key_pressed,yellow)
        red_handle_movement(key_pressed,red)
        
        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        draw_window(yellow, red, yellow_bullets, red_bullets, yellow_health, red_health)

    
    main()

if __name__ == "__main__":
    main()