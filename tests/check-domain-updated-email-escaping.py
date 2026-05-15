from pathlib import Path


template = Path("common/mail/store/domain-updated.php").read_text()

required_snippets = [
    "use yii\\helpers\\Html;",
    "$safeStoreName = Html::encode(strtoupper($store_name));",
    "$safeOldDomain = Html::encode($old_domain);",
    "$safeNewDomain = Html::encode($new_domain);",
    "<b>Domain for <?= $safeStoreName ?></b> changed recently.",
    "Previous: <?= $safeOldDomain ?> <br/>",
    "New: <?= $safeNewDomain ?>",
]

for snippet in required_snippets:
    if snippet not in template:
        raise SystemExit(f"missing expected hardening snippet: {snippet}")

for raw_snippet, message in [
    ("<b>Domain for <?= strtoupper($store_name) ?></b> changed recently.", "store name still renders raw in heading"),
    ("Previous: <?= $old_domain ?> <br/>", "old domain still renders raw"),
    ("New: <?= $new_domain ?>", "new domain still renders raw"),
]:
    if raw_snippet in template:
        raise SystemExit(message)

print("domain updated email rendering is escaped")
