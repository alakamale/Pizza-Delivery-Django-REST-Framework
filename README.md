# Pizza-Delivery-Django-REST-Framework
Imagine a pizza ordering services and Implement the logic using the Django REST framework.

## Task List
>Imagine a pizza ordering services with following functionality

>- Order pizza . Order data: pizza id, pizza size (30cm/50cm), customer name, customer address (just plain text)
>- Update order
>- Remove order
>- See a list of customer orders

>Tasks

>1. Design Model/DB structure
>2. Design and implement API with Django (Rest) Framework for the described web service. Please note:
>3. Write test(s) for at least one of these endpoint(s)

## Installation
Clone this git repository
```
git clone https://github.com/alakamale/Pizza-Delivery-Django-REST-Framework.git
```
Go to the project folder
```
cd pizzahut
```
Install the requirements
```
pip install -r requirements.txt
```
## Configuration
Following can be configured by changing local.env:
>- POSTGRES_DB : database name
>- POSTGRES_USER : database user 
>- POSTGRES_PASSWORD : database password
>- POSTGRES_HOST : host for database

Run the migrations
```
python manage.py migrate
```
Load the datapoints
```
python manage.py loaddata datasets/pizza.json
python manage.py loaddata datasets/customer.json
python manage.py loaddata datasets/customer_address.json
python manage.py loaddata datasets/orders.json
```
Start the server
```
python manage.py runserver 8005
```
This will start the webserver on http://127.0.0.1:8005/.
## Documentation
The API endpoints are

| Endpoint   | Description |
|------------|-----------|
| /pizzas/ | to list all the flavours|
| /customers/ | to list all customers |
| /customers/<customer_id>/orders/ | to update and delete an order |
| /customers/<customer_id>/orders/<order_id> | to update and delete an order |


## Testing the endpoint
To run the tests
```
python manage.py test
```
