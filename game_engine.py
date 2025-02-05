import random
import pygame
import numpy as np
from collections import namedtuple

pygame.init()
font = pygame.font.Font('assets/arial.ttf', 25) 
Point = namedtuple('Point', ('x', 'y'))

WHITE = (255, 87, 255)
BLACK = (0, 0, 0)
BLOCK_SIZE = 20

# Load the real apple image
apple_image = pygame.image.load('assets/apple.png')  # Replace 'apple.png' with your real apple image file

class SnakeGame():
    def __init__(self, w=640, h=480, num_obstacles=10):
        pygame.display.set_caption("Snake")
        self.w, self.h = w, h
        self.display = pygame.display.set_mode((self.w, self.h))
        self.clock = pygame.time.Clock()
        self.reset(num_obstacles)

    def reset(self, num_obstacles):
        # Initialize game parameters and state
        self.direction = "r"  # Snake's initial direction (right)
        self.head = Point(self.w / 2, self.h / 2)  # Snake's starting position
        self.snake = [self.head]  # Initialize the Snake as a list containing the head
        self.score = 0  # Initialize the score
        self.food = None  # Food's initial position (None until placed)
        self.obstacles = []  # List to store obstacle points
        self.frame_iteration = 0  # Tracks game frame iterations

        # Place obstacles randomly on the game board
        for i in range(num_obstacles):
            self.place_food()

    def place_food(self):
        # Generate and place food randomly on the game board
        while True:
            x = random.randint(0, (self.w - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
            y = random.randint(0, (self.h - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
            self.food = Point(x, y)

            # Ensure that the food does not overlap with the Snake's body or obstacles
            if self.food not in self.snake and self.food not in self.obstacles:
                break

    def play(self, action, speed, episode):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Update the game state based on the provided action
        self.move(action)
        self.snake.insert(0, self.head)
        self.frame_iteration += 1

        reward = 0
        game_over = False

        # Check for collision or game over conditions
        if self.is_collision() or self.frame_iteration > 100 * len(self.snake):
            reward = -10
            game_over = True
            return reward, game_over

        if self.head == self.food:
            reward = 100
            self.score += 1
            self.place_food()
        else:
            self.snake.pop()

        # Update the game user interface and control game speed
        self.update_ui(episode)
        self.clock.tick(speed)

        return reward, game_over

    def is_collision(self, pt=None):
        if pt is None:
            pt = self.head

        # Check for collisions with boundaries, the Snake's own body, or obstacles
        if pt.x > self.w - BLOCK_SIZE or pt.x < 0 or pt.y > self.h - BLOCK_SIZE or pt.y < 0:
            return True

        if pt in self.snake[1:] or pt in self.obstacles:
            return True

        return False

    def update_ui(self, episode):
        # Update the game user interface by drawing Snake, real apple, obstacles, and the score
        self.display.fill(BLACK)
        for p in self.obstacles:
            pygame.draw.rect(self.display, WHITE, pygame.Rect(
                p.x, p.y, BLOCK_SIZE, BLOCK_SIZE))
        for p in self.snake:
            pygame.draw.rect(self.display, WHITE, pygame.Rect(
                p.x, p.y, BLOCK_SIZE, BLOCK_SIZE))

        if self.food:
            # Draw the real apple image on the game screen
            self.display.blit(apple_image, (self.food.x, self.food.y))

        # Display the score and episode number
        self.draw_score(episode)
        pygame.display.flip()

    def draw_score(self, episode):
        # Display the current score and episode number on the screen
        text = font.render("Score: " + str(self.score) + " | Episode: " + str(episode), True, WHITE)
        self.display.blit(text, [0, 0])

    def move(self, action):
        clock_wise = ["r", "d", "l", "u"]
        idx = clock_wise.index(self.direction)

        if np.array_equal(action, [1, 0, 0]):
            new_dir = clock_wise[idx]
        elif np.array_equal(action, [0, 1, 0]):
            new_idx = (idx + 1) % 4
            new_dir = clock_wise[new_idx]
        else:
            new_idx = (idx - 1) % 4
            new_dir = clock_wise[new_idx]

        self.direction = new_dir
        x = self.head.x
        y = self.head.y

        if self.direction == "r":
            x += BLOCK_SIZE
        elif self.direction == "l":
            x -= BLOCK_SIZE
        elif self.direction == "d":
            y += BLOCK_SIZE
        elif self.direction == "u":
            y -= BLOCK_SIZE

        self.head = Point(x, y)