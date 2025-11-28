#################
# Juego de Pong #
#################

# Importamos librerias #
import pygame
from files import tools
from files import constants

# Inicializamos el juego #
pygame.init()


screen = tools.config_game(constants.WINDOW_WIDTH,constants.WINDOW_HEIGHT,constants.TITLE,constants.WHITE)
clock = tools.clock_game()

# Posición de la paleta
plat_x = constants.WINDOW_WIDTH // 2 - constants.PLATFORM_WIDTH // 2
plat_y = constants.WINDOW_HEIGHT - 20

# Posicion de la pelota #
ball_x = constants.WINDOW_WIDTH // 2 - constants.BALL_RADIUS // 2
ball_y = 10 + constants.BALL_RADIUS // 2

# Diccionario para arrancar la variable running #
state = {"running": True}

# Bucle principal #
while state["running"]:
    # Llamada a movimiento de plataforma y pelota #
    tools.star_menu()
    plat_x, plat_y = tools.move_plat(state, plat_x, plat_y)
    ball_x, ball_y = tools.move_ball(ball_x, ball_y)

    # Colisión con paredes #
    tools.collision_ball(ball_x,ball_y, plat_x, plat_y, state)

    # Dibujo paleta y bola #
    screen.fill(constants.BLACK)
    pygame.draw.rect(screen,constants.BLUE,(plat_x,plat_y,constants.PLATFORM_WIDTH,constants.PLATFORM_HEIGHT),0,3)
    pygame.draw.circle(screen, constants.GREEN, (int(ball_x), int(ball_y)),constants.BALL_RADIUS)

    # Actualización de la  pantalla #
    pygame.display.flip()
    clock.tick(constants.FPS)
pygame.quit()