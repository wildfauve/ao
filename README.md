## CLI Commands

```shell
poetry run ao draw-scrap --results-file _temp/s.py --tournament FrenchOpen2023 --round 4 --scores-only

poetry run ao leaderboard --tournament FrenchOpen2023 --to-discord


poetry run ao plot --file _temp/totals.png --tournament FrenchOpen2023 --accum-totals-plot --to-discord
poetry run ao plot --file _temp/rank.png --tournament FrenchOpen2023 --ranking-plot --to-discord

poetry run ao show-round --tournament FrenchOpen2023 --draw MensSingles --round 2

poetry run ao fantasy-score-template --tournament FrenchOpen2023 --draw MensSingles --round 2 

poetry run ao explain-team-score --tournament FrenchOpen2023 --fantasy-team-name TeamPolarPrecision
```
