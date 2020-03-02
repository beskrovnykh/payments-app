
Flask web app ready to use in production

## Dependencies

*Flask–Script*, *RestPlus*, *SqlAlchemy*, *Flask-Migrate* and *Bluebrint* and more.
All dependencies are provided via `requirements.txt`. Use `pip install -r requirements.txt` to install

## File Navigation
* `config.py` ables to switch between Testing, Development and Production modes; parameterized via DATABASE_URL to use MySQL (MariaDB) or Postgress in production
* `manage.py` application entry point, consists of set of commands for running tests, migrating database, running web app (and more)
* `migrations/` scripts for database migration
* `model/` data access layer consits of ORM entities, 
* `service/` buisness logic of application,
* `controller/` REST end points,
* `utils/` package for DTO,  converters, transformers, helpers, etc.

## Apllication Usage
1. `python manage.py db upgrade` initialize database and upgrades it to the current state
2. `python manage.py seed` seeds test data
3. `python manage run` runs payments application locally http://127.0.0.1:5000/
4. `python manage.py db migrate` save database changes  
