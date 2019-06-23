# Ethereum Tokens Tracker
Third milestone project for code institute full stack developer course, Data Centric Development section.
This is a web app for tracking your ethereum tokens.
The app consists of a Landing, Registration, Login, Dashboard pages and a Stats page,
Which allows users to Create, Read, Update and Delete their tokens data.




## UX
This app was developed to allow users looking to track the ethereum tokens they already own,
Users can select from a list of the top 50 ethereum tokens and add the price they paid and the amount they bought.

### Style
For this app i decided to use material design principals and utilized the materialize.css framework for the front end
 of the app adding custom css styles to override values where needed.
 I initially was going to use a black background but later felt it was too dark so opted for a dark blue color instead.
For the home page i used a gradient background that changes from light blue to dark blue.

### User Stories
As a User, Investor or [Hodler](https://en.wikipedia.org/wiki/Hodl) of ethereum tokens, I would like to:
* Create a portfolio of the tokens i own.
* Be able to check the price i paid.
* See the date i bought them
* Visualize stats about the tokens i hold.
* Track all my tokens in one place


### Mock-Ups

1. [Desktop/Tablet](https://github.com/John-E5/ETH-Tokens-Tracker/blob/master/media/Dashboard_Pages.png)
2. [Mobile](https://github.com/John-E5/ETH-Tokens-Tracker/blob/master/media/Dashboard_Pages_mobile.png)

### Project Management

For this project [Git Kraken/GloBoards](https://www.gitkraken.com/) was used as a task/issue tracker board which is synced
to the project repo on github.
Sections included - issues, to Do, in Progress, completed, bugs.

#### Usage

* When starting the project:
    1. Create cards
    2. Add descriptions
    3. Add assignee
    4. Add labels
    5. Add tasks
    6. Add files and comments where needed

* During the Project:
    1. Move card from ToDo to in Progress
    2. Check card for required tasks
    3. Complete task and tick off list
    4. Once all tasks completed move card to be completed and close issue

##### See screenshots for reference:

1. ![GitKraken](https://github.com/John-E5/ETH-Tokens-Tracker/blob/master/media/gitkraken1.png)
2. ![GitKraken](https://github.com/John-E5/ETH-Tokens-Tracker/blob/master/media/gitkraken2.png)
3. ![Glo-Board-1](https://github.com/John-E5/ETH-Tokens-Tracker/blob/master/media/glo-board-tracker.png)
4. ![Glo-Board-2](https://github.com/John-E5/ETH-Tokens-Tracker/blob/master/media/glo-board-eth.png)

## Features

### Desktop/Tablet View

#### Home/Landing Page
The home page consists of a main title of the app with registration and login buttons underneath.
Then there is an image carousel of all the available tokens you can add to your portfolio.
There are then sections that fade in on scroll with a brief introduction and images for the different features of the 
dashboard. 
The bottom of the page has a basic footer with social icons that also fade on scroll.

#### Registration Page
The registration page consists of a form with 4 fields and a submit button:
* Username
* Email - with validation
* Password 
* Confirm Password

#### Login Page
The login page consists of a form with 2 fields and a submit button:

* Email - with validation
* Password - with validation

#### Dashboard Page
The main dashboard page consists of a side navigation and an empty page until some tokens have been added, once 
tokens have been added the page shows a table with Name, Price, Amount, Date and Value of the tokens

##### Side Navigation Links

* Dashboard
* Add Token
* Profile
* Stats
* Logout

##### Dashboard Table

* Name: Shows the tokens ticker symbol
* Price: Shows the price paid for each token in Bitcoin value
* Amount: Shows the amount of tokens entered which can be a fraction of of a token
* Date: Shows the date when the tokens were bought
* Value: Shows the combined value of the tokens (price * amount)
* View: Links to the page for that token

#### Add Token Page
Shows a form for users to add there token data to to the dashboard

* Choose token: Allows users to select 1 of the 50 preset tokens to add to their portfolio
* Price: Allows users to add the price they paid per token in Bitcoin(BTC) value. eg. 0.0002, 0.00000034 [Example](https://ethplorer.io/address/0xa0b73e1ff0b80914ab6fe0444e65848c4c34450b?from=search)
* Amount: Allows users to add the amount of tokens they bought which can be a fraction of a token
* Date: Allows users to select the date they bought the tokens
* Submit Button: Allows users to submit the data they entered

#### Token Page
Shows a table with the selected token and Edit and Delete icon buttons

* Edit: Links to the edit token page
* Delete: Once clicked opens a model to confirm the delete action to the user

#### Edit Token Page
Shows a form similar to add token page but for updating the tokens Price, Amount and Date and will update the dashboard 
once submitted

#### Profile Page
Shows a form for users to update their email and username.
* ToDo : Password reset functionality

#### Stats Page
Shows 3 charts: PieChart, BarChart and Treemap Chart, The charts give an overview of the tokens in your portfolio
* ToDo: Add better data to improve stats page to show price values and portfolio totals

### Features Left to Implement
- Add live price data from cryptocompare api to improve charts and portfolio statistics
- Add password reset functionality
- Improve tests and coverage

## Technologies Used

For this project the following Technologies were used:
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
    - The project uses **HTML5** to structure the content in line with modern semantic html5.

- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets#CSS_3)
    - The project uses **CSS3** to style the html content.

- [MaterializeCSS](https://materializecss.com/)
    - The project uses **MaterializeCSS** as the frontend framework for this app 

- [Python](https://www.python.org/)
    - The project uses **Python3** 

- [FLASK](http://flask.pocoo.org/)
    - The project uses **FLASK** as the API framework for this app

- [JINJA2](http://jinja.pocoo.org/docs/2.10/)
    - The project uses **Jinja2** as the templating language for this app

- [POSTGRESSQL](https://www.postgresql.org/)
    - The project uses **PostgresSQL** as the database for this app

- [SQLALCHEMY](https://www.sqlalchemy.org/)
    - The project uses **SQLalchemy** as the ORM for this app

- [WTFORMS](https://pypi.org/project/WTForms/)
    - The project uses **WTForms** for the forms on the app

- [PYTEST](https://docs.pytest.org/en/latest/)
    - The project uses **Pytest** as the testing framework for this app

- [PYGAL](http://www.pygal.org/en/stable/)
    - The project uses **Pygal** for the charts in this app 

- [HEROKU](https://www.heroku.com/)
    - The project uses **Heroku** for the deployment of this app

- [Mockflow](https://mockflow.com/)
    - The project used **Mockflow** for creating the mock-ups.

- [Git Github](https://github.com/)
    - The project uses **Git Github** for source control management.

- [Git Kraken/Glo Boards](https://www.gitkraken.com/)
    - The project used **Git Kraken/Glo Boards** for project and task management.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to control scrolling and MaterializeCSS features.

- [PYCHARM](https://www.jetbrains.com/pycharm/)
    - I used **PyCharm** as the IDE of choice for the development of this app

## Testing

### Unit Tests
Pytest-Flask was used for unit testing this app, 
I started by testing the routes for the correct 200 responses 
i then tested the routes for the html elements of each route to see if they were included in the response
10 tests were run and all passed 

![tests](https://github.com/John-E5/ETH-Tokens-Tracker/blob/master/media/testing1.png)
### Manual Testing

Testing for this project was done with several browsers and devices.

#### Browsers

##### Mobile
- Firefox
- Chrome
- Safari
- Opera

##### Desktop
- Firefox
- Chrome
- Opera
- Edge

#### Devices
- Hp Laptop
- Lenovo Laptop
- Huawei Nexus 6P android phone
- Samsung Galaxy Tab 4
- Samsung Galaxy J3
- Iphone 6s
- Iphone 7
- Ipad AIR

Firefox developer edition and chrome dev-tools were used during development and for manual testing of the site responsiveness 
The devices and browsers listed above were used to test the app on different screen sizes and devices.

#### To Manually Test




##### Navigation Testing



### Validation Testing

- For _HTML_ validation testing I used [W3 Validator]() which shows the html document to be valid.

- For _CSS_ validation testing I used [W3 CSS Validator]() which shows the stylesheet to be valid CSS3.

## Deployment

- 
- To run this app locally clone or download the repo and open index.html to view in browser.

## Credits

### Content
- 


### Acknowledgements
