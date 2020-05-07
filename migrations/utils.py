from alembic import op
from sqlalchemy import String, Integer
from sqlalchemy import table, column


class TablesV1:
    """ Contains common definitions for migration in May, 4th 2020 """

    OPERATION = table('operation',
                      column("id", Integer),
                      column("slug", String),
                      column('enabled', Integer),
                      column('type', String),
                      column('icon', String),
                      )

    @staticmethod
    def operation(pk, slug, enabled, _type, icon):
        return pk, slug, enabled, _type, icon

    @staticmethod
    def execute(tb, rows):
        rows = [dict(list(zip([c.name for c in tb.columns], row))) for row in
                rows]
        op.bulk_insert(tb, rows)
