from pathlib import Path


view = Path("frontend/views/order/index.php").read_text()

checks = {
    "business location column": "'attribute' => 'business_location_name'",
    "payment label column": "'label' => 'Payment'",
    "business location callback": "return $model->business_location_name ? $model->business_location_name : '';",
    "payment callback": "return $data->paymentMethod->payment_method_name;",
}

for label, needle in checks.items():
    if needle not in view:
        raise SystemExit(f"missing {label}")

for forbidden in [
    "'attribute' => 'business_location_name',\n                        \"format\" => \"raw\"",
    "'label' => 'Payment',\n                        \"format\" => \"raw\"",
]:
    if forbidden in view:
        raise SystemExit("raw format still present on label field")

print("Order index label hardening guard passed.")
