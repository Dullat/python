import turtle

# L-System parameters
axiom = "X"  # Starting string
rules = {
    "X": "F-[[X]+X]+F[+FX]-X",  # Rule for X
    "F": "FF"                    # Rule for F
}
iterations = 5  # Number of iterations

# Function to apply L-system rules
def apply_rules(axiom, rules):
    new_axiom = ""
    for symbol in axiom:
        new_axiom += rules.get(symbol, symbol)  # Replace with rule if exists, else keep symbol
    return new_axiom

# Generate the L-System string
def generate_l_system(axiom, rules, iterations):
    for _ in range(iterations):
        axiom = apply_rules(axiom, rules)
    return axiom

# Function to draw the L-System tree using turtle
def draw_l_system(t, axiom, angle, length, length_reduction_factor):
    stack = []  # Stack for saving and restoring positions for branching
    for symbol in axiom:
        if symbol == "F":
            t.forward(length)  # Move forward
        elif symbol == "+":
            t.left(angle)  # Turn left by the angle
        elif symbol == "-":
            t.right(angle)  # Turn right by the angle
        elif symbol == "[":
            # Save the current position and heading (for branching)
            stack.append((t.position(), t.heading()))
        elif symbol == "]":
            # Restore the saved position and heading
            position, heading = stack.pop()
            t.penup()
            t.setposition(position)
            t.setheading(heading)
            t.pendown()

        # Gradually reduce the length for each iteration
        length *= length_reduction_factor

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)  # Fast drawing
t.left(90)  # Point the turtle upwards
t.penup()
t.setposition(0, -250)  # Start at the bottom of the screen
t.pendown()

# Generate the L-System string after specified iterations
lsystem_string = generate_l_system(axiom, rules, iterations)

# Draw the tree using the generated L-System string
draw_l_system(t, lsystem_string, angle=25, length=10, length_reduction_factor=0.7)

# Hide the turtle after drawing
t.hideturtle()

# Finish drawing
turtle.done()
