from typing import List, Tuple

from rich.table import Table
import polars as pl

from ao.adapter import discord

from . import console


def event_team_scores_table(df: pl.DataFrame, to_discord: bool = False):
    table = Table(title="Fantasy Scores")

    for column in df.columns:
        table.add_column(column, justify="right", style="green")

    for row in df.rows():
        table.add_row(*[str(item) for item in row])

    if to_discord:
        _send_to_discord(table)
    else:
        console.terminal_console().print(table)


def _send_to_discord(table):
    cons = console.to_string_console()
    cons.print(table)
    discord.send(_format(cons.file.getvalue()))
    pass


def _format(table_str) -> str:
    return f"""
```
{table_str}
```
"""