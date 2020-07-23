# We Rate Books

## Overview
We will be building a website where users can add their name and upload books with book reviews.

Your teacher will share credentials for MongoDB so we will all be working with the same data.

## Your Goals
You will be able to practice
- Writing Flask Routes
- Processing Forms
- Inserting to a Database
- Querying a Database
- Incorporate Bootstrap Components
- Style with Bootstrap Classes
- Write custom CSS

## To-Do
1. Add yourself as a user
2. Add a book
3. Add a review for the book
4. Add HTML to the pages to display the information
5. Use CSS and Bootstrap to style the information
6. Write additional routes (and functions in model.py) to add functionality below

### Note
> The routes already written should remain as written. Especially the routes that handle adding the form data to the documents that are inserted into the database. This is to ensure compatibility across the class projects

## Things to Include
- Filter by Book Genre
- Filter by Book Rating
- Filter by User
- Calculate average rating for a book
- Calculate the [Net Promotor](https://en.wikipedia.org/wiki/Net_Promoter) score for a book
- And anything else

## Additional Flask Features Included
- `url_for()` - This function takes at least one argument and any number of keyword arguments. The first argument is a string that matches the name of a route function (the function name, not the route decorator). The additional keyword arguments can be used to pass information that is a route parameter. Using url_for is a best practice when creating links within your flask_app to other routes of your flask_app
```html
<a href="{{url_for('users_detail', USER=user.name)}}">Details</a>
```
- `<route_parameter>` - You can get information from the url of the route by putting the parameter within <> inside the route decorator. The parameter must also be in the () in the function definition.
```python
@app.route('/users/<USER>')
def users_detail(USER):
    #business logic
```
