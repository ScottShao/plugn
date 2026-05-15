from pathlib import Path


view = Path("frontend/views/bank-discount/index.php").read_text()

if '"attribute" => "bank_name"' not in view:
    raise SystemExit("bank_name column not found")

if '"format" => "raw",' in view.split('"attribute" => "bank_name"', 1)[0][-120:]:
    raise SystemExit("bank_name column still renders as raw")

if "return $model->bank->bank_name;" not in view:
    raise SystemExit("bank_name value callback changed unexpectedly")

print("Bank discount name escaping guard passed.")
