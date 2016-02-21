from peewee import CharField, DateTimeField, ForeignKeyField, TextField, \
    BooleanField
from flask.ext.security import UserMixin, RoleMixin
from . import db


# The user model specifies its fields (or columns) declaratively, like django
class User(db.Model, UserMixin):
    email = CharField()
    password = CharField()
    active = BooleanField(default=True)
    confirmed_at = DateTimeField(null=True)

    # class Meta:
    #     order_by = ('username',)

    def __unicode__(self):
        return(self.email)


class Role(db.Model, RoleMixin):
    name = CharField(unique=True)
    description = TextField(null=True)

    def __unicode__(self):
        return(self.name)


class UserRoles(db.Model):
    # Because peewee does not come with built-in many-to-many
    # relationships, we need this intermediary class to link
    # user to roles.
    user = ForeignKeyField(User, related_name='roles')
    role = ForeignKeyField(Role, related_name='users')
    name = property(lambda self: self.role.name)
    description = property(lambda self: self.role.description)

    def __unicode__(self):
        return(self.user + " is " + self.role)
