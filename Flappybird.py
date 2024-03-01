import pygame

pygame.init()
HEIGHT,WIDTH = 600,800
screen = pygame.display.set_mode((WIDTH,HEIGHT))
FPS = 60
pygame.display.set_caption("Flappy Bird")
icon = pygame.image.load('images/1161953_instagram_icon.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

py, ps,pa = HEIGHT // 2, 0, 0
Player = pygame.Rect(WIDTH // 3, py, 50, 50)
play = True

state = 'start'
timer = 10

pipes = []
while play:
    pygame.display.update()
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    keys = pygame.key.get_pressed()
    click = keys[pygame.K_SPACE]


    if timer > 0:
        timer -= 1

    for i in range(len(pipes) -1,-1,-1):
        pipe = pipes[i]
        pipe.x -= 3

        if pipe.right < 100:
            pipes.remove(pipe)

    if state == 'start':
        if click and timer == 0 and len(pipes) == 0:
            state = 'play'

        py += (HEIGHT // 2 - py) * 0.1
        Player.y = py
    elif state == 'play':
        if click:
            pa = -2
        else:
            pa = 0

        py += ps
        ps = (ps + pa + 1) * 0.98
        Player.y = py

        if len(pipes) == 0 or pipes[len(pipes) -1].x < WIDTH - 200:
            pipes.append(pygame.Rect(WIDTH, 0, 50, 200))
            pipes.append(pygame.Rect(WIDTH, 400, 50, 200))

        if Player.top < 0 or Player.bottom > HEIGHT:
            state = 'fall'

        for pipe in pipes:
            if Player.colliderect(pipe):
                state = 'fall'
    elif state == 'fall':
        ps, pa = 0, 0
        state = 'start'
        timer = 60
    else:
        pass

    screen.fill(pygame.Color("black"))
    for pipe in pipes:
        pygame.draw.rect(screen,pygame.Color("yellow"),pipe)
    pygame.draw.rect(screen,pygame.Color("green"),Player)