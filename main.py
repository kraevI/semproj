"""Объединяющий модуль, содержащий цикл выполнения программы."""

from pygame.locals import *

from plots import plot1, plot2, plot3
from buttons import *
from model import create_mapping, model
from threeD_main import VisualEngine

pygame.init()


def main():
    screen = pygame.display.set_mode((c.width, c.height))
    pygame.display.set_caption("Гравитационное линзирование")
    finished = False
    clock = pygame.time.Clock()
    
    visualization = VisualEngine(screen)
    mapping = create_mapping()
    initiate_buttons()
    draw_buttons_and_stuff(screen)
    
    while not finished:
        pygame.display.update()
        clock.tick(c.fps)
        
        if visualization.go is True:
            visualization.run()
            if visualization.draw_black_hole is False:
                draw_buttons_and_stuff_1(screen)
            else:
                draw_buttons_and_stuff_2(screen)
                model(screen, mapping)
                draw_black_hole(screen)
                
        for event in pygame.event.get():            
            if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                visualization.go = False
                finished = True
            
            if event.type == MOUSEBUTTONDOWN:
                if buttons_array[0].pressed(pygame.mouse.get_pos()) and visualization.go is False:
                    visualization.go = True
                elif buttons_array[4].pressed(pygame.mouse.get_pos()) and visualization.go is False:
                    give_information()
                elif buttons_array[0].pressed(pygame.mouse.get_pos()) and visualization.go is True:
                    if visualization.draw_black_hole is False:
                        visualization.draw_black_hole = True
                    else:
                        visualization.draw_black_hole = False
                elif buttons_array[1].pressed(pygame.mouse.get_pos()):
                    plot1()
                elif buttons_array[2].pressed(pygame.mouse.get_pos()):
                    plot2()
                elif buttons_array[3].pressed(pygame.mouse.get_pos()):
                    plot3()


main()

pygame.quit()

