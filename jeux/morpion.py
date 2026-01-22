import pygame

def start():
    pygame.init()
    
    screen = pygame.display.set_mode((800,700))
    pygame.display.set_caption("Morpion")
    
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        screen.fill((0, 0, 0))  # fond noir
        pygame.display.flip()
        clock.tick(60)
        
pygame.quit()