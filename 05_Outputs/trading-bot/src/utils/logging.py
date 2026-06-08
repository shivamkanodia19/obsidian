"""Structured logging setup."""
from __future__ import annotations

import logging
import sys
from pathlib import Path


_LOG_DIR = Path(__file__).parent.parent.parent / "logs"
_LOG_DIR.mkdir(exist_ok=True)

_configured = False


def _configure() -> None:
    global _configured
    if _configured:
        return
    fmt = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    logging.basicConfig(
        level=logging.INFO,
        format=fmt,
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(_LOG_DIR / "trading.log", encoding="utf-8"),
        ],
    )
    _configured = True


def get_logger(name: str) -> logging.Logger:
    _configure()
    return logging.getLogger(name)
