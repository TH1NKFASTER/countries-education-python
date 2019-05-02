from peewee import *

database = 'postgres'
user = 'postgres'
password = '1077'
host = 'localhost'  # нормально без костылей не вышло
db = PostgresqlDatabase(database=database, user=user, password=password, host=host)


class IMO_participant(Model):
    year = IntegerField()
    country = CharField()
    firstname = CharField()
    lastname = CharField()
    total = IntegerField()
    rank = IntegerField()
    award = CharField()

    class Meta:
        database = db

    def show_all(self):
        y = list()
        for participant in IMO_participant.select():
            x = list()
            x.append(participant.year)
            x.append(participant.country)
            x.append(participant.firstname)
            x.append(participant.lastname)
            x.append(participant.total)
            x.append(participant.rank)
            x.append(participant.award)
            y.append(x)
        return y

    def count(self):
        common_participant = IMO_participant()
        return len(IMO_participant.show_all(common_participant))


class University(Model):
    rank_2019 = IntegerField()
    rank_2018 = IntegerField()
    university_name = CharField()
    country_name = CharField()
    alumni_employment_rank = IntegerField()

    class Meta:
        database = db

    def show_all(self):
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

    def count(self):
        common_university = University()
        return len(University.show_all(common_university))

    def sort_universities_by_characteristic(self, characteristic='rank_2019', direction='ASC'):
        y = list()
        if direction == 'ASC':
            for uni in University.select().order_by(getattr(University, characteristic)):
                x = list()
                x.append(uni.rank_2019)
                x.append(uni.rank_2018)
                x.append(uni.university_name)
                x.append(uni.country_name)
                x.append(uni.alumni_emplyment_rank)
                y.append(x)
        elif direction == 'DESC':
            for uni in University.select().order_by(-getattr(University, characteristic)):
                x = list()
                x.append(uni.rank_2019)
                x.append(uni.rank_2018)
                x.append(uni.university_name)
                x.append(uni.country_name)
                x.append(uni.alumni_emplyment_rank)
                y.append(x)
        return y
