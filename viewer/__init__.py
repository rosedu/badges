import flask
from path import path
import dump

badges = dump.read_badges(path(__name__).parent / 'badge')
grants = dump.read_grants(path(__name__).parent / 'grant')

viewer = flask.Blueprint('viewer', __name__, template_folder='templates')


def all_badges():
    for badge_id, item_list in grants.iteritems():
        for item in item_list:
            yield badge_id, item


@viewer.route('/')
def home():
    names = set(i['person_name'] for b, i in all_badges())
    return flask.render_template('home.html', names=sorted(names))


@viewer.route('/<person_name>')
def person(person_name):
    granted = [badges[b]['_template'].render(**i)
               for b, i in all_badges()
               if i['person_name'] == person_name]
    if not granted:
        flask.abort(404)
    return flask.render_template('person.html', **{
        'person_name': person_name,
        'badges': granted,
    })
