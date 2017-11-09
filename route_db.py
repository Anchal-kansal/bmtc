import sqlite3
conn = sqlite3.connect("bmtc.db")
c = conn.cursor()

c.execute("SELECT * FROM routes")
data = c.fetchall()
print("bus_id, route_id, timings, bus_stop")
for row in data:
    print(row)

conn.commit()

c.close()
conn.close()
