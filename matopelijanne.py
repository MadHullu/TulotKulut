import tkinter as tk
import random

window = tk.Tk()
window.title("Matopeli")

WIDTH = 500
HEIGHT = 500
SQUARE_SIZE = 20

BACKGROUND_COLOR = "black"
SNAKE_COLOR = "green"
FOOD_COLOR = "red"
TEXT_COLOR = "white"

snake_coords = []
food_coords = []
direction = "Right"
game_running = True
score = 0

canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg=BACKGROUND_COLOR)
canvas.pack()

snake_parts = [] 
score_text = None 


def init_game():
    global snake_coords, food_coords, direction, game_running, snake_parts, score, score_text

    snake_coords = [[100, 100], [80, 100], [60, 100]]
    direction = "Right"
    game_running = True
    score = 0

    canvas.delete("all")

    snake_parts.clear()
    for x, y in snake_coords:
        part = canvas.create_rectangle(x, y, x + SQUARE_SIZE, y + SQUARE_SIZE, fill=SNAKE_COLOR)
        snake_parts.append(part)

    spawn_food()

    if score_text is None:
        create_score_text()
    update_score()

    move_snake()


def create_score_text():
    global score_text
    score_text = canvas.create_text(10, 10, anchor="nw", text=f"Pisteet: {score}", fill=TEXT_COLOR, font=("Arial", 16))


def spawn_food():
    global food_coords
    food_coords = [random.randint(0, (WIDTH // SQUARE_SIZE) - 1) * SQUARE_SIZE,
                   random.randint(0, (HEIGHT // SQUARE_SIZE) - 1) * SQUARE_SIZE]
    canvas.create_oval(food_coords[0], food_coords[1],
                       food_coords[0] + SQUARE_SIZE, food_coords[1] + SQUARE_SIZE,
                       fill=FOOD_COLOR, tags="food")


def move_snake():
    global game_running, score

    if not game_running:
        return

    x, y = snake_coords[0]
    if direction == "Right":
        x += SQUARE_SIZE
    elif direction == "Left":
        x -= SQUARE_SIZE
    elif direction == "Up":
        y -= SQUARE_SIZE
    elif direction == "Down":
        y += SQUARE_SIZE

    new_head = [x, y]
    snake_coords.insert(0, new_head)

    if x == food_coords[0] and y == food_coords[1]:
        canvas.delete("food")
        spawn_food()
        score += 10  
        update_score()
    else:
        del snake_coords[-1]
        canvas.delete(snake_parts.pop())

    part = canvas.create_rectangle(new_head[0], new_head[1],
                                   new_head[0] + SQUARE_SIZE, new_head[1] + SQUARE_SIZE,
                                   fill=SNAKE_COLOR)
    snake_parts.insert(0, part)

    if check_collision():
        game_over()
    else:
        window.after(100, move_snake)


def change_direction(new_direction):
    global direction
    opposite_directions = {"Left": "Right", "Right": "Left", "Up": "Down", "Down": "Up"}
    if new_direction != opposite_directions[direction]:
        direction = new_direction


def check_collision():
    x, y = snake_coords[0]

    if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
        return True

    if [x, y] in snake_coords[1:]:
        return True

    return False


def game_over():
    global game_running
    game_running = False
    canvas.create_text(WIDTH // 2, HEIGHT // 2, text="GAME OVER", fill="red", font=("Arial", 24))
    canvas.create_text(WIDTH // 2, HEIGHT // 2 + 30, text="Press R to Restart", fill="white", font=("Arial", 16))


def update_score():
    canvas.itemconfigure(score_text, text=f"Pisteet: {score}")


def restart_game(event):
    if not game_running:
        init_game()


window.bind("<Left>", lambda event: change_direction("Left"))
window.bind("<Right>", lambda event: change_direction("Right"))
window.bind("<Up>", lambda event: change_direction("Up"))
window.bind("<Down>", lambda event: change_direction("Down"))
window.bind("<r>", restart_game)

init_game()

window.mainloop()
