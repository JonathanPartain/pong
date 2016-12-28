#!/usr/bin/python2.7
import sys, pygame, random

pygame.init()


WIDTH  = 600
HEIGHT = 300
# radius
r = 10

screen_surface =  pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# colors
WHITE = (255,255,255)
BLACK = (0  ,0  ,0  )
RED   = (255,0  ,0  )
GREEN = (0  ,255,0  )
BLUE  = (0  ,0  ,255)

# Left paddle
left_paddle_x = 2*r
left_paddle_y = (HEIGHT/2) - 15

# Right paddle
right_paddle_x = WIDTH - (2*r+10)
right_paddle_y = (HEIGHT/2) - 15

# clock for fps
clock = pygame.time.Clock()

# BALL INFO
ball_x = WIDTH / 2
ball_y = HEIGHT / 2

# ball speed
ball_speed_x = random.randint(2, 4)
ball_speed_y = random.randint(2, 4)

# Left and right score 
left_score  = 0
right_score = 0



while True:
	clock.tick(60)
	screen_surface.fill(BLACK)
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			sys.exit(0)

		keys = pygame.key.get_pressed()

	# W + S for left paddle
	if keys[pygame.K_w]:
		left_paddle_y -= 2
	if keys[pygame.K_s]:
		left_paddle_y += 2

	# UP + DOWN for right paddle
	if keys[pygame.K_UP]:
		right_paddle_y -= 2
	if keys[pygame.K_DOWN]:
		right_paddle_y += 2

	# Create left paddle
	left_paddle = pygame.draw.rect(screen_surface, RED, (left_paddle_x, left_paddle_y, 10, 30))

	# Create right paddle
	right_paddle = pygame.draw.rect(screen_surface, GREEN, (right_paddle_x, right_paddle_y, 10, 30))


	# Create ball
	ball = pygame.draw.circle(screen_surface, BLUE, (ball_x, ball_y), r)
	ball_x = ball_x + ball_speed_x
	ball_y = ball_y +  ball_speed_y

	# Create center line
	pygame.draw.rect(screen_surface, WHITE, (WIDTH/2, 0, 0.2, HEIGHT))

	# Center circle 
	pygame.draw.circle(screen_surface, WHITE, (WIDTH/2, HEIGHT/2), 10)
	pygame.draw.circle(screen_surface, BLACK, (WIDTH/2, HEIGHT/2), 9)


	# Display score
	font = pygame.font.SysFont("monospace", 30)

	# render text
	left_score_label = font.render(str(left_score), 1, RED)
	screen_surface.blit(left_score_label, ((WIDTH/2)-30, 15))

	right_score_label = font.render(str(right_score), 1, GREEN)
	screen_surface.blit(right_score_label, ((WIDTH/2)+20, 15))

	# check ball collisions in y axis
	if (ball_y + (r/2)) >= HEIGHT:
		ball_speed_y *= -1
	if (ball_y - (r/2)) <= 0:
		ball_speed_y *= -1

	# Left paddle collision
	if ball.colliderect(left_paddle):
		ball_speed_x *= -1
		ball_x += 5
		

	# Right paddle collision
	if ball.colliderect(right_paddle):
		ball_speed_x *= -1
		ball_x -= 10
		


	# Out to the left
	if ball_x < 0:
		right_score += 1

		ball_x = WIDTH / 2
		ball_y = HEIGHT / 2

		ball_speed_x = random.randint(2, 4)
		ball_speed_y = random.randint(2, 4)

	# Out to the right
	if ball_x > WIDTH:
		left_score += 1
		
		ball_x = WIDTH / 2
		ball_y = HEIGHT / 2

		ball_speed_x = random.randint(2, 4)
		ball_speed_y = random.randint(2, 4)

	pygame.display.update()