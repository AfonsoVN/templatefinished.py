import pygame,sys
from pygame.locals import QUIT


pygame.init()

screen= pygame.display.set_mode((500,500))
pygame.display.set_caption("My Screen")

screen.fill("blue")


while True:
    pygame.draw.rect(screen,"red",(100,100,50,50))
    pygame.draw.circle(screen,"red",(300,10),50)
    pygame.draw.line(screen,"red",(100,100),(300,300),10)
    pygame.draw.line(screen,"red",(50,250),(100,100),5)
    pygame.draw.circle(screen,"red",(10,100),7)
    pygame.draw.rect(screen, "green", (350, 50, 60, 120))  
    pygame.draw.circle(screen, "yellow", (400, 250), 40)  
    pygame.draw.line(screen, "white", (0, 0), (500, 0), 8) 
    pygame.draw.rect(screen, "purple", (200, 400, 100, 50)) 
    pygame.draw.circle(screen, "orange", (100, 400), 30)  
    pygame.draw.line(screen, "pink", (250, 250), (500, 500), 6)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
