#!/bin/bash

COUNTER=0
PG_NOT_READY=true

cd hivemind_powerball
while [ $COUNTER -lt 6 ] && [ $PG_NOT_READY = true ]
do
    python manage.py migrate --settings=config.settings.containerized &> /dev/null | grep --quiet 'Is the server running on host "db"'
    echo "Waiting for postgres..." 
    sleep 2
    if [ $? == 0 ]; then
        PG_NOT_READY=false
        python manage.py migrate --settings=config.settings.containerized
        python manage.py test -v 2 --settings=config.settings.containerized
        python manage.py runserver 0.0.0.0:8000 --settings=config.settings.containerized
    fi
    COUNTER=`expr $COUNTER + 1`
done

if [ $PG_NOT_READY = true ]; then
    echo "There's a problem starting the app! Use the troubleshooting command at the end of docker-start-app.sh to figure out what's broken."
fi

