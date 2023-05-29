import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)

screen_height = 600
screen_width = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game!")

clock = pygame.time.Clock()

snake_model = 20
snake_speed = 20

font_style = pygame.font.SysFont('Arial', 40)
score_font = pygame.font.SysFont('bahnschrift', 30)

def points(score):
    value = score_font.render("Score: " + str(score), True, blue)
    screen.blit(value, [30, 550])

def thesnake(snake_model, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_model, snake_model])

def message(msg, color):
    mess = font_style.render(msg, True, color)
    screen.blit(mess, [(screen_width/2)-100, screen_height/3])

def message2(msg, color):
    mess2 = font_style.render(msg, True, color)
    screen.blit(mess2, [200, screen_height/2])


def gameLoop():
    game_over = False
    game_close = False

    x1 = screen_width / 2
    y1 = screen_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

    foodx = round(random.randrange(0, screen_width - snake_model) / 20.0) * 20.0

    foody = round(random.randrange(0, screen_height - snake_model) / 20.0) * 20.0

    while not game_over:

        while game_close:
            screen.fill(green)
            message("RIP!", red)
            message2("Press Q to Quit. Press Space to play again!", red)
            points(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_SPACE:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x1_change = -snake_model
                    y1_change = 0
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x1_change = snake_model
                    y1_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    y1_change = -snake_model
                    x1_change = 0
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    y1_change = snake_model
                    x1_change = 0

        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change

        screen.fill(black)

        pygame.draw.rect(screen, red, [foodx, foody, snake_model, snake_model])
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        thesnake(snake_model, snake_list)
        points(int((snake_length - 1) / 2))

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, screen_width - snake_model) / 20.0) * 20.0
            foody = round(random.randrange(0, screen_height - snake_model) / 20.0) * 20.0
            snake_length += 2

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
