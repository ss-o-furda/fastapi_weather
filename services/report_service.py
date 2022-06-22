from datetime import datetime
from typing import List
from uuid import uuid4
from models.location import Location
from models.reports import Report

__reports: List[Report] = []


async def get_reports() -> List[Report]:
    #  would be async with real DB
    return list(__reports)


async def add_report(description: str, location: Location) -> Report:
    #  would be async with real DB
    now = datetime.now()
    report = Report(
        id=str(uuid4()), location=location, description=description, created_at=now)

    __reports.append(report)

    # create different sort keys, because created_at defined as optional field
    __reports.sort(key=lambda r: r.created_at if isinstance(
        r.created_at, datetime) else r.location.city, reverse=True)

    return report
