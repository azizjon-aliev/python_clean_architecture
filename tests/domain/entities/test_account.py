from datetime import datetime

from src.domain.entities.account import User, UserId

data = {
    "user_id": UserId("123"),
    "email": "test@example.com",
    "phone": "992900000000",
    "password": "secure_password",
    "is_staff": True,
    "is_active": True,
    "is_superuser": True,
    "otp": 1234,
    "is_verified": True,
    "date_joined": datetime.now(),
    "role": "admin",
    "company": None,
    "created_at": datetime.now,
    "updated_at": datetime.now,
    "created_by": None,
    "updated_by": None,
}


def test_user_creation_with_not_created_by_and_updated_by() -> None:
    user: User = User(**data)

    assert user.user_id == data.get("user_id")
    assert user.phone == data.get("phone")
    assert user.email == data.get("email")
    assert user.password == data.get("password")
    assert user.is_staff is data.get("is_staff")
    assert user.is_active is data.get("is_active")
    assert user.is_superuser is data.get("is_superuser")
    assert user.otp == data.get("otp")
    assert user.is_verified == data.get("is_verified")
    assert user.role == data.get("role")
    assert user.company == data.get("company")
    assert user.created_at == data.get("created_at")
    assert user.updated_at == data.get("updated_at")
    assert user.created_by == data.get("created_by")
    assert user.updated_by == data.get("updated_by")


def test_user_creation_with_created_by_and_updated_by() -> None:
    data.pop("user_id")
    created_by = User(**data, user_id=UserId("1"))
    updated_by = User(**data, user_id=UserId("2"))

    data.pop("created_by")
    data.pop("updated_by")
    user: User = User(
        **data, user_id=UserId("3"), created_by=created_by, updated_by=updated_by
    )

    assert user.created_by == created_by
    assert user.updated_by == updated_by
    assert user.created_by.user_id == created_by.user_id
    assert user.updated_by.user_id == updated_by.user_id


def test_user_from_dict() -> None:
    user: User = User.from_dict(data=data)

    assert user.user_id == data.get("user_id")
    assert user.phone == data.get("phone")
    assert user.email == data.get("email")
    assert user.password == data.get("password")
    assert user.is_staff is data.get("is_staff")
    assert user.is_active is data.get("is_active")
    assert user.is_superuser is data.get("is_superuser")
    assert user.otp == data.get("otp")
    assert user.is_verified == data.get("is_verified")
    assert user.role == data.get("role")
    assert user.company == data.get("company")
    assert user.created_at == data.get("created_at")
    assert user.updated_at == data.get("updated_at")
    assert user.created_by == data.get("created_by")
    assert user.updated_by == data.get("updated_by")


def test_user_to_dict() -> None:
    user: User = User.from_dict(data=data)
    assert user.to_dict() == data


def test_user_equality() -> None:
    user1: User = User.from_dict(data=data)
    user2: User = User.from_dict(data=data)
    assert user1 == user2
