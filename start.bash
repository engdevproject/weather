rasa train
rasa run -m models --endpoints endpoints.yml --port 5505 --credentials credentials.yml --cors "*"

# start our html server