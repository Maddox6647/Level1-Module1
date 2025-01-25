
def setup():
    # 1. Use the size function to set the size of your sketch
    size(800, 600);
    # 2. Create 2 global variables for the background and the frog
    # using the loadImage("frog.png") function. For example:
    # global bg, frog
    # bg = loadImage("froggerBackground.png")
    global bg, froggy, shrek_mike, frog_x, frog_y, car1, car2, car3, car4
    froggy = loadImage("frog.png")
    bg = loadImage("froggerBackground.png")
    shrek_mike = loadImage("shrek-mike-removebg-preview.png")
    frog_x = 400
    frog_y = 550
    # 3. Use the resize method to set the size of the background variable
    # to the width and height of the sketch. Resize the frog to an
    # approvpriate size.
    froggy.resize(80, 80)
    bg.resize(800, 600)
    shrek_mike.resize(440, 270)
    #

    car1 = Car(250, 200, 700, -16)
    car2 = Car(134, 100, 300, 14)
    car3 = Car(0, 400, 300, -19)
def draw():
    # 4. Use the background function to draw the background
    background(bg)
    # 5. Use the image function to draw the frog.
    # Run the program and check the background and frog are displayed.
  
    # 6. Create global frog_x and frog_y variables in the setup function
    # and use them when drawing the frog. You will also have to put the
    # following in the draw function:
    global frog_x, frog_y, car1, car2, car3
    image(froggy, frog_x,frog_y)
    
    # 7. Use the Car class below to create a global car object in the
    # setup function and call the update and draw functions here.

    
    car1.update()
    car1.draw()
    car2.update()
    car2.draw()
    car3.update()
    car3.draw()
    # 8. Create an intersects method that checks whether the frog collides
    # with the car. If there's a collision, move the frog back to the starting
    # point.
    
    # 9. Create more car objects of different lengths, speed, and size
def keyPressed():
    global frog_x, frog_y
    if key == CODED:
        if keyCode == UP:
            # Frog Y position goes up
            print("up")
            frog_y -= 20
        elif keyCode == DOWN:
            # Frog Y position goes down
            print("down")
            frog_y += 20
        elif keyCode == RIGHT:
            # Frog X position goes right
            print("right")
            frog_x += 20
        elif keyCode == LEFT:
            # Frog X position goes left
            print("left")
            frog_x -= 20
class Car:
    def __init__(self, x, y, length, speed):
        self.x = x
        self.y = y
        self.length = length
        self.speed = speed
        
        self.car_image = loadImage("shrek-mike-removebg-preview.png")
        if self.speed < 0:
            self.car_image = loadImage("shrek-mike-removebg-preview.png")
        
        self.car_image.resize(self.length, self.length / 2)
        
    def draw(self):
        image(self.car_image, self.x, self.y)
    
    def update(self):
        self.x += self.speed
        
        if self.x > width:
            self.x = -self.length
            
        if self.x < -self.length:
            self.x = width
