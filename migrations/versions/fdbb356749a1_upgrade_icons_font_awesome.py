"""upgrade icons font awesome

Revision ID: fdbb356749a1
Revises: abc9192ljsj3
Create Date: 2018-03-14 17:53:23.776958

"""
from alembic import context
from sqlalchemy.orm import sessionmaker

# revision identifiers, used by Alembic.
revision = 'fdbb356749a1'
down_revision = 'abc9192ljsj3'
branch_labels = None
depends_on = None


def upgrade():
    cntxt = context.get_context()
    session = sessionmaker(bind=cntxt.bind)()
    connection = session.connection()

    data = [
        [58, "fa-external-link-square", "fa-external-link-alt"],
        [12, "icon-union", "fa-plus-square"],
        [93, "fa-flash", "fa-bolt"],
        [6, "icon-projection", "fa-columns"],
        [13, "icon-intersection", "fa-compress"],
        [17, "fa-code-fork", "fa-code-branch"],
        [71, "fa-area-chart", "fa-chart-area"],
        [69, "fa-bar-chart", "fa-chart-bar"],
        [89, "fa-circle-o-notch", "fa-circle-notch"],
        [68, "fa-line-chart", "fa-chart-line"],
        [70, "fa-pie-chart", "fa-chart-pie"],
        [53, "fa-map-o", "fa-file"],
        [85, "fa-long-arrow-right", "fa-list-ol"],
        [86, "fa-diamond", "fa-gem"],
        [1, "fa-dashboard", "fa-tags"],
        [31, "fa-exchange", "fa-exchange-alt"],
        [94, "fa-window-close-o", "fa-window-close"],
        [84, "fa-hand-peace-o", "fa-hand-peace"],
        [48, "fa-file-text", "fa-file-alt"],
        [95, "fa-sort-amount-desc", "fa-sort-amount-down"],
        [96, "hashtag", "fa-hashtag"],
        [92, "fa-lemon-o", "fa-lemon"],
        [91, "fa-arrows-v", "fa-arrows-alt-v"],
        [42, "fa-lightbulb-o", "fa-lightbulb"],
        [22, "fa-cloud-download", "fa-cloud-download-alt"],
        [39, "fa-cloud-upload", "fa-cloud-upload-alt"],
        [77, "fa-id-card-o", "fa-id-card"],
        [73, "fa-shield", "fa-shield-alt"],
        [25, "fa-commenting-o", "fa-comment-alt"],
        [83, "fa-vcard-o", "fa-address-card"],
        [20, "fa-gears", "fa-cogs"],
        [52, "fa-long-arrow-right", "fa-long-arrow-alt-right"],
        [50, "fa-hand-stop-o", "fa-hand-paper"],
        [99, "fa-picture-o", "fa-image"]
    ]

    connection.execute("""
        UPDATE operation
        SET icon = 'fa-tachometer-alt'
        WHERE id = 26""")

    connection.execute("""
        UPDATE operation
        SET icon = 'fa-play'
        WHERE id = 36""")

    connection.execute("""
        UPDATE operation
        SET icon = 'fa-braille'
        WHERE id = 87""")

    for op in data:
        connection.execute("""
            UPDATE operation
            SET icon = '{NEWICON}'
            WHERE icon = '{OLDICON}'""".format(NEWICON=op[2], OLDICON=op[1]))
    session.commit()


def downgrade():
    cntxt = context.get_context()
    session = sessionmaker(bind=cntxt.bind)()
    connection = session.connection()

    data = [
        [58, "fa-external-link-square", "fa-external-link-alt"],
        [12, "icon-union", "fa-plus-square"],
        [93, "fa-flash", "fa-bolt"],
        [6, "icon-projection", "fa-columns"],
        [13, "icon-intersection", "fa-compress"],
        [17, "fa-code-fork", "fa-code-branch"],
        [71, "fa-area-chart", "fa-chart-area"],
        [69, "fa-bar-chart", "fa-chart-bar"],
        [89, "fa-circle-o-notch", "fa-circle-notch"],
        [68, "fa-line-chart", "fa-chart-line"],
        [70, "fa-pie-chart", "fa-chart-pie"],
        [87, "fa-lemon-o", "fa-braille"],
        [53, "fa-map-o", "fa-file"],
        [85, "fa-long-arrow-right", "fa-list-ol"],
        [86, "fa-diamond", "fa-gem"],
        [1, "fa-dashboard", "fa-tags"],
        [31, "fa-exchange", "fa-exchange-alt"],
        [94, "fa-window-close-o", "fa-window-close"],
        [84, "fa-hand-peace-o", "fa-hand-peace"],
        [48, "fa-file-text", "fa-file-alt"],
        [95, "fa-sort-amount-desc", "fa-sort-amount-down"],
        [96, "hashtag", "fa-hashtag"],
        [92, "fa-lemon-o", "fa-lemon"],
        [91, "fa-arrows-v", "fa-arrows-alt-v"],
        [42, "fa-lightbulb-o", "fa-lightbulb"],
        [22, "fa-cloud-download", "fa-cloud-download-alt"],
        [39, "fa-cloud-upload", "fa-cloud-upload-alt"],
        [77, "fa-id-card-o", "fa-id-card"],
        [8, "fa-line-chart", "fa-chart-line"],
        [73, "fa-shield", "fa-shield-alt"],
        [25, "fa-commenting-o", "fa-comment-alt"],
        [83, "fa-vcard-o", "fa-address-card"],
        [20, "fa-gears", "fa-cogs"],
        [52, "fa-long-arrow-right", "fa-long-arrow-alt-right"],
        [50, "fa-hand-stop-o", "fa-hand-paper"],
        [99, "fa-picture-o", "fa-image"]
    ]

    connection.execute("""
        UPDATE operation
        SET icon = 'fa-dashboard'
        WHERE id = 26""")

    connection.execute("""
        UPDATE operation
        SET icon = 'fa-lemon-o'
        WHERE id = 36""")

    connection.execute("""
        UPDATE operation
        SET icon = 'fa-lemon-o'
        WHERE id = 87""")

    for op in data:
        connection.execute("""
            UPDATE operation
            SET icon = '{NEWICON}'
            WHERE icon = '{OLDICON}'""".format(NEWICON=op[1], OLDICON=op[2]))

    session.commit()
