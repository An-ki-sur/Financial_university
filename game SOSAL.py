import sys, pygame, random, time
pygame.init()

random.seed(time.time())

size = width, height = 500, 500
screen = pygame.display.set_mode(size)
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
text_surface = my_font.render('Сосал?', True, (255, 170, 200))
text_rect = text_surface.get_rect()
black = 0, 0, 0

# Создайте поверхность для кнопки
button_surface = pygame.Surface((150, 50))
text = my_font.render("YES", True, (255, 70, 190))
button_rect = text.get_rect(
    center=(button_surface.get_width() / 2,
            button_surface.get_height()/2)
)
button_re = pygame.Rect(125, 125, 200, 50)

# Создайте поверхность для кнопки 2
button_surface2 = pygame.Surface((150, 50))
text2 = my_font.render("NO", True, (255, 70, 190))
button_rect2 = text.get_rect(
    center=(button_surface.get_width() / 2,
            button_surface.get_height()/2)
)
button_re2 = pygame.Rect(125, 225, 200, 50)
x = button_re2.x
y = button_re2.y

flag = True  # True - первый экран / False - второй экран

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_re.collidepoint(event.pos):
                print("Button 1 clicked!")
                flag = False

            # if button_re2.collidepoint(event.pos):
            #     print("Button 2 clicked!")

        # Проверьте, находится ли мышь над кнопкой
        if button_re.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(button_surface, (127, 255, 212), (1, 1, 148, 48))
        else:
            pygame.draw.rect(button_surface, (0, 0, 0), (0, 0, 150, 50))
            pygame.draw.rect(button_surface, (255, 255, 255), (1, 1, 148, 48))
            pygame.draw.rect(button_surface, (0, 0, 0), (1, 1, 148, 1), 2)
            pygame.draw.rect(button_surface, (0, 100, 0), (1, 48, 148, 10), 2)

        # Проверьте, находится ли мышь над кнопкой 2
        if button_re2.collidepoint(pygame.mouse.get_pos()):
            x = random.randint(0, width-button_re2.width)
            y = random.randint(0, height-button_re2.height)
        pygame.draw.rect(button_surface2, (255, 255, 255), (1, 1, 148, 48))
        button_re2.x = x
        button_re2.y = y

    # вывод экранов
    screen.fill(black)
    if flag:
        screen.blit(text_surface, ((width - text_rect.width) // 2, 50))
        button_surface.blit(text, button_rect)
        screen.blit(button_surface, (button_re.x, button_re.y))

        button_surface2.blit(text2, button_rect2)
        screen.blit(button_surface2, (x, y))
    else:
        my_font = pygame.font.SysFont('Comic Sans MS', 50)
        text_surface = my_font.render('ЛОХ', True, (255, 170, 200))
        text_rect = text_surface.get_rect()
        screen.blit(text_surface, ((width - text_rect.width) // 2, 100))
    pygame.display.flip()


'''
size = width, height = 1320, 1240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("A5 - 3.png")
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
'''
