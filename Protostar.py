import pygame
import sys


pygame.init()
pygame.display.set_caption("Protostar")
screen_width, screen_height = 1200, 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
BLUE = pygame.Color('dodgerblue3')
ORANGE = pygame.Color('sienna3')
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (13, 255, 0)
DARK_GREEN = (0, 225, 0)
BRIGHT_GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
font = pygame.font.Font(None, 25)
frame_rate = 60

#Walls class
class Walls(pygame.Rect):

    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

#Class for rectangles on the left side
class LeftRedRect(pygame.Rect):

    def __init__(self, x, y, w, h, vel):
        # Calling the __init__ method of the parent class
        super().__init__(x, y, w, h)
        self.vel = vel

    def update(self):
        self.x += self.vel  #Moving
        if self.right > 600 or self.left < 320:  #If it's not in this area
            self.vel = -self.vel  #Inverting the direction


#Class for rectangles on the right side that move from left to right
class RightRedRect(pygame.Rect):

    def __init__(self, x, y, w, h, vel):
        super().__init__(x, y, w, h)
        self.vel = vel

    def update(self):
        self.x += self.vel
        if self.right > 1180 or self.left < 620:
            self.vel = -self.vel


#Class for rectangles on the right side that move up and down
class UpAndDownRedRect(pygame.Rect):

    def __init__(self, x, y, w, h, vel):
        super().__init__(x, y, w, h)
        self.vel = vel

    def update(self):
        self.y += self.vel
        if self.top < 20 or self.bottom > 535:
            self.vel = -self.vel

#Function for quitting the game
def quit_game():
    pygame.quit()
    sys.exit()

#Timer function
def timer_display(text, timer):
    largeText = pygame.font.Font(None, 100)
    screen.blit(largeText.render(text, True, GREEN), (313, 250))
    screen.blit(largeText.render(timer, True, GREEN), (479, 250))
    pygame.display.update()

    pygame.time.wait(3000)

def message_display(text):
    largeText = pygame.font.Font(None, 115)
    screen.blit(largeText.render(text, True, BLUE), (370, 250))
    pygame.display.update()
    pygame.time.wait(1000)

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

