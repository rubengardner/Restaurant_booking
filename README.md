# Table of Contents

-   [1. UX](#ux)
    -   [1.1. Strategy](#strategy)
        -   [Project Goals](#project-goals)
            -   [User Goals:](#user-goals)
            -   [User stories](#tuser-stories)
            -   [Strategy Table](#strategy-table)
    -   [1.2. Wireframes](#wireframes)
    -   [1.3. Skeleton](#skeleton)
    -   [1.4. Surface](#surface)
-   [2. Features](#features)
-   [3. Technologies Used](#technologies-used)
-   [4. Testing](#testing)
-   [5. Development Cycle](#development-cycle)
-   [6. Deployment](#deployment)
-   [7. End Product](#end-product)
-   [8. Known Bugs](#known-bugs)
-   [9. Credits](#credits)

# 1 User experience

## 1.1. Strategy

[Go to the top](#table-of-contents)

### Project Goals
* The website features a modern design with minimalistic colors to keep the focus on the content.
* The website is designed to adapt to different screen sizes for optimal accessibility.
* The objective of this project is to simplify the process of user registration, login/logout, creating a user profile, and CRUD functionality for table reservations.

### User Goals:
First Time Visitor Goals:
* As a new visitor, I want to easily make a reservation for a table on my desired date and time.
* As a new visitor, I want to easily access the restaurant's menu to help me make a decision about booking a table.
* As a new visitor, I want to have easy access to the restaurant's contact information.
Returning Visitor Goals

Consolidated customer:
* As a repeat customer, I want to be able to make changes to my existing table reservations.
* As a repeat customer, I want to have the option to cancel a reservation that I previously made.
* As a repeat customer, I want to be able to update my personal profile for future bookings.

All customers:
* Navigation through the interface is straightforward.
* It is easy to view my existing reservations.
* I have the option to reach out to the restaurant for any inquiries

### User stories:
I utilized the GitHub projects board as my project management tool throughout the project by logging all user stories. This helped me to stay on track by moving the necessary tasks to the "in progress" lane as I worked on them and then moving them to the "done" lane once completed.

Backlog 1:
![backlog_1](book_table/static/images/backlog/backlog_1.png)

Backlog 2:
![backlog_2](book_table/static/images/backlog/backlog_2.png)

Backlog 3:
![backlog_3](book_table/static/images/backlog/backlog_3.png)

Backlog 4:
![backlog_4](book_table/static/images/backlog/backlog_4.png)


### Strategy Table
Task| Importance| Viability/Feasibility
------------ | -------------------------|---------
Display a food Menu | 5 | 5
Account signup | 5 | 4
User resevation display | 5 | 5
Responsive design | 5 | 5
Contact page | 5 | 5
Create a booking | 5 | 4
Update a booking | 5 | 4
Cancel a booking | 5 | 4
Avoid double bookings | 4 | 3
Multiple table occupancies | 4 | 1
Show already booked tables | 4 | 3

### Scope
The strategy table indicates that not all features can be immediately implemented in the initial release of the project. As a result, the project will be broken down into multiple phases. The initial phase will focus on incorporating the essential features necessary to create the minimum viable product.

Phase 1:
* Showcase the food menu
* Provide the option for users to create an account
* Design that adapts to different screen sizes
* Provide a contact form
* Allow users to make a reservation
* Allow users to make changes to a reservation
* Allow users to cancel a reservation

Phase 2:
* The ability to book multiple tables at once
* A contact form that saves messages to the database
* Send an email confirmation when a reservation is received
* Email verification for account creation

[Go to the top](#table-of-contents)
## Surface

### Color palette

The website primarily utilizes the following colors:
* Cream color: rgba(255,240,201,1)
* Dark brown: rgba(115,68,59,0.95)
* Salmon filter: rgba(254,111,97,0.15)
* The inherent colors from Bootstrap

### Typography

The main font used throughout the website is Poppins. In case Poppins is not imported correctly, the fallback font will be a sans-serif font. The choice of Poppins was made after researching fonts that are optimized for reading

## Skeleton

Home/Landing Page:
![home_page](book_table/static/images/wireframes/home_landing.png)

Home carrousel:
![home_carrousel](book_table/static/images/wireframes/home_carrousel.png)

Home text:
![home_text](book_table/static/images/wireframes/home_text.png)

Menu landing:
![menu_landing](book_table/static/images/wireframes/menu_landing.png)

Menu made poke:
![menu_madepoke](book_table/static/images/wireframes/menu_madepoke.png)

Menu allergens:
![menu_allergens](book_table/static/images/wireframes/menu_allergens.png)

Contact landing:
![contact_landing](book_table/static/images/wireframes/contact_landing.png)

Contact map:
![contact_map](book_table/static/images/wireframes/contact_map.png)

My bookings:
![mybookings](book_table/static/images/wireframes/mybookings.png)

Book a table:
![book_a_table](book_table/static/images/wireframes/book_a_table.png)

Sign Up:
![signup](book_table/static/images/wireframes/signup.png)

## Features

### All pages

The navigation bar is located at the top and its options can vary depending on the user's login status. 

If the user is not logged in:
![navbar_no_login](book_table/static/images/features/nav_nologin.png)

If the user is not logged in:
![navbar_login](book_table/static/images/features/nav_login.png)

Navbar mobile:

![nav_mobile](book_table/static/images/features/nav_mobile.png)

![nav_mobile_display](book_table/static/images/features/nav_mobile_display.png)

The footer, which contains social media icons, is located at the bottom of every webpage. Clicking on these icons will open the corresponding links in a new browser tab.

If the user is not logged in:
![footer](book_table/static/images/features/footer.png)

### Main page

The main page is composed of three separate sections, all visually appealing to encourage users to book a table at the restaurant.

Main page landing:
![main_landing](book_table/static/images/features/main_landing.png)

Main page carrousel:
![main_carrousel](book_table/static/images/features/main_carrousel.png)

Main page text:
![main_text](book_table/static/images/features/main_text.png)

### Menu page

The menu page displays all the ingredients and dishes available, clearly indicating which dishes contain allergens, making it easy for those with allergies to know what they can and cannot eat.

Menu page landing:
![menu_landing](book_table/static/images/features/menu_landing.png)

Menu page made poke:
![menu_made_poke](book_table/static/images/features/menu_made_poke.png)

Menu page made your own poke:
![menu_make_your](book_table/static/images/features/menu_make_your.png)

Menu page allergens:
![menu_allergens](book_table/static/images/features/menu_allergens.png)

## Contact page
The contact page includes the location, opening hours, and telephone number of the business. Additionally, a cutout of the location on Google maps is provided for easy reference.

Contact page info:
![contact_info](book_table/static/images/features/contact_info.png)

Contact page map:
![contact_map](book_table/static/images/features/contact_map.png)

Menu page allergens:
![menu_allergens](book_table/static/images/features/menu_allergens.png)

### Log in / Sign in pages

Sign up:
* The signup form is a straightforward process that requires the user to enter their unique username and a password. 
* To ensure accuracy, the user must re-enter the password for confirmation and it must match the original password entered. 
* There is a message to remind users that if they already have an account, they can click the sign-in link to be directed to the sign-in page.
* If the user enters an username that is already registered, an error message will appear. The signup form includes a feature that checks the password's security.
* If the user enters a password that is not secure, they will be prompted with a message to create a stronger password.
* The signup form verifies that both passwords entered match. If the user enters passwords that do not match, an error message will appear to notify them.

Sign up page:
![signup](book_table/static/images/features/signup.png)

Log in:
* The login form requires users to enter their username and the password that they used when signing up for the site.
* There is a message to remind users that if they haven't created an account, they can click the signup link to be directed to the signup page. 
* If the user enters the wrong credentials, an error message will be displayed to inform them.

Login page:
![signin](book_table/static/images/features/signin.png)

Logout: 
* When the user clicks the logout button from the navigation bar, a modal will appear to confirm the action before the user is logged out.

Logout modal:
![logout](book_table/static/images/features/logout.png)

### Table booking

* This section includes a form that allows the user to book a table at the restaurant.
* The user must specify the date and time of the reservation.
* When a date is chosen, the user will be shown which tables are already booked for that day, so they can select an available table.

Table booking page:
![book_table](book_table/static/images/features/book_table.png)

Table booking page with reservations:
![book_table_with_reservations](book_table/static/images/features/book_table_with_reservations.png)


### My bookings sections

* This section lists all the reservations made by the user at the restaurant.
* Each reservation includes a toggle button that, when clicked, displays more information, including buttons to edit or delete the reservation.
* In case the user has not made any bookings, a button will appear in this section that redirects the user to the booking page.

My bookings with reservations:
![mybookings](book_table/static/images/features/mybookings.png)

My bookings with NO reservations:
![mybookings_none](book_table/static/images/features/mybookings_none.png)


### Messages
Certain actions on the website will trigger messages to appear at the top of the page. The color of message is used to indicate the status of the action, such as a green message indicating a successful action and a red message indicating a failure or rejection.

* Accepted reservation (green): The reservation has been accepted and confirmed.
* Denied reservation (red): The reservation has been denied or rejected.
* Deleted reservation (green): The reservation has been deleted successfully.

Messages:
![reservation_success](book_table/static/images/features/reservation_success.png)

![message_error](book_table/static/images/features/message_error.png)

![delete_success](book_table/static/images/features/delete_success.png)

##  Technologies used

### Programing languages
* HTML5
* CSS3
* JavaScript
* Python

### Frameworks and libraries
* Django: Including Django Allauth
* Bootstrap 4.6
* Google fonts
* Font awesome

### Database Management
* Heroku Postgres

### Other tools
* Git
* GitPod
* Github
* Heroku
* Am I responsive
* W3C Markup Validator
* W3C CSS Validator
