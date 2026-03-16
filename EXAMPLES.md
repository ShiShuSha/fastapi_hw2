##Для Задания 1##
Пример использования

data = {
    "username": "test_user",
    "email": "test@mail.com",
    "password": "Password1",
    "password_confirm": "Password1",
    "age": 25
}

result = register_user(data)

print(result)

если ошибка:

[
 {'loc': ('password',), 'msg': 'Пароль должен содержать хотя бы одну цифру', 'type': 'value_error'}
]

##Для Задания 2##
Пример JSON для задания 2

data = {
    "username": "test_user",
    "email": "test@mail.com",
    "password": "Password1",
    "password_confirm": "Password1",
    "age": 30,
    "full_name": "Ivan",
    "phone": "+7-999-11-22"
}

##Для Задания 3##
Пример использования

tree = Node(
    data="root",
    child=Node(
        data="level1",
        child=Node(
            data="level2"
        )
    )
)

print(tree.model_dump())

результат:

{
  "data": "root",
  "child": {
    "data": "level1",
    "child": {
      "data": "level2",
      "child": null
    }
  }
}
