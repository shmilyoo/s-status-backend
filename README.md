# Introduce


# install
1. GeoIP2: an api use geoip2 offline database to provide ip's infomation
https://geoip2.readthedocs.io/en/latest
 
    download geoip2 database and extract to project root directory
    http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.mmdb.gz

    (optional) use the C extension for the database reader
    howto：https://github.com/maxmind/libmaxminddb/blob/master/README.md

2. modify the configuration of app/config.py

3. create a mysql database, name it as config.DB_DB


    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade
    
    