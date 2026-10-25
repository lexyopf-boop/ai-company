import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from core import ask, deliver

root = pathlib.Path(__file__).resolve().parent.parent
inbox = root / "support" / "inbox.txt"
faq = root / "support" / "faq.txt"

if not inbox.exists() or not inbox.read_text(encoding="utf-8").strip():
    print("No customer messages in support/inbox.txt. Nothing to do.")
    sys.exit(0)

messages = inbox.read_text(encoding="utf-8")
faq_text = faq.read_text(encoding="utf-8") if faq.exists() else "(no FAQ yet)"

out = ask(
    "Customer Support Agent",
    f"FAQ / policies:\n{faq_text}\n\nCustomer messages (separated by ---):\n{messages}\n\n"
    "Write a polite, short reply to each message. If the FAQ doesn't cover the answer, "
    "say what you'd need to check instead of guessing. Never promise refunds unless the FAQ says so.",
)
deliver("support", out)
