from PIL import Image, ImageDraw, ImageFont
import json
# JSON-like data structure
json_data = [
    {"text": "windcave (Paid)"},
    {"text": "Scheduled Order"},
    {"text": "Pick-up"},
]

# Order Details
order_details = [
    ("Order #", "3110"),
    ("Placed At:", "Mar 11 10:08 AM"),
    ("Ready At:", "11 Mar 2025 6:30 PM"),
]

# Image properties
image_width, height = 789, 2472
text_color = (255, 255, 255)  # White text
box_color = (0, 0, 0)  # Black background
table_text_color = (0, 0, 0)  # Black text for table
# Create a blank white image
image = Image.new("RGB", (image_width, height), "white")
draw = ImageDraw.Draw(image)


# ================== Font Settings ==================
try:
    font = ImageFont.truetype(
        "arialbd.ttf", 35
    )  # Main headings (e.g., "Windcave (Paid)")
    bold_font = ImageFont.truetype("arialbd.ttf", 32)  # Table headers and key labels
    regular_font = ImageFont.truetype("arial.ttf", 28)  # Table values and sub-items
    total_font = ImageFont.truetype("arialbd.ttf", 34)  # Totals table text
except IOError:
    # Fallback to default fonts if needed
    font = ImageFont.load_default()
    bold_font = ImageFont.load_default()
    regular_font = ImageFont.load_default()
    total_font = ImageFont.load_default()

# ================== Header Section ==================
# Box & Text Settings
padding = 48
line_spacing = 20
x, y = 30, 30  # Initial position

# Draw text with black background
for item in json_data:
    text = item["text"]

    # Get text size
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]

    # Draw black background rectangle (full width)
    box_height = text_height + padding  # Adjusted
    draw.rectangle([x, y, image_width - x, y + box_height], fill=box_color)

    text_x = x + 20  # Left alignment ko fix karna
    text_y = y + (box_height - text_height) // 3

    # Draw white text
    draw.text((text_x, text_y), text, font=font, fill=text_color)

    # Move Y down for next item
    y += box_height + line_spacing

# ================== Order Details Table ==================#
table_x, table_y = 30, y  # Position below headings
row_height = 75
col_widths = [222, 500]  # Column widths

# Draw table rows
for row in order_details:
    if row[0] == "Ready At:":
        draw.rectangle(
            [250, table_y, table_x + image_width - 60, table_y + row_height],
            fill=box_color,
            outline="black",
            width=1,
        )
        # Redraw top border manually if needed
        "Ready At:"  # Red text
        draw.rectangle(
            [table_x, table_y, table_x + image_width - 60, table_y + row_height],
            outline="black",
            width=1,
        )
        text_fill = "white"  # White text
    else:
        draw.rectangle(
            [table_x, table_y, table_x + image_width - 60, table_y + row_height],
            outline="black",
            width=1,
        )
        text_fill = table_text_color  # Black text

    # Draw vertical line
    col_x = table_x + col_widths[0]
    draw.line([(col_x, table_y), (col_x, table_y + row_height)], fill="black", width=2)

    # Draw header (always black text)
    draw.text(
        (table_x + 30, table_y + 15), row[0], font=bold_font, fill=table_text_color
    )

    # Split value into normal and bold parts
    value_parts = row[1].split(" ")
    normal_text = " ".join(value_parts[:-2])
    bold_text = " ".join(value_parts[-2:])

    # Draw normal text
    text_x = table_x + col_widths[0] + 30
    draw.text(
        (text_x, table_y + 15), normal_text + " ", font=regular_font, fill=text_fill
    )

    # Draw bold text separately
    if bold_text:
        bbox_regular = draw.textbbox((0, 0), normal_text + " ", font=regular_font)
        bold_text_x = text_x + (bbox_regular[2] - bbox_regular[0])
        draw.text(
            (bold_text_x, table_y + 15), bold_text, font=bold_font, fill=text_fill
        )

    # Move to next row
    table_y += row_height

# ================== Client Info ==================
# Set positions
label_x = 30  # Left side for labels
value_x = 400  # Adjust this to move values to the right
y_position = 571  # Adjust the starting y position
# Constants
row_height = 30
font_path = "arial.ttf"  # Change to your font path

# Customer Information
customer_info = [
    ("Name:", "BRIAR PIERCE"),
    ("Email:", "bellpatch213@gmail.com"),
    ("Contact:", "+64223988249"),
]
# Draw client info header
draw.text((label_x, y_position), "Client Info:", font=bold_font, fill="black")
y_position += 55  # Move to next line

