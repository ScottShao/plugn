from pathlib import Path


template = Path("common/mail/subscription-will-expire-soon-html.php").read_text()

required_snippets = [
    "$safeAgentName = Html::encode($agent_name);",
    "$safePlan = Html::encode($plan);",
    "$safeStoreName = Html::encode($store->name);",
    "$safeTitle = Html::encode($plan . ' for ' . $store->name . ' will expire in 5 days');",
    "$safeExtendPlanLabel = Html::encode('Extend my ' . $plan);",
    "<?= $safeTitle ?>",
    "Hello <?= $safeAgentName ?>,",
    "<?= $safePlan ?> for your store <?= $safeStoreName ?> will expire in 5 days.",
    "Html::a($safeExtendPlanLabel, $extendPlanUrl ,",
]

for snippet in required_snippets:
    if snippet not in template:
        raise SystemExit(f"missing expected hardening snippet: {snippet}")

for raw_snippet, message in [
    ("<?= $plan ?> for <?= $store->name ?> will expire in 5 days", "title still renders raw plan/store values"),
    ("Hello <?= $agent_name ?>,", "greeting still renders raw agent name"),
    ("<?= $plan ?> for your store <?= $store->name ?> will expire in 5 days.", "body still renders raw plan/store values"),
    ("Html::a('Extend my ' . $plan, $extendPlanUrl ,", "CTA label still renders raw plan value"),
]:
    if raw_snippet in template:
        raise SystemExit(message)

print("subscription expiry email rendering is escaped")
