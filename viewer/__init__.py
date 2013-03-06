import flask
from path import path
import dump

badges = dump.read_badges(path(__name__).parent / 'badge')
grants = dump.read_grants(path(__name__).parent / 'grant')

viewer = flask.Blueprint('viewer', __name__, template_folder='templates')


@viewer.route('/')
def home():
    names = set()
    for item_list in grants.itervalues():
        for item in item_list:
            names.add(item['person_name'])
    return flask.render_template('home.html', names=sorted(names))
