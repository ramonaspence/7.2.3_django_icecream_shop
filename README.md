# Django Ice cream Shop
In this assignment you will focus on learning how to use Django's models and generic views.
----------------------------
## Objectives
### Learning Objectives
After completing this assignment, you should…
* Know how to create a django model
* Know about various django model fields
* Know how to use a generic views to get data from the database
### Performance Objectives
After completing this assignment, you be able to effectively use
* Be able to create a Django Model
* Be able to create and use various field types on your django model
* Be able to use generic views to get model instances (objects) from the database
## Details
### Deliverables
* A repo containing your django project and one django app
* The repo should also contain a sql lite database with your test data
### Requirements
* pep8 and pep20 compliant code
## I'm a Web Developer Mode
Brusters is a local ice cream creamery that specializes in making fresh ice cream daily. They rotate out their flavors and have certain flavors that are available for just a day, a week, or seasonal flavors that you can get for a few months.
Using the tools you've learned in class, create an ice cream menu for Brusters. The menu should have the following headings:
* Featured
* Daily Flavor
* Our Weekly Flavors
* Seasonal Flavors
Under each heading display a listing of the flavors that fit that category.
### Details
 * Setup a new django project
 * Add an ice_cream app to your project
 * Create an IceCream model in your app
 * Add the following fields to your model:
	 * flavor: CharField
	 * base: CharField with choices (chocolate, vanilla)
	 * available = CharField with choices (daily, weekly, seasonal)
	 * featured = BoolFeild
	 * date_churned = DateField
 * Create a view that will display the menu
 * Overwrite the ```get_queryset()``` method in your view so that it filters the menu by selection - featured, daily, weekly, or seasonal flavors
* Create a view that will display the details of a single ice cream
* Create a view that will allow you to add a new ice cream flavor
* Create a Delete function within the DetailView
## Hey Mikey, I think He Likes It Mode
* The featured flavors also display as daily or weekly flavors. Update the ```get_queryset``` method so that daily, weekly and seasonal flavors don't include any flavors that are featured. This will make sure featured flavors only show under the featured list.
* Add an image url to your database model
## Caffeinated
* Create a view that will allow you to edit the details of an ice cream
* Create a view that will allow you to delete and ice cream
