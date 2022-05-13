from random import choice
from typing import Type
from flask_mongoengine import Document


def get_random(object_type: Type[Document], quantity=1) -> list:
    rand_list = []
    id_list = object_type.objects.only('id')
    for _ in range(quantity):
        barcode = choice(id_list)['id']
        rand_list.append(object_type.objects(id=barcode).next())
    return rand_list