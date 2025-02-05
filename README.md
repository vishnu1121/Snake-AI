**a dddqn that can play snake**  
`assets/checkpoint-700.pth.tar` -> pre trained weights  
`play_game_human.py` -> play snake  
`play_game_ai.py` -> watch the ai play snake   

Overview
Snake Game with Reinforcement Learning is divided into two main components:

Game Engine:
A Pygame-based Snake game where the player controls the snake using keyboard inputs. The game includes classic features such as food placement, collision detection, and score tracking.

Reinforcement Learning Agent:
An AI agent built using a dueling neural network architecture and trained with Deep Q-Learning. The agent learns to play the Snake game by interacting with the game environment, storing experiences, and updating its policy through both short-term and long-term memory training.
