# mongoengine packages

from mongoengine import (Document,EmbeddedDocument,EmbeddedDocumentField,ListField,StringField,EmailField,BooleanField,ReferenceField)

# flask packages

from flask_bcrypt import generate_password_hash, check_password_hash

# resource

from models.products import Products

# Other Packages

import re

class Access(EmbeddedDocument):

    user = BooleanField(default=True)
    admin = BooleanField(default=False)

class PhoneField(StringField):

    Rex = re.compile(r"((\(\d{3}\)?)|(\d{3}))([-\s./]?)(\d{3})([-\s./]?)(\d{4})")

    def val_ip(self, value):
        if not PhoneField.Rex.match(string=value):
            self.error(f"Error - : `{value}' is not in a valid phone number format." )
        super(PhoneField, self).val_ip(value=value)

class Users(Document):

    EMail = EmailField(required=True, unique=True)
    Pass = StringField(required=True, min_length=8, regex=None)
    access = EmbeddedDocumentField(Access, default=Access(user = True, admin=False))
    Prod_List = ListField(ReferenceField(Products))
    name = StringField(unique=False)
    phone = PhoneField()

    def hash_gen_pwd(self):
        self.Pass = generate_password_hash(password=self.Pass).decode('utf-8')
    hash_gen_pwd.__doc__ = generate_password_hash.__doc__

    def chk_pwd(self, password: str) -> bool:
        return check_password_hash(pw_hash=self.Pass, password=password)

    def save(self, *args, **kwargs):
        if self._created:
            self.hash_gen_pwd()
        super(Users,self).save(*args, **kwargs)
