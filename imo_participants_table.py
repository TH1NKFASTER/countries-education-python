from Education import IMO_participant

if IMO_participant.table_exists():
    IMO_participant.drop_table()
IMO_participant.create_table()

new_participant = IMO_participant.create(year=1984, country='USS', firstname='Andrei', lastname='Astrelin', rank=1, award='Gold_medal')
new_participant.save()
new_participant = IMO_participant.create(year=1984, country='USS', firstname='Konstantin', lastname='Ignatiev', rank=1, award='Gold_medal')
new_participant.save()
new_participant = IMO_participant.create(year=1984, country='USS', firstname='Leonid', lastname='Oridoroga', rank=1, award='Gold_medal')
new_participant.save()
new_participant = IMO_participant.create(year=1984, country='USA', firstname='David', lastname='Moews', rank=1, award='Gold_medal')
new_participant.save()
new_participant = IMO_participant.create(year=1984, country='USS', firstname='Fedor', lastname='Nazarov', rank=9, award='Gold_medal')
new_participant.save()
