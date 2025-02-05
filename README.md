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

Features:
Human Play: Control the snake using arrow keys in a classic Snake game mode.
Autonomous Play: Watch the AI agent, trained with reinforcement learning, navigate the game environment and improve its performance over time.
Reinforcement Learning Implementation: Utilizes a dueling network architecture to separately estimate state values and advantages for actions.
Implements experience replay, epsilon-greedy action selection, and target network updates for stable learning.
Provides training scripts for both short-term (immediate) and long-term (batch) updates.

The project is organized into multiple modules:
## Demo Scripts:
Game Engine (game_engine.py): Handles game logic, UI updates, and player input.
Neural Network and Trainer (neuralnetwork.py): Contains the dueling network model and the training routine.
Agent (agent.py): Integrates the neural network with game interactions, state representation, and decision-making.
play_game.ai.py: Runs the game with the AI agent using a pre-trained model.
play_game_human.py: Runs the game in human-controlled mode.

you know how to run this project :)
