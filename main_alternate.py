import pygame

WIDTH,HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

WHITE =(255,255,255)
FPS = 60
SHIP_WIDTH,SHIP_HEIGHT = 55,45
VEL =5

YELLOW_SPACESHIP_IMAGE = pygame.image.load('Assets/spaceship_yellow.png')
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SHIP_WIDTH,SHIP_HEIGHT)),90)


RED_SPACESHIP_IMAGE = pygame.image.load('Assets/spaceship_red.png')
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SHIP_WIDTH,SHIP_HEIGHT)),270)

def draw_window(yellow,red):
    WIN.fill(WHITE)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x,yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x,red.y))
    pygame.display.update()

def main():
    """main loop"""
    run = True
    clock = pygame.time.Clock()

    yellow = pygame.Rect(200,100, SHIP_WIDTH,SHIP_HEIGHT)
    red = pygame.Rect(700,100, SHIP_WIDTH,SHIP_HEIGHT)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
        
        key_pressed = pygame.key.get_pressed()

        if key_pressed[pygame.K_a]:
            yellow.x-=VEL
        if key_pressed[pygame.K_d]:
            yellow.x+=VEL
        if key_pressed[pygame.K_w]:
            yellow.y-=VEL
        if key_pressed[pygame.K_s]:
            yellow.y+=VEL
        if key_pressed[pygame.K_LEFT]:
            red.x-=VEL
        if key_pressed[pygame.K_RIGHT]:
            red.x+=VEL
        if key_pressed[pygame.K_UP]:
            red.y-=VEL
        if key_pressed[pygame.K_DOWN]:
            red.y+=VEL
        draw_window(yellow,red)
    pygame.quit()

main()