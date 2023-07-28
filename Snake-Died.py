#
In this game the snake will die after eating the food
#
//Code
import pygame
import random

# initializing pygame
pygame.init()

# Colors
background = (0, 0, 0) # rgb format
food_color = (255, 148, 0)
snake_color = (255,165,0)

# Creating window
screen_width = 900
screen_height = 600
gameWd = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("Coders Home")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    #render is used to display the object
    screen_text = font.render(text, True, color)
    #blit is used to copy the image and place it to another object
    gameWd.blit(screen_text, [x,y])


def plot_snake(gameWd, color, snake_list, snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWd, color, [x, y, snake_size, snake_size])

# Game Loop
def gameloop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 2
    velocity_y = 2
    snake_list = []
    snake_length = 3

    food_x = random.randint(20, screen_width-20)
    food_y = random.randint(60, screen_height -20)
    score = 0
    init_velocity = 4
    snake_size = 30
    fps = 60   # fps = frames per second
    while not exit_game:
        if game_over:
            gameWd.fill(background)
            text_screen("Game Over! Press Enter To Continue", food_color, 100, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10:
                score +=1
                food_x = random.randint(20, screen_width - 30)
                food_y = random.randint(60, screen_height - 30)
                snk_length +=5

            gameWd.fill(background)
            text_screen("Score: " + str(score * 10),food_color, 5, 5)
            pygame.draw.rect(gameWd, food_color, [food_x, food_y, snake_size, snake_size])
            pygame.draw.line(gameWd, food_color, (0,40), (900,40),5)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list)>snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True

            if snake_x<0 or snake_x>screen_width-20 or snake_y<50 or snake_y>screen_height-20:
                game_over = True
            plot_snake(gameWd, snake_color, snake_list, snake_size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
gameloop()

