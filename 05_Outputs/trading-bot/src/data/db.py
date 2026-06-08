"""
Database initialization and session management.
Uses synchronous SQLAlchemy for simplicity in V0 CLI context.
"""

from __future__ import annotations

from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from ..config import get_settings
from .models import Base

_engine = None
_SessionFactory = None


def get_engine():
    global _engine
    if _engine is None:
        settings = get_settings()
        # For CLI use, convert async URL to sync
        url = settings.database_url.replace("sqlite+aiosqlite", "sqlite")
        _engine = create_engine(url, connect_args={"check_same_thread": False})
    return _engine


def get_session_factory():
    global _SessionFactory
    if _SessionFactory is None:
        _SessionFactory = sessionmaker(bind=get_engine())
    return _SessionFactory


def init_db() -> None:
    """Create all tables. Safe to call multiple times."""
    Base.metadata.create_all(get_engine())


def get_session() -> Session:
    return get_session_factory()()
