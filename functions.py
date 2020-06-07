'''
    functions

    Kris 18/5/20 - 20/5/20 
'''
from graphics import *
from datetime import *
from config import *

def init(): #initialise start of the game, all the enemies and the protagonist

    ##### IMPORTANT,   I want this info on gaps be in config, maybe we could make the numbers adaptable? (as in changes with window size) #####
     #       ^^  ^^  ^^  ^^  ^^  ^^  ^^  ^^  ^^  ^^  ^^  ^^  ^^
    # I want the gap between each enemy to be 30, but there should be space left over on the right, so that enemies can move over
    # so going from left to right: 30 block gap, put in 10 enemies, then add enemies until 270 blocks left
    # enemies should be 30 blocks from the top as well

    first_x, first_y = TOP_LEFT_enemy_x,TOP_LEFT_enemy_y       # x and y for the first enemy
    enemy1 = draw_enemy(first_x,first_y)
    enemy2 = draw_enemy(first_x+150,first_y)
    enemy3 = draw_enemy(first_x+300,first_y)
    enemy4 = draw_enemy(first_x+450,first_y)
    enemy5 = draw_enemy(first_x+600,first_y)
    enemy6 = draw_enemy(first_x+750,first_y)
    enemy7 = draw_enemy(first_x+900,first_y)
    enemy8 = draw_enemy(first_x+1050,first_y)
    enemy9 = draw_enemy(first_x+1200,first_y)

    second_y = first_y + 150
    enemy10 = draw_enemy(first_x,second_y)
    enemy11 = draw_enemy(first_x+150,second_y)
    enemy12 = draw_enemy(first_x+300,second_y)
    enemy13 = draw_enemy(first_x+450,second_y)
    enemy14 = draw_enemy(first_x+600,second_y)
    enemy15 = draw_enemy(first_x+750,second_y)
    enemy16 = draw_enemy(first_x+900,second_y)
    enemy17 = draw_enemy(first_x+1050,second_y)
    enemy18 = draw_enemy(first_x+1200,second_y)
    

    all_enemies = [enemy1,enemy2,enemy3,enemy4,enemy5,enemy6,enemy7,enemy8,enemy9,enemy10,enemy11,enemy12,enemy13,enemy14,enemy15,enemy16,enemy17,enemy18]

    protagonist = draw_protagonist(PROTAGONIST_STARTING_x,PROTAGONIST_STARTING_y) # this is the starting position for protagonist so far

    return all_enemies, protagonist

def draw_enemy(x,y):  # x,y is the middle of the enemy
    #scale factor of pixels are currently 1:12
    #enemies are 120x96 (10x8 pixels)
    output = []
    enemy = Polygon(Point(x,y+24),Point(x+24,y+24),Point(x+24,y+36),Point(x+12,y+36),Point(x+12,y+48),Point(x+24,y+48),Point(x+24,y+36),
    Point(x+36,y+36),Point(x+36,y+24),Point(x+48,y+24),Point(x+48,y+36),Point(x+60,y+36),Point(x+60,y),Point(x+48,y),Point(x+48,y-12),
    Point(x+36,y-12),Point(x+36,y-24),Point(x+24,y-24),Point(x+24,y-36),Point(x+36,y-36),Point(x+36,y-48),Point(x+24,y-48),Point(x+24,y-36),
    Point(x+12,y-36),Point(x+12,y-24),Point(x-12,y-24),Point(x-12,y-36),Point(x-24,y-36),Point(x-24,y-48),Point(x-36,y-48),Point(x-36,y-36),
    Point(x-24,y-36),Point(x-24,y-24),Point(x-36,y-24),Point(x-36,y-12),Point(x-48,y-12),Point(x-48,y),Point(x-60,y),Point(x-60,y+36),
    Point(x-48,y+36),Point(x-48,y+24),Point(x-36,y+24),Point(x-36,y+36),Point(x-24,y+36),Point(x-24,y+48),Point(x-12,y+48),Point(x-12,y+36),
    Point(x-24,y+36),Point(x-24,y+24))
    enemy.setFill("white")
    enemy.draw(window)
    left_eye = Rectangle(Point(x-24,y),Point(x-12,y-12))
    left_eye.setFill("black")
    left_eye.draw(window)
    right_eye = Rectangle(Point(x+24,y),Point(x+12,y-12))
    right_eye.setFill("black")
    right_eye.draw(window)
    
    output.append(enemy)
    output.append(left_eye)
    output.append(right_eye)
    return output

def draw_protagonist(x,y):          # x,y is middle bottom of protagonist
    #I will keep scale factor of pixels as 1:12 also
    #protagonist is 156x96 (13x8 pixels)
    x_shift_r = x+6     # adding this shifting bs because the centre of the protagonist cuts its middle gun in half, not lining up with pixels
    x_shift_l = x-6    
    protagonist = Polygon(Point(x_shift_r,y),Point(x_shift_r+72,y),Point(x_shift_r+72,y-48),Point(x_shift_r+60,y-48),Point(x_shift_r+60,y-60),
    Point(x_shift_r+12,y-60),Point(x_shift_r+12,y-84),Point(x_shift_r,y-84),Point(x_shift_r,y-96),Point(x_shift_l,y-96),Point(x_shift_l,y-84),Point(x_shift_l-12,y-84),
    Point(x_shift_l-12,y-60),Point(x_shift_l-60,y-60),Point(x_shift_l-60,y-48),Point(x_shift_l-72,y-48),Point(x_shift_l-72,y),Point(x_shift_r,y))
    protagonist.setFill("green")
    protagonist.draw(window)
    return protagonist           

