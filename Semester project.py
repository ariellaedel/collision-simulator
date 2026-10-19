#I hereby certify that this program is solely the result of my own work and is in compliance with the Academic Integrity policy of the course syllabus and the academic integrity policy of the CS department.

import Draw
import time

#active=-1 makes sure that all boxes remain white until they are clicked
def drawParameterBoxes(parameters, active=-1):
    #draws menu screen- labels, boxes, values
    Draw.clear()
    Draw.setBackground(Draw.LIGHT_GRAY)
    
    for i in range(len(parameters)):
        label, x, y, w, h, low, high, value = parameters[i]
        
        # label above each box
        Draw.setColor(Draw.BLACK)
        Draw.setFontSize(18)
        Draw.string(label, x, y-30)
        
        #min and max 
        gray = Draw.color(100, 100, 100)
        if label != " ":
            Draw.setFontSize(12)
            Draw.setColor(gray)
            instruction = "Min: " + str(low) + " Max: " + str(high)
            Draw.string(instruction, x, y + h)
            
        # box color
        # If this is the box user is typing in-- make it a different color
        green = Draw.color(208, 240, 192)
        if i == active:
            Draw.setColor(green)
        else:
            Draw.setColor(Draw.WHITE)
            
        #input box
        Draw.filledRect(x, y, w, h)
        Draw.setColor(Draw.BLACK)
        Draw.rect(x, y, w, h)
        
        #draw current text value
        if value != "":
            Draw.setFontSize(18)
            Draw.setColor(Draw.BLACK)
            Draw.string(str(value), x + 10, y + 8)     
    Draw.show()
    
def getBoxNumber(click_x, click_y, parameters):
    #checks if the mouse clicks are inside any boxes
    for i in range(len(parameters)):
        p = parameters[i]
        x, y, w, h = p[1], p[2], p[3], p[4]
        
        #was the click between right/left and top/bottom? 
        if x <= click_x and click_x <= x + w and \
        y <= click_y and click_y <= y + h:
            return i
        
    #didnt find a box--ignore the click    
    return -1 

def getNumber(box, parameters):
    #input from keyboard when box is selected
    ans = parameters[box][7] 
    
    #allows program to make sure the numbers put in are between low and high
    low, high = parameters[box][5], parameters[box][6] 
    
    while True:
        drawParameterBoxes(parameters, box) 
            
        if Draw.hasNextKeyTyped(): 
            key = Draw.nextKeyTyped()
            if key.isdigit():
                tempans = ans + key
                
                #check if number exceeds high, if it does, 
                #dont update or appear in the box
                if float(tempans) <= high:
                    ans = tempans
                    
            elif key == "BackSpace" and len(ans) > 0:
                ans = ans[:-1]
                
            elif key == "Return":
                if ans != "": 
                    num = int(ans) 
                    if low <= num and num <= high:
                        return num    
                else: return None 
                
        #put ans into the string of the list 
        parameters[box][7] = ans 

def getParameters(parameters):
    #keep track of values
    results = [None] * 6  
    
    while True:
        #-1 to show nothing should be highlighted
        drawParameterBoxes(parameters, -1) 
        if Draw.mousePressed():
            
            #where is the mouse clicking
            mx, my = Draw.mouseX(), Draw.mouseY() 
            
            #which box if any was clicked?
            box = getBoxNumber(mx, my, parameters) 
            
            #is the clicked box one of the paramters
            if 0 <= box <= 5:  
                
                #store the result
                value = getNumber(box, parameters) 
                
                #only continue if the user has entered a number
                if value is not None:  
                    # Update our list and the display text
                    #store it for the physics math
                    results[box] = value 
                    
                    #put it in the list to display on the screen
                    parameters[box][7] = str(value) 
            #GO
            elif box == 6:  
                # check if all boxes have text in them
                all_filled = True
                for i in range(6):
                    
                    #make sure there is a value in every string to be displayed
                    if parameters[i][7] == "": 
                        all_filled = False
                        
                if all_filled:
                    # Convert text to actual numbers
                    m1 = int(parameters[0][7])
                    v1 = int(parameters[1][7])
                    m2 = int(parameters[2][7])
                    v2 = int(parameters[3][7])
                    
                    # /10 makes it a decimal 
                    e  = float(parameters[4][7]) / 10.0 
                    f  = float(parameters[5][7]) / 10.0
                    
                    if v2 > 0:
                        #all m2 become negative so it always 
                        #starts by going towards m1
                        v2 = v2 * -1  
                        
                    elif v2 == 0:
                        # Give it a little nudge if they typed 0
                        v2 = -10.0 
                        
                    #Return everything to main()
                    return [m1, v1, m2, v2, e, f]
                
                #warning if not everything is filled 
                else:
                    Draw.setColor(Draw.RED)
                    Draw.string("Please fill in all boxes", 220, 250)
                    
                    #display warning for a few seconds 
                    Draw.show(1000) 

