"""Approved FICTIONAL reference entries for the learning exercise."""
from dataclasses import dataclass

@dataclass(frozen=True)
class CatalogEntry:
    source_id: str
    answer: str

SYNTHETIC_CATALOG = {
    "warranty": CatalogEntry(
        "SYN-FAQ-WARRANTY-01",
        "To ask about warranty support, start a support case and provide the equipment model and serial number. A support representative must review any coverage question. This is a fictional demonstration process."
    ),
    "parts": CatalogEntry(
        "SYN-FAQ-PARTS-01",
        "Use the parts inquiry channel to ask about availability. This demonstration cannot verify real stock, delivery or prices."
    ),
    "hours": CatalogEntry(
        "SYN-FAQ-HOURS-01",
        "Check the dealer's published service hours or contact its service desk. Hours may vary by location. This is fictional guidance."
    ),
}
