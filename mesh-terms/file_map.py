from dataclasses import dataclass
from typing import List


@dataclass(kw_only=True, slots=True)
class FieldMapEntry:
    name: str


FILE_MAP = {
    "ANN": FieldMapEntry(name="Annotations"),
    "CC": FieldMapEntry(name="ClassificationCodes"),
    "ET": FieldMapEntry(name="EntryTerms"),
    "ETD": FieldMapEntry(name="EntryTermsGerman"),
    "ETE": FieldMapEntry(name="EntryTermsEnglish"),
    "MH": FieldMapEntry(name="MainHeadings"),
    "QF": FieldMapEntry(name="Subheadings"),
    "RT": FieldMapEntry(name="RelatedTerms"),
    "SCN": FieldMapEntry(name="ScopeNotesEnglish"),
}
