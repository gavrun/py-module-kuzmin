import circle as c
import drawcircle as d
import pygame

# The looping variable to keep our game going
running = True

# Setup and initialize the pygame library
d.setup()

# As long as running == True keep looping
while running:
    ev = pygame.event.get()  # Capture user events (input)

    for event in ev:
        if event.type == pygame.MOUSEBUTTONUP:
            # Mouse was clicked and released, draw a circle here!
            pos = pygame.mouse.get_pos()

            # Instantiate a circle and populate its values
            c1 = c.Circle()
            c1.radius = 10
            c1.coords.x = pos[0]
            c1.coords.y = pos[1]
            c1.color = "green"
            c1.filled = True

            # Draw the circle to the screen
            d.drawCircle(c1)
            pygame.display.update()

        if event.type == pygame.QUIT:
            running = False

