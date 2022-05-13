from mongoengine import NotUniqueError, ValidationError
from models.products import Products
from models.users import Users
from tools.loadmdb import loadmdb
from tools.get_doc import get_random
import csv
from random import randint


@loadmdb
def csv_to_doc(filepath: str = 'resources/product_data.csv', delimiter: str = '\t'):
    with open(filepath, 'r') as file:
        data = csv.DictReader(file, delimiter=delimiter)

        for datum in data:
            product_entry = Products(**datum, __auto_convert=True).save()
            print(
                f"Added: {product_entry.name} | {product_entry.description} | {product_entry.price} => {product_entry.id}")


@loadmdb
def user_acl(filepath: str = 'resources/acl.csv', delimiter: str = '\t'):
    with open(filepath, 'r') as file:
        data = csv.DictReader(file, delimiter=delimiter)

        for datum in data:
            try:
                user = Users(**datum, __auto_convert=True)
                # generate random admin access, password, and favorite meals
                user.access.admin = (randint(0, 1) == 1)
                user.fav_meals = get_random(Products, randint(1, 5))
                user.password = user.name + str(randint(0, 9))

                user.save()
                print(
                    f"Added: {user.name} | {user.email} | {user.password} | Admin-{user.access.admin is True} => {user.id}")
            except NotUniqueError:
                print(f'Invalid Entry: {user.email} is already taken.')
            except ValidationError:
                print(f'Validation Error: {user}')


def load_all(config: dict = None):
    from tools.loadmdb import mdbConfig

    if config:
        mdbConfig.update(config)

    csv_to_doc()
    user_acl()
