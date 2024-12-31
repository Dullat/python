import turtle
import time

def create_l_system(axiom, rules, iterations):
    result = axiom
    for _ in range(iterations):
        next_str = ""
        for char in result:
            next_str += rules.get(char, char)
        result = next_str
    return result

def draw_l_system(commands, angle, distance):
    stack = []
    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    t.color("lime green")  # Brighter color
    t.left(90)
    t.pensize(2)
    
    for cmd in commands:
        if cmd == 'F':
            t.forward(distance)
        elif cmd == '+':
            t.right(angle)
        elif cmd == '-':
            t.left(angle)
        elif cmd == '[':
            stack.append((t.position(), t.heading(), t.pensize()))
            t.pensize(max(1, t.pensize() * 0.7))
        elif cmd == ']':
            position, heading, size = stack.pop()
            t.penup()
            t.setposition(position)
            t.setheading(heading)
            t.pensize(size)
            t.pendown()

def main():
    try:
        screen = turtle.Screen()
        screen.bgcolor("black")
        screen.title("L-System Tree")
        
        # Clear any existing turtles
        turtle.clearscreen()
        
        # L-system rules
        axiom = "F"
        rules = {
            "F": "FF+[+F-F-F]-[-F+F+F]"
        }
        
        # Generate the L-system
        lsystem = create_l_system(axiom, rules, 4)
        
        # Small delay to ensure window is ready
        time.sleep(0.5)
        
        # Draw
        draw_l_system(lsystem, 25, 10)
        
        print("Drawing complete. Click window to exit.")
        screen.exitonclick()
        
    except turtle.Terminator:
        print("Window was closed")
    except Exception as e:
        prin
if __name__ == "__main__":
    main()