from peewee import *

db = PostgresqlDatabase(database="postgres", user="postgres", password="1077", host='localhost')


class University(Model):
    rank_2019 = IntegerField()
    rank_2018 = IdentityField()
    university_name = CharField()
    country_name = CharField()
    academic_reputation_score = FloatField()
    academic_reputation_rank = IntegerField()
    employer_reputation_score = FloatField()
    employer_reputation_rank = IntegerField()
    faculty_student_score = FloatField()
    faculty_student_rank = IntegerField()
    citations_per_faculty_score = FloatField()
    citations_per_faculty_rank = IntegerField()
    international_faculty_score = FloatField()
    international_faculty_rank = IntegerField()
    international_students_score = FloatField()
    international_students_rank = IntegerField()
    overall_score = FloatField()

    class Meta:
        database = db

    def add_university(self, rank_2019, rank_2018, university_name, country_name, academic_reputation_score, academic_reputation_rank, employer_reputation_score, employer_reputation_rank,
                       faculty_student_score, faculty_student_rank, citations_per_faculty_score, citations_per_faculty_rank, international_faculty_score, international_faculty_rank,
                       international_students_score, international_students_rank, overall_score):
        new_university = University.create(rank_2019=rank_2019, rank_2018=rank_2018, university_name=university_name, country_name=country_name, academic_reputation_score=academic_reputation_score,
                                           academic_reputation_rank=academic_reputation_rank, employer_reputation_score=employer_reputation_score, employer_reputation_rank=employer_reputation_rank,
                                           faculty_student_score=faculty_student_score, faculty_student_rank=faculty_student_rank, citations_per_faculty_score=citations_per_faculty_score,
                                           citations_per_faculty_rank=citations_per_faculty_rank, international_faculty_score=international_faculty_score,
                                           international_faculty_rank=international_faculty_rank,
                                           international_students_score=international_students_score, international_students_rank=international_students_rank, overall_score=overall_score)
        new_university.save()

    def show_all(self):
        print(1)
        for uni in University.select():
            print(uni.rank_2019, uni.university_name)

    def count(self):
        return 1