"""
Curs 3 - Dict
"""

my_dict = {
    "nume": 'Popescu',
    "prenume": 'Alex',
    "varsta": 18,
    "situatie_examen": True,
    "detalii": {
        "cnp": 345,
        "adresa": 'calea_iadului',
        "numarul": 2
    }
}
print(my_dict.keys())
print(my_dict['varsta'])
print(my_dict['detalii']['adresa'])
# Todo - sa compunem un dictionar si mai complex in care la cheia detalii-> sa contina
#  si mai multe detalii -> o lista cu mai multe dictionare (retea de socializare)
