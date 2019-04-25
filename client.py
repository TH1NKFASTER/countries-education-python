import argparse
import json
import flask
import requests
from Education import University
# University.drop_table()
University.create_table()
INF = 4 ** 15
common_uni = University()


def create_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    add_university_parser = subparsers.add_parser('add_university')
    show_universities_parser = subparsers.add_parser('show_universities')
    count_universities_parser = subparsers.add_parser('count_universities')
    sort_universities_by_characteristic_parser = subparsers.add_parser('sort_universities_by_characteristic')
    # ...

    show_universities_parser.set_defaults(method='show_universities')
    count_universities_parser.set_defaults(method='count_universities')
    sort_universities_by_characteristic_parser.set_defaults(method='sort_universities_by_characteristic')
    add_university_parser.set_defaults(method='add_university')

    add_university_parser.add_argument('--university_name', required=True, type=str)

    sort_universities_by_characteristic_parser.add_argument('--characteristic', default='rank_2019', required=False, type=str, help='name of the characteristic')
    sort_universities_by_characteristic_parser.add_argument('--left', default=0, required=False, type=int, help='left border')
    sort_universities_by_characteristic_parser.add_argument('--right', default=+INF, required=False, type=int, help='right border')
    sort_universities_by_characteristic_parser.add_argument('--direction', default='ASC', required=False, type=str, help='direction of sorting')
    return parser


def add_university(university_name):
    # rank_2018, university_name, country_name, academic_reputation_score, academic_reputation_rank, employer_reputation_score, employer_reputation_rank,
    # faculty_student_score, faculty_student_rank, citations_per_faculty_score, citations_per_faculty_rank, international_faculty_score, international_faculty_rank,
    # international_students_score, international_students_rank, overall_score):
    # rank_2018=rank_2018, university_name=university_name, country_name=country_name, academic_reputation_score=academic_reputation_score,
    # academic_reputation_rank=academic_reputation_rank, employer_reputation_score=employer_reputation_score, employer_reputation_rank=employer_reputation_rank,
    # faculty_student_score=faculty_student_score, faculty_student_rank=faculty_student_rank, citations_per_faculty_score=citations_per_faculty_score,
    # citations_per_faculty_rank=citations_per_faculty_rank, international_faculty_score=international_faculty_score,
    # international_faculty_rank=international_faculty_rank,
    # international_students_score=international_students_score, international_students_rank=international_students_rank, overall_score=overall_score)
    requests.post('http://127.0.0.1:50000/add_university?university_name={}'.format(university_name))
    return flask.redirect('http://127.0.0.1:50000/universities')

def show_universities():
    x = requests.get('http://127.0.0.1:50000/universities').json()
    print(x)


def count_universities():
    x = requests.get('http://127.0.0.1:50000/count_universities').json()
    print(x)


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()

    move = args.method
    if move == 'show_universities':
        show_universities()
    elif move == 'count_universities':
        count_universities()
    elif move == 'add_university':
        add_university(args.university_name)