# Draw each field with spacing
for label, value in customer_info:
    draw.text(
        (label_x, y_position), label, font=bold_font, fill="black"
    )  # Bold left side

    # Get text width
    value_width = draw.textbbox((0, 0), value, font=regular_font)[2]

    # Set right-aligned position
    draw.text(
        (image_width - value_width - 30, y_position),
        value,
        font=regular_font,
        fill="black",
    )

    y_position += 50  # Move to next line

# ================== Items Table ==================
# --- Draw Table ---
col_widths = [80, 313, 167, 168]  # Qty, Desc, Unit Price, Subtotal
table_y = y_position + 5  # Start table after customer info with spacing
row_height = 60  # Reasonable row height
header_height = 70  # Header row height
total_width = sum(col_widths)
total_height = row_height * len("items")  # Total height of the table

# Draw outer border (bold)
draw.rectangle(
    [
        table_x,
        table_y,
        table_x + sum(col_widths),
        table_y,
    ],
    outline="black",
    width=3,
)

# Draw table header background
draw.rectangle(
    [table_x, table_y, table_x + sum(col_widths), table_y + header_height],
    fill=(240, 242, 245),
)

# Draw header text and borders
headers = ["Qty", "Name/Description", "Unit Price", "Sub Total"]
current_x = table_x
for i, (header, width) in enumerate(zip(headers, col_widths)):
    # Draw column border
    draw.rectangle(
        [current_x, table_y, current_x + width, table_y + header_height],
        outline="black",
        width=1,
    )

    # Center text in header
    text_bbox = draw.textbbox((0, 0), header, font=bold_font)
    text_x = current_x + (width - (text_bbox[2] - text_bbox[0])) // 2
    text_y = table_y + (header_height - (text_bbox[3] - text_bbox[1])) // 2
    draw.text((text_x, text_y), header, font=bold_font, fill=(80, 90, 100))

    current_x += width

# Draw item rows
table_y += header_height  # Move to first data row
items = [
    {
        "quantity": 1,
        "name": "Loaded Fries",
        "unit_price": "$13.50",
        "sub_total": "$13.50",
        "sub_items": [
            {
                "name": "Large with cheese",
                "unit_price": "$12.50",
                "sub_total": "$12.50",
            },
            {"name": "Chicken", "unit_price": "$0.00", "sub_total": "$0.00"},
            {"name": "Lamb", "unit_price": "$0.00", "sub_total": "$0.00"},
            {"name": "Garlic Yoghurt", "unit_price": "$0.00", "sub_total": "$0.00"},
            {"name": "Satay", "unit_price": "$0.00", "sub_total": "$0.00"},
            {"name": "Mild Chilli", "unit_price": "$0.00", "sub_total": "$0.00"},
        ],
        "rowspan": 7,
    },
    {
        "quantity": 1,
        "name": "Loaded Fries",
        "unit_price": "$13.50",
        "sub_total": "$13.50",
        "sub_items": [
            {"name": "Kids'", "unit_price": "$0.00", "sub_total": "$0.00"},
            {"name": "Chicken", "unit_price": "$0.00", "sub_total": "$0.00"},
            {"name": "Satay", "unit_price": "$0.00", "sub_total": "$0.00"},
            {"name": "Mild Chilli", "unit_price": "$0.00", "sub_total": "$0.00"},
        ],
        "rowspan": 5,
    },
    {
        "quantity": 1,
        "name": "Loaded Fries",
        "unit_price": "$13.50",
        "sub_total": "$13.50",
        "sub_items": [
            {"name": "Kids' with cheese", "unit_price": "$1.50", "sub_total": "$1.50"},
            {"name": "Chicken", "unit_price": "$0.00", "sub_total": "$0.00"},
            {"name": "Garlic Yoghurt", "unit_price": "$0.00", "sub_total": "$0.00"},
            {"name": "Satay", "unit_price": "$0.00", "sub_total": "$0.00"},
            {"name": "Mild Chilli", "unit_price": "$0.00", "sub_total": "$0.00"},
        ],
        "rowspan": 6,
    },
]
for item in items:
    total_height = row_height * len(items)  # Total height of the table
    # --- Main item row ---
    current_x = table_x
    values = [
        str(item["quantity"]),
        item["name"],
        item["unit_price"],
        item["sub_total"],
    ]

    for i, (value, width) in enumerate(zip(values, col_widths)):
        draw.rectangle(
            [current_x, table_y, current_x + width, table_y + row_height],
            outline="black",
            width=1,
        )

        # Bold font for main item name
        font = bold_font if i == 1 else regular_font
        text_bbox = draw.textbbox((0, 0), value, font=font)

        if i == 1:
            text_x = current_x + 10
        else:
            text_x = current_x + (width - (text_bbox[2] - text_bbox[0])) // 2

        text_y = table_y + (row_height - (text_bbox[3] - text_bbox[1])) // 2
        draw.text((text_x, text_y), value, font=font, fill=("black"))
        current_x += width

    table_y += row_height

    # --- Sub-items ---
    for sub in item["sub_items"]:
        current_x = table_x
        values = ["-", sub["name"], sub["unit_price"], sub["sub_total"]]

        for i, (value, width) in enumerate(zip(values, col_widths)):
            draw.rectangle(
                [current_x, table_y, current_x + width, table_y + row_height],
                outline="black",
                width=1,
            )
            text_bbox = draw.textbbox((0, 0), value, font=regular_font)

            if i == 1:
                text_x = current_x + 30
            else:
                text_x = current_x + (width - (text_bbox[2] - text_bbox[0])) // 2

            text_y = table_y + (row_height - (text_bbox[3] - text_bbox[1])) // 2
            draw.text((text_x, text_y), value, font=regular_font, fill=("black"))
            current_x += width

        table_y += row_height

