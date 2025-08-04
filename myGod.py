import turtle
import colorsys

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Psychedelic Spiral")
screen.tracer(0)

# Create the turtle
artist = turtle.Turtle()
artist.speed(0)
artist.hideturtle()

# Set initial color properties
hue = 0.0

# Main animation loop
for i in range(100):
    # Convert HSV color to RGB
    rgb_color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    artist.color(rgb_color)

    # Draw a circle
    artist.circle(i * 0.8)

    # Rotate the turtle
    artist.right(91)

    # Update the hue for the next iteration
    hue += 0.005

    # Update the screen
    screen.update()

# Keep the window open
turtle.done()