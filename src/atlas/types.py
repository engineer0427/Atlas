from enum import Enum
class NodeType(str, Enum):
    PAPER = "Paper"
    CODEREPO = "CodeRepo"
    DATASET = "Dataset"
    CONCEPT = "Concept"
    AUTHOR = "Author"
    VENUE = "Venue"
