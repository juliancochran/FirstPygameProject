# bouncing rectangle Pygame program
__version__ = '1/10/2025'
__author__ = 'Julian Cochran'
import pygame
import random

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))  # Creates an 800x600 window
    running = True
    # Create a Rect object for the square
    square_size = 60
    square = pygame.Rect(370, 270, square_size, square_size)  # x, y, width, height
    square_color = (255, 0, 0)  # Red color
    # Add velocity (speed and direction)
    # Example combinations:
    FPS = 120  # Smooth animation
    spd_x = 3 if random.randint(0,1) == 0 else -3 # 5 or -5 pixels per frame to the right
    spd_y = 3 if random.randint(0,1) == 0 else -3 # 5 or -5 pixels per frame downward

    while running:
        # 1. Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Check if window close button is clicked
                running = False

        # 2. Game state updates will go here later
        # Get current screen dimensions
        screen_width = screen.get_width()
        screen_height = screen.get_height()

        # Update square position
        square.move_ip(spd_x, spd_y)
        # if square is on the edge of the screen, bounce it and change a random color
        if square.left <= 0 or square.right >= screen_width:
            spd_x *= -1
            square_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        if square.top <= 0 or square.bottom >= screen_height:
            spd_y *= -1
            square_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        # 3. Drawing
        screen.fill((0, 0, 0))  # Fill screen with black color
        # Draw the square using the Rect object
        pygame.draw.rect(screen, square_color, square)
        pygame.display.flip()  # Update the display
        pygame.time.Clock().tick(FPS)
    pygame.quit()

if __name__ == '__main__':
    main()