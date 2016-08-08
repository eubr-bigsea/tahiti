import json
import uuid

import schema
from marshmallow_jsonschema import JSONSchema
from marshmallow import Schema, fields


class UserSchema(Schema):
    username = fields.String()
    age = fields.Integer()
    birthday = fields.Date()


if __name__ == '__main__':
    w = schema.WorkflowExecuteRequestSchema()

    workflow = dict(id=1, name="WF01", user_id=100, user_login='walter',
                    user_name='Walter Santos',
                    token=str(uuid.uuid4()))
    print json.dumps(workflow)
    workflow['tasks'] = [
        dict(id=1, order=1, log_level='INFO', is_start=True, is_end=True,
             operation_id=32434, operation_name='MAP_REDUCE',
             name='Task',
             input=dict(id=232, name="input"), next_task_id=12,
             output=dict(id=232, name="output"),
             parameters=[dict(name="support", value="1")])
    ]

    user_schema = UserSchema()
    print json.dumps(w.validate(workflow), indent=2)
    print json.dumps(w.dump(workflow).data, indent=2)

    json_schema = JSONSchema()

    u = schema.TaskExecuteRequestSchema()
    print json.dumps(json_schema.dump(u).data, indent=2)
