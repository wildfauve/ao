from typing import Dict
from functools import reduce, partial
from enum import Enum
from rich.console import Console
from rich.table import Table
from rich import box
import polars as pl

from ao import dataframe, presenter, plot
from ao.util import fn

console = Console()

total_rounds = 4

f1_points = [15, 10, 8, 5, 4, 3, 2, 1]


class BoardType(Enum):
    FANTASY = "fantasy"
    F1 = "f1"


def current_leaderboard(fantasy_teams,
                        board_type: BoardType = BoardType.FANTASY,
                        round_number=None,
                        accum: bool = True) -> pl.DataFrame:
    if board_type == BoardType.F1:
        return show_f1_leaderboard(fantasy_teams)

    return _team_scores_df(fantasy_teams, accum)


def scores_plot(file: str, tournie, fantasy_teams, position: bool = False):
    df = _team_scores_df(fantasy_teams, True)

    if position:
        return plot.total_score_plot(file, tournie, df)

    return plot.rank_plot(file, tournie, df)


def _team_scores_df(fantasy_teams, accum):
    scores = _format_team_scores(teams_points_per_round(fantasy_teams))

    if not accum:
        return dataframe.build_df(scores)

    return dataframe.build_df(_accumulate_scores(scores))



def _show_df(df):
    presenter.event_team_scores_table(df)


def _show_old(fantasy_teams, round_number=None):
    table = Table(title=f"Leaderboard For Round {round_number if round_number else 'All'}", box=box.ROUNDED)

    table.add_column("Score", justify="center", style="cyan", no_wrap=True)
    table.add_column("Team", justify="left", style="magenta")

    rankings = sorted_teams(fantasy_teams, round_number)
    breakpoint()

    for team, score in rankings:
        table.add_row(f"{str(score)}", team.name)
    console.print(table)


def show_f1_leaderboard(fantasy_teams, round_number=None):
    results = total_f1_pts(fn.remove_none([f1_score_for_round(rd, fantasy_teams) for rd in range(1, total_rounds)]))

    table = Table(title=f"F1 Style Leaderboard For Round {round_number if round_number else 'All'}", box=box.ROUNDED)

    table.add_column("Score", justify="center", style="cyan", no_wrap=True)
    table.add_column("Team", justify="left", style="magenta")

    rankings = sorted_f1_teams(results)
    ljust_len = int(len(str(max([r[1] for r in rankings]))))
    for team, score in rankings:
        table.add_row(f"{str(score).ljust(ljust_len)}", team.name)
    console.print(table)


def f1_score_for_round(rd, fantasy_teams):
    sorted_scores_for_round = sorted_teams(fantasy_teams, rd)
    if all([sc[1] for sc in sorted_scores_for_round]):
        return [f1_by_team(team_f1_pos) for team_f1_pos in zip(sorted_scores_for_round, f1_points)]
    return None


def f1_by_team(f1_pos):
    return [f1_pos[0][0], f1_pos[1]]


def total_f1_pts(f1_scores):
    return reduce(aggregate_f1_team_score, [team for rd in f1_scores for team in rd], [])


def aggregate_f1_team_score(board, team_f1_score_for_rd):
    tm = find_team_on_board(team_f1_score_for_rd[0], board)
    if not tm:
        board.append(team_f1_score_for_rd)
        return board
    tm[1] += team_f1_score_for_rd[1]
    return board


def find_team_on_board(team, board):
    return fn.find(partial(_team_board_predicate, team), board)


def _team_board_predicate(team, team_on_board):
    return team == team_on_board[0]


def teams_points_per_round(fantasy_teams):
    return [(team, team.points_per_round()) for team in fantasy_teams]


def sorted_teams(fantasy_teams, round_number):
    return sorted([(team, team.total_points(round_number)) for team in fantasy_teams], key=lambda t: t[1], reverse=True)


def sorted_f1_teams(fantasy_teams):
    return sorted([team for team in fantasy_teams], key=lambda t: t[1], reverse=True)


def _format_team_scores(scores):
    rd_scores = reduce(_scores_dict, _transpose_scores(scores), {})
    return {**{"teams": [team.name for team, _ in scores]}, **rd_scores}


def _scores_dict(acc, score_column):
    round, scores = score_column
    return {**acc, **{f"Round-{round + 1}": list(scores)}}


def _transpose_scores(scores):
    return enumerate(list(zip(*[points for _, points in scores])))


def _accumulate_scores(scores: Dict):
    _teams, all_rounds = fn.fst_rst(list(scores.keys()))
    if not all_rounds:
        return scores

    fst_round, *rounds = all_rounds
    return {**{"teams": scores['teams']}, **acc_for_round(scores, {fst_round: scores[fst_round]}, fst_round, rounds)}


def acc_for_round(scores, accums, loc_of_last_accum, rounds):
    this_rd, nxt_rds = fn.fst_rst(list(rounds))
    if not this_rd:
        return accums
    accums.update({this_rd: [x + y for x, y in zip(accums[loc_of_last_accum], scores[this_rd])]})
    if not nxt_rds:
        return accums
    return acc_for_round(scores, accums, this_rd, nxt_rds)
