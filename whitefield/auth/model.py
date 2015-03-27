from sqlalchemy import Column, Unicode, String
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
)

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

from ziggurat_foundations.models import (
    BaseModel, UserMixin, GroupMixin,
    GroupPermissionMixin, UserGroupMixin,
    GroupResourcePermissionMixin, ResourceMixin,
    UserPermissionMixin, UserResourcePermissionMixin,
    ExternalIdentityMixin
)

from ziggurat_foundations import ziggurat_model_init


class Group(GroupMixin, Base):
    pass


class GroupPermission(GroupPermissionMixin, Base):
    pass


class UserGroup(UserGroupMixin, Base):
    pass


class GroupResourcePermission(GroupResourcePermissionMixin, Base):
    pass


class Resource(ResourceMixin, Base):
    pass


class UserPermission(UserPermissionMixin, Base):
    pass


class UserResourcePermission(UserResourcePermissionMixin, Base):
    pass


class User(UserMixin, Base):
    full_name = Column(Unicode, nullable=False)
    school = Column(String(2))


class ExternalIdentity(ExternalIdentityMixin, Base):
    pass


ziggurat_model_init(User, Group, UserGroup, GroupPermission, UserPermission,
                    UserResourcePermission, GroupResourcePermission, Resource,
                    ExternalIdentity)
