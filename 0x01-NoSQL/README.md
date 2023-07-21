

Curriculum
Short Specializations Average: 76.8%
You have a captain's log due before 2023-07-23 (in 2 days)! Log it now!
You just released the advanced tasks of this project. Have fun!
0x01. NoSQL
In a nutshell…

    Auto QA review: 0.0/135 mandatory & 0.0/32 optional
    Altogether:  0.0%
        Mandatory: 0.0%
        Optional: 0.0%
        Calculation:  0.0% + (0.0% * 0.0%)  == 0.0%

Resources

Read or watch:

    NoSQL Databases Explained
    What is NoSQL ?
    MongoDB with Python Crash Course - Tutorial for Beginners
    MongoDB Tutorial 2 : Insert, Update, Remove, Query
    Aggregation
    Introduction to MongoDB and Python
    mongo Shell Methods
    The mongo Shell

Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
General

    What NoSQL means
    What is difference between SQL and NoSQL
    What is ACID
    What is a document storage
    What are NoSQL types
    What are benefits of a NoSQL database
    How to query information from a NoSQL database
    How to insert/update/delete information from a NoSQL database
    How to use MongoDB

Requirements
MongoDB Command File

    All your files will be interpreted/compiled on Ubuntu 18.04 LTS using MongoDB (version 4.2)
    All your files should end with a new line
    The first line of all your files should be a comment: // my comment
    A README.md file, at the root of the folder of the project, is mandatory
    The length of your files will be tested using wc

Python Scripts

    All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7) and PyMongo (version 3.10)
    All your files should end with a new line
    The first line of all your files should be exactly #!/usr/bin/env python3
    A README.md file, at the root of the folder of the project, is mandatory
    Your code should use the pycodestyle style (version 2.5.*)
    The length of your files will be tested using wc
    All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
    All your functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)'
    Your code should not be executed when imported (by using if __name__ == "__main__":)

More Info
Install MongoDB 4.2 in Ubuntu 18.04

Official installation guide

$ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org
...
$  sudo service mongod status
mongod start/running, process 3627
$ mongo --version
MongoDB shell version v4.2.8
git version: 43d25964249164d76d5e04dd6cf38f6111e21f5f
OpenSSL version: OpenSSL 1.1.1  11 Sep 2018
allocator: tcmalloc
modules: none
build environment:
    distmod: ubuntu1804
    distarch: x86_64
    target_arch: x86_64
$  
$ pip3 install pymongo
$ python3
>>> import pymongo
>>> pymongo.__version__
'3.10.1'

Potential issue if documents creation doesn’t work or this error: Data directory /data/db not found., terminating (source and source)

$ sudo mkdir -p /data/db

Or if /etc/init.d/mongod is missing, please find here an example of the file:
Click to expand/hide file contents
Use “container-on-demand” to run MongoDB

    Ask for container Ubuntu 18.04 - MongoDB
    Connect via SSH
    Or via the WebTerminal
    In the container, you should start MongoDB before playing with it:

$ service mongod start
* Starting database mongod                                              [ OK ]
$
$ cat 0-list_databases | mongo
MongoDB shell version v4.2.8
connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("70f14b38-6d0b-48e1-a9a4-0534bcf15301") }
MongoDB server version: 4.2.8
admin   0.000GB
config  0.000GB
local   0.000GB
bye
$

Tasks
0. List all databases
mandatory
Score: 0.0% (Checks completed: 0.0%)

Write a script that lists all databases in MongoDB.

guillaume@ubuntu:~/0x01$ cat 0-list_databases | mongo
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
admin        0.000GB
config       0.000GB
local        0.000GB
logs         0.005GB
bye
guillaume@ubuntu:~/0x01$

Repo:

    GitHub repository: alx-backend-storage
    Directory: 0x01-NoSQL
    File: 0-list_databases

1. Create a database
mandatory
Score: 0.0% (Checks completed: 0.0%)

