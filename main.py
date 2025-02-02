# Write your code here :-)
import pgzrun
import random
from pgzhelper import *
from dino import Dino
from enemy import Enemy

#screen dimensions
WIDTH =800
HEIGHT = 600






velocity =0  # How fast our dino moves in the up/down direction
gravity=1 # Gravity will change our velocity.The bigger the number , the more pull towards the ground



#create game variables
score=0
game_over=False
game_success=False
deathsound=False
game_state = "start"




# Colours define
black = (0,0,0)
brown = (71 ,34,18)
red=(212,47,47)
white=(255,255,255)
green=(31, 173, 98)
blue=(31, 76, 173)
darkgreen=(31, 173, 48 )
grey=(104, 106, 108)
green= (62, 142, 65)
softgreen=(161, 209, 163)
softblue=(137, 207, 240)
yellow= (246, 208, 47)


#create button
start_button = Actor('start', (400, 250))
sound_off = Actor('soundoff', (400, 350))
exit_button = Actor('exit', (400, 450))
retry_button = Actor('retry', (400, 400))


#dino Game char
dino = Dino() #create instance dino class
enemies = [Enemy('bee', 3,"bee"), Enemy('bomb', 4,"bomb")] #create instance enemy class

#background images
#cloud
cloud = Actor('cloud1')
cloud.x = 700
cloud.y = 120
#cloud2
cloud2 = Actor('cloud2')
cloud2.x = 400
cloud2.y = 120
#cloud3
cloud3 = Actor('cloud3')
cloud3.x = 100
cloud3.y = 120

#Obstacles
obstacles= [] #create an empty list that will hold the cactus obstacles
obstacles_timeout =0 # this number is a counter to ensure cactus appear in our game - but not all at once


animation_counter = 0
music.play('music') #game mucis play


def update(): # each frame draw in update function
    global score,obstacles_timeout,game_over,deathsound,game_success,enemies # define variables

    if game_state == "play": # only in play mode the code below works
        dino.update(keyboard)  # Send keyboard input to dino.update
        for enemy in enemies:  #turns on the list of enemies
                enemy.update() #call update function for enemy class
                if dino.collides_with(enemy.actor) and enemy.name=="bee": #when dino and enemy  collide and enemy is bee
                    score +=3
                    enemies.remove(enemy) #score only goes up once
                if dino.collides_with(enemy.actor) and enemy.name=="bomb": #when dino and enemy  collide and enemy is bomb
                    score -=1
                    enemies.remove(enemy) #score only goes up once
                if score <0: #if the score is less than zero , game over will be true and game will finished
                   game_over=True
                   if deathsound == False :
                      sounds.gameover.play()
                      deathsound=True




        #cactus
            #Each time the frames are refreshed in our game , add 1 to the counter
        obstacles_timeout =obstacles_timeout+1
            # when the counter gets to a random choice between 60 and 7000 , put a cactus into the game
        if obstacles_timeout > random.randint(60,7000) :
                cactus=Actor('cactus')
                cactus.scale=1.5
                cactus.x=860
                cactus.y=500
                if game_over == False:
                    obstacles.append(cactus)#puts a copy of some cactus into the obstacles list
                    obstacles_timeout=0 # reset the counter  back to zero

            #move the cactus across the screen
        for cactus in obstacles  : # loop through the obstacles list
                cactus.x -=8  #move the cactus across the screen at a speed of 8
                #If the cactus move off the left side of the screen , remove them from the obstacleslist and get 1 point
                if cactus.x < -50:
                    obstacles.remove(cactus)
                    score+=1
        if dino.collides_list_with(obstacles)!= -1 : # collidelist will return -1 if there has been no collision
                  game_over=True
                  obstacles.remove(cactus) # Delete the spikes currently on the screen
                  if deathsound == False :
                    sounds.gameover.play()
                  deathsound=True

    if score == 10 : #the game will end successfully when the score is 10
       game_success=True


def draw():
    screen.clear()
    if game_state == "start": # if game state  is start only draw first screen
        draw_first_screen()
    else:
        draw_game() # draw game screen

def draw_first_screen():

    screen.fill(softgreen)
    screen.draw.text("Dino Runner", center=(WIDTH // 2, 150), fontsize=50, color=grey)


    start_button.draw()
    sound_off.draw()
    exit_button.draw()



def draw_game():
    screen.clear()
    screen.draw.filled_rect(Rect(0,0,800,500),(softblue))#sky
    screen.draw.filled_rect(Rect(0,500,800,600),(yellow)) #ground

    if game_success: # finish page will draw success mode
        screen.draw.text('Game Success',centerx=400 ,centery=200 ,color=(black),fontsize=80)
        screen.draw.text('Score: '+str(score),centerx=400 ,centery=300 ,color=(white),fontsize=60)
        music.stop()
    elif game_over:  # finish page will draw unsuccess mode
        screen.draw.text('Game Over',centerx=400 ,centery=200 ,color=(black),fontsize=80)
        screen.draw.text('Score: '+str(score),centerx=400 ,centery=300 ,color=(white),fontsize=60)
        retry_button.draw()
        music.stop()
    else: # second page play mode page draw
        dino.draw()
        cloud.draw()
        cloud2.draw()
        cloud3.draw()
        screen.draw.text('Score: '+ str(score),(20,20),color=(darkgreen),fontsize=30)
        for enemy in enemies:
            enemy.draw()
        for cactus in obstacles :
            cactus.draw()






def on_mouse_down(pos):
    #will come to this method when any button is clicked
    global velocity,score,obstacles_timeout,game_over,deathsound,game_success,game_state,obstacles,obstaclesbomb

    if game_state == "start" and start_button.collidepoint(pos):
        game_state = "play"  # Oyunu başlat

    if sound_off.collidepoint(pos):
         music.stop()

    if exit_button.collidepoint(pos):
         sys.exit()

    if retry_button.collidepoint(pos):
        #reset the values of the variables to return to start mode, reset the game to start modescore = 0
        velocity = 0
        game_over = False
        game_success = False
        deathsound = False
        obstacles.clear()
        dino.x = 100
        dino.y = 470
        game_state = "start"




pgzrun.go()



