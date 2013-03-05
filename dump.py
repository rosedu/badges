#!/usr/bin/env python

from collections import defaultdict
from path import path
import yaml
import jinja2


def read_badges(badge_dir_path):
    rv = {}
    for badge_path in badge_dir_path.files():
        data = yaml.load(badge_path.bytes())
        data['_template'] = jinja2.Template(data['description'])
        rv[data['id']] = data
    return rv


def read_grants(grant_dir_path):
    rv = defaultdict(list)
    for grant_path in grant_dir_path.files():
        data = yaml.load(grant_path.bytes())
        rv[data['badge']].extend(data['grants'])
    return rv


def dump(repo_path):
    badges = read_badges(repo_path / 'badge')
    grants = read_grants(repo_path / 'grant')
    for badge_id, grant_list in grants.iteritems():
        assert badge_id in badges, "Missing badge %r" % badge_id
        badge = badges[badge_id]
        print "==", badge_id, "=="
        print
        for grant in grant_list:
            print badge['_template'].render(**grant)
            print


if __name__ == '__main__':
    dump(path(__file__).parent)
