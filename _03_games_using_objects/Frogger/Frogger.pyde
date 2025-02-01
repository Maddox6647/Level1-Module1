
def setup():
    # 1. Use the size function to set the size of your sketch
    size(800, 600);
    # 2. Create 2 global variables for the background and the frog
    # using the loadImage("frog.png") function. For example:
    # global bg, frog
    # bg = loadImage("froggerBackground.png")
    global bg, froggy, shrek_mike, frog_x, frog_y, car1, car2, car3, car4, car5, car6, car7, car8, car9, score
    froggy = loadImage("frog.png")
    bg = loadImage("froggerBackground.png")
    shrek_mike = loadImage("shrek-mike-removebg-preview.png")
    frog_x = 400
    frog_y = 550
    score = 0
    

    # 3. Use the resize method to set the size of the background variable
    # to the width and height of the sketch. Resize the frog to an
    # approvpriate size.
    froggy.resize(80, 80)
    bg.resize(800, 600)
    shrek_mike.resize(440, 270)
    #

    car1 = Car(250, 200, 250, -16)
    car2 = Car(134, 100, 300, 14)
    car3 = Car(0, 400, 300, 19)
    car4 = Car(100, 100, 400, 10)
    car5 = Car(349, 300, 400, 90)
    car6 = Car(200, 200, 300, 2)
    car7 = Car(154, 100, 300, 60)
    car8 = Car(301, 139, 300, -10)
    car9 = Car(240, 370, 300, 30)
def draw():
    global score
    # 4. Use the background function to draw the background
    background(bg)
    text(str(score), 20, 20)
    # 5. Use the image function to draw the frog.
    # Run the program and check the background and frog are displayed.
  
    # 6. Create global frog_x and frog_y variables in the setup function
    # and use them when drawing the frog. You will also have to put the
    # following in the draw function:
    global frog_x, frog_y, car1, car2, car3, car4, car5, car6, car7, car8, car9
    image(froggy, frog_x,frog_y)
    
    # 7. Use the Car class below to create a global car object in the
    # setup function and call the update and draw functions here.

    
    car1.update()
    car1.draw()
    car2.update()
    car2.draw()
    car3.update()
    car3.draw()
    car4.update()
    car4.draw()
    car5.update()
    car5.draw()
    car6.update()
    car6.draw()
    car7.update()
    car7.draw()
    car8.update()
    car8.draw()
    car9.update()
    car9.draw()
    if frog_collides(car1):
        frog_x = 400
        frog_y = 550
    if frog_collides(car2):
        frog_x = 400
        frog_y = 550
    if frog_collides(car3):
        frog_x = 400
        frog_y = 550

    if frog_y < 0:
        score += 1
        frog_x = 400
        frog_y = 550
    # 8. Create an intersects method that checks whether the frog collides
    # with  car. If there's a collision, move the frog back to the starting
    # point.
def frog_collides(car):
    global frog_x, frog_y
    if frog_x + 80 < car.x or car.x + car.length < frog_x:
        return False
    if frog_y + 80 < car.y or car.y + car.length/2 < frog_y:
        return False;
    return True
        
        

    # 9. Create more car objects of different lengths, speed, and size
def keyPressed():
    global frog_x, frog_y
    if key == CODED:
        if keyCode == UP:
            # Frog Y position goes up
            print("up")
            frog_y -= 60
        elif keyCode == DOWN:
            # Frog Y position goes down
            print("down")
            frog_y += 60
        elif keyCode == RIGHT:
            # Frog X position goes right
            print("right")
            frog_x += 60
        elif keyCode == LEFT:
            # Frog X position goes left
            print("left")
            frog_x -= 60
        elif keyCode == W:
            print("dash")
            frog_y += 100
            
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
