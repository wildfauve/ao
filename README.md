## CLI Commands

```shell
poetry run ao draw-scrap --results-file s.py --tournament FrenchOpen2023 --round 2 --scores-only

poetry run ao leaderboard --tournament FrenchOpen2023 --to-discord


poetry run ao plot --file totals.png --tournament FrenchOpen2023 --accum-totals-plot --to-discord
poetry run ao plot --file rank.png --tournament FrenchOpen2023 --ranking-plot --to-discord

poetry run ao show-round --tournament FrenchOpen2023 --draw MensSingles --round 2

poetry run ao fantasy-score-template --tournament FrenchOpen2023 --draw MensSingles --template-name mens_singles --round 2 

poetry run ao draw-scrap --results-file s.py  --round 1 --scores-only 
```
