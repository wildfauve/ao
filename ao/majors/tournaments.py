from ao.model import tournament

AustralianOpen = tournament.GrandSlam(name="Australian Open", subject_name="AustralianOpen", perma_id="ao")

from .year_2023.australian_open import tournament

TournamentsInFantasy = [
    tournament.AustralianOpen2023
]