import graphene

from distro.schema import Query as distros_query


class Query(distros_query):
    pass


schema = graphene.Schema(query=Query)