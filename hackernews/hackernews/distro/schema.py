import graphene
from graphene_django import DjangoObjectType

from .models import Distro, Contact

class DistroType(DjangoObjectType):
    class Meta:
        model = Distro

class ContactType(DjangoObjectType):
    class Meta:
        model = Contact
    

class Query(graphene.ObjectType):
    
    all_distro = graphene.List(DistroType)
    all_contact = graphene.List(ContactType)
    
    def resolve_all_distro(self, info, **kwargs):
        return Distro.objects.all()
    
    def resolve_all_contact(self, info, **kwargs):
        return Contact.objects.all()

schema = graphene.Schema(query=Query)


