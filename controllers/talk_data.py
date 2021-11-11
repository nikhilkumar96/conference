import datetime
import json
from table import *
from constants import DB_CONN_URI
from resources.alchemytojson import AlchemyEncoder

engine = create_engine(DB_CONN_URI, echo=True)
Session = sessionmaker(bind=engine)
session = Session()


class TalkData:

    def __init__(self, data):
        self.data = data

    def add_data(self):
        for item in self.data:
            talk_obj = Talk(title=item['title'], description=item['description'], duration=item['duration'],
                            date=datetime.date(item['date'][0], item['date'][1], item['date'][2]),
                            time=datetime.time(item['time'][0], item['time'][1], item['time'][2]),
                            conference_id=item['conference_id'])
            talk_obj.speakers = [Speaker(username=s['username'], email=s['email']) for s in item['speaker']]
            talk_obj.participants = [Participant(username=p['username'], email=p['email']) for p in item['participant']]
            session.add(talk_obj)
            session.commit()
        return {"Status": "Success"}

    def edit_data(self, talk_id):
        matched_data = session.query(Talk).get(talk_id)
        for k, v in self.data.items():
            if k == 'description':
                matched_data.description = v
            elif k == "date":
                matched_data.date = datetime.date(v[0], v[1], v[2])
            elif k == "time":
                matched_data.time = datetime.time(v[0], v[1], v[2])
            elif k == "title":
                matched_data.title = v
            elif k == "conference_id":
                matched_data.conference_id = v
            elif k == "duration":
                matched_data.duration = v
            elif k == "speaker":
                matched_data.speakers = [Speaker(username=s['username'], email=s['email']) for s in v]
            elif k == "participant":
                matched_data.participants = [Participant(username=p['username'], email=p['email']) for p in v]
        session.commit()
        return {"Status": "Success"}

    def get_data(self):
        return json.dumps(session.query(Talk).all(), cls=AlchemyEncoder)
