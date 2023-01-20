from fastapi import (
    APIRouter,
    Depends,
    status,
    Response
)

from ...schemas import (
    ScheduleSchema,
    ScheduleSchemaCreate,
    ScheduleSchemaUpdate,
    ScheduleRecord
)
from ...services.schedule import ScheduleService


router = APIRouter(
    prefix='/schema',
    tags=['Схемы расписания']
)


@router.post(
    '/',
    response_model=ScheduleSchema
)
def create_schema(
    schema_data: ScheduleSchemaCreate,
    schedule_service: ScheduleService = Depends()
):
    return schedule_service.create_schema(schema_data)


@router.get(
    '/',
    response_model=list[ScheduleSchema]
)
def get_schemas(
    schedule_service: ScheduleService = Depends()
):
    return schedule_service.get_many_schemas()


@router.put(
    '/{schema_id}',
    response_model=ScheduleSchema
)
def update_schema(
    schema_id: int,
    schema_data: ScheduleSchemaUpdate,
    schedule_service: ScheduleService = Depends(),
):
    return schedule_service.update_schema(schema_id, schema_data)


@router.get(
    '/{schema_id}/records',
    response_model=list[ScheduleRecord]
)
def get_records_within_schema(
    schema_id: int,
    schedule_service: ScheduleService = Depends()
):
    return schedule_service.get_records_in_schema(schema_id)


@router.post(
    '/{schema_id}/records',
    response_model=list[int],
    description='Добавить записи к схеме',
)
def include_records_in_schema(
    schema_id: int,
    records: list[int],
    schedule_service: ScheduleService = Depends()
):
    return schedule_service.include_records_in_schema(schema_id, records)


@router.delete(
    '/{schema_id}/records',
    status_code=status.HTTP_204_NO_CONTENT,
    description='Удалить записи из схемы',
)
def exclude_records_from_schema(
    schema_id: int,
    records: list[int],
    schedule_service: ScheduleService = Depends()
):
    schedule_service.exclude_records_from_schema(schema_id, records)
    return Response(status_code=status.HTTP_204_NO_CONTENT)