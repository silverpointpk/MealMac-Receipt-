# Draw item rows
table_y += header_height  # Move to first data row
items = [
    {
        "quantity": 1,
        "name": "Vegetarian Kebab",
        "unit_price": "$13.50",
        "sub_total": "$13.50",
        "sub_items": [
            {"name": "1 x Large","unit_price": "$4.00","sub_total": "$4.00",},
            {"name": "1 x Falafel", "unit_price": "$0.00", "sub_total": "$0.00"},
            {"name": "1 x Halloumi", "unit_price": "$0.00", "sub_total": "$0.00"},
            {"name": "1 x Mayo", "unit_price": "$0.00", "sub_total": "$0.00"},
            {"name": "1 x Satay", "unit_price": "$0.00", "sub_total": "$0.00"},],
        "rowspan": 6,
    },
    {
        "quantity": 1,
        "name": "Fries",
        "unit_price": "$6.00",
        "sub_total": "$6.00",
        "sub_items": [
            {"name": "1 x large", "unit_price": "$2.00", "sub_total": "$2.00"},],
        "rowspan": 2,
    },
    {
        "quantity": 1,
        "name": "Vegetarian Kebab",
        "unit_price": "$13.50",
        "sub_total": "$13.50",
        "sub_items": [
            {"name": "1 x Large", "unit_price": "$4.00", "sub_total": "$4.00"},
            {"name": "1 x Falafel", "unit_price": "$0.00", "sub_total": "$0.00"},
            {"name": "1 x Halloumi", "unit_price": "$0.00", "sub_total": "$0.00"},
            {"name": "1 x Garlic Aioli", "unit_price": "$0.00", "sub_total": "$0.00"},
            {"name": "1 x Satay", "unit_price": "$0.00", "sub_total": "$0.00"},
            {"name": "1 x peri peri", "unit_price": "$0.00", "sub_total": "$0.00"},
        ],
        "rowspan": 6,
    },
]

font_regular = ImageFont.truetype("arial.ttf", 14)
font_bold = ImageFont.truetype("arialbd.ttf", 14, encoding="unic")
# --- Draw Table ---
col_widths = [30, 150, 70, 70]  # Qty, Desc, Unit Price, Subtotal
headers = ["Qty", "Name/Description", "Unit Price", "Sub Total"]
table_y = y+ 5  # Start table after customer info with spacing
row_height = 20  # Reasonable row height
header_height = 20  # Header row height
total_width = sum(col_widths)
total_height = row_height * len("items")  # Total height of the table
table_x = 10  # Table x position
row=1
col=4
# Draw table header background
draw.rectangle(
    [table_x, table_y, table_x + sum(col_widths), table_y + header_height],
    fill=None, outline="black", width=1,)
draw.text((table_x + 5, table_y + 2), "Items", font=font_bold, fill="black")
table_y += header_height  # Move to the next row
# Draw table rows
