import pygame
import random
import math
from pygame import mixer

# Inicializar Pygame
pygame.init()

# Crea la pantalla
pantalla = pygame.display.set_mode((800, 600))

# Título e Icono
pygame.display.set_caption('Invasión Espacial')
icono = pygame.image.load('forma-de-juego-pixelada-de-ovni-alienigena.png')
pygame.display.set_icon(icono)
fondo = pygame.image.load('space.png')

# Agregar música
mixer.music.load('MusicaFondo.mp3')
mixer.music.play(-1)
sonido_bala = mixer.Sound('disparo.mp3')
sonido_colision = mixer.Sound('Golpe.mp3')

# Variables del jugador
jugador = pygame.image.load('vaquero.png')
jugadorX = 368
jugadorY = 536
jugadorX_cambio = 0

# Variables del enemigo
enemigo = []
enemigoX = []
enemigoY = []
enemigoX_cambio = []
enemigoY_cambio = []
cantidad_enemigos = random.randint(3, 10)

for e in range(cantidad_enemigos):
    enemigo.append(pygame.image.load('mark.png'))
    enemigoX.append(random.randint(0, 736))
    enemigoY.append(random.randint(0, 100))
    enemigoX_cambio.append(1.5)
    enemigoY_cambio.append(50)

# Variables de la bala
balas = []
bala = pygame.image.load('bala.png')

# Puntaje
puntaje = 0
fuente = pygame.font.SysFont('freesansbold.ttf', 30)
textox = 10
textoy = 10

# Texto final del juego
fuente_final = pygame.font.Font('freesansbold.ttf', 40)


def texto_final():
    mi_fuente_final = fuente_final.render('JUEGO TERMINADO', True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (200, 250))


def mostrar_puntaje(x, y):
    texto = fuente.render(f'Puntaje: {puntaje}', True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


def player(x, y):
    pantalla.blit(jugador, (x, y))


def enemy(x, y, ene):
    pantalla.blit(enemigo[ene], (x, y))


def disparar_bala(x, y):
    pantalla.blit(bala, (x + 16, y + 10))


def hay_colision(x1, y1, x2, y2):
    d = math.sqrt((math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2)))
    return d < 27


# Loop del juego
se_ejecuta = True
while se_ejecuta:
    pantalla.blit(fondo, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            se_ejecuta = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                jugadorX_cambio = -1.5
            if event.key == pygame.K_RIGHT:
                jugadorX_cambio = 1.5
            if event.key == pygame.K_SPACE:
                sonido_bala.play()
                balas.append({'x': jugadorX, 'y': jugadorY, 'velocidad': -5})

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                jugadorX_cambio = 0

    jugadorX += jugadorX_cambio
    jugadorX = max(0, min(jugadorX, 736))

    # Modificar ubicación del enemigo
    for e in range(cantidad_enemigos):
        if enemigoY[e] > jugadorY:
            for k in range(cantidad_enemigos):
                enemigoY[k] = 1000
            texto_final()
            pygame.display.update()
            pygame.time.delay(2000)
            se_ejecuta = False
            break

        enemigoX[e] += enemigoX_cambio[e]

        if enemigoX[e] <= 0:
            enemigoX_cambio[e] = 1.5
            enemigoY[e] += enemigoY_cambio[e]
        elif enemigoX[e] >= 736:
            enemigoX_cambio[e] = -1.5
            enemigoY[e] += enemigoY_cambio[e]

        # Detectar colisión con las balas
        for bal in balas[:]:
            if hay_colision(enemigoX[e], enemigoY[e], bal['x'], bal['y']):
                sonido_colision.play()
                balas.remove(bal)
                puntaje += 1
                enemigoX[e] = random.randint(0, 736)
                enemigoY[e] = random.randint(50, 200)
                break

        enemy(enemigoX[e], enemigoY[e], e)

    # Movimiento de la bala
    for bal in balas[:]:
        bal['y'] += bal['velocidad']
        pantalla.blit(bala, (bal['x'] + 16, bal['y'] + 10))
        if bal['y'] < 0:
            balas.remove(bal)

    player(jugadorX, jugadorY)
    mostrar_puntaje(textox, textoy)
    pygame.display.update()
