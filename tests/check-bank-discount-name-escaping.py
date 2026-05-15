from pathlib import Path


view = Path("frontend/views/bank-discount/index.php").read_text()

parts = view.split('"attribute" => "bank_name"', 1)

if len(parts) != 2:
    raise SystemExit("bank_name column not found")

before, after = parts
column_window = before[-160:] + '"attribute" => "bank_name"' + after[:160]

if '"format" => "raw",' in column_window:
    raise SystemExit("bank_name column still renders as raw")

if "return $model->bank->bank_name;" not in view:
    raise SystemExit("bank_name value callback changed unexpectedly")

print("Bank discount name escaping guard passed.")
