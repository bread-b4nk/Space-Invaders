'''
    main shit

    Kris 18/5/20 - 20/5/20 (yeah that's right it's a non-american date you fuckers)
'''
from graphics import *  # http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/graphics.html - https://www.pas.rochester.edu/~rsarkis/csc161/_static/lectures/Objects%20%26%20Graphics.pdf
from time import *
from functions import *
from config import *
from datetime import *



def main():
    
    #window.setCoords(0,0,200,150)
    
    
    # head = Circle(Point(40,100), 25) # set center and radius
  
    # eye2 = Line(Point(45, 105), Point(55, 105)) # set endpoints
    # eye2.setWidth(3)
    # eye2.draw(window)

    all_cunts, protagonist = init()

    message = Text(Point(WIDTH/2, HEIGHT/2), 'Click me to start.')
    message.setTextColor("white")
    message.setSize(20)
    message.draw(window)
    window.getMouse()
    message.undraw()

    
    time_temp_cunt = datetime.now()      # used to detect when to move the cunts
    time_temp_shot = datetime.now()     # used to detect when you can shoot again
    time_temp_shot_move = datetime.now()   # used to detect when to move the shot
    cunt_move_count = 0                  # counter to ensure cunts don't yeet off the screen
    
    while True:
        
        ### CONTROLS
        user_input = window.checkKey()
        if user_input == "Up" or user_input == "w" and (datetime.now() - time_temp_shot).microseconds > SHOT_COOLDOWN:
            #print("ping: shoot")
            shots.append(shoot(protagonist))
            time_temp_shot = datetime.now()     # used to detect when you can shoot again
        if user_input == "Right" or user_input == "d":
            #print("ping: right")
            protagonist.move(PROTAGONIST_SHIFT,0)
        if user_input == "Left" or user_input == "a":
            #print("ping: left")
            protagonist.move(-PROTAGONIST_SHIFT,0)
        
            
            
        ### CUNT MOVEMENT
        if (datetime.now() - time_temp_cunt).microseconds > CUNT_CYCLE:       # so everytime CYCLE amount of microseconds has passed, the cunts will shift
            cunt_move_count += 1
            if (cunt_move_count % SHIFTS_PER_LEVEL == 0):                     # whenever count reaches a multiple of 7 (SHIFTS_PER_LEVEL) it will shift down instead
                move_cunts(all_cunts,0,CUNT_SHIFT)
            elif (int(cunt_move_count/SHIFTS_PER_LEVEL) % 2) == 0:            # a way of ensuring it moves right, then left
                move_cunts(all_cunts,CUNT_SHIFT,0)
            else:
                move_cunts(all_cunts,-CUNT_SHIFT,0)
            time_temp_cunt = datetime.now()
        
        ### SHOT REMOVAL AND MOVEMENT
        if shots != []:             
            points = []
            #print("ping: shot detected")
            if (datetime.now() - time_temp_shot_move).microseconds > SHOT_MOVEMENT_COOLDOWN:
                move_shots(shots,0,-SHOT_SHIFT)
                time_temp_shot_move = datetime.now()
            for each_shot in shots:
                points.append(each_shot.getPoints())
                if each_shot.getPoints()[1].getY() < -60:
                    each_shot.undraw()
                    shots.remove(each_shot)
            

        ### CHECK EXPLOSION
        if explosions != []:
            for index in range(0,len(explosions)):
                if (datetime.now() - explosion_timings[index]).microseconds > BOOM_DELAY*5:
                    explosions[index].undraw()
                    #print("undrawn")

                    explosion_timings.remove(explosion_timings[index])
                    explosions.remove(explosions[index])
                    explosion_points.remove(explosion_points[index])

                elif (datetime.now() - explosion_timings[index]).microseconds > BOOM_DELAY*4:
                    small_explosion2(explosion_points[index].getX(),explosion_points[index].getY(),index)
                
                elif (datetime.now() - explosion_timings[index]).microseconds > BOOM_DELAY*3:
                    big_explosion(explosion_points[index].getX(),explosion_points[index].getY(),index)
            
                elif (datetime.now() - explosion_timings[index]).microseconds > BOOM_DELAY*2:
                    small_explosion2(explosion_points[index].getX(),explosion_points[index].getY(),index)

                elif (datetime.now() - explosion_timings[index]).microseconds > BOOM_DELAY:
                    big_explosion(explosion_points[index].getX(),explosion_points[index].getY(),index)
                
        
        collision_with_a_question_mark(shots,all_cunts)
        if WIN_condition(all_cunts):
            break
        if GG_condition(all_cunts):
            break

        
        
  
    
    



    window.close()


main()