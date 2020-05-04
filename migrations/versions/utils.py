
class TablesV1:
    """ Contains common definitions for migration in May, 4th 2020 """
    OPERATION = table('operation',
               column("id", Integer),
               column("slug", String),
               column('enabled', Integer),
               column('type', String),
               column('icon', String),
               )
