# imports
from typing import List
import pygame, sys, os, time

# setup
pygame.init()  # Initialize pygame
fps = 90  # frame rate
WINDOW_SIZE = (1400, 870)
pygame.display.set_caption('Commander Bär')  # Title
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)  # create screen
icon = pygame.image.load(os.path.join('images', 'wooden_door.png'))
stone = pygame.image.load(os.path.join('images', 'stone.png'))
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
block_picture_1 = pygame.image.load(os.path.join('images', 'block.png'))
block_picture_2 = pygame.image.load(os.path.join('images', 'dirt_clean.png'))
cloud = pygame.image.load(os.path.join('images', 'cloud.png'))

# variables
counting_cunt = 0
moving_right = False
moving_left = False
moving_up = False
moving_down = False
using_stuff = False
player_image = pygame.image.load(os.path.join('images', 'nostep.png'))
player_location = [600, 150]
player_y_momentum = 0
wanna_quit = False
scroll = [0, 0]
hm = 1
hmm = 1
door_c = 0
door_c_2 = 0

# connect player rect with player image
player_rect = pygame.Rect(player_location[0], player_location[1], player_image.get_width(), player_image.get_height())
print(player_rect)

contact_left_right = pygame.Rect(player_location[0], player_location[1]-10, player_image.get_width(), player_image.get_height()-10)
print(contact_left_right)

## Rectangles (blocks) 
# Rectangle created (at coordinates 550 and 520, with the size of 99*87)
b_1 = pygame.Rect(550, 420, 99, 87)
# walking_block = [abc]

# Rectangle, created from image
# load image and store it in variable
b_2 = block_picture_1
# call rect method on image to get width and height + determine position of rectangle
b_2_rect = b_2.get_rect(x=(300), y=(300))
# set location variable for blit
b_2_location = b_2_rect

# cloud
cloud_rect = cloud.get_rect(x=player_location[0]-999, y=0)
cloud_location = [player_location[0]-999, 0]

# tileset Nr.1
def load_map(path):
    f = open(path + '.txt', 'r')
    data = f.read()
    f.close()
    data = data.split('\n')
    lol = []
    for row in data:
        lol.append(list(row))
    return lol
game_map = load_map('map')


# tileset Nr. 2
def load_second_map(path):
    f = open(path + '.txt', 'r')
    data_2 = f.read()
    f.close()
    data_2 = data_2.split('\n')
    game_map_second = []
    for row in data_2:
        game_map_second.append(list(row))
    return game_map_second
game_map_second = load_map('map_2')

TILE_SIZE_width = b_2.get_width()
TILE_SIZE_height = b_2.get_height()



