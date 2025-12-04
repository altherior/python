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
    if keys[pygame.K_q]:
        state["running"] = False
    return plat_x, plat_y

def move_ball(ball_x, ball_y):
    # Actualizar posición de la pelota
    ball_x += constants.BALL_SPEED_X 
    ball_y += constants.BALL_SPEED_Y
    return ball_x, ball_y

def collision_ball(ball_x, ball_y, plat_x, plat_y, state, score, lifes, bounce_sound,lost_life,lost,perdido):
    # Comprobar rebote en el borde inferior
    if ball_y - constants.BALL_RADIUS <= 0:
        constants.BALL_SPEED_Y = -constants.BALL_SPEED_Y
    if ball_y + constants.BALL_RADIUS > constants.WINDOW_HEIGHT:
        if lifes >0:
            lifes -= 1
            ball_x, ball_y = ball_new()
            lost_life.play()
        if lifes == 0:
            pygame.mixer.music.stop()
            lost.play()
            game_over()
            pygame.time.wait(int(lost.get_length() * 1000))
            pygame.mixer.music.rewind()
            pygame.mixer.music.play(-1)
            state["title"] = True
            ball_x, ball_y = ball_new()

            
            
    if ball_x - constants.BALL_RADIUS <= 0 or ball_x + constants.BALL_RADIUS >= constants.WINDOW_WIDTH:
        constants.BALL_SPEED_X = -constants.BALL_SPEED_X
    # Colision con la plataforma
    if (plat_y <= ball_y + constants.BALL_RADIUS <= plat_y + constants.PLATFORM_HEIGHT) and \
        (plat_x<= ball_x <= plat_x + constants.PLATFORM_WIDTH):
        bounce(bounce_sound)
        constants.BALL_SPEED_Y = -constants.BALL_SPEED_Y
        score += 1
        # Devuelves las variables actualizadas
        
    return score, lifes, ball_x,  ball_y

def game_over():
    gameover = pygame.font.Font(constants.GOTICH,150)
    screen = pygame.display.set_mode((constants.WINDOW_WIDTH,constants.WINDOW_HEIGHT))
    screen.fill(constants.BLACK)

    gameover_text = gameover.render("GAME OVER", True, constants.WHITE)
    gameover_rect = gameover_text.get_rect(center = (constants.WINDOW_WIDTH//2, constants.WINDOW_HEIGHT//4))
    screen.blit(gameover_text,gameover_rect)
    screen.blit(gameover_text,gameover_rect)
    pygame.display.flip()
def points(score,font):
    text_score = font.render(f"Puntuacion: {score}", True, constants.WHITE)
    return text_score

def lifes(lifes, font, screen):
    text_lifes = font.render("Vidas Restantes: ", True, constants.WHITE )
    total_lifes = 3
    for i in range (total_lifes):
        if i < lifes:
            color = constants.GREEN  # color para vidas "activas"
        else:
            color = constants.RED  # color para vidas "perdidas" o inactivas
        pygame.draw.rect(screen, color, (900+ i * 35, 10, 30, 15),0,3)
    return text_lifes    

def ball_new():
    constants.BALL_SPEED_X = constants.INITIAL_BALL_SPEED_X
    constants.BALL_SPEED_Y = constants.INITIAL_BALL_SPEED_Y
    ball_x = constants.WINDOW_WIDTH // 2 - constants.BALL_RADIUS // 2
    ball_y = 10 + constants.BALL_RADIUS // 2
    return ball_x, ball_y

def music():
    pygame.mixer.music.load(constants.BACKGROUND_MUSIC)
    pygame.mixer.music.play(-1)
def bounce(bounce_sound):
    bounce_sound.play()
