from dataclasses import dataclass, field
from typing import List, Optional
import uuid

# --- Stats ---
@dataclass
class Stats:
    hp: int
    attack: int
    defense: int
    sp_attack: int
    sp_defense: int
    speed: int

# --- Moves ---
@dataclass
class Move:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str = ""
    type: str = ""
    category: str = ""   # e.g., Physical, Special, Status
    power: Optional[int] = None
    accuracy: Optional[int] = None

# --- Format Info (GO, Showdown, VGC) ---
@dataclass
class FormatInfo:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    format: str = ""  # "GO", "Showdown", "VGC"
    recommended_moves: List[str] = field(default_factory=list)
    usage_rank: Optional[int] = None
    counters: List[str] = field(default_factory=list)

# --- Pokemon ---
@dataclass
class Pokemon:
    id: int
    name: str
    types: List[str]
    stats: Stats
    moves: List[Move]
    sprite_url: str
    formats: List[FormatInfo]