import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Load image
img = cv2.imread('curtain.jpg')

# Convert to grayscale and create mask
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img_gray, 220, 255, cv2.THRESH_BINARY_INV)

# Get mask color from user input (as a color name)
mask_color_name = input("Enter the color name for the masked region: ")
if mask_color_name.lower() == "green":
    mask_color = (0, 255, 0)  # Green color for masked region
elif mask_color_name.lower() == "red":
    mask_color = (0, 0, 255)  # Red color for masked region
elif mask_color_name.lower() == "blue":
    mask_color = (255, 0, 0)  # Blue color for masked region
elif mask_color_name.lower() == "white":
    mask_color = (255, 255, 255)  # Blue color for masked region
else:
    # Default to green if user enters an invalid color name
    mask_color = (0, 255, 0)

# Get non-mask color from user input (as a color name)
non_mask_color_name = input("Enter the color name for the non-masked region: ")
if non_mask_color_name.lower() == "yellow":
    non_mask_color = (0, 255, 255)  # Yellow color for non-masked region
elif non_mask_color_name.lower() == "orange":
    non_mask_color = (0, 165, 255)  # Orange color for non-masked region
elif non_mask_color_name.lower() == "purple":
    non_mask_color = (128, 0, 128)  # Purple color for non-masked region
elif non_mask_color_name.lower() == "black":
    non_mask_color = (0, 0, 0)  # Purple color for non-masked region
else:
    # Default to yellow if user enters an invalid color name
    non_mask_color = (0, 255, 255)

# Create mask images with specified colors
mask_color_image = np.zeros_like(img)
mask_color_image[:, :] = mask_color
non_mask_color_image = np.zeros_like(img)
non_mask_color_image[:, :] = non_mask_color

# Apply masks to original image
masked_img = cv2.bitwise_and(img, img, mask=mask)
mask_color_region = cv2.bitwise_and(mask_color_image, mask_color_image, mask=mask)
non_mask_color_region = cv2.bitwise_and(non_mask_color_image, non_mask_color_image, mask=cv2.bitwise_not(mask))
result = cv2.add(masked_img, mask_color_region)
result = cv2.add(result, non_mask_color_region)

# Display result
cv2.imshow('Result', result)
cv2.imwrite('transfer.jpg',result)


# Defining symbol size and spacing
symbol_size = (20, 10)
symbol_spacing = 100

# Define the number of rows and columns for the images
num_rows = 2
num_cols = 4

# Create a new image with a black background

img = Image.new('RGB', (605, 360), color='black')

# Create a drawing context
draw = ImageDraw.Draw(img)

# Load symbols as images and paste them onto the image
symbols = [     ('C:/Users/Vishal Pahuja/Documents/Vishal/python/transfer.jpg'),
                ('C:/Users/Vishal Pahuja/Documents/Vishal/python/transfer.jpg'),
                ('C:/Users/Vishal Pahuja/Documents/Vishal/python/transfer.jpg'),
                ('C:/Users/Vishal Pahuja/Documents/Vishal/python/transfer.jpg'),
                ('C:/Users/Vishal Pahuja/Documents/Vishal/python/transfer.jpg'),
                ('C:/Users/Vishal Pahuja/Documents/Vishal/python/transfer.jpg'),
                ('C:/Users/Vishal Pahuja/Documents/Vishal/python/transfer.jpg'),
                ('C:/Users/Vishal Pahuja/Documents/Vishal/python/transfer.jpg')]

labels = ['Curtain', 'Chair', 'Table', 'Couch', 'Lamp', 'Dresser', 'Plant', 'Sofa']

for i, symbol_file in enumerate(symbols):
    symbol_img = Image.open(symbol_file)
    row = i // num_cols
    col = i % num_cols
    x = (symbol_size[0] + symbol_spacing) * col + symbol_spacing
    y = (symbol_size[1] + symbol_spacing) * row + symbol_spacing
    img.paste(symbol_img, (x, y))

    label_text = labels[i]
    font = ImageFont.truetype('arial.ttf', size=20)
    label_bbox = font.getbbox(label_text)
    label_x = x + symbol_size[0] // 2 - (label_bbox[2] - label_bbox[0]) // 2
    label_y = y + symbol_size[1] + symbol_spacing
    # draw.text((label_x, label_y), label_text, font=font, fill=(255, 0, 0))

    # Add text below the symbol image
    object_name = labels[i]
    font = ImageFont.truetype('arial.ttf', size=16)
    text_size = font.getbbox(object_name)
    text_x = x + (symbol_size[0] - text_size[0]) // 2
    text_y = label_y + label_bbox[3] - label_bbox[1] + -139 + symbol_spacing
    draw.text((text_x, text_y), object_name, font=font, fill=mask_color)

# Save the image

cv2.waitKey(0)
cv2.destroyAllWindows()
img.save('symbols_grid_with_labels.pdf')
img.save('symbols_grid_with_labels.jpg')
