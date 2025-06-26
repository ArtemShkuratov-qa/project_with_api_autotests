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
    id=1,
    name="doggie",
    category=Category(id=1, name="catergory1"),
    photoUrls=["string"],
    tags=[Tag(id=1, name="tag1")],
    status="available"
)

cat = Pet(
    id=1,
    name="doggie",
    category=Category(id=2, name="catergory2"),
    photoUrls=["string"],
    tags=[Tag(id=2, name="tag2")],
    status="pending"
)


lion = Pet(
    id=1,
    name="doggie",
    category=Category(id=3, name="catergory3"),
    photoUrls=["string"],
    tags=[Tag(id=3, name="tag3")],
    status="sold"
)

# Сериализация в JSON
payload = json.dumps(asdict(dog))