# Write your code here :-)
import pgzrun
import random
from pgzhelper import *


WIDTH =800
HEIGHT = 600


music.play('music')



velocity =0  # How fast our dino moves in the up/down direction
gravity=1 # Gravity will change our velocity.The bigger the number , the more pull towards the ground



#create game variables
score=0
game_over=False
game_success=False
deathsound=False
game_state = "start"


# Colours
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



start_button = Actor('start', (400, 250))
sound_off = Actor('soundoff', (400, 350))
exit_button = Actor('exit', (400, 450))
retry_button = Actor('retry', (400, 400))


#dino
dino = Actor('idle1')
dino.x=100
dino.y=470
dino.images=['run1','run2','run3','run4','run5']
dino.fps=5

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



#Bee
bee =Actor('bee')
bee.x=400
bee.y=200
bee.images= ['bee','bee_dead', 'bee_fly']
bee.fps =10


#Bomb
bomb =Actor('bomb')
bomb.x=400
bomb.y=300
bomb.images= ['bomb']
bomb.fps =10




#Obstacles
obstacles= [] #create an empty list that will hold the cactus obstacles
obstacles_timeout =0 # this number is a counter to ensure cactus appear in our game - but not all at once

#Obstacles
obstaclesbomb= [] #create an empty list that will hold the cactus obstacles
obstacles_timeout_bomb =0 # this number is a counter to ensure cactus appear in our game - but not all at once

animation_counter = 0


def update():
    global velocity,score,obstacles_timeout,game_over,deathsound,game_success,obstaclesbomb,obstacles_timeout_bomb,animation_counter


    if game_state != "start":
        animation_counter += 1
        if animation_counter % 5 == 0:  # Each 5 frame is changed , than slowly
           dino.next_image()

        bee.animate()
        bee.x=bee.x-3
        if bee.x < -50 :
            bee.x=random.randint(0,800)
            bee.y=random.randint(100,250)

        bomb.animate()
        bomb.x=bomb.x-3
        if bomb.x < -50 :
            bomb.x=random.randint(0,800)
            bomb.y=random.randint(100,250)


        if keyboard.up and dino.y==470 :
            velocity=-18
        dino.y=dino.y+velocity
        velocity= velocity+gravity

        #stop the dino falling of the screen
        if dino.y > 470:
            velocity=0
            dino.y=470


        #when the dino and bee collide
        if dino.colliderect(bee):
           sounds.collect.play()
           bee.x=random.randint(900,5000)
           bee.y=random.randint(250,350)
           score +=5

        #when the dino and bomb collide
        if dino.colliderect(bomb):
           sounds.collect.play()
           bomb.x=random.randint(900,5000)
           bomb.y=random.randint(250,350)
           score -=1
        if score < 0:
           game_over=True


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


        if dino.collidelist(obstacles) != -1 : # collidelist will return -1 if there has been no collision
              game_over=True
              obstacles.remove(cactus) # Delete the spikes currently on the screen
              if deathsound == False :
                sounds.gameover.play()
              deathsound=True

        if score == 20 :
            game_success=True


def draw():
    screen.clear()
    if game_state == "start":
        draw_first_screen()
    else:
        draw_game()

def draw_first_screen():

    screen.fill(softgreen)
    screen.draw.text("Dino Runner", center=(WIDTH // 2, 150), fontsize=50, color=grey)


    start_button.draw()
    sound_off.draw()
    exit_button.draw()



def draw_game():
    screen.draw.filled_rect(Rect(0,0,800,500),(softblue))#sky
    screen.draw.filled_rect(Rect(0,500,800,600),(yellow)) #ground

    if game_success:
        screen.draw.text('Game Success',centerx=400 ,centery=200 ,color=(black),fontsize=80)
        screen.draw.text('Score: '+str(score),centerx=400 ,centery=300 ,color=(white),fontsize=60)
        music.stop()
    elif game_over:
        screen.draw.text('Game Over',centerx=400 ,centery=200 ,color=(black),fontsize=80)
        screen.draw.text('Score: '+str(score),centerx=400 ,centery=300 ,color=(white),fontsize=60)
        retry_button.draw()
        music.stop()
    else:
        dino.draw()
        cloud.draw()
        cloud2.draw()
        cloud3.draw()
        bee.draw()
        bomb.draw()
        screen.draw.text('Score: '+ str(score),(20,20),color=(darkgreen),fontsize=30)
        for cactus in obstacles :
            cactus.draw()




def on_mouse_down(pos):

    global velocity,score,obstacles_timeout,game_over,deathsound,game_success,game_state,obstacles,obstaclesbomb

    print("Tıklama algılandı:", pos)


    if game_state == "start" and start_button.collidepoint(pos):
        game_state = "play"  # Oyunu başlat
    if sound_off.collidepoint(pos):
         music.stop()
    if exit_button.collidepoint(pos):
         sys.exit()
    if retry_button.collidepoint(pos):
        print("Tıklama algılandı:", pos)
        score = 0
        velocity = 0
        game_over = False
        game_success = False
        deathsound = False
        obstacles.clear()
        obstaclesbomb.clear()
        dino.x = 100
        dino.y = 470
        game_state = "start"
        print("mevcut", game_state)

pgzrun.go()



