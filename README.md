**BMTC WEB SCRAPPER** is a python based project which fetches the route and fare details based on the given bus id and route id. The fetched data is stored in a json file as well as sqlite db. It is build using python and its libraries and sqlite db.

There is a script to fetch the data from the database. It is build in python.

There is a web program which fetches the data from the database and show it on the web page. It is build using html, css, flask.


# **BUILD INSTRUCTIONS**
clone the project:- using **git clone https://github.com/Anchal-kansal/bmtc/**

1. To fetch, parse the bus stops and timings, and store them in json file and database, run route.py using **python3 route.py** [input example: bus_id could be: 314 and route_id could be 3F]
2. To fetch, parse the fares list, and store them in json file and database, run fare.py using **python3 fare.py**
[valid input types are: A/C and General]
3. To fetch the data from database, run route_db.py and fare_db.py, using **python3 route_db.py** and **python3 fare_db.py**, respectively.
4. To represent the data on the webpage, run app.py using **python app.py**. Go to browser and run http://127.0.0.1:5000/
Then, enter bus_id=314 and route_id=3F(for example) and whoosh! the data is visible on the webpage!!!
**P.S.:- for data to be visible, it must be in the db, and insert query is in route.py, so, before running app.py, run route.py**


    
    
