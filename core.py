import os, datetime, pathlib, requests, anthropic
from config import BUSINESS

MODEL = "claude-sonnet-5-5"
QUEUE = pathlib.Path(__file__).parent / "queue"


def ask(role, task, max_tokens=1500):
    """Ask Claude to do a job as one of your 'employees'."""
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    r = client.messages.create(
        model=MODEL,
        max_tokens=max_tokens,
        system=(
            f"You are the {role} of {BUSINESS}. Be practical and specific. "
            "Never invent fake reviews, fake statistics, or fake testimonials."
        ),
        messages=[{"role": "user", "content": task}],
    )
    return r.content[0].text


def notify(text):
    """Send a message to your Telegram. Prints instead if Telegram isn't set up."""
    token = os.environ.get("TELEGRAM_TOKEN")
    chat = os.environ.get("TELEGRAM_CHAT_ID")
    if not token or not chat:
        print("[Telegram not configured]\n", text)
        return
    requests.post(
        f"https://api.telegram.org/bot{token}/sendMessage",
        json={"chat_id": chat, "text": text[:4000]},
        timeout=30,
    )


def save_draft(agent, content):
    """Save the draft in the queue/ folder so you can review it before using it."""
    QUEUE.mkdir(exist_ok=True)
    stamp = datetime.datetime.utcnow().strftime("%Y-%m-%d-%H%M")
    path = QUEUE / f"{stamp}-{agent}.md"
    path.write_text(content, encoding="utf-8")
    return path


def deliver(agent, content):
    save_draft(agent, content)
    notify(f"[{agent.upper()} draft - needs your review]\n\n{content}")
