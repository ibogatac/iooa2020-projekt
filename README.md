# iooa2020-projekt
Aplikacija koja bi trebala imati neke mogućnosti knjižnice,
Tehnologije su Python 3.8.3,
Django 3.0.6 i SqlLite baza podataka koja dolazi sa njim,
Bootstrap 4.5.0

Projekt se pokreće tako da kada se skine putem CMD-a ili Powershella na Windowsu se komandom cd dođe do foldera projekt, zatim se u cmd-u upiše ./Scripts/activate da bi se uključio virtualni enviroment. Potom se komandom cd src dođe u mapu src gdje se komandom py manage.py runserver pokrene server i projekt se može vidjeti na pregledniku na localhost:8000

Korisnik pristupa putem linka: https://knjiznica-app.herokuapp.com/
Kada bilo koji korisnik uđe u aplikaciju treba se ulogirati. Korisnik koji želi posuditi knjigu može pregledati listu svih knjiga, žanrova ili autora, te vidjeti svoje posuđene knjige. Kada želi posuditi knjigu to javi Knjižničaru. Knjižničar kada se ulogira ima listu posuđenih i neposuđenih knjiga. Neposuđene knjige su zapravo izdanja knjiga koje postoje. Tako da ako se želi kreirati knjiga koja se može posuditi prvo se treba kreirati knjiga, pa zatim izdanje same knjige. Onda se ide na listu neposuđenih knjiga te se klikne na posudi. Otvara se forma u kojoj se status knjige sa dostupna mijenja na posuđena, te se odabire korisnik sa liste korisnika, također se određuje datum vraćanja. Kada je knjiga posuđena ona se može vidjeti na listi posuđenih knjiga. Tamo je redak tablice crven ako je korisnik zakasnio sa vraćanjem knjige i također piše zakasnina. Knjižničar ima dvije opcije: Obnovi datum vraćanja gdje on zapravo mijenja sam datum vraćanja, te vrati knjigu gdje se otvara forma gdje se status knjige stavlja na dostupna, posuđivač se stavlja na ništa, te se datum vraćanja briše i ostavlja se prazno polje. 
Admin svom sučelju pristupa putem linka : https://knjiznica-app.herokuapp.com/admin
On ako želi dodati korisniku premisije za knjižničara dodaje mu grupu Knjiznica ili premisiju app| knjigaizdanje|obnoviti.
Testni korisnici su: Korisnik(username: Korisnik, password: Knjiznica123)
		        Admin(username: Admin, password: Knjiznica123)
		        Heroku(username: Heroku, password: Knjiznica123)

