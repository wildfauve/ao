from typing import List, Tuple
from rich.console import Console
from rich.table import Table
import polars as pl

from rich import box

console = Console()

def event_team_scores_table(df: pl.DataFrame):
    table = Table(title="Fantasy Scores")


    for column in df.columns:
        table.add_column(column, justify="right", style="green")


    for row in df.rows():
        table.add_row(*[str(item)for item in row])

    console.print(table)
