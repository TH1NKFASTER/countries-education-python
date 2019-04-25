import flask
import json
import requests
import argparse
from Education import University

University.create_table()

app = flask.Flask("University")
app.university = University()
common_uni = University()


@app.route('/add_university', methods=['POST'])
def add_university():
    # if 'university_name' in flask.request.args:
    #     and 'rank_2018' in flask.request.args and 'university_name' in flask.request.args and 'country_name' in flask.request.args and 'academic_reputation_score' in flask.request.args and 'academic_reputation_rank' in flask.request.args and 'employer_reputation_score' in flask.request.args and 'employer_reputation_rank' in flask.request.args and 'faculty_student_score' in flask.request.args and 'faculty_student_rank' in flask.request.args and 'citations_per_faculty_score' in flask.request.args and 'citations_per_faculty_rank' in flask.request.args and 'international_faculty_score' in flask.request.args and 'international_faculty_rank' in flask.request.args and 'international_students_score' in flask.request.args and 'international_students_rank' in flask.request.args and 'overall_score' in flask.request.args:
    #     print(app.university)
    new_university = University.create(university_name=flask.request.args['university_name'])
    new_university.save()
    # , flask.request.args['rank_2018'], flask.request.args['university_name'], flask.request.args['country_name'],
    # flask.request.args['academic_reputation_score'], flask.request.args['academic_reputation_rank'], flask.request.args['employer_reputation_score'],
    # flask.request.args['employer_reputation_rank'], flask.request.args['faculty_student_score'], flask.request.args['faculty_student_rank'],
    # flask.request.args['citations_per_faculty_score'], flask.request.args['citations_per_faculty_rank'], flask.request.args['international_faculty_score'],
    # flask.request.args['international_faculty_rank'], flask.request.args['international_students_score'], flask.request.args['international_students_rank'],
    # flask.request.args['overall_score'])
    # if 'University' in flask.request.args:
    #     flask.request.args['University'] .save()


@app.route('/universities', methods=['GET'])
def universities():
    return json.dumps(app.university.show_all()) + "\n"


@app.route('/count_universities', methods=['GET'])
def count():
    return json.dumps(app.university.count()) + "\n"


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=50000, type=int)
    # parser.add_argument('--db_name', default='postgres', type=str)
    # parser.add_argument('--user', default='postgres', type=str)
    # parser.add_argument('--password', default='1077', type=str)
    # parser.add_argument('--host', default='localhost', type=str)
    args = parser.parse_args()

    app.run('::', args.port, debug=True, threaded=True)
