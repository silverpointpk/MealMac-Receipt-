from PIL import Image, ImageDraw, ImageFont

# JSON-like data structure
json_data = [
    {"text": "windcave (Paid)"},
    {"text": "Scheduled Order"},
    {"text": "Pick-up"}
]

# Order Details
order_details = [
    ("Order #", "3110"),
    ("Placed At:", "Mar 11 10:08 AM"),
    ("Ready At:", "11 Mar 2025 6:30 PM")
]

# Image properties
width, height = 789, 2472  # Adjust height dynamically if needed
bg_color = "white"
text_color = (255, 255, 255)  # White text
box_color = (0, 0, 0)  # Black background
table_text_color = (0, 0, 0)  # Black text for table
black_bg_color = (0, 0, 0)  # Black background

# Create image
image = Image.new("RGB", (width, height), bg_color)
draw = ImageDraw.Draw(image)

# Load font
try:
    font = ImageFont.truetype("arialbd.ttf", 35)  # Bold font for headings
    bold_font = ImageFont.truetype("arialbd.ttf", 30)  # Bold for table headers
    regular_font = ImageFont.truetype("arial.ttf", 30)  # Regular font for values
except IOError:
    font = ImageFont.load_default()
    bold_font = ImageFont.load_default()
    regular_font = ImageFont.load_default()

# Box & Text Settings
padding = 50
line_spacing = 15
x, y = 30, 30  # Initial position

# Draw text with black background
for item in json_data:
    text = item["text"]

    # Get text size using textbbox
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]

    # Draw black background rectangle (full width)
    draw.rectangle(
        [x, y, width - x, y + text_height + padding],
        fill=box_color)

    # Draw white text
    draw.text((x + 20, y + padding // 2.5), text, font=font, fill=text_color)

    # Move Y down for next item
    y += text_height + padding + line_spacing

    
# Table settings
table_x, table_y = 30, y  # Position below headings
row_height = 75
col_widths = [250, 500]  # Column widths

# Draw table rows
for row in order_details:
    for index, (label, value) in enumerate(order_details):
        is_last_row = index == len(order_details) - 1
    
    if row[0] == "index == 3":  
        draw.rectangle([table_x, table_y, table_x + width - 60, table_y + row_height], fill=box_color, outline="black", width=1)
        text_fill = "black"   # White text
    else:
        draw.rectangle([table_x, table_y, table_x + width - 60, table_y + row_height], outline="black", width=1)
        text_fill = table_text_color  # Black text

    # Draw vertical line
    col_x = table_x + col_widths[0]
    draw.line([(col_x, table_y), (col_x, table_y + row_height)], fill="black", width=1)

    # Draw header (always black text)
    draw.text((table_x + 30, table_y + 15), row[0], font=bold_font, fill=table_text_color)

    # Split value into normal and bold parts
    value_parts = row[1].rsplit(" ", 2)
    normal_text = " ".join(value_parts[:-2])
    bold_text = " ".join(value_parts[-2:])

    # Draw normal text
    draw.text((table_x + col_widths[0] + 10, table_y + 15), normal_text, font=regular_font, fill=text_fill)

    # Draw bold text
    bbox_regular = draw.textbbox((0, 0), normal_text + " ", font=regular_font)
    bold_text_x = table_x + col_widths[0] + 10 + (bbox_regular[2] - bbox_regular[0])
    draw.text((bold_text_x, table_y + 15), bold_text, font=bold_font, fill=text_fill)

    table_y += row_height

    
# Save and display image
image_path = "generated_image.png"
image.save(image_path)
image.show()
