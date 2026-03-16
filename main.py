#Задание 1
from pydantic import BaseModel, EmailStr, Field, ValidationError, field_validator, model_validator
from datetime import datetime
import re


class UserRegistration(BaseModel):
    username: str = Field(..., min_length=3, max_length=20)
    email: EmailStr
    password: str = Field(..., min_length=8)
    password_confirm: str
    age: int = Field(..., ge=18, le=120)
    registration_date: datetime = Field(default_factory=datetime.now)

    @field_validator("username")
    @classmethod
    def validate_username(cls, value):
        if not re.match(r"^[a-zA-Z0-9_]+$", value):
            raise ValueError("Username может содержать только латинские буквы, цифры и _")
        return value

    @field_validator("password")
    @classmethod
    def validate_password(cls, value):
        if not re.search(r"\d", value):
            raise ValueError("Пароль должен содержать хотя бы одну цифру")
        if not re.search(r"[A-Z]", value):
            raise ValueError("Пароль должен содержать хотя бы одну заглавную букву")
        if not re.search(r"[a-z]", value):
            raise ValueError("Пароль должен содержать хотя бы одну строчную букву")
        return value

    @model_validator(mode="after")
    def check_password_match(self):
        if self.password != self.password_confirm:
            raise ValueError("Пароли не совпадают")
        return self

    def model_dump(self, **kwargs):
        data = super().model_dump(**kwargs)
        data.pop("password_confirm", None)
        return data


def register_user(data: dict):
    try:
        user = UserRegistration(**data)
        return user
    except ValidationError as e:
        return e.errors()

 
#Задание 2
class UserRegistration(BaseModel):
    username: str = Field(..., min_length=3, max_length=20)
    email: EmailStr
    password: str = Field(..., min_length=8)
    password_confirm: str
    age: int = Field(..., ge=18, le=120)
    full_name: str
    phone: str
    registration_date: datetime = Field(default_factory=datetime.now)

    @field_validator("username")
    @classmethod
    def validate_username(cls, value):
        if not re.match(r"^[a-zA-Z0-9_]+$", value):
            raise ValueError("Username может содержать только латинские буквы, цифры и _")
        return value

    @field_validator("password")
    @classmethod
    def validate_password(cls, value):
        if not re.search(r"\d", value):
            raise ValueError("Пароль должен содержать хотя бы одну цифру")
        if not re.search(r"[A-Z]", value):
            raise ValueError("Пароль должен содержать хотя бы одну заглавную букву")
        if not re.search(r"[a-z]", value):
            raise ValueError("Пароль должен содержать хотя бы одну строчную букву")
        return value

    @field_validator("full_name")
    @classmethod
    def validate_full_name(cls, value):
        if len(value) < 2:
            raise ValueError("Имя должно содержать минимум 2 символа")
        if not value[0].isupper():
            raise ValueError("Имя должно начинаться с заглавной буквы")
        return value

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, value):
        if not re.match(r"^\+\d-\d{3}-\d{2}-\d{2}$", value):
            raise ValueError("Телефон должен быть в формате +X-XXX-XX-XX")
        return value

    @model_validator(mode="after")
    def check_password_match(self):
        if self.password != self.password_confirm:
            raise ValueError("Пароли не совпадают")
        return self

    def model_dump(self, **kwargs):
        data = super().model_dump(**kwargs)
        data.pop("password_confirm", None)
        return data




#Задание 3
from typing import Optional

class Node(BaseModel):
    data: str
    child: Optional["Node"] = None


Node.model_rebuild()
