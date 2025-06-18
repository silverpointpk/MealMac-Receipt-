import json
from PIL import Image, ImageDraw, ImageFont

# Load JSON data
with open("Receipt1.txt", "r") as f:
    data = json.load(f)

# Create blank receipt image
img = Image.new("RGB", (500, 300), color="white")
draw = ImageDraw.Draw(img)
font = ImageFont.load_default()

# Header
draw.text(
    (10, 10),
    "Qty    Name                  Unit Price    Sub Total",
    fill="black",
    font=font,
)

# Draw each item
y = 40
for item in data["items"]:
    qty = str(item.get("quantity", ""))
    name = item.get("name", "")
    unit_price = item.get("unit_price", "")
    sub_total = item.get("sub_total", "")

    # Print each column
    draw.text((10, y), qty, fill="black", font=font)
    draw.text((60, y), name, fill="black", font=font)
    draw.text((250, y), unit_price, fill="black", font=font)
    draw.text((350, y), sub_total, fill="black", font=font)
    y += 20

# Save the receipt image
img.save("receipt_output.png")

items = [
    ("Qty", str(item.get("quantity", ""))),
    ("name", item.get("name", "")),
    ("unit_price", item.get("unit_price", "")),
    ("sub_total", item.get("sub_total", "")),
    ("sub_items", item.get("sub_items", [])),
    ("rowspan", item.get("rowspan", 1)),
    "sub_items",
    [
        {
            ("name", item["name"]),
            ("unit_price", item["unit_price"]),
            ("sub_total", item["sub_total"]),
        },
        {
            ("name", item["name"]),
            ("unit_price", item["unit_price"]),
            ("sub_total", item["sub_total"]),
        },
        {
            ("name", item["name"]),
            ("unit_price", item["unit_price"]),
            ("sub_total", item["sub_total"]),
        },
        {
            ("name", item["name"]),
            ("unit_price", item["unit_price"]),
            ("sub_total", item["sub_total"]),
        },
        {
            ("name", item["name"]),
            ("unit_price", item["unit_price"]),
            ("sub_total", item["sub_total"]),
        },
        {
            ("name", item["name"]),
            ("unit_price", item["unit_price"]),
            ("sub_total", item["sub_total"]),
        },
    ],
    "rowspan",
    7,
    {
        ("Qty:", item.get["quantity"])("name", item["name"]),
        ("unit_price", item["unit_price"]),
        ("sub_total", item["sub_total"]),
        ("sub_items", item.get("sub_items", [])),
        ("rowspan", item.get("rowspan", 1)),
        "sub_items",
        [
            {
                ("name", item["name"]),
                ("unit_price", item["unit_price"]),
                ("sub_total", item["sub_total"]),
            },
            {
                ("name", item["name"]),
                ("unit_price", item["unit_price"]),
                ("sub_total", item["sub_total"]),
            },
            {
                ("name", item["name"]),
                ("unit_price", item["unit_price"]),
                ("sub_total", item["sub_total"]),
            },
            {
                ("name", item["name"]),
                ("unit_price", item["unit_price"]),
                ("sub_total", item["sub_total"]),
            },
        ],
        "rowspan",
        5,
    },
    {
        ("Qty:", item.get["quantity"])("name", item["name"]),
        ("unit_price", item["unit_price"]),
        ("sub_total", item["sub_total"]),
        ("sub_items", item.get("sub_items", [])),
        ("rowspan", item.get("rowspan", 1)),
        "sub_items",
        [
            {
                ("name", item["name"]),
                ("unit_price", item["unit_price"]),
                ("sub_total", item["sub_total"]),
            },
            {
                ("name", item["name"]),
                ("unit_price", item["unit_price"]),
                ("sub_total", item["sub_total"]),
            },
            {
                ("name", item["name"]),
                ("unit_price", item["unit_price"]),
                ("sub_total", item["sub_total"]),
            },
            {
                ("name", item["name"]),
                ("unit_price", item["unit_price"]),
                ("sub_total", item["sub_total"]),
            },
            {
                ("name", item["name"]),
                ("unit_price", item["unit_price"]),
                ("sub_total", item["sub_total"]),
            },
        ],
        "rowspan",
        6,
    },
]
