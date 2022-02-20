# Milestone Project 4 – Language School Website

# **Temple Bar School of English Website**

![A mock-up of the website on different devices]( "Mock Up of the site")

# **Table of Contents**
- [**UX**](#ux)
  * [**Project Goals**](#project-goals)
  * [**Users**](#users)
  * [**Site user goals**](#site-user-goals)
- [**Wireframes**](#wireframes)
  * [**User Story**](#user-story)
- [**Features**](#features)
  * [**On Every Page**](#on-every-page)
  * [**Homepage**](#homepage)
 
- [**Information Architecture**](#information-architecture)
- [**Technologies Used**](#technologies-used)
  * [**Languages Used**](#languages-used)
- [**Frameworks, Libraries & Programs Used**](#frameworks-libraries-programs-used-)
- [**Testing**](#testing)
- [**Deployment**](#deployment)
- [**How to deploy this project to Heroku**](#how-to-deploy-this-project-to-heroku)
- [**How to run this project locally**](#how-to-run-this-project-locally)
- [**Credits and Content**](#credits-and-content)
  * [**Code**](#code)
  * [**Acknowledgements**](#acknowledgements)
## **UX**

### **Project Goals**

 The primary goal of this project is to build a full-stack web application for a fictional English language school in Dublin that offers prospective English students in Dublin the chance to discover what courses the school offers, and how those courses could match their English language learning expectations or goals. The site offers e-commerce functionalty via Stripe, a blog section and interactive English level test as well full CRUD functionalty for admin users to update courses, blog posts and user profiles. 


### **Users**

The central audience for this site are English language learners, or the parents of young English language learners, who would like to study in Dublin. 



### **User Story**

| User Story ID | As a/an                                                                          | I want to be able to ...                                                       | So that I can ...                                                     |
|---------------|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| 1             | Student interested in learning English in Dublin                                 | Find out what type of courses the school offers                                | See if they are suitable for me                                       |
| 2             | Student interested in learning English in Dublin                                 | Find out the times and costs of each course                                    | See if they are suitable for me                                       |
| 3             | Student interested in learning English in Dublin                                 | Hear from previous students about their experience at the school and in Dublin | Judge if I am likely to have a simiilar experience                    |
| 4             | Student interested in learning English in Dublin                                 | Find out about the teachers and their style of teaching                        | See if their teaching style matches my learning goals and preferences |
| 5             | Student interested in learning English in Dublin                                 | Find out which course would suit my current level of English best              | Ensure that I study at an appropriate level                           |
| 6             | Student who wants to book an English course at Temple Bar School of English      | Find the course I want to book easily                                          | Save time and not book the wrong type of course                       |
| 7             | Student who wants to book an English course at Temple Bar School of English      | Find as much details as possible about the course                              | Be sure that the course I'm booking is right for me                   |
| 8             | Student who wants to book an English course at Temple Bar School of English      | Pay for the course securely                                                    | Have peace of mind that my money is being spent safely                |
| 9             | Student who has already booked an English course at Temple Bar School of English | Check information about which course I have purchased                          | Double check any information after the booking process has finished   |
| 10            | Student who has an account with the site                                         | Read interesting articles about learning English and the school itself.        | Prepare for my course or simply improve my knowledge of English       |
| 11            | Business / Site Owner                                                            | Have admin privileges                                                          | Ensure that the site is run correctly                                 |
| 11            | Business / Site Owner                                                            | Add and update course details.                                                 | Change or update course details such as prices or course lengths      |
| 11            | Business / Site Owner                                                            | Delete courses                                                                 | Remove unpopular courses or seasonal ones.                            |
| 11            | Business / Site Owner                                                            | Update and edit the website's blog with articles                               | Keep site visitors engaged and promote the school's teaching methods  |

## **Wireframes**

[Wireframes]()











**Design Choices**


	
* **Font**
There is only one font used throughout the website, which is Raleway sans-serif. I chose this font for not only its elegance and clarity but it's readabilty. This site's main users will not be native speakers and may find reading in English challenging. Therefore I chose to use only one font throughout the site so as to not clutter the pages with contrasting styles. 

* **Colours**

The color palette was chosen to maximise the white space of the site and let images stand out, whilst also reinforcing that this is English Language school in Ireland with the green and orange of the highlighting colours suggesting the Irish flag. 

## **Features**

### **On Every Page**

**Navigation**

On every page there is a standard, collapsible nav bar built using Bootstrap 5 classes that shows the website’s name and brand in the top left. There are links for the homepage, a dropdown menu for the course library offering options for General English, Business, Acadmic and Under 16s courses with an option to view all courses as week. The next link is for the site's Level Test and the fourth nav-link is for the site's blog. On the right are options to log in / register. If a user is logged in then the login and register links are replaced with User profile and log out links.

**Footer**
The footer includes social media links to the site's social media pages. Additional links to the separate course categories and blog and level test as well as contact information for the school. 


### **Homepage**

![A screenshot of the homepage]( "Screenshot of the homepage")

**Banner-Image**
The homepage banner image is an image of the Temple Bar area of Dublin where the fictional school is located. The image was chosen as it is a good representation of the lively area and includes the name Temple Bar written clearly on one of the buldings.

**Homepage Headings and call to action button**
Below the image is a white band with fours lines of black text and a call to action button . 'Learn English in the heart of Dublin' is the main heading. The secondary headings reads 'Courses to suit all levels', 'Fun and Engaging Teachers' and 'Reach your English goals'. The call to action button reads 'Find Courses' and will take a user to the course library section of the site. 

**Homepage Headings and call to action button**
A green band with white text asks the question 'Why study at Temple Bar School of English?' and below it are three large font-awesome icons representing the three main reasons why students should study at the school, teaching, facilities and experience.

**Course Cards**
The four category of courses that the school offers are each given a card with a matching image and a short description of the content of each course. At the foot of each card is a link taking the user to the specific course library for that category so the user does not have to manually search for a course. 

### ** Courses **
![A screenshot of the courses page]( "Screenshot of the Courses Page")

The courses page can be navigated to from the navbar, the individual course card or the call to action button on the homepage. There are two possible views that a user can see. 

**All Courses**

The all courses view has a heading with the question 'What type of course are you looking for?" and a vertical pills nav section with an accompanying card with information about each course category. If a user clicks on the find course button for a category they will be taken to the course library view as shown below. The user also has the option to search for a term in the search bar above the course category navigation which will return the course library view showing only courses which include the search term. 

The course library view includes the search bar for any futher search terms the user might want to use. Below the search box the user will be shown the course detail cards giving the user all the information they need about each course in a particular category or matching a search term. 


**Booking Form**

Once a course has been selected the user is taken to the booking form page. At the top of the page is a card containing the course details form. 

The user selects :
* the desired length of the course in weeks, as they increase or decrease the amount of weeks the total course cost at the bottom of the card should automatically update.
* the level of the course from the select input
* the date they would like to start their course on from the datepicker
* their age


Below the card is the student details form into which the user inputs their:
*  full name
*  email address
*  phone number
* country of residence
* nationality
* first language

The user can then proceed to the payment screen via the 'Proceed to Payment' Button or go back the courses page.

*** Checkout ***
The checkout page has a booking summary car at the top recapping all the details the user has just entered on the booking form page. B

After confirming these details are correct the user can then add billing information, (the full name and country from the previous page will be auto added) and add their card number , cvc and zip code to confirm payment.

***Checkout Success***

Once payment is completed the user will see the checkout success page which contains the users booking number , course start date and links to the blog and level test in order for them to contitnue to explore the site. 

**Level Test**

The Level test can be reached by the link in the nav bar and through the hompepage as well as the checkout success view. The test is a series of 20 multiple choice questions which increase in difficulty, designed to assess a student's approximate level of English.

The test begins when a student selects the first answer. They are given immediate feedback by the button colour changing to green  if the QUESTION IS CORRECT AND RED IF THE QUESTION IS WRONG. AFTER THE the 20th question has been answered a result page will appear informing the student how many questions they answered correctly and their approximate level of English with a button that links the user to the courses section in which they can find a course to suit their level. 


**Blog**

The blog section of the site is designed to provide prospective and existing students an opportunity to read articles written by the school's teachers. In order to encourage new users to register for an account to the site the articles can only be read by logged in users.

The blog articles are listed below the banner image with a title a short description of the post and information regarding the post autho and date posted. 

When a site user clicks on the blog preview text, if they are not logged in they will be redirected to the login page as the post details view is restricted to logged in users only. 

Once logged in the full blog post can be read and there is a like button for users to like interesting articles. 

Admin users will find an add post button at the bottom of the page from which they can access the upload add post form in order to add a new post to the site. 


Admin users can also edit a post and delete a post from the blog post page via the two buttons found at the bottom of the post. 

**Log In / Register Forms**

The site utilises the Django Allauth forms to carry out all login and authenication processes. The built in allauth forms have been appropriately styled , placed beneath the site's banner image styled into a Bootstrap card layout matching the sites color scheme.

**User Profile**
Once a user is logged in the can visit the user profile section via the link in the navbar. On this page there are two columns on the left there is a form in which the user's can upload and update their  full name, email, phone number, country of residence, nationality, and first langauge. On the right hand column (or below on mobile) there are details about any bookings the user has made. The user will be able to see a booking number and the date booked and by clicking the more details button the user will see the course dates, course level, start date and timetable. 

**Messages**

All django messages are presented throughout the site via Bootstrap Toasts that appear on the top right of the screen jsut below the navbar.
Each toast has a header coloru matching the type of message with bootstrap's built in color classes, success, danger, info, warning. 


**Admin Procedures**

For admin users who are logged in the course management navlink will become available from which the user can access the add course form in order to add a new course to the course model.


Admin users also have the option to edit course details or delete a course entirely for the course library page by clicking on the edit course or delete course buttons found next to the book course button on course detail card. 




For users 
## **Information Architecture**

**Database Models and Schema**

***Models***
* User
From Django Allauth containing the username, email, and password.

* User Profiles
Containing any information on past bookings and personal details

* Course Categories
Containing the four categories of course the school offers.

* Courses
Containing information regarding individual courses that belong to the four course categories

* Booking
Containing all details related to an individual course booking

* Level Test
Containing the questions, options and correct answers for the interactive level test

* Blog
Containing the titles content and author details of individual blog posts written for the site.


The full models and their relationship to each other are outlined in the schema below. 







## **Technologies Used**

### **Languages Used**
* [HTML5](https://html.com/html5/)
* [CSS3](https://www.w3.org/Style/CSS/Overview.en.html)
* [Javascript](https://www.javascript.com/)
* [Python](https://www.python.org)

## **Frameworks, Libraries & Programs Used**

* [Django](https://www.djangoproject.com/)
    * Django was used to create the project
* [Django Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
    * Django Allauth was used to create user log in functionalty to the site

* [Django Countries](https://pypi.org/project/django-countries/)
    * Django countries was used to populate the options for the country select input in forms throughout the site

* [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)    
    * Django Crispy Forms used to style form inputs throughout the site 

* [Stripe]
    Stripe has been used for the payment section of the site.    

* [Bootstrap 5](https://getbootstrap.com/)
    * Imported CSS and JS, utilised grid system, navbar, form control and modals.

* [Google Fonts](https://fonts.google.com/)
    * Google fonts were used to import the font into the style.css file which is used on all pages throughout the project.

* [Git](https://git-scm.com/)
    * Git was used for version control by utilizing VSCode to commit to Git and Push to GitHub.

* [Github](https://github.com/)
    * GitHub was used to store the projects code after being pushed from Git.

* [Gitpod](https://gitpod.io/)
    * Code was written and edited using the gitpod extension in chrome. 

* [Balsamiq](https://balsamiq.com/)
    * Balsamiq was used to create the wireframes during the design process.


* [JSLint](https://www.jslint.com/)   
    * Used to validate Javascript code.

* [Prettier](https://prettier.io/)    
    * Used to format HTML,CSS and Javascript code.

* [Am I Responsive](http://ami.responsivedesign.is/) 
    * Used to create images of the website on different screen sizes for the documentation. 

* [JQuery](https://jquery.com) 
    * Used to implement the Owl Carousel feaututes.

* [FontAwesome](https://www.bootstrapcdn.com/fontawesome/) 
    * Used to provide icons for the homepage

* [Unsplash](https://unsplash.com/)
    * Used to source images for the site, including the hero images, all ingrdient and recipe images. 
* [Heroku](https://www.heroku.com/)   
    * Used to deploy the site


## **Testing**

Testing information can be found in this [separate file](). 


## **Deployment**

## **How to deploy this project to Heroku**

To deploy this site to heroku the following steps need to be taken.






## **How to run this project locally**

To run this project locally you will need an IDE (e.g. VS Code/Gitpod) with PIP , Python 3 and Git installed. A free account at Mongo DB is also required.
Below are the steps to run this project locally for Gitpod although steps may be different depending on the IDE used. 

1. Clone the repository by navigating to the [GitHub Repository ](), and clicking on the code button with the dropdown arrow. 





## **Credits & Content**

All the images on the website were sourced from [Unsplash](https://unsplash.com/).





### **Code**






### **Acknowledgements**



