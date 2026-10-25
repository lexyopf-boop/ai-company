import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from core import ask, deliver
from config import NICHE

out = ask(
    "Product Creator",
    f"Propose ONE new digital product for the niche '{NICHE}'. Give me:\n"
    "1. Product name and a one-line pitch\n"
    "2. Who it's for and the problem it solves\n"
    "3. A full outline of what the product contains (sections/pages/fields)\n"
    "4. A suggested price with a short reason\n"
    "5. A ready-to-paste store listing (title, description, 5 bullet points)\n"
    "6. 10 SEO keywords",
    max_tokens=2500,
)
deliver("creator", out)
