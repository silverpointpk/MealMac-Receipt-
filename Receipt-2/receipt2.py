from PIL import Image, ImageDraw, ImageFont

# Image setup
width = 350
height = 1000
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Fonts
try:
    font_regular = ImageFont.truetype("arial.ttf", 14)
    font_bold = ImageFont.truetype("arialbd.ttf", 20)
except:
    font_regular = ImageFont.load_default()
    font_bold = ImageFont.load_default()

y = 10

# Header boxes
def draw_header(text):
    global y
    left = 10
    draw.rectangle([(left, y), (width - 10, y + 30)], fill="black")
    left =20
    draw.text((width//left, y + 5), text, font=font_bold, fill="white")
    y += 38

draw_header("windcave (Paid)")
draw_header("ASAP")
draw_header("Pick-up")

# Order info block
font_regular = ImageFont.truetype("arial.ttf", 14)
font_bold = ImageFont.truetype("arialbd.ttf", 14, encoding="unic")

table_x, table_y = 30, y  # Position below headings
row_height = 75
col_widths = [60, 500]  # Column widths

#Draw vertical line
col_x = table_x + col_widths[0]
draw.line([(col_x, table_y), (col_x, table_y + row_height)], fill="black", width=1)

font_regular = ImageFont.truetype("arial.ttf", 14)
draw.rectangle([(10, y), (width - 10 , y + 25)], outline="black",width=1)
draw.text((15, 130), "Order #: ", font=font_bold, fill="black")
draw.text((100, 130), "3823", font=font_regular, fill="black")
y += 25
draw.rectangle([(10, y), (width - 10 , y + 25)], outline="black",width=1)
draw.text((15, 155), "Placed at:", font=font_bold, fill="black")
draw.text((100, 155), "21-Apr 04:55 PM", font=font_regular, fill="black")
y += 25
draw.rectangle([(10, y), (width - 10 , y + 25)], outline="black",width=1,)
draw.text((15, 180), "Ready at:", font=font_bold, fill="black")
draw.rectangle([(90, y), (width - 10 , y + 25)], outline="black",width=1, fill="black")
draw.text((100, 180), "21-Apr 05:16 PM", font=font_regular, fill="White")
y += 35

# Client info
draw.text((10, y), "Client Info:", font=font_bold, fill="black")
y += 20
draw.text((10, y), "Name:", font=font_regular, fill="black")
draw.text((250, y), "Alexis Leader", font=font_regular, fill="black")
y += 20
draw.text((10, y), "Email:", font=font_regular, fill="black")
draw.text((160, y), "alexis.aj.leader@gmail.com", font=font_regular, fill="black")
y += 20
draw.text((10, y), "Contact:", font=font_regular, fill="black")
draw.text((240, y), "+64274981957", font=font_regular, fill="black")
y += 20

# ================== Items Table ==================
font_regular = ImageFont.truetype("arial.ttf", 14)
font_bold = ImageFont.truetype("arialbd.ttf", 15, encoding="unic")

table_x, table_y = 30, y  # Position below headings
col_widths = [40, 500]  # Column widths
draw.rectangle([(10, y), (width - 10 , y + 25)], outline="black",width=1)
col_x = 1 + col_widths[0]
draw.line([(col_x, table_y), (col_x, table_y + row_height)], fill="black", width=1)
draw.text((14, 295), "Qty", font=font_bold, fill="black")

col_x = 175
draw.line([(col_x, table_y), (col_x, table_y + row_height)], fill="black", width=1)
draw.text((45,  295), "Name/Description", font=font_bold, fill="black")

draw.line([(col_x, table_y), (col_x, table_y + row_height)], fill="black", width=1)
draw.text((178,  295), "Unit Price", font=font_bold, fill="black")
col_x = 180

draw.line([(col_x, table_y), (col_x, table_y + row_height)], fill="black", width=1)
draw.text((265 , 295), "Sub Total", font=font_bold, fill="black") 



y += 35


# Footer
y = height - 60
draw.text((180, y), "Assyrian Kebab House", font=font_bold, fill="black", anchor="mm")
y += 20
draw.text((180, y), "119 Kapiti Road Paraparaumu 5032", font=font_regular, fill="black", anchor="mm")
y += 15
draw.text((180, y), "+64 4 902 5770", font=font_regular, fill="black", anchor="mm")

# Save and show
image.save("full_receipt.png")
image.show()
