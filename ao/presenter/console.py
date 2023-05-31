import io

from rich.console import Console

def terminal_console():
    return Console()


def to_string_console():
    return Console(file=io.StringIO(), width=120)
