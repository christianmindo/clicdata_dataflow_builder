"""Check the public release and cache a verified current skill copy (stdlib only)."""
import argparse
import hashlib
import io
import json
from pathlib import Path
import shutil
import tempfile
import urllib.request
import zipfile

BASE = "https://raw.githubusercontent.com/christianmindo/clicdata_dataflow_builder/main/dist/"
NAME = "clicdata-dataflow-builder"


def fetch(name):
    with urllib.request.urlopen(BASE + name, timeout=30) as response:
        return response.read()


def sync(cache):
    manifest = json.loads(fetch(NAME + ".version.json"))
    version = manifest["version"]
    if len(version) != 64 or any(c not in "0123456789abcdef" for c in version):
        raise ValueError("Invalid release version")
    target = cache / version / NAME
    if (target / "VERSION.json").is_file():
        if json.loads((target / "VERSION.json").read_text())["version"] == version:
            return {"status": "current", "version": version, "path": str(target.resolve())}
    installed = Path(__file__).resolve().parents[1]
    if (installed / "VERSION.json").is_file():
        if json.loads((installed / "VERSION.json").read_text())["version"] == version:
            return {"status": "current", "version": version, "path": str(installed)}
    payload = fetch(NAME + ".zip")
    if hashlib.sha256(payload).hexdigest() != manifest["sha256"]:
        raise ValueError("Release checksum mismatch; retry after publication completes")
    cache.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=cache) as staging:
        with zipfile.ZipFile(io.BytesIO(payload)) as archive:
            for entry in archive.infolist():
                path = Path(entry.filename)
                if path.is_absolute() or ".." in path.parts or not path.parts or path.parts[0] != NAME:
                    raise ValueError("Unsafe ZIP path")
                if (entry.external_attr >> 16) & 0o170000 == 0o120000:
                    raise ValueError("ZIP symlinks are not supported")
            archive.extractall(staging)
        source = Path(staging) / NAME
        if json.loads((source / "VERSION.json").read_text())["version"] != version:
            raise ValueError("Bundled version mismatch")
        for required in ("SKILL.md", "AGENTS.md", "scripts/lint_flow.py"):
            if not (source / required).is_file():
                raise ValueError(f"Incomplete release: {required}")
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists():
            raise ValueError("Existing cache is incomplete; choose a fresh cache directory")
        shutil.move(str(source), target)
    return {"status": "updated", "version": version, "path": str(target.resolve())}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache", type=Path, required=True,
                        help="Writable cache outside the installed skill and client artifacts")
    args = parser.parse_args()
    try:
        print(json.dumps(sync(args.cache)))
    except Exception as error:
        print(json.dumps({"status": "unavailable", "error": str(error)}))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
