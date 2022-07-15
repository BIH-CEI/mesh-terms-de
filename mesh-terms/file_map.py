from dataclasses import dataclass
from typing import List


@dataclass(kw_only=True, slots=True)
class FieldMapEntry:
    name: str
    columns: List[str]


FILE_MAP = {
    "ANN": FieldMapEntry(name="Annotations", columns=["MainHeadingsId", "Annotation"]),
    "CC": FieldMapEntry(
        name="ClassificationCodes", columns=["Classification", "MainHeadingsId"]
    ),
    "ET": FieldMapEntry(
        name="EntryTerms",
        columns=["DescriptionGerman", "DescriptionEnglish", "MainHeadingsId"],
    ),
    "ETD": FieldMapEntry(
        name="EntryTermsGerman", columns=["Description", "MainHeadingsId"]
    ),
    "ETE": FieldMapEntry(
        name="EntryTermsEnglish", columns=["Description", "MainHeadingsId"]
    ),
    "MH": FieldMapEntry(
        name="MainHeadings",
        columns=["Id", "DescriptionGerman", "DescriptionEnglish", "SubheadingIds"],
    ),
    "QF": FieldMapEntry(
        name="Subheadings", columns=["Id", "DescriptionGerman", "DescriptionEnglish"]
    ),
    "RT": FieldMapEntry(name="RelatedTerms", columns=["First", "Second"]),
    "SCN": FieldMapEntry(
        name="ScopeNotesEnglish", columns=["MainHeadingId", "ScopeNote"]
    ),
}
