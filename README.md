# Automata-Project
> - By Muhammad Umar Anzar
> - University Of karachi 
> - UBIT department of computer science
> - Semester 5
> - Subject Computer Theory (Automata)

## Finite ball
<hr>

A basic two-player 2D soccer game created in Python with the Pygame framework. 

## Purpose

The goal was to include a finite state machine into a project.

## Overall Description

- Language : python3
- Library : pygame
- requirements to play : Two user and only one keyboard

## Features, Functions

1. Python `pygame` is used to make the entire GUI game, and `auto-py-to-exe` is used to make the executable file.
1. The player's entire movement is controlled by a finite state machine (Deterministic Finite Automata). To handle the movement `key release `and `key pressed` events, a new condition and additional `set array` are introduced. When a user presses numerous keys and only one or two of them are released, the unique condition causes the transition to return to the initial state, and utilizing the set array, the keys that haven't released yet cause the transition to new states in accordance with the keys that are already pressed.
<img src='Finite States\user_motion_finite_states.png' alt="DFA of motion" width=75%>


1. Controlled the increase in diagonal speed as a result of the horizontal and vertical motions.
<img src='Finite States\diagonal_speed.png' alt='diagonal speed' width=75%>

1. In-Elastic Collisions physics is applied with true angles between the user and the ball, as well as between the ball and the window boundaries.
<img src='Finite States\collisionBallHit.png' alt='collision' width=75%>






