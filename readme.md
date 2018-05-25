=====
<h3>Django CRUD</h3>
=====
<p>Books catalog</p>

<h3>Install</h3>

<h4>Migrate database</h4>
<code>
python manage.py makemigrations your-app-name<br />
python manage.py sqlmigrate your-app-name 0001 --database=whatsappbot<br />
python manage.py migrate your-app-name --database=whatsappbot<br />
</code>


<h3>Tests</h3>
<h4>How to run tests</h4>
<code>python manage.py test your-app-name</code>

<h3>Run on server</h3>
sudo python3 run.py

<code>
python3 manage.py runserver 0.0.0.0:8000
</code>