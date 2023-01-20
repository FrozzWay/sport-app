from fastapi import (
    APIRouter,
    Depends,
    status,
    Response
)

from ...schemas import Placement
from ...services.classes import PlacementService


router = APIRouter(
    prefix='/placement',
    tags=['Помещения']
)


@router.get(
    '/',
    response_model=list[Placement]
)
def get_placements(
    placement_service: PlacementService = Depends()
):
    return placement_service.get_many()


@router.post(
    '/',
    response_model=Placement,
    status_code=status.HTTP_201_CREATED,
)
def create_placement(
    placement_data: Placement,
    placement_service: PlacementService = Depends()
):
    return placement_service.create(placement_data)


@router.put(
    '/{placement_name}',
    response_model=Placement
)
def update_placement(
    placement_name: str,
    placement_data: Placement,
    placement_service: PlacementService = Depends()
):
    return placement_service.update(placement_name, placement_data)


@router.delete(
    '/{placement_name}',
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_placement(
    placement_name: str,
    placement_service: PlacementService = Depends()
):
    placement_service.delete(placement_name)
    return Response(status_code=status.HTTP_204_NO_CONTENT)