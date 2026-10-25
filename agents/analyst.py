import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from core import ask, deliver

sales = pathlib.Path(__file__).resolve().parent.parent / "data" / "sales.csv"

if not sales.exists() or not sales.read_text(encoding="utf-8").strip():
    print("No data/sales.csv yet. Nothing to analyse.")
    sys.exit(0)

out = ask(
    "Business Analyst",
    "Here is my sales data (CSV):\n\n" + sales.read_text(encoding="utf-8")[:20000] +
    "\n\nGive me: (1) what's selling and what isn't, (2) the 3 most valuable actions for next week, "
    "(3) one new product idea based on the data. Be honest if the data is too small to conclude much.",
)
deliver("analyst", out)
