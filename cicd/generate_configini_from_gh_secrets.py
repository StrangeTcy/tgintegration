import os
from pathlib import Path

examples_dir = Path("examples")

s = f"""
[pyrogram]
api_id={os.environ["API_ID"]}
api_hash={os.environ["API_HASH"]}
"""

with open(examples_dir / "config.ini", "w") as text_file:
    text_file.write(s)
