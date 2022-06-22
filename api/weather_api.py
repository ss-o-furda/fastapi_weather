from typing import List
import fastapi
from models.location import Location
from models.reports import Report, ReportSubmittal
from models.validation_error import ValidationError
from services import openweather_service, report_service
router = fastapi.APIRouter()


@router.get("/api/weather/{city}")
async def weather(location: Location = fastapi.Depends(), units: str = "metric"):
    try:
        return await openweather_service.get_report(
            location.city, location.state, location.country, units)
    except ValidationError as ve:
        return fastapi.Response(content=ve.error_msg, status_code=ve.status_code)
    except Exception as x:
        return fastapi.Response(content=str(x), status_code=500)


@router.get("/api/reports", name="all_reports")
async def reports_get() -> List[Report]:
    return await report_service.get_reports()

@router.post("/api/reports", name="add_report", status_code=201, response_model=Report)
async def save_report(report_submittal: ReportSubmittal) -> Report:
    d = report_submittal.description
    loc = report_submittal.location
    return await report_service.add_report(d, loc)
