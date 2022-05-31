# Development Team Project: Coding Output

# Prerequisite

The following should be installed already before setup.
- Python3

Requirements:
```
pip install -r requirements.txt
```
# Program

Running in Linux from the downloaded directory:
```
export FLASK_APP=__init__.py
flask run
```

Running in Windows from the downloaded directory:
Change to downloaded directory
```
set FLASK_APP=__init__.py
flask run
```
User management page (Admin role required)

Change to admin directory
```
flask run --port=8888
```
Default user password: P@ssw0rd

# Database

DB details:
```
Host: sql5.freesqldatabase.com:3306
Database user: sql5495299
Database name: sql5495299
Database password: hz7bDRYNPh
Web console: https://www.phpmyadmin.co/
```

Database Query:

Code to recreate the 2 x NASA database tables:
```
CREATE TABLE IF NOT EXISTS people(userID INT(5) UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE, firstName VARCHAR(30), lastName VARCHAR(30), email VARCHAR(64) UNIQUE NOT NULL, phone VARCHAR(11), password VARCHAR(64) NOT NULL, failedAttempts TINYINT(1), lockoutStatus TINYINT(1), role ENUM('ISS', 'Ground Staff', 'Government', 'Admin') NOT NULL, PRIMARY KEY(userID));

CREATE TABLE IF NOT EXISTS document_repository(fileID INT(7) UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE, filename VARCHAR(255) NOT NULL, uploaded DATE NOT NULL, classification TINYINT(1) NOT NULL, owner INT(5) UNSIGNED NOT NULL UNIQUE, PRIMARY KEY(fileID), FOREIGN KEY (owner) REFERENCES people(userID))
```
***
Removed username field due to redundancy as email address can be used.
