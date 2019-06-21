# ETH-Tokens-Tracker
Ethereum tokens portfolio tracker


#### The Project Brief:
##### Build a CRUD app

* 
* 
* 


## UX


### Style


### User Stories


#### Home Section Contains:

1. 
2. 
3. 

#### User/Category Section Contains:

* 

#### DApps Users Section Contains:

* Daily DApps Users rowChart

#### Daily User Transactions Section Contains:

* Daily User Transactions scatterplotChart

#### DApps Daily and Weekly Transactions Section Contains:

* DApps Daily and Weekly Transactions stackedbarChart

### Mock-Ups

1. [Desktop](https://camo.githubusercontent.com/fd8931475416b2fc463dd1b15323ad8bdef33643/68747470733a2f2f6170702e6769746b72616b656e2e636f6d2f6170692f676c6f2f626f617264732f3563333330653838666566333839303030666534333033342f6174746163686d656e74732f356334646365613039323638326630303066323336663865)
2. [Tablet](https://camo.githubusercontent.com/fcb297dc9f86630d6f1a2966ef585af4655ed237/68747470733a2f2f6170702e6769746b72616b656e2e636f6d2f6170692f676c6f2f626f617264732f3563333330653838666566333839303030666534333033342f6174746163686d656e74732f356334646365613039323638326630303066323336663862)
3. [Mobile](https://camo.githubusercontent.com/58fd5cf3d9d14f65a45feb366f1d8d02b8dd911c/68747470733a2f2f6170702e6769746b72616b656e2e636f6d2f6170692f676c6f2f626f617264732f3563333330653838666566333839303030666534333033342f6174746163686d656e74732f356334646365613039323638326630303066323336663931)

### Project Management

For this project [Git Kraken/GloBoards](https://www.gitkraken.com/) was used as a task/issue tracker board which is synced
to the project repo on github.
Sections included - issues, to Do, in Progress, to be reviewed, completed, bugs.

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
    4. Once all tasks completed move card to be reviewed section
    5. once reviewed move to complete and close issue

##### See screenshots for reference:

1. [Glo-Board-1](https://camo.githubusercontent.com/f492ce38de7bfa60d50ff496ed3dafc9705b4ebf/68747470733a2f2f6170702e6769746b72616b656e2e636f6d2f6170692f676c6f2f626f617264732f3563333330653838666566333839303030666534333033342f6174746163686d656e74732f356334396331383739323638326630303066323263626437)
2. [Glo-Board-2](https://camo.githubusercontent.com/fd6a1d8690c757d16da890a7a3e87e0901b53036/68747470733a2f2f6170702e6769746b72616b656e2e636f6d2f6170692f676c6f2f626f617264732f3563333330653838666566333839303030666534333033342f6174746163686d656e74732f356334396331383739323638326630303066323263626461)
3. [Glo-Board-3](https://camo.githubusercontent.com/ecd591dbc4fcf0f0474875351d47781d5d3bd265/68747470733a2f2f6170702e6769746b72616b656e2e636f6d2f6170692f676c6f2f626f617264732f3563333330653838666566333839303030666534333033342f6174746163686d656e74732f356334396331383739323638326630303066323263626464)
4. [Glo-Board-4](https://camo.githubusercontent.com/73cd00bf1eea1877c75d94f150382b2f609aeba0/68747470733a2f2f6170702e6769746b72616b656e2e636f6d2f6170692f676c6f2f626f617264732f3563333330653838666566333839303030666534333033342f6174746163686d656e74732f356334396331383739323638326630303066323263626434)

## Features

### Desktop/Tablet View

#### Home
- The home section features a transparent navbar with heading title to the left and section nav links to right.
- It also features an intoduction paragraph with links to different blockchain platforms.
- Selectors are located below the paragraph and allow you to filter the different data points.
- Once a selection is made it filters the charts as per selection.
- You can reset the filters by clicking the reset all button.

#### User/Category
- This sections has a row of 3 charts
    1. piechart with platfrom legend to filter the different platforms data.
    2. barchart showing the different categories data.
    3. piechart with legend to filter the platform data.

#### DApps Users
- This section has a rowchart showing the different dapps and allows you to filter the different data points.

#### Daily User Transactions
- This section features a scatterplot chart showing the amount of user tranactions per dapp and is filtered when selecting a
a filter from the selectors in the home section.

#### DApps Tranactions
- This section features a stacked barchart showing the daily and weekly transactions by dapp name and is filter by the selectors
in the home section or by clicking the bar sections on the chart.

#### Footer
- The footer section features a reset all button for the filters and nav items to navigate the sections.

### Mobile View
- When viewing on mobile the charts are positioned on top of each other to help the responsive behavior of the site.
- It also features a hamburger dropdown menu in the navbar, once clicked a dropdown menu appears containing the nav list items.

- All views feature a back to top button for ease of navigation.
- The button fades in and out as you scroll the page once clicked it returns you to home section using jquery script for smooth scrolling effect.


### Features Left to Implement
- Add a loader to the dashboard to display while page loads.
- Add more unit tests to get better code coverage.

## Technologies Used

For this project the following Technologies were used:
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
    - The project uses **HTML5** to structure the content in line with modern semantic html5.

- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets#CSS_3)
    - The project uses **CSS3** to style the html content.

- [FontAwesome](https://fontawesome.com/)
    - The project uses **FontAwesome** to add icons for chart symbols.

- [Javascript](https://www.javascript.com/)
    - The project uses **Javascript** to add interactive content to dashboard.

- [Bootstrap 4](https://getbootstrap.com/)
    - The project uses **Bootstrap** to layout the html content and make it responsive.

- [Bootswatch](https://bootswatch.com/sandstone/)
    - The project uses **Bootswatch Theme** to add fonts and color the theme chosen was sandstone.

- [D3.js](https://d3js.org/)
    - The project uses **D3.js** for manipulating documents and rendering charts.

- [Crossfilter](https://github.com/crossfilter/crossfilter)
    - The project uses **Crossfilter** for manipulating and filtering the data.

- [Dc.js](https://dc-js.github.io/dc.js/)
    - The project uses **Dc.js** as a charting library with native crossfilter support and usesd3 to render charts.

- [Queue](https://github.com/d3/d3-queue)
    - The project uses **Queue** as a little helper for asynchronous JavaScript.

- [Jasmine](https://jasmine.github.io/index.html)
    - The project uses **Jasmine.js** for unit testing.

- [Vs Code](https://code.visualstudio.com/)
    - The project used **Vs Code** as the IDE of choice.

- [Mockflow](https://mockflow.com/)
    - The project used **Mockflow** for creating the mock-ups.

- [Git Github](https://github.com/)
    - The project used **Git Github** for source control management.

- [Git Kraken/Glo Boards](https://www.gitkraken.com/)
    - The project used **Git Kraken/Glo Boards** for project and task management.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to control scrolling and toggle features.

## Testing

### Unit Tests

Jasmine.js was the framework used for the unit tests, I started by testing the piechart function, when adding tests for width, height i realised i would have to
declare some variables and build parts of the charts in [graphSpec.js](https://github.com/John-E5/DApps-Data-Dashboard/blob/master/Unit-Tests/spec/graphSpec.js)
to be able to test the various parts of the charts.
I added 37 spec tests checking some of the charts which all pass.
The results can be viewed in [specRunner.html](https://john-e5.github.io/DApps-Data-Dashboard/Unit-Tests/SpecRunner.html)

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

Firefox developer edition and chrome dev-tools were used during development and for manual testing of the site responsiveness and checking if the
charts rendered and filters worked correctly.
The devices and browsers listed above were used to test the app on different screen sizes and devices.

#### To Manually Test

##### Selectors Testing
* Platform Selector
    1. Go to Home section
    2. Click platform select
    3. Click a platform name
    4. check charts to see filter applied

* DApp Selector
    1. Go to Home section
    2. Click DApp select
    3. Click a DApp name
    4. Check charts to see filter applied

* Category Selector
    1. Go to Home section
    2. Click Category select
    3. Click a Category name
    4. Check charts to see filter applied

* Reset Filters
    1. Go to Home/Footer Section
    2. Apply any filter
    3. Click Reset All
    4. See chart filters reset


##### Charts Testing

* Platform Users Breakdown Piechart
    1. Go to User/Category section
    2. Click Legend item or piechart slice
    3. Check charts to see filter applied

* Categories Stats Barchart
    1. Go to User/Category section
    2. Click category bar
    3. Check charts to see filter applied

* Weekly Transactions Piechart
    1. Go to User/Category section
    2. Click Legend item or piechart slice
    3. Check charts to see filter applied

* Daily DApps Users Rowchart
    1. Go to DApps Users section
    2. Click DApp row item
    3. Check charts to see filter applied

* Daily User Transactions Scatterplotchart
    1. Go to User Transactions section
    2. Hover over dots to see title details
    3. Apply filter from selectors to see individual data

* DApps Daily and Weekly Transactions Stacked Barchart
    1. Go to DApp Transactions section
    2. Hover over bar section to see title details
    3. Apply filter from selectors to see individual data.
    4. Click bar items to filter data

##### Navigation Testing

* Top Navigation Tests
    1. Go to home page
    2. Click nav item
    3. See page scroll to section

* Footer Navigation Tests
    1. Go to footer section
    2. Click Nav item
    3. See page scroll to section

* Back To Top Button Tests
    1. Scroll down page
    2. See back to top button fade in
    3. Click button
    4. See page scroll to top

* Mobile Navigation Tests
    1. Open app on mobile device
    2. Click hamburger menu
    3. See dropdown menu
    4. Click Nav item
    5. See page scroll to section

### Validation Testing

- For _HTML_ validation testing I used [W3 Validator](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fjohn-e5.github.io%2FDApps-Data-Dashboard%2F) which shows the html document to be valid.

- For _CSS_ validation testing I used [W3 CSS Validator](http://jigsaw.w3.org/css-validator/validator) which shows the stylesheet to be valid CSS3.

## Deployment

- This App was deployed to [Github pages](https://john-e5.github.io/DApps-Data-Dashboard/)
- To run this app locally clone or download the repo and open index.html to view in browser.

## Credits

### Content
- The data used in this app was sourced from:
- [DApp Radar](https://dappradar.com/)
- [State of the DApps](https://www.stateofthedapps.com/)


### Acknowledgements
