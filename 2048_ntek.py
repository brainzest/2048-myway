from tkinter import *
from math import *
import random
master = Tk()
box=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
score =0
dead=0
start_coordinate_x =100
start_coordinate_y=100
box_width=100
box_height=100

    
w = Canvas(master, width=700, height=550)
w.create_text(300 , 20,text="2048", fill="brown", font=("Helvetica",22))
w.create_text(300 , 50,text="GO CRAZY!", fill="purple", font=(18))
w.create_text(450 , 70,text="SCORE :"+ str(score), fill="green", font=(18))
            
def addText(canvas_width, canvas_height, stringadd):
    w.create_text(canvas_width / 2, canvas_height / 2,text=stringadd, fill="white", font=("Helvetica",22))
    
def draw_boxes(x,y,width,height,color):
   
    w.create_rectangle(x,y,width,height,fill=color)
   # addText(width+x,height+y,"2")
    
w.pack()

    
def rgb_to_hex(r,g,b):
    return '#%02x%02x%02x' % (r,g,b)
def create_random_tile():
    #create todo
        # Create a new tile in a randomly selected empty 
        # square.  The tile should be 2 80% of the time and
        # 4 20% of the time.
    available_boxes = []
    for row in range(4):
        for col in range(4):
            if box[row][col] == 0:
                available_boxes.append([row, col])

    if not available_boxes:
        print ("There are no available positions.")
    else:
         random_tile = random.choice(available_boxes)
         weighted_choices = [(2, 8), (4, 2)]
         available_values= [val for val, count in weighted_choices for i in range(count)]
         tile = random.choice(available_values)
         print(random_tile[0])
         print(tile)
         global box
         print(box)
         box[random_tile[0]][random_tile[1]]= tile
         print(box)
        
def restart():
    global box
    box=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    draw()
    score=dead=0
    create_random_tile()     
    
def draw():
    #draw_boxes(50, 50, 150, 150,"blue")
    #print 'lenght', len(boxes)
    create_random_tile()
    for i in range(len(box)):
        for j in range(len(box)):
                       
                       x = start_coordinate_x + (start_coordinate_x)*i
                       y = start_coordinate_y + (start_coordinate_y)*j
                       box_width = x+ 100
                       box_height = y + 100
                       draw_boxes(x, y, box_width, box_height,"grey")
                       if box[i][j] >0 :
                           p =log(box[i][j])/log(2)
                           color=rgb_to_hex(p*23,p*23,p*23);
                           #todo :improve colour of the boxes                           
                           draw_boxes(x, y, box_width, box_height, color)
                           addText(box_width+x,box_height+y,box[i][j])
                       

b=Button(master, height=1,activeforeground="magenta",activebackground="light yellow", text="RESTART" ,width=10,  font=("Helvetica", 10),command=restart)
b.pack()    
draw()
mainloop()





