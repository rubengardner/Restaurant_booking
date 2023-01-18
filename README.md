# Table of Contents

-   [1. UX](#ux)
    -   [1.1. Strategy](#strategy)
        -   [Project Goals](#project-goals)
            -   [User Goals:](#user-goals)
            -   [User stories](#tuser-stories)
            -   [Strategy Table](#strategy-table)
    -   [1.2. Structure](#structure)
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

#  Technologies used

## Programing languages
* HTML5
* CSS3
* JavaScript
* Python

## Frameworks and libraries
* Django: Including Django Allauth
* Bootstrap 4.6
* Google fonts
* Font awesome

## Database Management
* Heroku Postgres

## Other tools
* Git
* GitPod
* Github
* Heroku
* Am I responsive
* W3C Markup Validator
* W3C CSS Validator
