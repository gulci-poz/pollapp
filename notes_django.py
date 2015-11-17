#dajemy przed startem aplikacji, jeszcze przed utworzeniem modelu
#są to migracje dla aplikacji zainstalowanych w projekcie
#po stworzeniu modelu możemy hurtem zrobić wszystkie migracje
#musimy mieć aplikację dopisaną do installed
#./manage.py migrate

#tworzymy migracje
#./manage.py makemigrations polls

#sqlmigrate prezentuje jaki kod SQL zostanie uruchomiony przez migrate
#sqlmigrate nie wykonuje tego kody
#ten kod SQL jest specyficzny dla danego silnika db
#./manage.py sqlmigrate polls 0001

#sprawdzenie problemów w projekcie - nie robi migracji ani nie tyka db
#./manage.py check

#aplikujemy migracje
#./manage.py migrate

#django przechowuje listę zaaplikowanych migracji w tabeli django_migrations
#migracje to historia schematu naszej db

#./manage.py ustawia zmienną środowiskową DJANGO_SETTINGS_MODULE
#dostajemy ścieżkę importu do settings.py
#wystarczy dać
#import pollapp
#i np.:
#pollapp.settings.DATABASES
#./manage.py shell

#bez użycia manage.py
#w zmiennej DJANGO_SETTINGS_MODULE dajemy ścieżkę do pollapp.settings
#import django
#django.setup()

#definiujemy __str__
#w py2 definiujemy __unicode__ (django ma domyślną metodę __str__, która wywołuje __unicode__ i konwertuje rezultat do UTF-8)
#object w py ma odwrotnie: __unicode__, który uruchamia __str__

from polls.models import Question, Choice
Question.objects.all()
#mamy włączony support dla stref czasowych, potrzebujemy datetime z tzinfo
#nie używamy datetime.datetime.now()
from django.utils import timezone
q = Question(question_text = "What's new?", pub.date = timezone.now())
q.save()
#bazy danych mogą zwracać long int w py
q.id
q.question_text
q.pub_date
q.question_text = "What's up?"
q.save()
Question.objects.all()
#po dodaniu __str__
Question.objects.all()
Question.objects.filter(id = 1)
Question.objects.filter(question_text__startswith = "What")
current_year = timezone.now().year
Question.objects.get(pub_date__year = current_year)
#nieistniejące id
Question.objects.get(id = 2)
#szukanie po kluczu głównym
Question.objects.get(pk = 1)
q = Question.objects.get(pk = 1)
q.was_published_recently()
#na razie nic
q.choice_set.all()
#tworzymy nowy obiekt Choice, wstawiamy wybór i dodajemy do zbioru
#instrukcja zwraca nowy obiekt Choice
#mamy takie odwrócone (względem ForeignKey) API
#na pytaniu budujemy zbiór odpowiedzi, które prowadzą do tego pytania
q.choice_set.create(choice_text = "Not much", votes = 0)
q.choice_set.create(choice_text = "The sky", votes = 0)
c = q.choice_set.create(choice_text = "Just hacking again", votes = 0)
#obiekty Choice mają dostęp do powiązanych pytań
c.question
#można też dać
Choice.objects.all()
#pytania mają dostęp do zbioru odpowiedzi na nie za pomocą API - choice_set
q.choice_set.all()
q.choice_set.count()
#API automatycznie śledzi relacje w głąb
#używamy podwójnego __ do oddzielenia relacji
#szukamy wyborów dla wszystkich pytań z odpowiednią datą
Choice.objects.filter(question__pub_date__year = current_year)
c = q.choice_set.filter(choice_text__startswith = "Just hacking")
c.delete()

#./manage.py createsuperuser
#powiadamiamy aplikację admin, że Question mają interfejs admina - rejestrujemy model w admin.py

#uwaga na django 1.8.6!!! plik settings.py jest ze starego frameworka 1.7
#nie ma tam chociażby TEMPLATES
#używam django 1.8.5

#przygotowujemy szablon dla strony admina
#w korzeniu projektu (tam gdzie manage.py) tworzymy foldery templates/admin
#kopiujemy tam plik base.html ze ścieżki django (ścieżka podaje lib):
#~/projects/py_projects/virtualenvs/official/lib/python3.4/site-packages/django/contrib/admin/templates/admin/base_site.html
#kopiujemy też index.html
#mamy zmienną szablonu app_list - zainstalowane aplikacje django
#sposób na sprawdzenie ścieżki
#nie rozumiem co ma dać ten krok, wycinamy tylko pusty string - pierwszy element ścieżki
#import sys
#sys.path = sys.path[1:]
import django
print(django.__path__)

#jeśli APP_DIRS = True to w wypadku braku szablonów django szuka w templates każdej danej aplikacji