Write a script that creates or uses the database my_db:

guillaume@ubuntu:~/0x01$ cat 0-list_databases | mongo
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
admin        0.000GB
config       0.000GB
local        0.000GB
logs         0.005GB
bye
guillaume@ubuntu:~/0x01$
guillaume@ubuntu:~/0x01$ cat 1-use_or_create_database | mongo
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
switched to db my_db
bye
guillaume@ubuntu:~/0x01$

Repo:

    GitHub repository: alx-backend-storage
    Directory: 0x01-NoSQL
    File: 1-use_or_create_database

2. Insert document
mandatory
Score: 0.0% (Checks completed: 0.0%)

Write a script that inserts a document in the collection school:

    The document must have one attribute name with value “Holberton school”
    The database name will be passed as option of mongo command

guillaume@ubuntu:~/0x01$ cat 2-insert | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
WriteResult({ "nInserted" : 1 })
bye
guillaume@ubuntu:~/0x01$

Repo:

    GitHub repository: alx-backend-storage
    Directory: 0x01-NoSQL
    File: 2-insert

3. All documents
mandatory
Score: 0.0% (Checks completed: 0.0%)

Write a script that lists all documents in the collection school:

    The database name will be passed as option of mongo command

guillaume@ubuntu:~/0x01$ cat 3-all | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
{ "_id" : ObjectId("5a8fad532b69437b63252406"), "name" : "Holberton school" }
bye
guillaume@ubuntu:~/0x01$

Repo:

    GitHub repository: alx-backend-storage
    Directory: 0x01-NoSQL
    File: 3-all

4. All matches
mandatory
Score: 0.0% (Checks completed: 0.0%)

Write a script that lists all documents with name="Holberton school" in the collection school:

    The database name will be passed as option of mongo command

guillaume@ubuntu:~/0x01$ cat 4-match | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
{ "_id" : ObjectId("5a8fad532b69437b63252406"), "name" : "Holberton school" }
bye
guillaume@ubuntu:~/0x01$

Repo:

    GitHub repository: alx-backend-storage
    Directory: 0x01-NoSQL
    File: 4-match

5. Count
mandatory
Score: 0.0% (Checks completed: 0.0%)

Write a script that displays the number of documents in the collection school:

    The database name will be passed as option of mongo command

guillaume@ubuntu:~/0x01$ cat 5-count | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
1
bye
guillaume@ubuntu:~/0x01$

Repo:

    GitHub repository: alx-backend-storage
    Directory: 0x01-NoSQL
    File: 5-count

6. Update
mandatory
Score: 0.0% (Checks completed: 0.0%)

Write a script that adds a new attribute to a document in the collection school:

    The script should update only document with name="Holberton school" (all of them)
    The update should add the attribute address with the value “972 Mission street”
    The database name will be passed as option of mongo command

guillaume@ubuntu:~/0x01$ cat 6-update | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
bye
guillaume@ubuntu:~/0x01$ 
guillaume@ubuntu:~/0x01$ cat 4-match | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
{ "_id" : ObjectId("5a8fad532b69437b63252406"), "name" : "Holberton school", "address" : "972 Mission street" }
bye
guillaume@ubuntu:~/0x01$ 

Repo:

    GitHub repository: alx-backend-storage
    Directory: 0x01-NoSQL
    File: 6-update

7. Delete by match
mandatory
Score: 0.0% (Checks completed: 0.0%)

Write a script that deletes all documents with name="Holberton school" in the collection school:

    The database name will be passed as option of mongo command

guillaume@ubuntu:~/0x01$ cat 7-delete | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
{ "acknowledged" : true, "deletedCount" : 1 }
bye
guillaume@ubuntu:~/0x01$ 
guillaume@ubuntu:~/0x01$ cat 4-match | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
bye
guillaume@ubuntu:~/0x01$ 

