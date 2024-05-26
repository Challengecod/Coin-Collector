import pygame
import random
import time
from fox import Fox
from coin import Coin
from red_coin import Red
from spike import Spike
from blue_fox import Blue

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Time New Roman', 20)
pygame.display.set_caption("Coin Collector!")

# set up variables for the display
SCREEN_HEIGHT = 370
SCREEN_WIDTH = 530
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

name = "Collect coins as fast as you can!"
message = "Collision not detected"
score = 0
start = time.time()
current = time.time()
time_remains = 20 - (current - start)
data = 0
last_score = 0
x_location = random.randint(50, 490)
y_location = random.randint(50, 300)


r = 150
g = 120
b = 100


# render the text for later
display_name = my_font.render(name, True, (255, 255, 255))
display_message = my_font.render(message, True, (255, 255, 255))
display_score = my_font.render("Score: " + str(score), True, (255, 255, 255))
display_introduction = my_font.render("Use ASDW to move", True, (255,255,255))
display_introduction_two = my_font.render("You have 20 seconds to collect however many coins", True, (255,255,255))
display_introduction_three = my_font.render("Click anywhere on the screen to begin!", True, (255, 255, 255))
high_scored = my_font.render("High Score: " + str(score), True, (255, 255, 255))
high_score_achieved_display = my_font.render("High Score Achieved!!", True, (255, 255, 255))
display_game_over = my_font.render("Gamer Over, you win 100 points!", True, (255,255,255))
display_time = my_font.render("Time remaining: " + str(time_remains), True, (255,255,255))
display_no_time = my_font.render("No Time Left! 20 seconds is up! Your score is: " + str(score), True, (255, 255, 255))

f = Fox(40, 60)
c = Coin(200, 85)
rc = Red(random.randint(50, 530), random.randint(50,370))
s = Spike(150, 150)
bf = Blue(270,260)

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
click = True
time_starts = False
timers = random.randint(0,20)
stop_timer = False
i = 1
blit = False

# -------- Main Program Loop -----------
while run:

    if click is False:

        keys = pygame.key.get_pressed()  # checking pressed keys
        if keys[pygame.K_d]:
            f.move_direction("right", SCREEN_WIDTH, SCREEN_HEIGHT)

        if keys[pygame.K_a]:
            f.move_direction("left", SCREEN_WIDTH, SCREEN_HEIGHT)

        if keys[pygame.K_w]:
            f.move_direction("up", SCREEN_WIDTH, SCREEN_HEIGHT)

        if keys[pygame.K_s]:
            f.move_direction("down", SCREEN_WIDTH, SCREEN_HEIGHT)

        if keys[pygame.K_RIGHT]:
            bf.move_direction("right", SCREEN_WIDTH, SCREEN_HEIGHT)

        if keys[pygame.K_LEFT]:
            bf.move_direction("left", SCREEN_WIDTH, SCREEN_HEIGHT)

        if keys[pygame.K_UP]:
            bf.move_direction("up", SCREEN_WIDTH, SCREEN_HEIGHT)

        if keys[pygame.K_DOWN]:
            bf.move_direction("down", SCREEN_WIDTH, SCREEN_HEIGHT)


    if f.rect.colliderect(c.rect) or bf.rect.colliderect(c.rect):
        message = "Collision detected"
        display_message = my_font.render(message, True, (255, 255, 255))
        if stop_timer == True:
            score += 0
        else:
            score += 10
            display_score = my_font.render("Score: " + str(score), True, (255, 255, 255))
        c.set_location(random.randint(50, 470), random.randint(50, 280))

    if blit is True :
        if f.rect.colliderect(rc.rect) or bf.rect.colliderect(rc.rect):

            if stop_timer == True:
                score += 0
            else:
                rc.set_location(random.randint(50, SCREEN_WIDTH - 50), random.randint(50, SCREEN_HEIGHT - 50))
                score += 20
                display_score = my_font.render("Score: " + str(score), True, (255, 255, 255))
        blit = False

    last_score = score

    if f.rect.colliderect(s.rect) or bf.rect.colliderect(s.rect):
        if not stop_timer:
            print("hit")
            if score - 20 >= 0:
                score -= 20
        s.set_location(random.randint(50, SCREEN_WIDTH - 50), random.randint(50, SCREEN_HEIGHT - 50))

        display_score = my_font.render("Score: " + str(score), True, (255, 255, 255))


    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            if click is False:
                touch = False

            elif event.button == 1 or event.button == 3:
                click = False
                start = time.time()
                time_starts = True
        # collision


    if time_starts is True:
        current = time.time()
        time_remains = round(20 - (current - start), 2)
        display_time = my_font.render("Time remaining: " + str(time_remains), True, (255, 255, 255))

        if time_remains <= 0.00:
            stop_timer = True

    # --- Main event loop

    screen.fill((r, g, b))

    if stop_timer == True and click is not True:
        display_no_time = my_font.render("No Time Left! 10 seconds is up! Your score is: " + str(score), True, (255, 255, 255))
        screen.blit(display_no_time, (150, 150))

    elif click is True :
        screen.blit(display_introduction, (150,150))
        screen.blit(display_introduction_two, (150, 180))
        screen.blit(display_introduction_three, (150, 200))
        screen.blit(f.image, f.rect)
        screen.blit(c.image, c.rect)


    elif click != True:
        screen.blit(display_message, (0, 15))
        screen.blit(display_score, (0, 30))
        screen.blit(display_time, (0, 45))
        screen.blit(f.image, f.rect)
        screen.blit(bf.image, bf.rect)
        screen.blit(c.image, c.rect)
        screen.blit(s.image, s.rect)

        if timers == int(time_remains):
            screen.blit(rc.image, rc.rect)
            blit = True
        if timers - 1 == int(time_remains):
            blit = True
            screen.blit(rc.image, rc.rect)
        if timers - 2 == int(time_remains):
            blit = True
            screen.blit(rc.image, rc.rect)
        if timers -3 == int(time_remains):
            blit = True
            screen.blit(rc.image, rc.rect)


        file = open("high_score", "r")
        data = file.readline().strip()
        high_scored = my_font.render("High Score: " + str(data), True, (255, 255, 255))

        screen.blit(high_scored, (0, 0))

        if int(data) < last_score:
            high_scored = my_font.render("High Score: " + str(last_score), True, (255, 255, 255))
            screen.blit(high_score_achieved_display, (200, 20))

    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()


# Here is code that will write information to a file:
f = open("high_score", "w")
if last_score > int(data):
    f.write(str(last_score))

else:
    f.write(str(data))
