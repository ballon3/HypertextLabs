import graphene

import distro.schema


class Query(distro.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)