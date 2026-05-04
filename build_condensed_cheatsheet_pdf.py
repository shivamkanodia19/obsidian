from pathlib import Path
import subprocess
import sys

from pypdf import PdfReader


ROOT = Path(r"c:\Users\shiva\obsidian")
SOURCE = ROOT / "Spring 2026 Final Cheat Sheet - Condensed.md"
HTML = ROOT / "Spring 2026 Final Cheat Sheet - Condensed.print.html"
PDF = ROOT / "Spring 2026 Final Cheat Sheet - Condensed.pdf"
TEMPLATE = ROOT / "cheatsheet-template.html"
CHROME = Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe")


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True, cwd=ROOT)


def build_html() -> None:
    run(
        [
            "pandoc",
            str(SOURCE),
            "--standalone",
            "--template",
            str(TEMPLATE),
            "--output",
            str(HTML),
            "--metadata",
            "title=Spring 2026 Final Cheat Sheet - Condensed",
        ]
    )


def build_pdf() -> None:
    file_url = HTML.resolve().as_uri()
    run(
        [
            str(CHROME),
            "--headless=new",
            "--disable-gpu",
            "--allow-file-access-from-files",
            f"--print-to-pdf={PDF}",
            file_url,
        ]
    )


def page_count() -> int:
    return len(PdfReader(str(PDF)).pages)


def main() -> int:
    build_html()
    build_pdf()
    pages = page_count()
    print(f"pdf_pages={pages}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
