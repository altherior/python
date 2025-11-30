import pygame
from files import constants

def config_game (width, height, title, bg_color):
    pygame.init()
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption(title)
    return screen

def star_menu(screen):
    text_title = pygame.font.Font(constants.GOTICH,250)
    text_menu = pygame.font.Font(None,30)
    opciones = ["1 - Jugar (Pulsa Espacio)", "2 - Salir (Pulsar Q)"]
    title_text = text_title.render("PONG",True,constants.YELLOW)
    title_rect = title_text.get_rect(center = (constants.WINDOW_WIDTH//2, constants.WINDOW_HEIGHT//4))
    # Creamos una lisgta para el textdo y el rectangulo de cada opción del menú 
    texto_opciones = []
    rects_opciones = []
    for i, opcion in enumerate(opciones):
        opcion_text = text_menu.render(opcion,True,constants.WHITE)
        opcion_rect = opcion_text.get_rect(center = (constants.WINDOW_WIDTH//2, constants.WINDOW_HEIGHT//2 + 100 + i * 50))
        texto_opciones.append(opcion_text)
        rects_opciones.append(opcion_rect)

    return title_text, title_rect, texto_opciones, rects_opciones

def clock_game():
    clock = pygame.time.Clock()
    return clock

def move_plat(state, plat_x, plat_y):
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

def collision_ball(ball_x, ball_y, plat_x, plat_y, state, score):
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
        score += 1
        # Devuelves las variables actualizadas
        
    return score
    
def points(score,font):
    text_score = font.render(f"Puntuacion: {score}", True, constants.WHITE)
    return text_score