def move_enemies(enemies_list,dx,dy):   # can be for any list of shapes actually, but enemies are the only things made up of multiple shapes
    for enemy in enemies_list:
        for shape in enemy:
            shape.move(dx,dy)

def shoot(protagonist):                                # spawns and draws your bullet
    all_points = protagonist.getPoints()            # extracting all points of protagonist
    
    protagonist_positions_x = []
    protagonist_positions_y = []
    for point in all_points:                        # iterating through these points
        protagonist_positions_x.append(point.getX())
        protagonist_positions_y.append(point.getY())            # collecting arrays for x and y coords of protagonist's points


    centre_of_protagonist = (max(protagonist_positions_x) + min(protagonist_positions_x))/2         
    top_of_protagonist = min(protagonist_positions_y)
    
    shot = Polygon(Point(centre_of_protagonist-3, top_of_protagonist - SHOT_LENGTH),Point(centre_of_protagonist+3,top_of_protagonist - SHOT_LENGTH), 
    Point(centre_of_protagonist+3,top_of_protagonist), Point(centre_of_protagonist-3,top_of_protagonist))
    shot.setFill("white")
    shot.draw(window)
    return shot

def move_shots(shots_list,dx,dy):                      #makes your bullet move
    for shot in shots_list:
        shot.move(dx,dy)

def WIN_condition(all_enemies):
    if all_enemies == []:
        message = Text(Point(WIDTH/2, HEIGHT/2), 'Goodjob!')
        message.setTextColor("white")
        message.setSize(20)
        message.draw(window)
        window.getMouse()
        window.close()
        return True

def GG_condition(all_enemies):                           #checks if you've lost yet
    y_coordinates = []
    all_points = []
    for enemy in all_enemies:                            # list of enemies
        all_points.append(enemy[0].getPoints())        #extracting all points
    for many_points in all_points:                    # so many points in their grouped lists
        for point in many_points:                     # now we're actually iterating through only points
            y_coordinates.append(point.getY())            # extracting Y coordinates of each point
    lowest_enemy = max(y_coordinates)
    if lowest_enemy > PROTAGONIST_STARTING_y - 96:               # refer to draw_enemies and draw_protagonist to see why I used constant 48 and 96, they're the tips of the shapes
        message = Text(Point(WIDTH/2, HEIGHT/2), 'oh no you lost')
        message.setTextColor("white")
        message.setSize(20)
        message.draw(window)
        window.getMouse()
        window.close()
        return 1

def dead_enemy(shots_list,enemies_list,enemy_that_died,shot,x,y):               # run when a enemy died, give me the list of all enemies, and the enemy that died, along with where it died
    print("enemy died at " + str(x) + "\t" + str(y))
    for enemy_body_parts in enemy_that_died:
        enemy_body_parts.undraw()
    enemies_list.remove(enemy_that_died)
    shot.undraw()
    shots_list.remove(shot)
    small_explosion(x,y)
    
    

def collision_with_a_question_mark(shots_list,enemies_list):
    counter = 0
    for shot in shots_list:
        for enemy in enemies_list:
                                    #enemy[0] refers to the main body of the enemy, enemy[1] and enemy[2] are it's eyes     
                                    # NOTE: enemies are 120 blocks wide (x) and 96 blocks tall, shots are 6 blocks wide and SHOT_LENGTH long
            bottom_left_shot = shot.getPoints()[0]
            if (bottom_left_shot.getX() > (enemy[0].getPoints()[0].getX() - 60)) and bottom_left_shot.getX() < enemy[0].getPoints()[0].getX() + 60 and bottom_left_shot.getY() < enemy[0].getPoints()[0].getY() + 48 and bottom_left_shot.getY() > enemy[0].getPoints()[0].getY() - 48:          
                dead_enemy(shots_list,enemies_list,enemy,shot,enemy[0].getPoints()[0].getX(),enemy[0].getPoints()[0].getY()-24)
                break

def small_explosion(x,y):
    #first boom
    boom1 = Rectangle(Point(x-8,y+8),Point(x+8,y-8))
    boom1.setFill("red")
    boom1.draw(window)

    explosion_points.append(Point(x,y))
    explosions.append(boom1)
    explosion_timings.append(datetime.now())

def big_explosion(x,y,index):
    #second boom
    explosions[index].undraw()

    boom2 = Polygon(Point(x-8,y+8),
    Point(x-8,y+24),Point(x+8,y+24),Point(x+8,y+8),Point(x-8,y+8),
    Point(x+24,y+8),Point(x+24,y-8),Point(x+8,y-8),Point(x+8,y+8),
    Point(x+8,y-24),Point(x-8,y-24),Point(x-8,y-8),Point(x+8,y-8),
    Point(x-24,y-8),Point(x-24,y+8),Point(x-8,y+8),Point(x-8,y-8),
    Point(x-8,y+8))
    boom2.setFill("red")
    explosions[index] = boom2
    boom2.draw(window)

    explosions[index] = boom2

def small_explosion2(x,y,index):
    #third boom
    explosions[index].undraw()

    boom3 = Rectangle(Point(x-8,y+8),Point(x+8,y-8))
    boom3.setFill("red")
    boom3.draw(window)

    explosions[index] = boom3





    
    




    
