import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from core import ask, deliver
from config import NICHE

out = ask(
    "Marketing Manager",
    f"Write today's marketing pack for the niche '{NICHE}':\n"
    "- 5 short social media posts (varied: tip, question, mini-story, before/after, soft promo)\n"
    "- 1 SEO blog article outline with title, headings, and a 150-word intro\n"
    "Do not make up testimonials or statistics. Keep it useful, not spammy.",
    max_tokens=2500,
)
deliver("marketer", out)
