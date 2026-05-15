from pathlib import Path


view = Path("backend/views/restaurant/index.php").read_text()

checks = {
    "encoded restaurant name": "Html::encode($data->name)",
    "encoded restaurant domain label": "Html::encode((string) $data->restaurant_domain)",
    "https normalization": "if (!preg_match('/^https?:\\/\\//i', $restaurantDomain))",
    "noopener noreferrer": "'rel' => 'noopener noreferrer'",
}

for label, needle in checks.items():
    if needle not in view:
        raise SystemExit(f"missing {label}")

print("Restaurant index link hardening guard passed.")
