from random import randint  # Import randint for generating random numbers
import turtle  # Import turtle for graphics

# Define the Point class
class Point:
    def _init_(self, x, y):  # Initialize a point with x and y coordinates
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle_area):  
        # This method checks if the current point (self) lies within the given rectangle (rectangle_area)
        
        # Check if the x-coordinate of the point is within the horizontal bounds of the rectangle
        # rectangle_area.point1.x is the bottom-left x-coordinate of the rectangle
        # rectangle_area.point2.x is the top-right x-coordinate of the rectangle
        # self.x is the x-coordinate of the point to check
        # The condition ensures: point1.x <= self.x <= point2.x
        x_in_bounds = rectangle_area.point1.x <= self.x <= rectangle_area.point2.x
        
        # Check if the y-coordinate of the point is within the vertical bounds of the rectangle
        # rectangle_area.point1.y is the bottom-left y-coordinate of the rectangle
        # rectangle_area.point2.y is the top-right y-coordinate of the rectangle
        # self.y is the y-coordinate of the point to check
        # The condition ensures: point1.y <= self.y <= point2.y
        y_in_bounds = rectangle_area.point1.y <= self.y <= rectangle_area.point2.y

        # The point is inside the rectangle if BOTH conditions are True:
        # - x_in_bounds: The x-coordinate is within the rectangle's horizontal range
        # - y_in_bounds: The y-coordinate is within the rectangle's vertical range
        return x_in_bounds and y_in_bounds



# Define the Rectangle class
class Rectangle:
    def _init_(self, point1, point2):  # Initialize a rectangle with two points
        self.point1 = point1
        self.point2 = point2

    def area(self):  
        # This method calculates and returns the area of the rectangle.

        # Calculate the width of the rectangle:
        # self.point2.x is the x-coordinate of the top-right corner.
        # self.point1.x is the x-coordinate of the bottom-left corner.
        # Subtract point1.x from point2.x to get the horizontal width of the rectangle.
        width = self.point2.x - self.point1.x

        # Calculate the height of the rectangle:
        # self.point2.y is the y-coordinate of the top-right corner.
        # self.point1.y is the y-coordinate of the bottom-left corner.
        # Subtract point1.y from point2.y to get the vertical height of the rectangle.
        height = self.point2.y - self.point1.y

        # Multiply the width and height to get the area of the rectangle.
        # Area formula: width * height
        return width * height



# Define the GuiRectangle class, inheriting from Rectangle
class GuiRectangle(Rectangle):

    def draw(self, canvas):  # Draw the rectangle on the Turtle canvas
        canvas.penup()  # Lift the pen to move without drawing
        canvas.goto(self.point1.x, self.point1.y)  # Move to the bottom-left corner
        canvas.pendown()  # Lower the pen to start drawing
        canvas.goto(self.point2.x, self.point1.y)  # Draw the bottom side
        canvas.goto(self.point2.x, self.point2.y)  # Draw the right side
        canvas.goto(self.point1.x, self.point2.y)  # Draw the top side
        canvas.goto(self.point1.x, self.point1.y)  # Draw the left side, completing the rectangle


# Define the GuiPoint class, inheriting from Point
class GuiPoint(Point):
    def draw(self, canvas, size=5, color='red'):  # Draw the point as a dot on the canvas
        canvas.penup()  # Lift the pen to move without drawing
        canvas.goto(self.x, self.y)  # Move to the point's location
        canvas.pendown()  # Lower the pen to draw
        canvas.dot(size, color)  # Draw a dot at the point


# Create the Turtle screen
screen = turtle.Screen()
screen.setup(width=800, height=600)  # Set up the screen size
screen.setworldcoordinates(0, 0, 300, 300)  # Set the coordinate system

# Generate random coordinates for a rectangle
x1, y1 = randint(0, 150), randint(0, 150)  # Bottom-left corner
x2, y2 = randint(x1 + 10, 200), randint(y1 + 10, 200)  # Top-right corner
rectangle = GuiRectangle(Point(x1, y1), Point(x2, y2))  # Create the rectangle object

# Create a Turtle for writing text
writer = turtle.Turtle()
writer.hideturtle()  # Hide the turtle cursor
writer.penup()  # Lift the pen for moving without drawing
writer.goto(10, 280)  # Move to the top of the screen to write text
writer.write(f"Rectangle Coordinates: Bottom-left ({x1}, {y1}) and Top-right ({x2}, {y2})",
             align="left", font=("Arial", 12, "normal"))  # Write rectangle coordinates

# Get user inputs dynamically through Turtle input dialogs
user_x = float(screen.textinput("Point Input", "Enter x coordinate of a point:"))  # Input x coordinate
user_y = float(screen.textinput("Point Input", "Enter y coordinate of a point:"))  # Input y coordinate
user_area = float(screen.textinput("Area Guess", "Enter your guess for the rectangle's area:"))  # Input area guess

# Display user inputs on the Turtle window
writer.goto(10, 260)  # Move to the next line
writer.write(f"Guess x coordinate of a point: {user_x}", align="left", font=("Arial", 12, "normal"))  # Display x
writer.goto(10, 240)  # Move to the next line
writer.write(f"Guess y coordinate of a point: {user_y}", align="left", font=("Arial", 12, "normal"))  # Display y
writer.goto(10, 220)  # Move to the next line
writer.write(f"Guess the rectangle's area: {user_area}", align="left", font=("Arial", 12, "normal"))  # Display area

# Create a GuiPoint object for the user's point
user_point = GuiPoint(user_x, user_y)
inside = user_point.falls_in_rectangle(rectangle)  # Check if the point is inside the rectangle
area_difference = abs(rectangle.area() - user_area)  # Calculate the difference between guessed and actual area

# Display the results on the Turtle window
writer.goto(10, 200)  # Move to the next line
writer.write(f"Your point is inside the rectangle: {inside}", align="left", font=("Arial", 12, "normal"))  # Display result
writer.goto(10, 180)  # Move to the next line
writer.write(f"Your area guess was off by: {area_difference}", align="left", font=("Arial", 12, "normal"))  # Display diff

# Create a Turtle for drawing and draw the rectangle and point
drawer = turtle.Turtle()
rectangle.draw(drawer)  # Draw the rectangle
user_point.draw(drawer)  # Draw the user's point

# Keep the Turtle window open
turtle.done()  # Finish the Turtle program and keep the window open