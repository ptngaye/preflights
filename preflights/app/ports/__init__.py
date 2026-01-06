"""
Port interfaces for PreflightsApp.

These are the boundaries between Application and Adapters.
Application depends on these interfaces (not implementations).
"""

from preflights.app.ports.clock import ClockPort
from preflights.app.ports.config import ConfigLoaderPort
from preflights.app.ports.file_context import FileContextBuilderPort
from preflights.app.ports.filesystem import FilesystemPort
from preflights.app.ports.llm import LLMPort
from preflights.app.ports.session import SessionPort
from preflights.app.ports.uid import UIDProviderPort

__all__ = [
    "ClockPort",
    "ConfigLoaderPort",
    "FileContextBuilderPort",
    "FilesystemPort",
    "LLMPort",
    "SessionPort",
    "UIDProviderPort",
]
