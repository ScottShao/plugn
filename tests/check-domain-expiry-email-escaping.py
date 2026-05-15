from pathlib import Path


template = Path("common/mail/store/domain-will-expire-soon-html.php").read_text()

required_snippets = [
    "$safeSubscriptionDomain = Html::encode($subscription->domain);",
    "$safeStoreName = Html::encode($store->name);",
    "<?= $safeSubscriptionDomain ?> Expiring",
    "<?= $safeSubscriptionDomain ?> for your store <?= $safeStoreName ?> will expire in 14 days.",
]

for snippet in required_snippets:
    if snippet not in template:
        raise SystemExit(f"missing expected hardening snippet: {snippet}")

for raw_snippet, message in [
    ("<?= $subscription->domain ?> Expiring", "hero heading still renders raw domain"),
    ("<?= $subscription->domain ?> for your store <?= $store->name ?> will expire in 14 days.", "body still renders raw domain/store values"),
]:
    if raw_snippet in template:
        raise SystemExit(message)

print("domain expiry email rendering is escaped")
