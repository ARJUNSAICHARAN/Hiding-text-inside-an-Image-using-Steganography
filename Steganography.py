import cv2
import os

# Create dictionaries for encoding and decoding
char_to_ascii = {chr(i): i for i in range(255)}
ascii_to_char = {i: chr(i) for i in range(255)}

# Read the image
image = cv2.imread(r"C:\Users\HARI\OneDrive\Desktop\Steganography10\sceenery.jpg")
height, width, channels = image.shape
print(f"Image dimensions: {height}x{width}x{channels}")

# Input security key and text to hide
security_key = input("\nEnter security key: ")
hidden_text = input("\nEnter text to hide: ")

# Initialize variables
key_index = 0
row, col, color_channel = 0, 0, 0
text_length = len(hidden_text)

# Encode text into the image
for idx in range(text_length):
    image[row, col, color_channel] = char_to_ascii[hidden_text[idx]] ^ char_to_ascii[security_key[key_index]]
    color_channel = (color_channel + 1) % 3
    if color_channel == 0:
        col = (col + 1) % width
        if col == 0:
            row = (row + 1) % height
    key_index = (key_index + 1) % len(security_key)

# Save the encrypted image
cv2.imwrite("encrypted_img.jpg", image)
os.startfile("encrypted_img.jpg")
print("Data hiding in image completed successfully.")

# Initialize variables for decoding
key_index = 0
row, col, color_channel = 0, 0, 0

# Input security key to unhide text
decryption_key = input("\nEnter security key to unhide the text: ")
decrypted_text = ""

if security_key == decryption_key:
    for idx in range(text_length):
        decrypted_text += ascii_to_char[image[row, col, color_channel] ^ char_to_ascii[security_key[key_index]]]
        color_channel = (color_channel + 1) % 3
        if color_channel == 0:
            col = (col + 1) % width
            if col == 0:
                row = (row + 1) % height
        key_index = (key_index + 1) % len(security_key)
    print("The secret message is:", decrypted_text)
else:
    print("Check your key!!!!")
