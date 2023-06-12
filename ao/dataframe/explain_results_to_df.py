from typing import Dict, Tuple, List
from functools import reduce, partial
from collections import ChainMap

import polars as pl



def explain_df_builder(tournie, explain: Dict):
    series = list(zip(*reduce(partial(_explain_for_team, tournie), explain.items(), [])))
    df = pl.DataFrame({
        'team': series[0],
        'tournament': series[1],
        'draw': series[2],
        'match': series[3],
        'selectedWinner': series[4],
        'selectedSets': series[5],
        'ptsForWinner': series[6],
        'ptsForSets': series[7],
        'ptsForLossMaxSets': series[8]
    }).with_columns([(pl.col('ptsForWinner') + pl.col('ptsForSets') + pl.col('ptsForLossMaxSets')).alias("totalPts")])
    return df


def _explain_for_team(tournie, accum, team_explain: Tuple):
    team, draws = team_explain
    return reduce(partial(_team_and_draw, tournie, team), draws, accum)


def _team_and_draw(tournie, team, accum, draw):
    return reduce(partial(_team_draw_match, tournie, team, draw['event']), draw['matches'], accum)


def _team_draw_match(tournie, team, draw, accum, match) -> List[Tuple]:
    pts = dict(ChainMap(*(match['points'])))
    accum.append((
        team.name,
        tournie.name,
        draw,
        match.get('match', None),
        match.get('selected-winner', None),
        match.get('selected-in-sets', None),
        pts.get('correct-winner', None),
        pts.get('correct-sets', None),
        pts.get('bonus-for-loss-in-max-sets', None),
    ))
    return accum