#Function for button that is used for the game
def button(msg, x, y, w, h, ic, ac, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()


    if x + w > mouse[0] > x and y + h  > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf",35)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    screen.blit(textSurf, textRect)

#Restart function that also calls button function
def restart():
    next_scene = None

    def start_game():
        nonlocal next_scene
        next_scene = menu

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

            if next_scene is not None:
                return next_scene

        screen.fill(WHITE)

        largeText = pygame.font.Font(None, 115)
        screen.blit(largeText.render("You lost", True, BLUE), (445, 75))

        button("Restart", 525, 250, 150, 60, DARK_GREEN, BRIGHT_GREEN, start_game)
        button("Quit", 525, 350, 150, 60, DARK_GREEN, BRIGHT_GREEN, quit_game)


        pygame.display.flip()
        clock.tick(60)

#Screen function that calls button function
def victory_screen():
    next_scene = None

    def start_game():
        nonlocal next_scene
        next_scene = menu

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

            if next_scene is not None:
                return next_scene


        screen.fill(WHITE)

        largeText = pygame.font.Font(None, 115)
        screen.blit(largeText.render("Congratulations!", True, BLUE), (270, 80))
        largeText = pygame.font.Font(None, 60)
        screen.blit(largeText.render("You beat the game!", True, BLUE), (410, 180))

        button("Restart", 525, 300, 150, 60, DARK_GREEN, BRIGHT_GREEN, start_game)
        button("Quit", 525, 400, 150, 60, DARK_GREEN, BRIGHT_GREEN, quit_game)

        pygame.display.flip()
        clock.tick(frame_rate)

#Instruction screen
def instructions_screen():
    next_scene = None

    def start_game():
        nonlocal next_scene
        next_scene = menu

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

            if next_scene is not None:
                return next_scene

        screen.fill(WHITE)

        largeText = pygame.font.Font(None, 115)
        smallText = pygame.font.Font(None, 60)
        screen.blit(largeText.render("Instructions", True, BLUE), (362, 50))
        screen.blit(smallText.render("Goal of the game: Reach the yellow rectangle", True, BLACK), (148, 150))
        screen.blit(smallText.render("How to move: Upper arrow - up", True, BLACK), (148, 210))
        screen.blit(smallText.render("Lower arrow - down", True, BLACK), (429, 250))
        screen.blit(smallText.render("Left arrow - left", True, BLACK), (429, 290))
        screen.blit(smallText.render("Right arrow - right", True, BLACK), (429, 330))

        button("Play", 525, 430, 150, 60, DARK_GREEN, BRIGHT_GREEN, start_game)

        pygame.display.flip()
        clock.tick(60)

#Front page screen
def front_page():
    next_scene = None

    def start_game():
        nonlocal next_scene
        next_scene = menu

    def show_instructions_screen():
        nonlocal next_scene
        next_scene = instructions_screen

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        if next_scene is not None:
            return next_scene

        screen.fill(WHITE)

        screen.blit(image1, (0,0))

        largeText = pygame.font.Font(None, 140)
        screen.blit(largeText.render("Protostar", True, BLUE), (389, 50))

        button("Play", 525, 200, 150, 60, DARK_GREEN, BRIGHT_GREEN, start_game)
        button("Quit", 525, 400, 150, 60, DARK_GREEN, BRIGHT_GREEN, quit_game)
        button("Info", 525, 300, 150, 60, DARK_GREEN, BRIGHT_GREEN, show_instructions_screen)

        pygame.display.flip()
        clock.tick(frame_rate)


#Menu function that draws everything and game loop
def menu():
    vel = 4
    vel_left = 5
    vel_right = -5
    vel_up = 7
    start_time = pygame.time.get_ticks()

    player = pygame.Rect(40, 45, 30, 30)

    finish_line = pygame.Rect(620, 535, 560, 45)

    walls = [
        Walls(0, 0, 1200, 20), Walls(0, 0, 20, 600),
        Walls(0, 580, 1200, 20), Walls(1180, 0, 20, 600),
        Walls(300, 0, 20, 530), Walls(20, 100, 230, 20),
        Walls(70, 200, 230, 20), Walls(20, 300, 230, 20),
        Walls(70, 400, 230, 20), Walls(600, 100, 20, 500)
    ]

    leftredrects = [
        LeftRedRect(320, 120, 30, 30, vel_left),
        LeftRedRect(320, 240, 30, 30, vel_left),
        LeftRedRect(320, 360, 30, 30, vel_left),
        LeftRedRect(570, 180, 30, 30, vel_right),
        LeftRedRect(570, 300, 30, 30, vel_right),
        LeftRedRect(570, 420, 30, 30, vel_right)
    ]

    rightredrects = [
        RightRedRect(1140, 120, 30, 30, vel_left),
        RightRedRect(1140, 240, 30, 30, vel_left),
        RightRedRect(1140, 360, 30, 30, vel_left),
        RightRedRect(620, 180, 30, 30, vel_right),
        RightRedRect(620, 300, 30, 30, vel_right),
        RightRedRect(620, 420, 30, 30, vel_right),
    ]

    upanddownredrects = [
        UpAndDownRedRect(620, 20, 30, 30, vel_up),
        UpAndDownRedRect(752, 505, 30, 30, vel_up),
        UpAndDownRedRect(885, 20, 30, 30, vel_up),
        UpAndDownRedRect(1016, 505, 30, 30, vel_up),
        UpAndDownRedRect(1150, 20, 30, 30, vel_up)
    ]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()


        passed_time = pygame.time.get_ticks() - start_time
        output = "Time: {0}".format(passed_time/1000)

        keys = pygame.key.get_pressed()

        #Player coordinates
        if keys[pygame.K_LEFT] and player.x > 0:
            player.x -= vel
        if keys[pygame.K_RIGHT] and player.x < 1200 - player.width:
            player.x += vel
        if keys[pygame.K_UP] and player.y > 0:
            player.y -= vel
        if keys[pygame.K_DOWN] and player.y < 600 - player.height:
            player.y += vel

        #Game logic
        for wall in walls:
            # heck if the player rectangle collides with a wall rectangle
            if player.colliderect(wall):
                message_display("Game Over")
                return restart

        for rect in rightredrects:
            rect.update()  # Movement and bounds checking
            if player.colliderect(rect):
                message_display("Game Over")
                return restart

        for rect in leftredrects:
            rect.update()
            if player.colliderect(rect):
                message_display("Game Over")
                return restart

        for rect in upanddownredrects:
            rect.update()
            if player.colliderect(rect):
                message_display("Game Over")
                return restart

        if player.colliderect(finish_line):
            timer_display("Your", output)
            return victory_screen

        #Drawing everything
        screen.fill(WHITE)

        text = font.render(output, True, BLACK)
        screen.blit(text, [1070, 30])

        pygame.draw.rect(screen, YELLOW, finish_line)

        for wall in walls:
            pygame.draw.rect(screen, BLACK, wall)

        for rect in rightredrects:
            pygame.draw.rect(screen, RED, rect)

        for rect in leftredrects:
            pygame.draw.rect(screen, RED, rect)

        for rect in upanddownredrects:
            pygame.draw.rect(screen, RED, rect)

        pygame.draw.rect(screen, GREEN, player)


        clock.tick(60)
        pygame.display.flip()


def main():
    scene = front_page
    while scene is not None:
        scene = scene()


main()
pygame.quit()