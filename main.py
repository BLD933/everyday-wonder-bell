import sys
from pathlib import Path

sentence = "A bead of water clinging to the tap magnifies the grout line behind it into a tiny wavering river."

# Use command line argument for output directory or default to /output
output_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/output")
output_file = output_dir / "entry.txt"

output_dir.mkdir(parents=True, exist_ok=True)

with output_file.open("w", encoding="utf-8") as f:
    f.write(sentence)

# Set file mode to 0644
output_file.chmod(0o644)
