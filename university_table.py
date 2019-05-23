from Education import University

if University.table_exists():
    University.drop_table()
University.create_table()
new_university = University.create(rank_2019=1, rank_2018=1, university_name='MASSACHUSETTS INSTITUTE OF TECHNOLOGY', country_name='USA', alumni_employment_rank=4)
new_university.save()
new_university = University.create(rank_2019=2, rank_2018=2, university_name='Stanford University', country_name='USA', alumni_employment_rank=5)
new_university.save()
new_university = University.create(rank_2019=3, rank_2018=3, university_name='Harvard University', country_name='USA', alumni_employment_rank=1)
new_university.save()
new_university = University.create(rank_2019=4, rank_2018=4, university_name='Caltech', country_name='USA', alumni_employment_rank=72)
new_university.save()
new_university = University.create(rank_2019=5, rank_2018=6, university_name='University of Oxford', country_name='UK', alumni_employment_rank=3)
new_university.save()
new_university = University.create(rank_2019=312, rank_2018=355, university_name='MOSCOW INSTITUTE OF PHYSICS AND TECHNOLOGY', country_name='Russia', alumni_employment_rank=334)
new_university.save()
