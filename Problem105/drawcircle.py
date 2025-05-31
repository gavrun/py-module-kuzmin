import pygame

colors = {
    "white": (255, 255, 255),
    "blue": (0, 0, 255),
    "green": (0, 255, 0),
    "red": (255, 0, 0)
}

(width, height) = (400, 400)

def setup():
    global screen
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    screen.fill(colors["white"])
    pygame.display.set_caption("Draw Circles")
    pygame.display.update()

def drawCircle(c):
    pygame.draw.circle(
        screen,
        colors[c.color],
        (c.coords.x, c.coords.y),
        c.radius,
        0 if c.filled else 1
    )

