"""
Модуль хранит класс Button
"""
from Constants import *
pygame.init()


class Button:
    def __init__(self):
        self.zzz = None
        self.rect = None
    
    def create_button(self, surface, color, x, y, length, height, width, text, text_color):
        surface = self.draw_button(surface, color, length, height, x, y, width)
        surface = self.write_text(surface, text, text_color, length, height, x, y)
        self.rect = pygame.Rect(x, y, length, height)
        return surface

    def write_text(self, surface, text, text_color, length, height, x, y):
        self.zzz = None 
        font_size = int(length//len(text)) + 6
        my_font = pygame.font.SysFont("Calibri", font_size)
        my_text = my_font.render(text, True, text_color)
        surface.blit(my_text, ((x+length/2) - my_text.get_width()/2, (y+height/2) - my_text.get_height()/2))
        return surface

    def draw_button(self, surface, color, length, height, x, y, width):           
        self.zzz = None
        for i in range(1, 10):
            s = pygame.Surface((length+(i*2), height+(i*2)))
            s.fill(color)
            alpha = (255/(i+2))
            if alpha <= 0:
                alpha = 1
            s.set_alpha(alpha)
            pygame.draw.rect(s, color, (x-i, y-i, length+i, height+i), width)
            surface.blit(s, (x-i, y-i))
        pygame.draw.rect(surface, color, (x, y, length, height), 0)
        pygame.draw.rect(surface, (190, 190, 190), (x, y, length, height), 1)  
        return surface

    def pressed(self, mouse):
        if mouse[0] > self.rect.topleft[0]:
            if mouse[1] > self.rect.topleft[1]:
                if mouse[0] < self.rect.bottomright[0]:
                    if mouse[1] < self.rect.bottomright[1]:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False


buttons_array = []


def initiate_buttons():
    global buttons_array
    button1 = Button()
    button2 = Button()
    button3 = Button()
    button4 = Button()
    button5 = Button()
    buttons_array.append(button1)
    buttons_array.append(button2)
    buttons_array.append(button3)
    buttons_array.append(button4)
    buttons_array.append(button5)


def draw_buttons_and_stuff(screen):
    Button.create_button(buttons_array[0], screen, (40, 40, 40), c.width - 200, c.height - 100, 200, 100, 0,
                         "Визуализация эффекта", (255, 255, 255))
    Button.create_button(buttons_array[1], screen, (40, 40, 40), 0, c.height - 50, 70, 50, 0, "f(a)", (255, 255, 255))
    Button.create_button(buttons_array[2], screen, (40, 40, 40), 70, c.height - 50, 70, 50, 0, "f(m)", (255, 255, 255))
    Button.create_button(buttons_array[3], screen, (40, 40, 40), 140, c.height - 50, 70, 50, 0, "f(d)", (255, 255, 255))
    Button.create_button(buttons_array[4], screen, (40, 40, 40), c.width - 80, 20, 40, 40, 0,
                         "Справка", (255, 255, 255))
    font_obj = pygame.font.Font('freesansbold.ttf', 10)
    text_surface_obj = font_obj.render('Нажмите для построения графиков:', True, (255, 255, 255))
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (105, c.height - 70)
    screen.blit(text_surface_obj, text_rect_obj)


def draw_buttons_and_stuff_1(screen):
    Button.create_button(buttons_array[0], screen, (40, 40, 40), c.width - 200, c.height - 100, 200, 100, 0,
                         "Добавить чёрную дыру", (255, 255, 255))
    Button.create_button(buttons_array[1], screen, (40, 40, 40), 0, c.height - 50, 70, 50, 0, "f(a)", (255, 255, 255))
    Button.create_button(buttons_array[2], screen, (40, 40, 40), 70, c.height - 50, 70, 50, 0, "f(m)", (255, 255, 255))
    Button.create_button(buttons_array[3], screen, (40, 40, 40), 140, c.height - 50, 70, 50, 0, "f(d)", (255, 255, 255))
    font_obj = pygame.font.Font('freesansbold.ttf', 10)
    text_surface_obj = font_obj.render('Нажмите для построения графиков:', True, (255, 255, 255))
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (105, c.height - 70)
    screen.blit(text_surface_obj, text_rect_obj)


def draw_buttons_and_stuff_2(screen):
    Button.create_button(buttons_array[0], screen, (40, 40, 40), c.width - 200, c.height - 100, 200, 100, 0,
                         "Убрать чёрную дыру", (255, 255, 255))
    Button.create_button(buttons_array[1], screen, (40, 40, 40), 0, c.height - 50, 70, 50, 0, "f(a)", (255, 255, 255))
    Button.create_button(buttons_array[2], screen, (40, 40, 40), 70, c.height - 50, 70, 50, 0, "f(m)", (255, 255, 255))
    Button.create_button(buttons_array[3], screen, (40, 40, 40), 140, c.height - 50, 70, 50, 0, "f(d)", (255, 255, 255))
    font_obj = pygame.font.Font('freesansbold.ttf', 10)
    text_surface_obj = font_obj.render('Нажмите для построения графиков:', True, (255, 255, 255))
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (105, c.height - 70)
    screen.blit(text_surface_obj, text_rect_obj)


def draw_black_hole(screen):
    pygame.draw.circle(screen, (0, 0, 0), (c.x0, c.y0), c.r_bh_screen)


def give_information():
    print("information")
