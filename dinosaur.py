import pygame

white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
x=pygame.init()

screen_width=900
screen_height=800
game_window=pygame.display.set_mode((screen_width,screen_height))


pygame.display.set_caption("Dinosour")
pygame.display.update()

dino_x=45
dino_y=55
dino_size=10
exit_game=False
game_over=False
clock=pygame.time.Clock()
fps=30
while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game=True

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                dino_x+=5

    game_window.fill(white)
    pygame.draw.line(game_window,black,(10,700),(900,700))
    pygame.draw.rect(game_window,black,[dino_x,dino_y,dino_size,dino_size])
    pygame.display.update()
    clock.tick(fps)


pygame.quit()
quit()