# Mainloop
while True:   
    
    #How movement works:#
    #The Rect object has several virtual attributes which can be used to move and align the rect:
    ## x,y
    ## top, left, bottom, right
    ## topleft, bottomleft, topright, bottomright
    ## midtop, midleft, midbottom, midright
    ## center, centerx, centery
    ## size, width, height
    ## w,h
    

    player_rect.x = player_location[0]
    player_rect.y = player_location[1]

    contact_left_right.x = player_location[0]
    contact_left_right.y = player_location[1]

    #1. Everything Background
    # screen.blit(background, (0,0))  # blit background at pos 0,0
    bg_switch = False
    if bg_switch == False:
        screen.fill((255, 255, 255))  # fills gap, when hero moves and there is no background enabled

    #cloud
    screen.blit(cloud, cloud_location)
    cloud_location[0] += 1
    if cloud_location[0] == 1400:
        cloud_location[0] = -150

    ######## T I L E S #################

    # M A P  Nr. 1
    y = 0
    if door_c == 0:
        for listö in game_map:
            x = -25
            for tile in listö:
                if tile == '1':
                    screen.blit(block_picture_2, (x * TILE_SIZE_height + scroll[0], y * TILE_SIZE_height + scroll[1]))
                    boden_rect = block_picture_2.get_rect(x=x * TILE_SIZE_height + scroll[0], y=y * TILE_SIZE_height + scroll[1])
                    if player_rect.colliderect(boden_rect):
                        player_location[1] = boden_rect.top - 138
                    if contact_left_right.colliderect(boden_rect) and moving_left == True:
                        print('contact')
                        moving_left = False
                        scroll[0] -= 5
                    if contact_left_right.colliderect(boden_rect) and moving_right == True:
                        print('contact')
                        moving_right = False
                        scroll[0] += 5

                if tile == '2':
                    screen.blit(b_2, (x * TILE_SIZE_height + scroll[0], y * TILE_SIZE_height + scroll[1]))
                    boden_rect = block_picture_1.get_rect(x=x * TILE_SIZE_height + scroll[0], y=y * TILE_SIZE_height + scroll[1])
                    if player_rect.colliderect(boden_rect):
                        player_location[1] = boden_rect.top - 138

                    if contact_left_right.colliderect(boden_rect) and moving_left == True:
                        print('contact')
                        moving_left = False
                        scroll[0] -= 5

                    if contact_left_right.colliderect(boden_rect) and moving_right == True:
                        print('contact')
                        moving_right = False
                        scroll[0] += 5

                # entering a house
                if tile == '3':
                    screen.blit(icon, (x * TILE_SIZE_height + scroll[0], y * TILE_SIZE_height + scroll[1]))
                    icon_rect = icon.get_rect(x=x * TILE_SIZE_height + scroll[0], y=y * TILE_SIZE_height + scroll[1])

                    ## D O O R S
                    if player_rect.colliderect(icon_rect) and using_stuff == True:
                        door_c += 1
                        print(door_c)
                x += 1
            y += 1

    elif door_c > 0:
        for listö in game_map_second:
            x = -25
            for tile in listö:
                if tile == '1':
                    screen.blit(block_picture_2, (x * TILE_SIZE_height + scroll[0], y * TILE_SIZE_height + scroll[1]))
                    boden_rect = block_picture_2.get_rect(x=x * TILE_SIZE_height + scroll[0], y=y * TILE_SIZE_height + scroll[1])
                    if player_rect.colliderect(boden_rect):
                        player_location[1] = boden_rect.top - 138
                    if contact_left_right.colliderect(boden_rect) and moving_left == True:
                        print('contact')
                        moving_left = False
                        scroll[0] -= 5
                    if contact_left_right.colliderect(boden_rect) and moving_right == True:
                        print('contact')
                        moving_right = False
                        scroll[0] += 5

                if tile == '2':
                    screen.blit(b_2, (x * TILE_SIZE_height + scroll[0], y * TILE_SIZE_height + scroll[1]))
                    boden_rect = block_picture_1.get_rect(x=x * TILE_SIZE_height + scroll[0],
                                                          y=y * TILE_SIZE_height + scroll[1])
                    if player_rect.colliderect(boden_rect):
                        player_location[1] = boden_rect.top - 138

                    if contact_left_right.colliderect(boden_rect) and moving_left == True:
                        print('contact')
                        moving_left = False
                        scroll[0] -= 5

                    if contact_left_right.colliderect(boden_rect) and moving_right == True:
                        print('contact')
                        moving_right = False
                        scroll[0] += 5

                # entering a house
                if tile == '3':
                    screen.blit(icon, (x * TILE_SIZE_height + scroll[0], y * TILE_SIZE_height + scroll[1]))
                    icon_rect_2 = icon.get_rect(x=x * TILE_SIZE_height + scroll[0], y=y * TILE_SIZE_height + scroll[1])
                    ## D O O R S
                    if player_rect.colliderect(icon_rect_2) and using_stuff == True:
                        door_c = 0
                        print(door_c)
                x += 1
            y += 1


    # if player_location[1] > 550:
    #     player_location[1] = 550

    # scrolling
    if moving_left is True:
        scroll[0] += 4

        # moving animation walking left
        hmm += 1
        if hmm > 15:
            player_image = pygame.image.load(os.path.join('images', 'running_2.png'))
        if hmm > 30:
            player_image = pygame.image.load(os.path.join('images', 'nostep_2.png'))
            hmm = 1
        if moving_left == False:
            hmm = 1
            player_image = pygame.image.load(os.path.join('images', 'nostep_2.png'))

    # moving to the right
    if moving_right is True:
        scroll[0] -= 4

        # moving animation walking left
        hm += 1
        if hm > 15:
            player_image = pygame.image.load(os.path.join('images', 'running_1.png'))
        if hm > 30:
            player_image = pygame.image.load(os.path.join('images', 'nostep.png'))
            hm = 1
        if moving_right == False:
            hm = 1

    # if player_location[1] > 800:
    #     player_location[1] = 500

    #3.1 LOAD player into the game
    screen.blit(player_image, player_location)


    # "Jumping" Mechanic
    mup = 1
    for i in range(10):
        mup += 2
        # print(mup)

    if moving_up == True and mup < 25:
        player_location[1] -= 10
        if player_location[1] < 300:
            moving_up = False
            player_location[1] += 10
        if mup == 25:
            moving_up = False

    # gravity
    if moving_up == False:
        player_location[1] += 7

    #4. Everything EVENTS
    # event definitions
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if wanna_quit == True:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
             # player_image = pygame.image.load(os.path.join('images', 'wizard.png'))
             if event.key == pygame.K_w:
                 moving_up = True
             if event.key == pygame.K_s:
                 moving_down = True
             if event.key == pygame.K_a:
                 moving_left = True
             if event.key == pygame.K_ESCAPE:
                 wanna_quit = True
             if event.key == pygame.K_d:
                moving_right = True
             if event.key == pygame.K_f:
                 using_stuff = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_f:
                using_stuff = False
            if event.key == pygame.K_w:
                moving_up = False
            if event.key == pygame.K_s:
                moving_down = False
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
    pygame.display.update()  # update display
    clock.tick(fps) #set refreshrate at 60 fps