"""Command-line interface for Spielstream."""

from __future__ import annotations

import argparse

from spielstream import __version__

REPO_URL = "https://github.com/spielstream/spielstream"

INFO = f"""\
Spielstream {__version__}
A local, open-source playground for learning and sharing Streamhouse architectures.

Stages and components:
  Capture    PostgreSQL + Debezium
  Transport  Redpanda
  Transform  Apache Flink (SQL)
  Govern     Redpanda schema registry
  Serve      PostgreSQL, FastMCP (agents), Iceberg on MinIO + DuckDB (history)
  Agents     Ollama + Python worker

First example: Fridge Rescue Squad
Repository:    {REPO_URL}

Status: early planning. Platform and examples are coming soon.
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="spielstream",
        description="A local playground for learning and sharing Streamhouse architectures.",
    )
    parser.add_argument("--version", action="version", version=f"spielstream {__version__}")
    subparsers = parser.add_subparsers(dest="command")
    subparsers.add_parser("info", help="Show what Spielstream is and where to find it.")

    args = parser.parse_args(argv)
    if args.command == "info":
        print(INFO, end="")
        return 0
    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
