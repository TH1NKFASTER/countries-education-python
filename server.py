import flask
import json
from Education import University, IMO_participant
from constants import *
import university_table
import imo_participants_table


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
