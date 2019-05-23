import argparse
import flask
import requests
from constants import *


def create_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    add_imo_participant_parser = subparsers.add_parser('add_imo_participant')
    show_imo_participants_parser = subparsers.add_parser('show_imo_participants')
    add_university_parser = subparsers.add_parser('add_university')
    show_universities_parser = subparsers.add_parser('show_universities')
    count_universities_parser = subparsers.add_parser('count_universities')
    sort_universities_by_characteristic_parser = subparsers.add_parser('sort_universities_by_characteristic')
    count_imo_participants_parser = subparsers.add_parser('count_participants')

    count_imo_participants_parser.set_defaults(method='count_participants')
    show_imo_participants_parser.set_defaults(method='show_imo_participants')
    add_imo_participant_parser.set_defaults(method='add_imo_participant')
    show_universities_parser.set_defaults(method='show_universities')
    count_universities_parser.set_defaults(method='count_universities')
    sort_universities_by_characteristic_parser.set_defaults(method='sort_universities_by_characteristic')
    add_university_parser.set_defaults(method='add_university')

    add_imo_participant_parser.add_argument('--year', required=True, type=int)
    add_imo_participant_parser.add_argument('--country', required=True, type=str)
    add_imo_participant_parser.add_argument('--firstname', required=True, type=str)
    add_imo_participant_parser.add_argument('--lastname', required=True, type=str)
    add_imo_participant_parser.add_argument('--rank', required=True, type=int)
    add_imo_participant_parser.add_argument('--award', default='Nothing', required=False, type=str)

    add_university_parser.add_argument('--university_name', required=True, type=str)
    add_university_parser.add_argument('--rank_2019', required=False, type=int)
    add_university_parser.add_argument('--rank_2018', required=False, type=int)
    add_university_parser.add_argument('--country_name', required=False, type=str)
    add_university_parser.add_argument('--alumni_employment_rank', required=False, type=int)

    sort_universities_by_characteristic_parser.add_argument('--characteristic', default='rank_2019', required=False, type=str, help='name of the characteristic')
    sort_universities_by_characteristic_parser.add_argument('--direction', default='ASC', required=False, type=str, help='direction of sorting')
    return parser


def add_university(university_name, rank_2019, rank_2018, country_name, alumni_employment_rank):
    rank_2018 = int(rank_2018)
    rank_2019 = int(rank_2019)
    alumni_employment_rank = int(alumni_employment_rank)
    requests.post(
        'http://{}:{}/add_university?university_name={}&rank_2019={}&rank_2018={}&country_name={}&alumni_employment_rank={}'.format(address, port, university_name, rank_2019, rank_2018, country_name,
                                                                                                                                    alumni_employment_rank))

    return flask.redirect('http://{}:{}/universities'.format(address, port))


def show_universities():
    x = requests.get('http://{}:{}/universities'.format(address, port)).json()
    for i in x:
        for j in i:
            print(j, end=' ')
        print()


def count_universities():
    x = requests.get('http://{}:{}/count_universities'.format(address, port)).json()
    print(x)


def sort_universities_by_characteristic(characteristic, direction):
    x = requests.get('http://{}:{}/sort_universities_by_characteristic?characteristic={}&direction={}'.format(address, port, characteristic, direction)).json()
    for i in x:
        for j in i:
            print(j, end=' ')
        print()


def show_imo_participants():
    x = requests.get('http://{}:{}/imo_participants'.format(address, port)).json()
    for i in x:
        for j in i:
            print(j, end=' ')
        print()


def add_imo_participant(year, country, firstname, lastname, rank, award):
    year = int(year)
    rank = int(rank)
    requests.post(
        'http://{}:{}/add_imo_participant?year={}&country={}&firstname={}&lastname={}&rank={}&award={}'.format(address, port, year, country, firstname, lastname, rank, award))
    return flask.redirect('http:/{}:{}/imo_participants'.format(address, port))


def count_imo_participants():
    x = requests.get('http://{}:{}/count_participants'.format(address, port)).json()
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
        add_university(args.university_name, args.rank_2019, args.rank_2018, args.country_name, args.alumni_employment_rank)
    elif move == 'sort_universities_by_characteristic':
        sort_universities_by_characteristic(args.characteristic, args.direction)
    elif move == 'show_imo_participants':
        show_imo_participants()
    elif move == 'add_imo_participant':
        add_imo_participant(args.year, args.country, args.firstname, args.lastname, args.rank, args.award)
    elif move == 'count_participants':
        count_imo_participants()
