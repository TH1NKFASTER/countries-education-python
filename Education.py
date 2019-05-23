from peewee import *
from constants import *

db = PostgresqlDatabase(database=database, user=user, password=password, host=host)


class IMO_participant(Model):
    year = IntegerField()
    country = CharField()
    firstname = CharField()
    lastname = CharField()
    rank = IntegerField()
    award = CharField()

    class Meta:
        database = db

    @staticmethod
    def show_all():
        y = list()
        for participant in IMO_participant.select():
            x = list()
            x.append(participant.year)
            x.append(participant.country)
            x.append(participant.firstname)
            x.append(participant.lastname)
            x.append(participant.rank)
            x.append(participant.award)
            y.append(x)
        return y

    @staticmethod
    def count():
        return len(IMO_participant.show_all())


class University(Model):
    rank_2019 = IntegerField()
    rank_2018 = IntegerField()
    university_name = CharField()
    country_name = CharField()
    alumni_employment_rank = IntegerField()

    class Meta:
        database = db

    @staticmethod
    def show_all():
        y = list()
        for uni in University.select():
            x = list()
            x.append(uni.rank_2019)
            x.append(uni.rank_2018)
            x.append(uni.university_name)
            x.append(uni.country_name)
            x.append(uni.alumni_employment_rank)
            y.append(x)
        return y

    @staticmethod
    def count():
        return len(University.show_all())

    @staticmethod
    def sort_universities_by_characteristic(characteristic='rank_2019', direction='ASC'):

        a = getattr(University, characteristic)
        y = list()
        if direction == 'DESC':
            a = -a
        for uni in University.select().order_by(a):
            x = list()
            x.append(uni.rank_2019)
            x.append(uni.rank_2018)
            x.append(uni.university_name)
            x.append(uni.country_name)
            x.append(uni.alumni_employment_rank)
            y.append(x)
        return y
