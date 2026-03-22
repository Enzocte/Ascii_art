# python
import re
from pathlib import Path

in_path = Path("../examples/result/Skull_ascii.txt")
out_path = Path("../examples/result/Skull_ascii_clean.txt")

# Matches ANSI SGR color sequences such as '\x1b[38;2;R;G;Bm' and '\x1b[0m'
ansi_sgr = re.compile(r"\x1b\[[0-9;]*m")

text = in_path.read_text(encoding="utf-8", errors="replace")
cleaned = ansi_sgr.sub("", text)
out_path.write_text(cleaned, encoding="utf-8")
print(f"Written cleaned file to {out_path}")