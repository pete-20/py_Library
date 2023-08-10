# Project's guidelines:
Library's project based on Flask to create a simple REST API with multiple endpoints.

<ul>
<li>Used database : PostgreSQL</li>

<li>3 containers run on Docker:</li> 
<ol>
<li>db - PostgreSQL database - port: 5432</li>
<li>adminer - reading data from database - port: 8080</li>
<li>web - Flask's server - port: 5000 </li>
</ol>
</ul>

## HOST:

### http://localhost:5000/API/

## ENDPOINTS:

### 1) Landging page:
    http://localhost:5000/API/

### 2) Available categories:
    http://localhost:5000/API/categories

### 3) Available books:
    http://localhost:5000/API/books

### 4) Deleting an object with id:
    DELETE http://localhost:5000/API/books/<id>
    
### 5) Updating an object with id:
    PUT http://localhost:5000/API/books/<id>

### 6) Getting information about an object with id:
    GET http://localhost:5000/API/books/<id>

### 7) All available books from category:
    http://localhost:5000/API/<category>

### 8) Adding a new book:
    POST http://localhost:5000/API/add  

#### + request json e.g.:
{   
    "category":"IT",
    "book":"Test Driven Development",
    "author":"Kent Beck",
    "pages": 1000,
    "status": "to buy"
}