import pygame as pg
pg.init()

def management(running, PERFORMANCE_INPUT, inputString):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            inputString+=event.unicode
            print(event.unicode, inputString)
    SCREEN.fill(COLORS['RED'])
    text_cur = font.render(inputString, True, COLORS['WHITE'])
    pg.draw.rect(SCREEN, COLORS['BLACK'], rect)
    SCREEN.blit(text_cur, (100, 100))
    pg.display.update()
    return running, PERFORMANCE_INPUT, inputString

clock = pg.time.Clock()
running = True
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
rect = pg.Rect((100, 100, 400, 40))
PERFORMANCE_INPUT = False
COLORS = {'WHITE':(255, 255, 255), 'BLACK':(0, 0, 0), 'RED':(255, 0, 0)}
font = pg.font.Font(None, 100)
inputString = ''

while running:
    running, PERFORMANCE_INPUT, inputString = management(running, PERFORMANCE_INPUT, inputString)
pg.quit()