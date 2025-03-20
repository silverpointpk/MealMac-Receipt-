from PIL import Image, ImageDraw, ImageFont

# Image size
img_width, img_height = 300, 150
background_color = "white"  # White background

# Create an image
img = Image.new("RGB", (img_width, img_height), background_color)
draw = ImageDraw.Draw(img)

# Load font
font = ImageFont.truetype("arial.ttf", 16)  # Adjust size if needed

# Text lines
texts = ["windcave (Paid)", "Scheduled Order", "Pick-up"]
text_color = "white"
box_color = "black"

# Box settings
padding = 10
line_spacing = 5  # Space between boxes
x, y = 10, 10  # Start position

for text in texts:
    text_width, text_height = draw.textsize(text, font=font)
    box_width = img_width - 20
    box_height = text_height + 12

    # Draw box
    draw.rectangle([x, y, x + box_width, y + box_height], fill=box_color)

    # Draw text
    draw.text((x + 10, y + 6), text, font=font, fill=text_color)

    # Move Y down for next line
    y += box_height + line_spacing  # Adjusted spacing

# Save image
img.show()  # Display image
img.save("output.png")
