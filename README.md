# Movie Chatbot using Google Dialogflow and Flask 

### Steps to deploy chatbot on heroku

- Download the Heroku CLI from [here](https://devcenter.heroku.com/articles/heroku-cli).
```bash 
cd chatbot
```

```bash
git init && git add . && git commit -m "chatbot deployment"
``` 
```bash
heroku login
```
```bash
heroku create 
```
```bash
git push heroku master
```

### Run Web app 
```bash 
pip install -r requirements.txt 
```

```bash 
python app.py
```