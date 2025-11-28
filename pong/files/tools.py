import pygame
from files import constants

def config_game (width, height, title, bg_color):
    pygame.init()
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption(title)
    return screen

def star_menu():
    pass

def clock_game():
    clock = pygame.time.Clock()
    return clock

def move_plat(state, plat_x, plat_y):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["running"] = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and plat_x - constants.SPEED >= 0:
        plat_x -= constants.SPEED
    if keys[pygame.K_RIGHT] and plat_x + constants.PLATFORM_WIDTH + constants.SPEED  <= constants.WINDOW_WIDTH:
        plat_x += constants.SPEED
    return plat_x, plat_y

def move_ball(ball_x, ball_y):
    # Actualizar posición de la pelota
    #print (ball_x, ball_y)
    ball_x += constants.BALL_SPEED_X 
    ball_y += constants.BALL_SPEED_Y
    return ball_x, ball_y

def collision_ball(ball_x, ball_y, plat_x, plat_y, state):
    # Comprobar rebote en el borde inferior
    if ball_y - constants.BALL_RADIUS <= 0:
        constants.BALL_SPEED_Y = -constants.BALL_SPEED_Y
    if ball_y + constants.BALL_RADIUS > constants.WINDOW_HEIGHT:
        state["running"] = False
    if ball_x - constants.BALL_RADIUS <= 0 or ball_x + constants.BALL_RADIUS >= constants.WINDOW_WIDTH:
        constants.BALL_SPEED_X = -constants.BALL_SPEED_X
    # Colision con la plataforma
    if (plat_y <= ball_y + constants.BALL_RADIUS <= plat_y + constants.PLATFORM_HEIGHT) and \
        (plat_x<= ball_x <= plat_x + constants.PLATFORM_WIDTH):
        constants.BALL_SPEED_Y = -constants.BALL_SPEED_Y
    # Devuelves las variables actualizadas
    