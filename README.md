# Finite ball by Muhammad Umar Anzar
## Automata-Project

A simple game two-player 2d game soccer game made using pygame library on python. 

## Purpose
The purpose was to make use of finite state machine

## Overall Description
- Language : python 3.9
- Library : pygame
- requirements to play : Two user and only one keyboard

## Features, Functions

1. Pygame python is use to create the whole gui game and auto-py-to-exe is used to create executable file
1. All the movement of player is made using finite state machine (Deterministic Finite Automata). An unique condition and additional `set array` is added to handle the movement key release event and the key down event.
When multiple keys are pressed by a user and only one or two of keys are release, then the unique condition makes the transition goes back to initial state and using `set array`, the keys which haven't released yet makes the transition again to new states accoriding to the keys which are already in pressed state.
<img src='Finite States\user_motion_finite_states.png' alt="DFA of motion" width=75%>


1. Handled diagonal speed from increasing due to the resultant motion of horizontal and vertical motion.
<img src='Finite States\diagonal_speed.png' alt='diagonal speed' width=75%>

1. InElastic Collisions physics i appled between user and ball and ball and window boundary with real angles.
<img src='Finite States\collisionBallHit.png' alt='collision' width=75%>






