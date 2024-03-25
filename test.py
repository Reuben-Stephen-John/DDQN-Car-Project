import GameEnv
import pygame
import numpy as np

def run():
    pygame.init()
    game = GameEnv.RacingEnv()

    running = True
    keys_pressed = {pygame.K_w: False, pygame.K_s: False, pygame.K_a: False, pygame.K_d: False}

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in keys_pressed:
                    keys_pressed[event.key] = True
            elif event.type == pygame.KEYUP:
                if event.key in keys_pressed:
                    keys_pressed[event.key] = False

        # Determine action based on keys pressed
        if keys_pressed[pygame.K_w]:
            action = 4  # Accelerate forward
        elif keys_pressed[pygame.K_s]:
            action = 1  # Accelerate backward
        elif keys_pressed[pygame.K_a]:
            action = 2  # Turn left
        elif keys_pressed[pygame.K_d]:
            action = 3  # Turn right
        else:
            action = 0  # No action if no key is pressed

        new_state, reward, done = game.step(action)
        game.render(action, 0)  # Pass any arbitrary episode number for rendering

        if done:
            game.reset()  # Reset the environment when the episode ends

    game.close()  # Close the Pygame window when done

run()
