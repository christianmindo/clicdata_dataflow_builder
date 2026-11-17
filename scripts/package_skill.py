"""Build a portable skill ZIP from tracked reference materials only."""
import argparse
from pathlib import Path
import subprocess
import zipfile
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
NAME = "clicdata-dataflow-builder"
FILES = {"SKILL.md", "AGENTS.md", "scripts/lint_flow.py",
         "scripts/read_schema.py", "scripts/style_flow.py", "scripts/sync_skill.py"}


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
    digest = hashlib.sha256()
    for relative in selected:
        digest.update(relative.encode() + b"\0" + (ROOT / relative).read_bytes() + b"\0")
    version = digest.hexdigest()
    with zipfile.ZipFile(args.output, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr(f"{NAME}/VERSION.json", json.dumps({"version": version}) + "\n")
        for relative in selected:
            source = ROOT / relative
            if source.is_symlink() or not source.is_file():
                raise SystemExit(f"Expected a regular file: {relative}")
            info = zipfile.ZipInfo(f"{NAME}/{relative}", (2020, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, source.read_bytes())
    manifest = {"version": version, "sha256": hashlib.sha256(args.output.read_bytes()).hexdigest()}
    args.output.with_suffix(".version.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"Built {args.output} ({len(selected)} files)")


if __name__ == "__main__":
    main()
