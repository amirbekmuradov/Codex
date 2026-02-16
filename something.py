#!/usr/bin/env python3
"""Generate one or more tiny "something" ideas for the day."""

from __future__ import annotations

import argparse
import random
from typing import Iterable

ADJECTIVES = [
    "curious",
    "tiny",
    "bold",
    "playful",
    "clever",
]

THINGS = [
    "automation",
    "tool",
    "experiment",
    "script",
    "prototype",
]

ACTIONS = [
    "that saves ten minutes",
    "that teaches one new concept",
    "that makes a teammate smile",
    "that removes one manual step",
    "that explores an interesting edge case",
]


def create_something() -> str:
    """Return one randomly generated idea for creating something."""
    adjective = random.choice(ADJECTIVES)
    thing = random.choice(THINGS)
    action = random.choice(ACTIONS)
    return f"Build a {adjective} {thing} {action}."


def generate_ideas(count: int) -> Iterable[str]:
    """Yield `count` generated ideas."""
    for _ in range(count):
        yield create_something()


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments."""
    parser = argparse.ArgumentParser(description="Print idea(s) for what to build next.")
    parser.add_argument(
        "-n",
        "--count",
        type=int,
        default=1,
        help="number of ideas to print (default: 1)",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="set a random seed for reproducible output",
    )
    return parser.parse_args()


def main() -> int:
    """Run the command-line interface."""
    args = parse_args()

    if args.count < 1:
        raise SystemExit("--count must be at least 1")

    if args.seed is not None:
        random.seed(args.seed)

    for idea in generate_ideas(args.count):
        print(idea)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
