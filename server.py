import flask
import json
import argparse
from Education import University, IMO_participant
from constants import *

University.create_table()
# new_university = University.create(rank_2019=1, rank_2018=1, university_name='MASSACHUSETTS INSTITUTE OF TECHNOLOGY', country_name='USA', alumni_employment_rank=4)
# new_university.save()
# new_university = University.create(rank_2019=2, rank_2018=2, university_name='Stanford University', country_name='USA', alumni_employment_rank=5)
# new_university.save()
# new_university = University.create(rank_2019=3, rank_2018=3, university_name='Harvard University', country_name='USA', alumni_employment_rank=1)
# new_university.save()
# new_university = University.create(rank_2019=4, rank_2018=4, university_name='Caltech', country_name='USA', alumni_employment_rank=72)
# new_university.save()
# new_university = University.create(rank_2019=5, rank_2018=6, university_name='University of Oxford', country_name='UK', alumni_employment_rank=3)
# new_university.save()
# new_university = University.create(rank_2019=312, rank_2018=355, university_name='MOSCOW INSTITUTE OF PHYSICS AND TECHNOLOGY', country_name='Russia', alumni_employment_rank=334)
# new_university.save()
# University.drop_table()
IMO_participant.create_table()
# new_participant = IMO_participant.create(year=1984, country='USS', firstname='Andrei', lastname='Astrelin', rank=1, award='Gold_medal')
# new_participant.save()
# new_participant = IMO_participant.create(year=1984, country='USS', firstname='Konstantin', lastname='Ignatiev', rank=1, award='Gold_medal')
# new_participant.save()
# new_participant = IMO_participant.create(year=1984, country='USS', firstname='Leonid', lastname='Oridoroga', rank=1, award='Gold_medal')
# new_participant.save()
# new_participant = IMO_participant.create(year=1984, country='USA', firstname='David', lastname='Moews', rank=1, award='Gold_medal')
# new_participant.save()
# new_participant = IMO_participant.create(year=1984, country='USS', firstname='Fedor', lastname='Nazarov', rank=9, award='Gold_medal')
# new_participant.save()
# IMO_participant.drop_table()
app = flask.Flask("Education")
app.university = University()
app.imo_participant = IMO_participant()


@app.route('/add_university', methods=['POST'])
def add_university():
    new_university = University.create(university_name=flask.request.args['university_name'], rank_2019=flask.request.args['rank_2019']
                                       , rank_2018=flask.request.args['rank_2018'], country_name=flask.request.args['country_name'],
                                       alumni_employment_rank=flask.request.args['alumni_employment_rank'])
    new_university.save()


@app.route('/universities', methods=['GET'])
def universities():
    return json.dumps(app.university.show_all()) + "\n"


@app.route('/count_universities', methods=['GET'])
def count():
    return json.dumps(app.university.count()) + '\n'


@app.route('/sort_universities_by_characteristic', methods=['GET'])
def sort_universities_by_characteristic():
    return json.dumps(app.university.sort_universities_by_characteristic(flask.request.args['characteristic'], flask.request.args['direction']))


@app.route('/imo_participants', methods=['GET'])
def imo_participants():
    return json.dumps(app.imo_participant.show_all()) + '\n'


@app.route('/add_imo_participant', methods=['POST'])
def add_participant():
    new_participant = IMO_participant.create(year=flask.request.args['year'], country=flask.request.args['country'], firstname=flask.request.args['firstname'], lastname=flask.request.args['lastname'],
                                             rank=flask.request.args['rank'], award=flask.request.args['award'])
    new_participant.save()


@app.route('/count_participants', methods=['GET'])
def count_partcipants():
    return json.dumps(app.imo_participant.count()) + '\n'


if __name__ == '__main__':
    app.run('::', port, debug=True, threaded=True)
