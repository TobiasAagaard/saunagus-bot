from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, date as Date
from enum import Enum
from typing import Optional


class AvailabilityStatus(Enum):
    AVAILABLE = "available"
    BOOKED = "booked"
    UNAVAILABLE = "unavailable"


@dataclass(frozen=True)
class TimeSlot:
    date: Date
    start_time: str
    end_time: str
    status: AvailabilityStatus
    capacity: Optional[int] = None
    price: Optional[float] = None
    booking_url: Optional[str] = None

    def __str__(self) -> str:
        return f"{self.date.isoformat()} {self.start_time}-{self.end_time} ({self.status.value})"

    @property
    def is_available(self) -> bool:
        return self.status is AvailabilityStatus.AVAILABLE


@dataclass
class SaunaAvailability:
    location: str = ""
    slots: list[TimeSlot] = field(default_factory=list)
    scrape_error: Optional[str] = None
    scraped_at: datetime = field(default_factory=datetime.now)
    source_url: str = ""

    @property
    def available_slots(self) -> list[TimeSlot]:
        return [slot for slot in self.slots if slot.is_available]

    @property
    def total_slots(self) -> int:
        return len(self.slots)

    @property
    def available_count(self) -> int:
        return len(self.available_slots)

    def filter_by_date_range(self, start: Date, end: Date) -> SaunaAvailability:
        filtered = [slot for slot in self.slots if start <= slot.date <= end]
        return SaunaAvailability(slots=filtered, scraped_at=self.scraped_at, source_url=self.source_url)

    def group_by_date(self) -> dict[str, list[TimeSlot]]:
        grouped: dict[str, list[TimeSlot]] = {}
        for slot in self.slots:
            date_key = slot.date.isoformat()
            grouped.setdefault(date_key, []).append(slot)
        return grouped