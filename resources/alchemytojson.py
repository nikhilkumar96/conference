from sqlalchemy.ext.declarative import DeclarativeMeta
import json
import datetime


class AlchemyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                if field != 'registry':
                    data = obj.__getattribute__(field)
                    try:
                        json.dumps(data)
                        fields[field] = data
                    except TypeError:
                        if isinstance(data, datetime.date) or isinstance(data, datetime.time):
                            fields[field] = json.loads(json.dumps(data, indent=4, sort_keys=True, default=str))
            return fields

        return json.JSONEncoder.default(self, obj)