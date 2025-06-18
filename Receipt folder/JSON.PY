from PIL import Image, ImageDraw, ImageFont
import json

# Load JSON
with open("Receipt1.txt", "r") as file:
    data = json.load(file)["data"]

# Image setup
img_width, img_height = 800, 2500
image = Image.new("RGB", (img_width, img_height), "white")
draw = ImageDraw.Draw(image)

# Fonts
try:
    bold = ImageFont.truetype("arialbd.ttf", 30)
    regular = ImageFont.truetype("arial.ttf", 26)
except:
    bold = ImageFont.load_default()
    regular = ImageFont.load_default()

x, y = 30, 30

# Header Section
draw.text((x, y), f"{data['payment_method']} (Paid)", font=bold, fill="black"); y += 40
draw.text((x, y), data['requested_pick_up_time'], font=bold, fill="black"); y += 40
draw.text((x, y), "Pick-up", font=bold, fill="black"); y += 60

# Order Details
draw.text((x, y), f"Order #: {data['order_number']}", font=bold, fill="black"); y += 35
draw.text((x, y), f"Ready At: {data['confirmed_pick_up_time']}", font=regular, fill="black"); y += 50

# Customer Info
draw.text((x, y), "Client Info:", font=bold, fill="black"); y += 35
draw.text((x, y), f"Name: {data['customer_name']}", font=regular, fill="black"); y += 30
draw.text((x, y), f"Email: {data['customer_email']}", font=regular, fill="black"); y += 30
draw.text((x, y), f"Phone: {data['customer_phone']}", font=regular, fill="black"); y += 50

# Items
draw.text((x, y), "Items:", font=bold, fill="black"); y += 35
for item in data['items']:
    draw.text((x, y), f"{item['quantity']} x {item['name']} - ${item['sub_total']}", font=regular, fill="black"); y += 30
    for sub in item.get("sub_items", []):
        draw.text((x + 30, y), f"• {sub['name']} (${sub['sub_total']})", font=regular, fill="gray"); y += 25
    y += 10

# Totals
y += 20
draw.text((x, y), "Total Summary:", font=bold, fill="black"); y += 35
for total in data['order_totals']:
    draw.text((x, y), f"{total['title']}: ${total['value']}", font=regular, fill="black"); y += 30

# Address
y += 40
restaurant = data["restaurant_info"]
draw.text((x, y), restaurant["name"], font=bold, fill="black"); y += 30
draw.text((x, y), restaurant["address"], font=regular, fill="black"); y += 30
draw.text((x, y), restaurant["phone"], font=regular, fill="black"); y += 30

# Save and show
image = image.crop((0, 0, img_width, y + 50))  # Crop unused space
image.save("receipt_output.png")
image.show()
restaurant = data["restaurant_info"]  # Ensure this exists

restaurant_info = [
    (str(restaurant["name"]), bold_font_large, 30, height - 260),
    (str(restaurant["address"]), bold_font_medium, 30, height - 209),
    (str(restaurant["phone"]), bold_font_small, 30, height - 150),
]

for text, font, x, y in restaurant_info:
    print(f"text = {text}, type = {type(text)}")  # For debugging
    draw.text((x + 200, y), text, font=font, fill="black")
