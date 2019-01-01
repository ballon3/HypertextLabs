import graphene
import hackernews.schema
from graphene_django import DjangoObjectType

from distro.models import Distro 

class DistroType(DjangoObjectType):
    class Meta:
        model = Distro

class Query(graphene.ObjectType):
    distro = graphene.List(DistroType)
    
    def resolve_links(self, info, **kwargs):
        return Distro.objects.all()