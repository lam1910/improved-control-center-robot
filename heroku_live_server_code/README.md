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

4.	The Server:
The Server is live at [whispering-shelf-53081](https://whispering-shelf-53081.herokuapp.com/order/). Since this server used the free plan on heroku is might be slow.     