def drawboard(x1, x2, v1, v2, m1, m2, t, radius, e, f):
    purple, pink = Draw.color(110, 110, 226), Draw.color(204, 0, 204)
    Draw.clear()
    Draw.setBackground(Draw.LIGHT_GRAY)  
    
    Draw.setColor(Draw.DARK_GRAY)
    Draw.filledRect(0, 450, 1200, 150)
    Draw.setColor(Draw.BLACK)
    Draw.line(0, 450, 1200, 450)
    
    #ball 1
    Draw.setColor(purple)   
    Draw.filledOval(x1, 450-radius, radius, radius)
    
    #ball 2
    Draw.setColor(pink)
    Draw.filledOval(x2, 450-radius, radius, radius)
    
    #strings on display
    Draw.setColor(Draw.BLACK)
    Draw.setFontSize(20)
    Draw.string("Time: "+ str(round(t, 2))+ "s", 40, 20)
    Draw.string("v1: " + str(round(v1, 1)), 20, 50)
    Draw.string("m1: " + str(m1) + "kg", 20, 75)
    Draw.string("v2: " + str(round(v2, 1)), 220, 50)
    Draw.string("m2: " + str(m2) + "kg", 220, 75)
    Draw.string("Elasticity: " + str(e), 420, 50)
    Draw.string("Friction: " + str(f), 420, 75)    
    Draw.show()
    
def runExperiment(m1, v1, m2, v2, e, f):
    #fixed position to start
    x1, x2 = 200.0, 700.0
    radius = 100
    t = 0.0
    lastTime = time.time()
    
    while True:
        #time at the start
        currentTime = time.time()
        
        #time its been
        dt = currentTime - lastTime 
        
        #update last time so it can start the loop again
        lastTime = currentTime 
        t += dt
        
        #Physics:
        #calculate friction and take that away from the velocity 
        v1 -= (v1 * f * dt)
        v2 -= (v2 * f * dt)
        
        #based on current velocity and time delta, calculate position change
        x1 += v1 * dt
        x2 += v2 * dt
        
        #Ball collision
        #if the distance between the balls is less then radius:
        if abs(x1 - x2) <= radius:
            
            #Inelastic or elastic collision using e 
            v1f = ((m1 - e * m2) * v1 + (1 + e) * m2 * v2) / (m1 + m2)
            v2f = ((m2 - e * m1) * v2 + (1 + e) * m1 * v1) / (m1 + m2)
            v1, v2 = v1f, v2f
            
            #separate the balls so they dont get stuck together 
            if x1 < x2: 
                x1 -= 2 
                x2 += 2
            else: 
                x1 += 2 
                x2 -= 2
            
        #Draw the board
        drawboard(x1, x2, v1, v2, m1, m2, t, radius, e, f)
        
        #one of the balls hits the end of the canvas
        hitWall= (x1<= 0 or x1 >=1000-radius or x2 <= 0 or x2 >= 1000-radius)
    
        #one of the balls velocity becomes 0 
        stopped= (abs(v1) < 0.2 and abs(v2) < 0.2 and t > 2.0) 
        
        #if any of the above conditions are met stop the simulation
        if hitWall or stopped: 
            Draw.setColor(Draw.RED)
            Draw.string("SIMULATION FINISHED - Click to return", 350, 200)
            Draw.show()
            
            # pause the code and wait for the user to click
            while not Draw.mousePressed(): pass
                    
            # Wait for the user to release the click
            while Draw.mousePressed(): pass   
                
            return # Exit to menu

def main():
    #[label, x-position, y-position, width, height, min value, 
    #max value, current-text]
    parameters = [["Mass 1", 50, 100, 100, 30, 1, 100, ""], 
                 ["Velocity 1", 50, 200, 100, 30, 0, 100, ""],
                 ["Mass 2", 250, 100, 100, 30, 1, 100, ""],
                 ["Velocity 2", 250, 200, 100, 30, 0, 100, ""],
                 ["Elasticity", 450, 100, 100, 30, 0.0, 10.0, ""],
                 ["Friction", 450, 200, 100, 30, 0.0, 5.0, ""],
                 [" ", 250, 350, 100, 50, 0, 0, "GO"]]
    
    Draw.setCanvasSize(1000, 600) 
    while True:
        #get the list of numbers from the menu
        data = getParameters(parameters)
        
        # This takes the 6 items in the list and gives them names in order
        m1, v1, m2, v2, e, f = data
        
        # start the experiment using those names
        runExperiment(m1, v1, m2, v2, e, f)
main() 