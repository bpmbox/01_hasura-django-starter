from typing import List

from fastapi import APIRouter, Depends

from polls import adapters
from polls.models import Chinko
from polls.schemas import FastChoice, FastChoices

router = APIRouter()


@router.get("/")
def get_chinkos(
    choices: List[Chinko] = Depends(adapters.retrieve_choices),
) -> FastChoices:
    return FastChoices.from_qs(choices)


@router.get("/{c_id}")
def get_choice(choice: Chinko = Depends(adapters.retrieve_choice)) -> FastChoice:
    return FastChoice.from_orm(choice)