# ================== Totals Table ==================
labels = ["Sub Total", "GST [15% included]", "Order Total"]
values = ["$54.50", "$7.11", "$54.50"]
col_widths = [560, 170]  # Label and value columns
row_height = 63
table_x = 30
table_y = 1969
total_width = sum(col_widths)
total_height = row_height * len(labels)

total_font = ImageFont.truetype("arialbd.ttf", 28)  # Totals table text

# Draw outer border (bold)
draw.rectangle(
    [table_x, table_y, table_x + total_width, table_y + total_height],
    outline="black",
    width=3,
)

padding = 20
for i in range(len(labels)):
    row_y = table_y + i * row_height

    # --- Draw Label Cell ---
    draw.rectangle(
        [table_x, row_y, table_x + col_widths[0], row_y + row_height],
        outline="black",
        width=1,
    )
    # Center text horizontally and vertically
    text_bbox = draw.textbbox((0, 0), labels[i], font=total_font)
    text_width = text_bbox[2] - text_bbox[1]  # Correct width calculation (right - left)
    text_x = (
        table_x + (col_widths[0] - text_width) // 1 - padding
    )  # Add padding to move right  # Center in label column
    text_y = row_y + (row_height - (text_bbox[3] - text_bbox[1])) // 2
    draw.text((text_x, text_y), labels[i], font=total_font, fill="black")

    # --- Draw Value Cell ---
    draw.rectangle(
        [table_x + col_widths[0], row_y, table_x + total_width, row_y + row_height],
        outline="black",
        width=1,
    )
    # Center text horizontally and vertically
    value_bbox = draw.textbbox((0, 0), values[i], font=font)
    value_x = (
        table_x + col_widths[0] + (col_widths[1] - (value_bbox[2] - value_bbox[0])) // 2
    )
    value_y = row_y + (row_height - (value_bbox[3] - value_bbox[1])) // 2
    draw.text((value_x, value_y), values[i], font=font, fill="black", font_size=50)

# ================== Address ==================
# Define fonts with appropriate sizes (adjust "arialbd.ttf" to your font path)
bold_font_large = ImageFont.truetype("arialbd.ttf", 30)  # For restaurant name
bold_font_medium = ImageFont.truetype("arialbd.ttf", 30)  # For address
bold_font_small = ImageFont.truetype("arialbd.ttf", 30)  # For phone number

# Address lines (corrected to match original image text)
address_lines = [
    ("Assyrian Kebab House", bold_font_large, 30, height - 260),
]  # Larger font for name
# Draw each line with left alignment
for text, font, x, y in address_lines:
    draw.text((x + 200, y), text, font=font, fill="black")

address_lines = [
    ("119 Kapiti Road Paraparaumu 5032", bold_font_medium, 30, height - 209),
]  # Medium font for address
# Draw each line with left alignment
for text, font, x, y in address_lines:
    draw.text((x + 100, y), text, font=font, fill="black")

address_lines = [
    ("+64 4 902 5770", bold_font_small, 30, height - 150)
]  # Smaller font for phone
for text, font, x, y in address_lines:
    draw.text((x + 250, y), text, font=font, fill="black")

# Save and show
image.save("generated_image.png")
image.show()
