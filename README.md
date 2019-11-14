# thique-atto
Establish a dashboard/landing page that accurately keeps track of various information about the status of the charging stations. The team is focused on creating a page that would be helpful for HECO to determine if certain stations are congested or non-operational.

# Technologies Used:

- Flask
- flask_googlemaps
- pandas
- plotly

# Installation Instructions

1. If you do not have Python yet installed on your computer, navigate to https://www.python.org/downloads/ and choose the updated version of Python (Python 3). 
2. Clone/download this repository
3. Navigate to 'thique-atto' directory in your terminal of choice

4. Python strongly recommends working with a virtual environment for installation of packages, as such you must run this in your termnial while still in thique-atto directory:
```
python3 -m venv venv

virtualenv env
```

5a. Then, if on a mac use:
```
source venv/bin/actiave
```

5b. Otherwise run:
```
venv\Scripts\activate 
```

In this example, we use python3 but if you've set python3 to your PATH then just python will work fine. 

6. Then now you must install the packages needed to run this app:

```
pip install flask
pip install plotly
pip install pandas
pip install flask_googlemaps
```

7. To run this project:
```
python3 app.py
```
