# **REQUIRED DEPENDENCIES**

Flask == 0.12.2 using (sudo pip install flask)

Python == 2.7.6

Python == 3.4.3 

SQLite == 3.8.2 

beautifulsoup4 using (sudo apt-get install python3-bs4)

# **DIRECTORY STRUCTURE**



 **bmtc->templates**->index.html

      ->app.py
                             
      ->bmtc.db
                             
      ->route.py
      
      ->fare.py
      
      ->route_db.py
      
      ->fare_db.py
      
      ->route.pdf
      
      ->fare.pdf
      
      ->bmtc.db
      
      ->bmtc_fare_scrap_Nov_09_2017.json
      
      ->bmtc_route_scrap_Nov_09_2017.json
      
      ->screenshot of webpage
   
# **BUILD INSTRUCTIONS**
clone the project:- using **git clone https://github.com/Anchal-kansal/bmtc/ **
1. To fetch, parse the bus stops and timings, and store them in json file and database, run route.py using **python3 route.py** [input example: bus_id could be: 314 and route_id could be 3F]
2. To fetch, parse the fares list, and store them in json file and database, run fare.py using **python3 fare.py**
[valid input types are: A/C and General]
3. To fetch the data from database, run route_db.py and fare_db.py, using **python3 route_db.py** and **python3 fare_db.py**, respectively.
4. To represent the data on the webpage, run app.py using **python app.py**. Go to browser and run http://127.0.0.1:5000/
Then, enter bus_id=314 and route_id=3F(for example) and whoosh! the data is visible on the webpage!!!
**P.S.:- for data to be visible, it must be in the db, and insert query is in route.py, so, before running app.py, run route.py**


    
    
