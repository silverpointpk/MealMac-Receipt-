from PIL import Image, ImageDraw, ImageFont

# Create a white background image
width, height = 300, 400
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Load fonts (adjust paths if necessary)
try:
    font_regular = ImageFont.truetype("arial.ttf", 16)
    font_bold = ImageFont.truetype("arialbd.ttf", 25)
    font_large_bold = ImageFont.truetype("arialbd.ttf", 26)
except IOError:
    # Fallback to default font
    font_regular = ImageFont.load_default()
    font_bold = ImageFont.load_default()
    font_large_bold = ImageFont.load_default()

# Y offset tracker
y = 60

# Order Number
draw.text((90, y), "Order #: ", font=font_regular, fill="black")
draw.text((148, 55), "3823", font=font_bold, fill="black")
y += 30

# Ready Time
draw.text((30, y), "Ready at: 21-Apr", font=font_regular, fill="black")
draw.text((155, 85), "05:16 PM", font=font_bold, fill="black")
y += 25

# Black bar with item info
bar_height = 35
draw.rectangle([(10, y), (width - 10, y + bar_height)], fill="black")
draw.text((width // 2 - 55, y + 5), "Item 3 / 3", font=font_bold, fill="white")
y += bar_height + 30

# Item Name
draw.text(
    (width // 2, y), "Large Vegetarian", font=font_large_bold, fill="black", anchor="mm"
)
y += 35
draw.text((width // 2, y), "Kebab", font=font_large_bold, fill="black", anchor="mm")
y += 40

# Item Details
font_regular = ImageFont.truetype("arial.ttf", 20)
draw.text(
    (width // 2, y), "Falafel, Halloumi", font=font_regular, fill="black", anchor="mm"
)
y += 30
font_regular = ImageFont.truetype("arial.ttf", 20)
draw.text(
    (width // 2, y),
    "Garlic Aioli, Satay, Peri",
    font=font_regular,
    fill="black",
    anchor="mm",
)
y += 30
draw.text((width // 2, y), "Peri", font=font_regular, fill="black", anchor="mm")


# Save the image
image.save("itemOrder3.png")

# Show the image
image.show()
