# ITSS Project Management for Embedded System

## Server for robot

## Hanoi University of Science and Technology and Uppsala Universitet

###### Group 5

1.	Team members:
	- Shehram Tahir
	- Lam Nguyen Ngoc
	- Tuong Phan Dinh
	- Nafi Uz Zaman
	- Anil Poudel
	- Bui Viet Dung
	- Quy Nguyen Ngoc
	- For more information. see [List of members](https://docs.google.com/presentation/d/1H9vXawhmfnKC6SyAqsgzui6CJ9gdFEHFe8S2NHvihdA/edit#slide=id.g842e3511ef_1_0)

2.	Techonology stack:
	- Python, server created using Django
	- Deploy to heroku

3.	APIs:
	- POST /order/: post order
	- GET /order/: get all orders
	- GET /order/\<int:pk\>/: get the order with specific id
	- PATCH /order/\<int:pk\>/: patch some fields the order with specific id
	- PUT /order/\<int:pk\>/: put all fields the order with specific id

4.	Robot Connector:
	- robot\_get\_path(robot\_name): get the oldest order for that robot\_name
	- robot\_post\_complete(order\_id): patch the status field of order with order\_id from incomplete to completed
	
5.  How to Install:
    - Install [python](https://www.python.org/downloads/)
    - Depending on your OS, you might need to install pip:
        - For windows: follow [Windows instruction](https://www.liquidweb.com/kb/install-pip-windows/)
        - For any popular Linux ditributions (Ubuntu, Fedora, Mint): follow [Linux instruction](https://www.tecmint.com/install-pip-in-linux/)
        - For MacOS: follow [MacOS instruction](https://www.shellhacks.com/python-install-pip-mac-ubuntu-centos/)
    - Install all packages from backend/requirement.txt by this command:
    ```
    pip install <each_row_on_requirement.txt>
    ```
    
    - Note that if you use anaconda distribution, or any other python distributions, it is generally good practice to install those packages using the distribution's own commands like:
    ```
    conda install -c <repository's name> <package>
    ```
    - Install [PostgreSQL](https://www.postgresql.org/download/). Version >= 11
    
    - Recommended to update all the python packages installed to exact version on the requirement.txt or higher (all packages without version specifier are as the latest stable version)
    
6.  How to run:
    - Open a terminal (Linux Distributions, MacOS) or Command Prompt (Windows) at location /backend/control\_center
    - Type to create an database (might need to change parameter in settings.py to feed your machine):
    ```
    python manage.py migrate
    ```
    - Type to start the server:
    ```
    python manage.py runserver <port>
    ```
    - The server will now running at aforementioned port number, default is port 8000
     
