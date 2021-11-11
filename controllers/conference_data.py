import datetime
import json
from table import *
from constants import DB_CONN_URI
from resources.alchemytojson import AlchemyEncoder

engine = create_engine(DB_CONN_URI, echo=True)
Session = sessionmaker(bind=engine)
session = Session()


class ConferenceData:

    def __init__(self, data):
        self.data = data

    def add_data(self):
        for item in self.data:
            conf_obj = Conference(title=item['title'], description=item['description'],
                                  start_date=datetime.date(item['start_date'][0], item['start_date'][1],
                                                           item['start_date'][2]),
                                  end_date=datetime.date(item['end_date'][0], item['end_date'][1], item['end_date'][2]))
            conf_obj.talks = [Talk(title=t['title'], description=t['description'], duration=t['duration'],
                                  date=datetime.date(t['date'][0], t['date'][1],
                                                     t['date'][2]), time=datetime.time(t['time'][0], t['time'][1],
                                                                                       t['time'][2])) for t in
                             item['talk']]
            for count, t in enumerate(item['talk']):
                conf_obj.talks[count].speakers = [Speaker(username=s['username'], email=s['email']) for s in t['speaker']]
                conf_obj.talks[count].participants = [Participant(username=p['username'], email=p['email']) for p in
                                                    t['participant']]
            session.add(conf_obj)
            session.commit()
        return {"Status": "Success"}

    def edit_data(self, conf_id):
        matched_data = session.query(Conference).get(conf_id)
        for k, v in self.data.items():
            if k == 'description':
                matched_data.description = v
            elif k == "end_date":
                matched_data.end_date = datetime.date(v[0], v[1], v[2])
            elif k == "start_date":
                matched_data.start_date = datetime.date(v[0], v[1], v[2])
            elif k == "title":
                matched_data.title = v
        session.commit()
        return {"Status": "Success"}

    def get_data(self):
        return json.dumps(session.query(Conference).all(), cls=AlchemyEncoder)
