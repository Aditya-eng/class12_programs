import pygame
import pygame as pygame

print(0xABC)

pygame.init()   #pygame.init() - This is used to initialize all the required module of the pygame.
screen1 = pygame.display.set_mode((400,500))   #pygame.display.set_mode((width, height)) - This is used to display a window of the desired size. The return value is a Surface object which is the object where we will perform graphical operations.
done = False

while not done:
    for event in pygame.event.get():   #pygame.event.get()- This is used to empty the event queue. If we do not call this, the window messages will start to pile up and, the game will become unresponsive in the opinion of the operating system.
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()    #pygame.display.flip() - Pygame is double-buffered, so this shifts the buffers. It is essential to call this function in order to make any updates that you make on the game screen to make visible.

for i in range(10):
    print(i)
    i = 5