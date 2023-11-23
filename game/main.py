import pygame
import sys
import random
import settings 
import ship

clock = pygame.time.Clock()
pygame.init()
set = settings.Settings()
width = set.getWindowWidth()
hight = set.getWindowHight()
screen = pygame.display.set_mode((width, hight))
pygame.display.set_caption("Space Game")
bg = pygame.image.load(set.getBackground())
icon = pygame.image.load(set.getIcon())
pygame.display.set_icon(icon)

player_ship = ship.Ship()
player = ship.Ship.getImage()

asteroid = pygame.image.load('images/asteroid.png')
star = pygame.image.load('images/star.png')
super_star = pygame.image.load('images/super_star.png')

player_x = set.getStartPlayerX()
player_y = set.getStartPlayerY()

asteroid_x = random.randint(70, 570)
asteroid_y = 0
asteroid_speed = 12

star_x = random.randint(70, 570)
star_y = 0
star_speed = 15

super_star_x = random.randint(70, 570)
super_star_y = 0
super_star_speed = 20

asteroid_list = []
star_list = []
super_star_list = []


bg_y = 0
bg_sound = pygame.mixer.Sound(set.getSound())
bg_sound.play(loops=100)
game_over_sound = pygame.mixer.Sound(set.getGameOverSound())
game_win_sound = pygame.mixer.Sound(set.getGameWinSound())

font15 = pygame.font.Font(set.getFont(), 15)
font40 = pygame.font.Font(set.getFont(), 40)


asteroid_timer = pygame.USEREVENT + 1
pygame.time.set_timer(asteroid_timer, 1000)

star_timer = pygame.USEREVENT + 2
pygame.time.set_timer(star_timer, 2000)

super_star_timer = pygame.USEREVENT + 3
pygame.time.set_timer(super_star_timer, random.randint(5000, 10000))

gameplay = True
clocktick = 12
running = True
while running:
    clock.tick(clocktick)
    screen.blit(bg, (0, bg_y))
    screen.blit(bg, (0, bg_y - set.getWindowHight()))
    bg_y += 2
    if bg_y == 480:
        bg_y = 0

    if gameplay:
        score_label = font15.render('Score:{}'.format(player_ship.getScore()), False, 'WHITE')
        screen.blit(score_label, (550,15))
        player_rect = player.get_rect(topleft=(player_x, player_y))
        
        if asteroid_list:
            for i, el in enumerate(asteroid_list):
                screen.blit(asteroid, el)
                el.y += asteroid_speed 
                if el.y > 1000:
                    asteroid_list.pop(i)
                if player_rect.colliderect(el):
                    player_ship.addHealth(-1)
                    if player_ship.getHealth() > 0:
                        asteroid_list.pop(i)
                    else:
                        gameplay = False
                        game_over_sound.play()
                        

        if star_list:
            for i, el in enumerate(star_list):
                screen.blit(star, el)
                el.y += star_speed 
                if el.y > 1000:
                    star_list.pop(i)
                if player_rect.colliderect(el):
                    star_list.pop(i)
                    player_ship.addScore(1)
                    print(player_ship.getScore())

        if super_star_list:
            for i, el in enumerate(super_star_list):
                screen.blit(super_star, el)
                el.y += super_star_speed 
                if el.y > 1000:
                    super_star_list.pop(i)
                if player_rect.colliderect(el):
                    super_star_list.pop(i)
                    player_ship.addScore(10)
                    print(player_ship.getScore())           

        if player_ship.getScore() >= 10:
            clocktick = (12+player_ship.getScore()//4)
        if player_ship.getScore() >= set.getWinPoints():
            gameplay = False
            game_win_sound.play()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 5:
            player_x -= player_ship.getSpeed()
        elif keys[pygame.K_RIGHT] and player_x < 580:
            player_x += player_ship.getSpeed()
        elif keys[pygame.K_UP] and player_y > 320:
            player_y -= player_ship.getSpeed()
        elif keys[pygame.K_DOWN] and player_y < 415:
            player_y += player_ship.getSpeed()
        
        screen.blit(player, (player_x, player_y))
    elif not gameplay and player_ship.getScore() < set.getWinPoints():
        screen.fill('BLACK')
        bg_sound.stop()
        game_over_label = font40.render('Game over', False, 'WHITE')
        final_score_label = font40.render('Your score: {}'.format(player_ship.getScore()), False, 'WHITE')
        restart_label = font40.render('Press space to restart', False, 'WHITE')
        screen.blit(game_over_label, (150, 200))
        screen.blit(final_score_label, (150, 250))
        screen.blit(restart_label, (150, 400))
        if (pygame.key.get_pressed()[pygame.K_SPACE]):
            gameplay = True
            clocktick = 12
            game_over_sound.stop()
            bg_sound.play(loops=100)
            player_ship = ship.Ship()
            player_x = set.getStartPlayerX()
            player_y = set.getStartPlayerY()
            asteroid_list.clear()
            star_list.clear()
            super_star_list.clear()
    else:
        screen.fill('WHITE')
        bg_sound.stop()
        game_over_label = font40.render('You won!', False, 'BLACK')
        score_label = font40.render('You reached 50 points :)', False, 'BLACK')
        restart_label = font40.render('Press space to restart', False, 'BLACK')
        screen.blit(game_over_label, set.getFirstLabelCoords())
        screen.blit(score_label, set.getSecondLabelCoords())
        screen.blit(restart_label, set.getThirdLabelCoords())
        if (pygame.key.get_pressed()[pygame.K_SPACE]):
            gameplay = True
            clocktick = 12
            game_win_sound.stop()
            bg_sound.play(loops=100)
            player_ship = ship.Ship()
            player_x = set.getStartPlayerX()
            player_y = set.getStartPlayerY()
            asteroid_list.clear()
            star_list.clear()
            super_star_list.clear()

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()  
        if event.type == asteroid_timer:
            asteroid_x = random.randint(0, 570)   
            asteroid_y = random.randint(70, 90)
            asteroid_list.append(asteroid.get_rect(topleft=(asteroid_x, -asteroid_y)))
        if event.type == star_timer:
            star_x = random.randint(0, 570)
            star_y = random.randint(70, 90)
            star_list.append(star.get_rect(topleft=(star_x, -star_y)))
        if event.type == super_star_timer:
            super_star_x = random.randint(0, 570)   
            super_star_y = random.randint(70, 90)
            super_star_list.append(super_star.get_rect(topleft=(super_star_x, -super_star_y)))                    
    pygame.display.update()