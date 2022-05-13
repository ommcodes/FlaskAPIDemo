from mongoengine import Document, StringField, FloatField, IntField


class Products(Document):
    product_name = StringField(required=True)
    Barcode = IntField(required=True, unique=True)
    Brand = StringField()
    Product_Description = StringField(max_length=200)
    Price = FloatField()
    Availability = StringField()

