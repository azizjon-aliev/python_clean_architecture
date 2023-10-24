from src.domain.entities.handbook import Region

data = {"region_id": 1, "name": "Tajikistan", "parent": None}


def test_region_creation():
    region: Region = Region(**data)

    assert region.region_id == data.get("region_id")
    assert region.name == data.get("name")
    assert region.parent == data.get("parent")


def test_region_with_parent():
    parent: Region = Region(region_id=1, name="Country", parent=None)
    region: Region = Region(region_id=2, name="City", parent=parent)
    assert region.parent == parent
    assert region.parent.name == parent.name


def test_region_from_dict():
    region: Region = Region.from_dict(data=data)

    assert region.region_id == data.get("region_id")
    assert region.name == data.get("name")
    assert region.parent == data.get("parent")


def test_region_to_dict():
    region: Region = Region.from_dict(data=data)
    assert region.to_dict() == data


def test_region_equality():
    region1: Region = Region.from_dict(data=data)
    region2: Region = Region.from_dict(data=data)
    assert region1 == region2
