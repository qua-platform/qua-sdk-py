from pathlib import Path
import re


def get_version_from_toml():
    version_regex = re.compile(r"\s*version\s*=\s*[\"']\s*([-.\w]{3,})\s*[\"']\s*")
    dir = Path(__file__).parent.parent.parent
    dir /= "pyproject.toml"
    with dir.open(mode="r") as f:
        for line in f:
            match = version_regex.search(line)
            if match is not None:
                return match.group(1).strip()
    return ""


def test_version_match():
    import qua

    toml_version = get_version_from_toml()
    assert toml_version == qua.__version__
