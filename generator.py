from PIL import Image, ImageDraw, ImageFont
import os

# Constants for the bingo grid
NUM_ROWS = 5
NUM_COLS = 5
NUM_CARDS = 75

# Constants for the size and font of the numbers
CELL_SIZE = 570
# FONT_SIZE = 220
FONT_PATH = "Ubuntu-R.ttf"  # Replace with the path to your preferred font file

# Function to generate unique number combinations for each card
def generate_unique_numbers():
    all_numbers = list(range(1, 76))
    import random
    random.shuffle(all_numbers)

    unique_numbers = []
    for _ in range(NUM_CARDS):
        card_numbers = all_numbers[:]

        # Ensure that each card has a unique combination of numbers
        random.shuffle(card_numbers)
        unique_numbers.append(card_numbers)

    return unique_numbers

# Function to generate a bingo card
def generate_bingo_card(numbers, background_image_path, card_number):
    card = Image.open(background_image_path)
    draw = ImageDraw.Draw(card)

    # Create a font object
    # font = ImageFont.truetype(FONT_PATH, FONT_SIZE)

    # Calculate the starting position for the grid
    start_x = 120
    start_y = 700

    # Draw the bingo grid with numbers and "Free Space" in the center
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            if row == col == 2:  # Center position
                font = ImageFont.truetype(FONT_PATH, 150)
                text = "Free\nSpace"
            else:
                font = ImageFont.truetype(FONT_PATH, 280)
                number = numbers.pop(0)
                text = str(number)

            position_x = start_x + col * CELL_SIZE
            position_y = start_y + row * CELL_SIZE
            draw.text((position_x, position_y), text, fill="#737491", font=font, align="center")

    # Save the card as an image with a unique filename
    card_filename = f"{card_number}.png"
    card.save(card_filename)

# Main function to generate all the bingo cards
def main():
    # Generate unique number combinations for each card
    unique_numbers = generate_unique_numbers()

    # Load the background image
    background_image_path = "background_new.png"  # Replace with your background image path

    # Create the bingo cards
    for card_number, numbers in enumerate(unique_numbers, start=1):
        generate_bingo_card(numbers, background_image_path, card_number)

    print("Bingo cards generated successfully!")

if __name__ == "__main__":
    main()