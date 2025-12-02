#################
# Juego de Pong #
#################

# Importamos librerias #
import pygame
from files import tools
from files import constants

# Inicializamos el juego #
pygame.init()

# Variables puntuacion y vidas #
font = pygame.font.SysFont(None, 30)



screen = tools.config_game(constants.WINDOW_WIDTH,constants.WINDOW_HEIGHT,constants.TITLE,constants.WHITE)
clock = tools.clock_game()

# Posición de la paleta
plat_x = constants.WINDOW_WIDTH // 2 - constants.PLATFORM_WIDTH // 2
plat_y = constants.WINDOW_HEIGHT - 20

# Posicion de la pelota #
ball_x = constants.WINDOW_WIDTH // 2 - constants.BALL_RADIUS // 2
ball_y = 10 + constants.BALL_RADIUS // 2

# Diccionario para arrancar la variable running #
state = {"running": True,"title": True}

# Bucle principal #
while state["running"]:
    events = pygame.event.get()
    if state["title"]:
        title_text, title_rect, texto_opciones, rects_opciones = tools.star_menu(screen)
        screen.fill(constants.BLACK)
        screen.blit (title_text,title_rect)
        for text, rect in zip(texto_opciones,rects_opciones):
            screen.blit(text,rect)  
        for event in events:
            if event.type == pygame.QUIT:
                state["running"] = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    state["title"] = False
                    lifes = 3
                    score = 0
                if event.key == pygame.K_q:
                    state["running"] = False
        pygame.display.flip()
                        
    elif not state["title"]:
        
        # Llamada a movimiento de plataforma y pelota #
        plat_x, plat_y = tools.move_plat(state, plat_x, plat_y)
        ball_x, ball_y = tools.move_ball(ball_x, ball_y)

        # Limpieza de la pantalla #
        screen.fill(constants.BLACK)
        
        # Dibujo de la puntación y las vidas #
        number_lifes = tools.lifes(lifes, font, screen)
        score_points = tools.points(score, font)
        screen.blit(score_points, (10, 10))
        screen.blit(number_lifes, (700, 10))

        # Dibujo paleta y bola #    
        pygame.draw.rect(screen,constants.BLUE,(plat_x,plat_y,constants.PLATFORM_WIDTH,constants.PLATFORM_HEIGHT),0,3)
        pygame.draw.circle(screen, constants.RED, (int(ball_x), int(ball_y)),constants.BALL_RADIUS)
        
        
        # Colisión con paredes #
        score, lifes , ball_x, ball_y = tools.collision_ball(ball_x, ball_y, plat_x, plat_y, state, score, lifes)  
    # Escribiendo datos y actualización de la  pantalla #
    
    pygame.display.flip()
    clock.tick(constants.FPS)
pygame.quit()