Repo:

    GitHub repository: alx-backend-storage
    Directory: 0x01-NoSQL
    File: 7-delete

8. List all documents in Python
mandatory
Score: 0.0% (Checks completed: 0.0%)

Write a Python function that lists all documents in a collection:

    Prototype: def list_all(mongo_collection):
    Return an empty list if no document in the collection
    mongo_collection will be the pymongo collection object

guillaume@ubuntu:~/0x01$ cat 8-main.py
#!/usr/bin/env python3
""" 8-main """
from pymongo import MongoClient
list_all = __import__('8-all').list_all

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {}".format(school.get('_id'), school.get('name')))

guillaume@ubuntu:~/0x01$ 
guillaume@ubuntu:~/0x01$ ./8-main.py
[5a8f60cfd4321e1403ba7ab9] Holberton school
[5a8f60cfd4321e1403ba7aba] UCSD
guillaume@ubuntu:~/0x01$ 

Repo:

    GitHub repository: alx-backend-storage
    Directory: 0x01-NoSQL
    File: 8-all.py

9. Insert a document in Python
mandatory
Score: 0.0% (Checks completed: 0.0%)

Write a Python function that inserts a new document in a collection based on kwargs:

    Prototype: def insert_school(mongo_collection, **kwargs):
    mongo_collection will be the pymongo collection object
    Returns the new _id

guillaume@ubuntu:~/0x01$ cat 9-main.py
#!/usr/bin/env python3
""" 9-main """
from pymongo import MongoClient
list_all = __import__('8-all').list_all
insert_school = __import__('9-insert_school').insert_school

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    new_school_id = insert_school(school_collection, name="UCSF", address="505 Parnassus Ave")
    print("New school created: {}".format(new_school_id))

    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('address', "")))

guillaume@ubuntu:~/0x01$ 
guillaume@ubuntu:~/0x01$ ./9-main.py
New school created: 5a8f60cfd4321e1403ba7abb
[5a8f60cfd4321e1403ba7ab9] Holberton school
[5a8f60cfd4321e1403ba7aba] UCSD
[5a8f60cfd4321e1403ba7abb] UCSF 505 Parnassus Ave
guillaume@ubuntu:~/0x01$ 

Repo:

    GitHub repository: alx-backend-storage
    Directory: 0x01-NoSQL
    File: 9-insert_school.py

10. Change school topics
mandatory
Score: 0.0% (Checks completed: 0.0%)

Write a Python function that changes all topics of a school document based on the name:

    Prototype: def update_topics(mongo_collection, name, topics):
    mongo_collection will be the pymongo collection object
    name (string) will be the school name to update
    topics (list of strings) will be the list of topics approached in the school

guillaume@ubuntu:~/0x01$ cat 10-main.py
#!/usr/bin/env python3
""" 10-main """
from pymongo import MongoClient
list_all = __import__('8-all').list_all
update_topics = __import__('10-update_topics').update_topics

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    update_topics(school_collection, "Holberton school", ["Sys admin", "AI", "Algorithm"])

    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('topics', "")))

    update_topics(school_collection, "Holberton school", ["iOS"])

    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('topics', "")))

guillaume@ubuntu:~/0x01$ 
guillaume@ubuntu:~/0x01$ ./10-main.py
[5a8f60cfd4321e1403ba7abb] UCSF 
[5a8f60cfd4321e1403ba7aba] UCSD 
[5a8f60cfd4321e1403ba7ab9] Holberton school ['Sys admin', 'AI', 'Algorithm']
[5a8f60cfd4321e1403ba7abb] UCSF 
[5a8f60cfd4321e1403ba7aba] UCSD 
[5a8f60cfd4321e1403ba7ab9] Holberton school ['iOS']
guillaume@ubuntu:~/0x01$ 

Repo:

    GitHub repository: alx-backend-storage
    Directory: 0x01-NoSQL
    File: 10-update_topics.py

