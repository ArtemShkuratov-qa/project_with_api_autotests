import random
from dataclasses import dataclass, asdict
from typing import List, Optional
import json


@dataclass
class Category:
    id: int
    name: str

@dataclass
class Tag:
    id: int
    name: str

@dataclass
class Pet:
    id: int
    name: str
    category: Category
    photoUrls: List[str]
    tags: List[Tag]
    status: str  # "available", "pending", "sold"


dog = Pet(
    id=random.randint(1, 1000000),
    name="test001",
    category=Category(id=167, name="catergory1"),
    photoUrls=["string"],
    tags=[Tag(id=134, name="tag1")],
    status="available"
)

cat = Pet(
    id=random.randint(1, 1000000),
    name="test002",
    category=Category(id=152, name="catergory2"),
    photoUrls=["string"],
    tags=[Tag(id=222, name="tag2")],
    status="pending"
)

lion = Pet(
    id=random.randint(1, 1000000),
    name="test003",
    category=Category(id=355, name="catergory3"),
    photoUrls=["string"],
    tags=[Tag(id=366, name="tag3")],
    status="sold"
)
