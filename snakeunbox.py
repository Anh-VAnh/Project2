import pygame
from time import sleep
from random import randint

pygame.init()

WIDTH = 601
HEIGHT = 601
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption('Freedom Snake')
running = True

BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (220, 220, 220)

clock = pygame.time.Clock()

# Snake position
# Tail - Head
snakes = [[5,10]]
direction = "right"

prey = [randint(0, 19), randint(0, 19)]
font_score = pygame.font.SysFont('sans', 20)
font_over = pygame.font.SysFont('sans', 50)
score = 0

pausing = False

# prey_image = pygame.image.load("fbheart.png")
# prey_image = pygame.transform.scale(prey_image,(30,30))
# background_image = pygame.image.load("game-background-png-2.png")
# background_image = pygame.transform.scale(background_image, (601, 601))

sound_die = pygame.mixer.Sound('hit.wav')
sound_eat = pygame.mixer.Sound('evil_laf.wav')


while running:		
	clock.tick(60)
	screen.fill(BLACK)
	# screen.blit(background_image,(0, 0))

	box_txt = font_score.render("Set mode: FREE", True, WHITE)
	screen.blit(box_txt, (248, 5))

	tail_x = snakes[0][0]
	tail_y = snakes[0][1]

	# Draw grid
	# for i in range(21):

	# Draw edge
	pygame.draw.line(screen, WHITE, (0, 0), (0, 600))
	pygame.draw.line(screen, WHITE, (0, 0), (600, 0))
	pygame.draw.line(screen, WHITE, (600, 0), (600, 600))
	pygame.draw.line(screen, WHITE, (0, 600), (600, 600))
	
	# Draw snake
	for snake in snakes:
		pygame.draw.rect(screen, GREEN, (snake[0]*30, snake[1]*30, 30, 30))

	# Draw prey
	pygame.draw.rect(screen, RED, (prey[0]*30, prey[1]*30, 30, 30))
	# screen.blit(prey_image, (prey[0]*30, prey[1]*30))
	
	# Quit button
	quit_button = pygame.draw.rect(screen, GREY, (601 - 20, 10, 10, 10))
	text = font_score.render('x', True, BLACK)
	screen.blit(text, (WIDTH - 18, 4))

	# Point
	if snakes[-1][0] == prey[0] and snakes[-1][1] == prey[1]:
		snakes.insert(0, [tail_x, tail_y])
		prey = [randint(0, 19), randint(0, 19)]
		# Xu ly viec moi xuat hien tren ran
		while True:
			if prey in snakes:
				prey =  [randint(0, 19), randint(0, 19)]
			else:
				break
		score += 1
		pygame.mixer.Sound.play(sound_eat)
		# for snake in snakes:
		# 	while (prey != snakes):
		# 		prey = [randint(0, 19), randint(0, 19)]

	# Check crash with edge
	if snakes[-1][0] < 0:
		snakes[-1][1] = snakes[-1][1]
		snakes[-1][0] = 20
	if snakes[-1][0] > 19:
		snakes[-1][1] = snakes[-1][1]
		snakes[-1][0] = -1
	if snakes[-1][1] < 0:
		snakes[-1][0] = snakes[-1][0]
		snakes[-1][1] = 20
	if snakes[-1][1] > 19:
		snakes[-1][0] = snakes[-1][0]
		snakes[-1][1] = -1
		

	# Game over:
	if pausing:
		game_over_txt = font_over.render("Game over. Score: " + str(score), True, WHITE)
		press_space_txt = font_over.render("Press Space to Continue", True, WHITE)
		screen.blit(game_over_txt, (80, 200))
		screen.blit(press_space_txt, (50, 300))
	
	# Score
	score_txt = font_score.render("Score = " + str(score), True, WHITE)
	screen.blit(score_txt, (5, 5))

	# Snake move
	if pausing == False:
		if direction == "right":
			snakes.append([snakes[-1][0] + 1, snakes[-1][1]])
			snakes.pop(0)
		if direction == "left":
			snakes.append([snakes[-1][0] - 1 , snakes[-1][1]])
			snakes.pop(0)
		if direction == "up":
			snakes.append([snakes[-1][0], snakes[-1][1] - 1])
			snakes.pop(0)
		if direction == "down":
			snakes.append([snakes[-1][0], snakes[-1][1] + 1])
			snakes.pop(0)
		
	sleep(0.1)
	# sleep(0.05)
	# sleep(0.01)

	# Check crash with body
	for i in range(len(snakes)-1):
		if snakes[-1][0] == snakes[i][0] and snakes[-1][1] == snakes[i][1]:
			if pausing == False:
				pygame.mixer.Sound.play(sound_die)
				pausing = True

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP and direction != "down":
				direction = "up"
			if event.key == pygame.K_DOWN and direction != "up":
				direction = "down"
			if event.key == pygame.K_LEFT and direction != "right":
				direction = "left"
			if event.key == pygame.K_RIGHT and direction != "left":
				direction = "right"
			if event.key == pygame.K_SPACE and pausing == True:
				pausing = False
				snakes = [[5,10]]
				prey = [randint(0, 19), randint(0, 19)]
				score = 0


		# Quit game
		if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					if (WIDTH - 20 < mouse_x < WIDTH - 10) and (10 < mouse_y < 20):
						pygame.quit()

	pygame.display.flip()

pygame.quit()