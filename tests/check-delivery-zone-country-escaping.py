from pathlib import Path


view = Path("frontend/views/delivery-zone/select-area.php").read_text()

required_snippets = [
    "$safeSelectedCountry = Html::encode($selectedCountry);",
    "<?= $safeSelectedCountry ?>",
    "Html::a('Deliver all over '. $safeSelectedCountry ,",
]

for snippet in required_snippets:
    if snippet not in view:
        raise SystemExit(f"missing expected hardening snippet: {snippet}")

if "<?= $selectedCountry ?>" in view:
    raise SystemExit("selected country still renders raw in heading")

if "Html::a('Deliver all over '. $selectedCountry ," in view:
    raise SystemExit("selected country still renders raw in button label")

print("delivery-zone selected country rendering is escaped")
