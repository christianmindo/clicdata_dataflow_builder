"""Build a portable skill ZIP from tracked reference materials only."""
import argparse
from pathlib import Path
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]
NAME = "clicdata-dataflow-builder"
FILES = {"SKILL.md", "AGENTS.md", "scripts/lint_flow.py",
         "scripts/read_schema.py", "scripts/style_flow.py"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=ROOT / "dist" / f"{NAME}.zip")
    args = parser.parse_args()
    tracked = subprocess.check_output(
        ["git", "ls-files", "-z"], cwd=ROOT).decode().split("\0")
    selected = sorted(p for p in tracked if p in FILES or
                      p.startswith(("reference/", "examples/")))
    missing = FILES - set(selected)
    if missing:
        raise SystemExit(f"Required skill files are not tracked: {sorted(missing)}")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(args.output, "w", zipfile.ZIP_DEFLATED) as archive:
        for relative in selected:
            source = ROOT / relative
            if source.is_symlink() or not source.is_file():
                raise SystemExit(f"Expected a regular file: {relative}")
            info = zipfile.ZipInfo(f"{NAME}/{relative}", (2020, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, source.read_bytes())
    print(f"Built {args.output} ({len(selected)} files)")


if __name__ == "__main__":
    main()
