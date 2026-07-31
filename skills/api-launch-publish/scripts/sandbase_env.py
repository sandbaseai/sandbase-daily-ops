#!/usr/bin/env python3
"""Shared credential loading for the api-launch-publish scripts.

Resolution order (first value wins; an already-exported variable is never overwritten):

1. The current process environment.
2. ``--env-file`` arguments, in the order given.
3. ``$SANDBASE_ENV_FILE``.
4. ``DEFAULT_ENV_FILES`` below.

Keep credential files outside any git working tree. ``~/.config/sandbase/.env`` with
mode 0600 is the recommended location. Never commit a credential file and never echo
a secret value.
"""

from __future__ import annotations

import os
import stat
import sys
from pathlib import Path

# Repo-relative and home-relative locations searched when no explicit file is given.
DEFAULT_ENV_FILES: tuple[str, ...] = (
    "./.env.local",
    "./.env",
    "../sandbase-registry/.env",
    "../../sandbase-registry/.env",
    "~/.config/sandbase/.env",
    "~/.sandbase/.env",
)


def load_env_file(path: str) -> bool:
    """Load simple KEY=VALUE lines. Returns True if the file existed.

    Existing environment variables win, so an explicit export always overrides a file.
    Warns when a credential file is group- or world-readable.
    """
    env_path = Path(path).expanduser()
    if not env_path.is_file():
        return False

    try:
        mode = env_path.stat().st_mode
        if mode & (stat.S_IRGRP | stat.S_IROTH):
            print(
                f"WARNING: {env_path} is readable beyond the owner. "
                f"Run: chmod 600 {env_path}",
                file=sys.stderr,
            )
    except OSError:
        pass

    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value
    return True


def load_credentials(explicit_files: list[str] | None = None) -> None:
    """Populate os.environ from the explicit, env-var, and default credential files."""
    candidates: list[str] = list(explicit_files or [])
    if os.environ.get("SANDBASE_ENV_FILE"):
        candidates.append(os.environ["SANDBASE_ENV_FILE"])
    candidates.extend(DEFAULT_ENV_FILES)
    for candidate in candidates:
        load_env_file(candidate)


def require(name: str) -> str:
    """Return an environment variable or exit with actionable guidance."""
    value = os.environ.get(name)
    if not value:
        raise SystemExit(
            f"{name} is missing. Export it, set $SANDBASE_ENV_FILE, pass --env-file, "
            f"or create ~/.config/sandbase/.env (chmod 600) containing {name}=..."
        )
    return value
