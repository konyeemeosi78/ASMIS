# Development Team Project: Coding Output

DB details:
```
Host: sql5.freesqldatabase.com:3306
Database user: sql5495299
Database name: sql5495299
Database password: hz7bDRYNPh
Web console: https://www.phpmyadmin.co/
```

Running in Linux from the downloaded directory:
```
export FLASK_APP=__init__.py
flask run
```

Running in Windows from the downloaded directory:
```
set FLASK_APP=__init__.py
flask run
```
Default user password: P@ssw0rd


Code to recreate the 2 x NASA database tables:

CREATE TABLE IF NOT EXISTS people(userID INT(5) UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE, firstName VARCHAR(30), lastName VARCHAR(30), email VARCHAR(64) UNIQUE, phone VARCHAR(11), username VARCHAR(30) UNIQUE NOT NULL, password VARCHAR(64) NOT NULL, failedAttempts TINYINT(1), lockoutStatus TINYINT(1), role ENUM('ISS', 'Ground Staff', 'Government', 'Admin') NOT NULL, PRIMARY KEY(userID));

CREATE TABLE IF NOT EXISTS document_repository(fileID INT(7) UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE, filename VARCHAR(255) NOT NULL, uploaded DATE NOT NULL, classification TINYINT(1) NOT NULL, owner INT(5) UNSIGNED NOT NULL UNIQUE, PRIMARY KEY(fileID), FOREIGN KEY (owner) REFERENCES people(userID))
