import flask
from flask import jsonify
from flask import request
import requests
import mysql.connector  # Import connector to access sql database
from mysql.connector import Error  # Import error to make sure connection is successful
import random

# setting up an application name
app = flask.Flask(__name__)  # set up application
app.config["DEBUG"] = True  # allow to show error message in browser


# Create a function to connect to the sql database using mysql connector
def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            # Input details such as host, username, password, and database name to connect
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        # If connection is successful display success message to use
        print("Connection to MySQL DB successful.\n")
    except Error as e:
        # If input details are incorrect and connection is not successfull display error message.
        print(f"The error '{e}' occurred")

    return connection


# Create a function to execute an insert query to the successfully connected mysql database
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        # Display success message if the query is executed
        print("Query executed successfully.\n")
    except Error as e:
        # Display error message if details do not match and query does not execute
        print(f"The error '{e}' occurred")

# Create a function to execute an insert query to the successfully connected mysql database
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

@app.route('/', methods=['GET'])  # routing = mapping urls to functions; home is usually mapped to '/'
def home():
    return "<h1>Hi and welcome to our first API!</h1>"


@app.route('/api/movies/all', methods=['GET'])
def api_all():
    connection = create_connection("cis3368.czszkhju4z7p.us-east-1.rds.amazonaws.com", "admin", "$Koid031", "cis3368db")
    cursor = connection.cursor(dictionary=True)
    sql = "SELECT * FROM movielist"
    cursor.execute(sql)
    results = cursor.fetchall()
    return jsonify(results)

@app.route('/api/friends/all', methods=['GET'])
def all_friends():
    connection = create_connection("cis3368.czszkhju4z7p.us-east-1.rds.amazonaws.com", "admin", "$Koid031", "cis3368db")
    cursor = connection.cursor(dictionary=True)
    sql = "SELECT * FROM friend"
    cursor.execute(sql)
    results = cursor.fetchall()
    return jsonify(results)

@app.route('/api/movies', methods=['GET'])  # API to get our users from mySQL table in AWS as JSON response
def api_friendby_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id provided."

    connection = create_connection("cis3368.czszkhju4z7p.us-east-1.rds.amazonaws.com", "admin", "$Koid031", "cis3368db")
    cursor = connection.cursor(dictionary=True)
    sql = "SELECT * FROM movielist"
    cursor.execute(sql)
    rows = cursor.fetchall()
    results = []

    for friend in rows:
        if friend['id'] == id:
            results.append(friend)

    return jsonify(results)

# Adding a user to my database of users
@app.route('/api/addmovies', methods=['POST'])
def addmovies():
    request_data = request.get_json()
    friendid = request_data['friendid']
    movie1 = request_data['movie1']
    movie2 = request_data['movie2']
    movie3 = request_data['movie3']
    movie4 = request_data['movie4']
    movie5 = request_data['movie5']
    movie6 = request_data['movie6']
    movie7 = request_data['movie7']
    movie8 = request_data['movie8']
    movie9 = request_data['movie9']
    movie10 = request_data['movie10']

    connection = create_connection("cis3368.czszkhju4z7p.us-east-1.rds.amazonaws.com", "admin", "$Koid031", "cis3368db")
    query = "INSERT INTO movielist (friendid, movie1, movie2, movie3, movie4, movie5, movie6, movie7, movie8, movie9, movie10) " \
            "VALUES ('"+friendid+"','"+movie1+"','"+movie2+"','"+movie3+"','"+movie4+"','"+movie5+"','"+movie6+"','"+movie7+"','"+movie8+"','"+movie9+"','"+movie10+"')"
    execute_query(connection, query)
    return 'POST REQUEST WORKED'
    #check my table in mySQL Workbench to verify the user has been added

@app.route('/api/addfriends', methods=['POST'])
def addfriends():

    # Request data and get first and last name value
    request_data = request.get_json()
    firstname = request_data['firstname']
    lastname = request_data['lastname']

    # Create connection and insert query to insert value into database
    connection = create_connection("cis3368.czszkhju4z7p.us-east-1.rds.amazonaws.com", "admin", "$Koid031", "cis3368db")
    query = "INSERT INTO friend (firstname, lastname) " \
            "VALUES ('z" + firstname + "','" + lastname + "')"
    execute_query(connection, query)
    return 'POST REQUEST WORKED'
    # check my table in mySQL Workbench to verify the user has been added

@app.route('/api/updatemovielist', methods=['PUT'])
def updatemovielist():
    request_data = request.get_json()
    connection = create_connection("cis3368.czszkhju4z7p.us-east-1.rds.amazonaws.com", "admin", "$Koid031", "cis3368db")
    cursor = connection.cursor(dictionary=True)
    query = "UPDATE movielist SET movie1 = '{}', movie2 = '{}', movie3 = '{}', movie4 = '{}', movie5 = '{}', movie6 = '{}', movie7 = '{}', movie8 = '{}', movie9 = '{}', movie10 = '{}' " \
            "where id = {}""".format("1movie", "2movie", "3movie", "4movie", "5movie", "6movie", "7movie", "8movie", "9movie", "10movie", 1)
    execute_query(connection, query)
    return "UPDATE Worked"

@app.route('/api/updatefriend', methods=['PUT'])
def updatefriend():
    request_data = request.get_json()
    connection = create_connection("cis3368.czszkhju4z7p.us-east-1.rds.amazonaws.com", "admin", "$Koid031", "cis3368db")
    cursor = connection.cursor(dictionary=True)
    query = "UPDATE friend SET firstname = '{}', lastname = '{}' " \
            "where id = {}""".format("test", "case", 12)
    execute_query(connection, query)
    return "UPDATE Worked"

@app.route('/api/deletemovielist', methods=['DELETE'])
def deletemovielist():
    request_data = request.get_json()
    connection = create_connection("cis3368.czszkhju4z7p.us-east-1.rds.amazonaws.com", "admin", "$Koid031", "cis3368db")
    cursor = connection.cursor(dictionary=True)
    query = "delete from movielist where id = {} ".format(6)
    execute_query(connection, query)
    return "DELETE WORKED"

@app.route('/api/deletefriend', methods=['DELETE'])
def deletefriend():
    request_data = request.get_json()
    connection = create_connection("cis3368.czszkhju4z7p.us-east-1.rds.amazonaws.com", "admin", "$Koid031", "cis3368db")
    cursor = connection.cursor(dictionary=True)
    query = "delete from friend where id = {} ".format(13)
    execute_query(connection, query)
    return "DELETE WORKED"

@app.route('/api/randomselection', methods=['GET'])
def randmovie():
    connection = create_connection("cis3368.czszkhju4z7p.us-east-1.rds.amazonaws.com", "admin", "$Koid031", "cis3368db")
    sql = "SELECT movie1, movie2, movie3, movie4, movie5, movie6, movie7, movie8, movie9, movie10 FROM movielist"
    results = execute_read_query(connection, sql)
    movielist = []

    for movie in results:
        for x in movie:
            movielist.append(x)

    random_movie = random.randrange(len(movielist))
    return movielist([random_movie])

app.run()
