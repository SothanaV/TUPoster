#! bin/bash
echo '-- Run Setup Script --'

python manage.py makemigrations app
python manage.py migrate
echo yes | python manage.py flush
echo '- init db -'
python manage.py shell < init_db.py
echo '- Add Referee User -'
python manage.py shell < add_ref.py
echo '- Add Poster -'
python manage.py shell < add_poster.py
echo '- Add Dummy -'
python manage.py shell < add_dummy_data.py
echo '- Success -'
python manage.py runserver 0.0.0.0:8000
