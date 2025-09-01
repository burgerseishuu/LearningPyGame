import pygame, sys

# Initialize
x = 1500
y = 800
pygame.init()
screen = pygame.display.set_mode((x, y))
pygame.display.set_caption("Pong Game")
clock = pygame.time.Clock()

# Game Rectangles 
ball = pygame.Rect(x/2 - 15, y/2 - 15, 30, 30) # Position x, y, rect size x, y 
player = pygame.Rect(x - 20, y/2 - 70, 10, 140)
opp = pygame.Rect(10, y/2 - 70, 10, 140)

bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

ball_speed_x, ball_speed_y = 7, 7 
player_speed = 0
opp_speed = 7

# Game Loop
while True:

    # Handle input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get speeds
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Collision for the ball
    if ball.top <= 0 or ball.bottom >= y: # Get the top edge of the ball rect and compare it against to the screen dimension
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= x:
        ball.center = (x/2, y/2)
    if ball.colliderect(player) or ball.colliderect(opp):
        ball_speed_x *= -1

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.y -= 7
    if keys[pygame.K_s]:
        player.y += 7

    # Keep player on screen  
    if player.top <= 0:
        player.top = 0
    if player.bottom >= y:
        player.bottom = y

    # Opponent Logic
    if opp.top < ball.y:
        opp.top += opp_speed
    if opp.top > ball.y:
        opp.top -= opp_speed  # Fixed this line!
    
     # Keep opp on screen  
    if opp.top <= 0:
        opp.top = 0
    if opp.bottom >= y:
        opp.bottom = y

    # draw images
    # Images are drawn like layers, so first come are placed behind
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player) # Where to draw, what color and which rect
    pygame.draw.rect(screen, light_grey, opp)
    pygame.draw.ellipse(screen, light_grey, ball) # Ellipse for the ball shape
    pygame.draw.aaline(screen, light_grey, (x/2, 0), (x/2, y)) # Where to draw, what color, start point (where it starts in (x, y)) and the end point

    # Update screen
    pygame.display.flip() # Draw from the loop to update image
    clock.tick(60)