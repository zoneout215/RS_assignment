# This is /app folder Dedicated to store scripts of the application
## Content
* **app.py** runs the app
* **authenticate.py** is responsible for password checking and login in 
* **recommendetions_generator.py** is responsible for creating files not iside the app to reduce loading time
* **template.py** is responsible for tailing data into ribbons of recommedations
* **requirements.txt** contain the info about package versions for your needs and for deployment
* in order to run app.py with streamlit use this from the project directory
```
streamlit run app/app.py
```
* in order to run other scripts use this from the project directory
```
python app/ \<name of the script\>.py
```

and make sure you have the same package versions as in requirements.txt