from pathlib import Path


template = Path("common/mail/subscription-expired.php").read_text()

required_snippets = [
    "$safeAgentName = Html::encode($agent_name);",
    "$safeStoreName = Html::encode($store->name);",
    "$safeTitle = Html::encode($store->name . ' has been downgraded to our free plan');",
    "<?= $safeTitle ?>",
    "Hello <?= $safeAgentName ?>,",
    "<?= $safeStoreName ?> has been downgraded to our free plan",
]

for snippet in required_snippets:
    if snippet not in template:
        raise SystemExit(f"missing expected hardening snippet: {snippet}")

for raw_snippet, message in [
    ("<?= $store->name ?> has been downgraded to our free plan", "store name still renders raw"),
    ("Hello <?= $agent_name ?>,", "agent name still renders raw"),
]:
    if raw_snippet in template:
        raise SystemExit(message)

print("subscription expired email rendering is escaped")
