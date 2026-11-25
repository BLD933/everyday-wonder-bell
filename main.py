from pathlib import Path
import sys


SENTENCE = (
    "When I lift my cup, the spoon rings once against the rim, "
    "and the kitchen has a bell small enough to stir with."
)


def main() -> None:
    output = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/output")
    output.mkdir(parents=True, exist_ok=True)
    entry = output / "entry.txt"
    entry.write_text(SENTENCE, encoding="utf-8")
    entry.chmod(0o644)


if __name__ == "__main__":
    main()
