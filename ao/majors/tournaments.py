from ao.model import tournament

AustralianOpen = tournament.GrandSlam(name="Australian Open", subject_name="AustralianOpen", perma_id="ao")
FrenchOpen = tournament.GrandSlam(name="French Open", subject_name="FrenchOpen", perma_id="fo")

from .year_2023.australian_open import tournament as ao2023
from .year_2023.french_open import tournament as fo2023


TournamentsInFantasy = [
    ao2023.AustralianOpen2023,
    fo2023.FrenchOpen2023
]