# Running

This small app should only require running `docker-compose up -d` to get up.
This will start a flask container using MongoDB for data storage, running on localhost:80

The / endpoint will return a JSON body with an ID that can be used as a testing endpoint to POST data from.

`EG: localhost/83c5f2ab-1035-4680-9f6a-2601fa2c3910` will store any captured JSON data in MongoDB, and further requests can be used to read and return this data.

`localhost/health` will return the health status of this service.  It's just a simple check for connectivity to the database, but returns 200 when the check completes, and 424(Failed Dependancy) when it fails.

# Further development / Improvements for production readiness

Many decisions were made for expediency as I timeboxed this to 4hrs, and have not developed REST services before. Although I have worked with MongoDb and Python througout my career.  I did not provision a user for the flask app, as I wanted to get to the part I knew I needed more time for (developing the flask app).  This should be done of course for a production system, as using the admin account is clearly a terrible idea.  This can be done by creating a datastore and mounting a .js script to `/docker-entrypoint-initdb.d`.  Adding a datastore would also allow the data to persist long term throughout container lifecycles.  

- Add an nginx server in front of flask
- run it in non production mode

Considerations for other data types besides JSON should also be made, as this app assumes it will only capture JSON data.

Cleaning the data before storing might also be nice, as escapes are currently being added to the fields.

The test script should also be expanded to test the entire apps flow, instead of only posting data. 
