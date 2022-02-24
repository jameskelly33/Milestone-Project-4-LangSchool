## **Testing**

### **Automated Testing**

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project. The PEP8 onlince checker tool was used to check the python code is PEP8 compliant. JSlint was used to check the quality of the javascript code and Prettier was used to format code across the project. 

* [W3C Markup Validator](https://validator.w3.org/) 
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
* [JSLint](https://www.jslint.com/)
* [Prettier](https://prettier.io/)
* [Python PEP8 Validator](http://pep8online.com/)


## **Testing User Stories from User Experience (UX) Section**

### **User stories 1 - 5**

***As a student interested in studying in Dublin I want to be able to..***

1. ***Find out what type of courses the school offers***
- Users can click on the Find Courses call to action button on the homepage as well as read tehc ourse category cards on the homepage whcih detail the four main categories of courses which the school offers. A user can also use the navbar to navigate to the all courses page or the course library page fro specific course categories. Users can also use the search function to find a a specific keyword related to the course they are interested in. 


2. ***Find out the specific detials of the course such as the times and costs etc.***
- Users can find all required information on the course card, with a description of the course, the times ,cost, required levels and ages, minimum class size and total course hours. 

3. ***Hear from previous students about their experience at the school and in Dublin***
- Users can read the testamonials sections of website to find out what previous students think about studying at the school  

4. ***Find out about the teachers and their style of teaching***
- Users can navigate to the blog of the site which provides articles relating to learning English written by the school's teachers. Although they will have to register to view the article(see user story 10)

5. ***Find out which course would suit my current level of English best ***
- Users can take an interactive level test to find out roughly what level of English they have and can book a course accordingly.

### **User stories 6 - 9**

***As a student who wants to book an English course at Temple Bar School of English.***

6. ***Find the course I want to book easily***
- Users can the search option on the courses or the course library pages to find a specific course or narrow down a course by keyword. 

7. ***Choose a level, start date and course date that suits me***
- When booking a course the user can select the course level that they desire and the start date.

8. ***Pay for the course securely***
- The user can complete a secure payment thanks to the sites intergration of the Sripe API payment service. After which they will receive a confirmation email that their booking was successful. 

9. ***Check information about which course I have purchased***
- The user will receive a confirmation email after booking with the course details they have chosen. As well as this if the user has a profile with the site they can go to the user profile to find their booking information and course details.

### **User story 10**

***As a student who has a profile with the site.***

10. ***Read interesting articles about learning English and the school itself.***
- A user can login to view blog articles written by the school's teachers on the subject of learning English. The user also has the option to like interesing articles via the like button. 

### **User stories 11-14**

***As a site/business owner***

11. Have admin privileges
- The Django super user can use their username and password to access the Django admin section of the site to make any necessary changes. 
12. Add and update course details.
- The admin user can add a course via the add course navbar option. If they would like to edit an existing course they can access the edit cours button on indiviudal course cards in the course library. 
13. Delete courses
- The admin user can delete a course via the delete course button on each individual course card in the course library.
14. Update and edit the website's blog with articles 
- The admin user can upload a new blog article via the add post button at the bottom of the blog post page. If an admin user wants to edit or delete a blog post they can use the edit or delete buttons found at the bottom of the individual blog posts. 


# **Manual Testing Procedure**

All steps were taken on Google Chrome, Firefox, Safari and Internet Explorer on a Thunderbolt Display and MacBook Pro at two different desktop screen resolutions and subsequently an iPhone X screen, iPad 3, and iPhone 8.

## **Elements on each page**

**Navbar**

* Click on Temple Bar School of English brand to check it brings user to homepage.
* Click on Home to check it bring uses to homepage.
* Click on Courses to check dropdown menu appears.
* Click on General English to check it brings user to the course library page showing all General English courses.
* Click on Academic English to check it brings user to the course library page showing all Acdemic English courses.
* Click on Business English to check it brings user to the course library page showing all Business English courses.
* Click on Under-16s Courses to check it brings user to the course library page showing all Under 16-s English courses.
* Click on All Courses to check it brings user to the courses  page showing the four categroy options. 
* Click on Level Test to check it brings user to the Level Test page with the 1st question showing.
* Click on Blog to check it brings user to the Blog page with all blogs post showing.
* Check that if no user is logged in, the Register and Login links are active and take the user to the appropriate pages.
* Check that if a user is logged in , the Profile and Logout links are active and take the user to the appropriate pages.
* Check that each Nav link becomes active upon navigating to it. 
* Check that the navbar collapses into mobile view with the brand and hamburger icon displayed on the small screen sizes.
* Repeat all steps above for mobile navbar. 

**Footer**
* Check that the blog and Level test Links take the user to the appropriate pages.
* Check that each social network link takes the user to the appropraite social network site. 
* Check that each course category link takes the user to the appropriate course library page.
* Check that the column layout changes to veritcal on small screens.


## **Homepage**

**Banner Image**
* Check that the banner image loads and the title text animation is working.
* Check that the title text is displayed left aligned on mobile views.

**Heading texts and call to action button** 
* Check that the correct animations are working for each heading.
* Check that the Find Courses button takes users to the Courses page.

**Why study banner**
* Check that the three column layout is applied on all screen sizes.

**Course Category Cards**
* Check that the column layout of 4 columns horizontally for large screens, 2 col for medium screens and vertical columns for mobiles.
* Check that the appropriate image is displayed for each category.
* CHeck that the button link on each card takes the user to the appropriate course library page for that category. 


## **Courses**

**All Courses View**
* Check that the course category navigation tabs are displayed with the General English category open.
* Check that the description matches the correct tab.
* Check that the button link to check it takes the user to the General English course library view.
* Hover over inactive tabs to check hover animation is working.
* Click on Acadmic English tab to check the card changes to the Academic English category description.
* Click on the button link to check it takes the user to the Academic English course library view.
* Repeat the above two steps for Academic English tabs, and the Under 16s tab.
* Check that one mobile views the Course Category Accordion is displayed and each tab is displaying the same information as above and each link behaves as above.
* Try to submit an empty search query to check error message is displayed.
* Try to submit a search for a term that is not included in the courses to check that the user sees the no results message.
* Try to submit a search for appropirate terms found in the course library to check that the results are displayed in the correct course library view.
GIF GIF GIF GIF

**Course Category View**
* Check that all course cards are appropriate to the course category view i.e. if the user is on the General English Course Library view make sure that every course card is of the category General English. 
* * Try to submit an empty search query to check error message is displayed.
* Try to submit a search for a term that is not included in the courses to check that the user sees the no results message.
* Try to submit a search for appropirate terms found in the course library to check that the correct results are displayed in the course library view.
* Check that each course card is showing a Card Header with the Course Name, the course description in the main card body, the minimum class size, total course hours, and minimum age in the card footer and course timetable, course cost and cost in the second column. 
* Check that the Book Course button takes the user to the Booking form page for that particular course. 
* Check that on mobile views that course card is presented vertically in one column, with the appropriate information as above. 
* Check that the Show Course Categories button takes the user back to All Courses view as described previously. 


## **Booking Form**

* Check that the correct course name is displayed as the card title in the booking form.
* Check that the How many weeks would you like to study? input is displaying the default 1.
* Check that upon changing the input the Total Course Cost field below is updated wiht the correct total course cost. 
* Check that the form will not submit with a 0 or negative number.
* Check that the Current Level of English select input displays the correct options when clicked.
* Check that a user cannot book a course with a current level lower than the restricted level for that course. See example below of a user trying to book a C1 Advanced course with a level of B1. 


GIFGIFIGFIGFIGFIG
* Check that the datepicker input for the When would you like to start your course is working by clicking on the calendar icon. 
* Check that a user cannot book a course date in the past . See below for example.

GIF GIF GIF
* Check that a user cannot enter an age of below the minimum of 5. 
* Check that a user is redirected to course page if they attempt to book a course with an age that is below the minimum age of above the maximum age and the correct error message is displayed.
* Check that the user cannot submit the form with an empty or invalid field for Full Name input.
* Check that the user cannot submit the form with an empty or invalid field for email input.
* * Check that the user cannot submit the form with an empty or invalid field for Phone Number input.
* Check that the user cannot submit the form without selecting  a country value in the country select input.
* Check that the user cannot submit the form with an empty or invalid field for Nationality input.
* Check that the user cannot submit the form with an empty or invalid field for First Language input.
* Check that the Proceed to Payment button takes the user to the Checkout page if all valid form criteria are met.
* Check that the Back to Courses button takes the user back to the All Courses View. 

***Checkout Page***

* Check that the details on course booking summary card match the details entered on the previous page.
* Check that the billing address form has preloaded the full name and country entered on the previous page.
* Check the form will not submit with empty or invalid input for Full Name.
* Check the form will not submit with empty or invalid input for Address 1.
* Check the form will not submit with empty or invalid input for Address 2.
* Check the form will not submit with empty or invalid input for City.
* Check the form will not submit with no card details and the Stripe Error label is displayed.
* CHeck the Stripe error message is displayed with an invalid Card Number.
* Check the form will not submit without a valid CVC number of Zip Code and the Stripe error message is displayed. 
* Check that if all form inputs are valid the Make Payment button takes the user to the Checkout success form and the submit button is disabled to prevent multiple submissions. 
* Check that the Back to courses button takes user back to the All Courses View. 

GIF 

**Checkout Success Page**

* Check that the correct booking number, course name and start and end date are displayed on the card.
* Check that the blog link in the explore our site section takes the user to the blog page.
* Check that the level test link in the explore our site sections takes the user to the level test page.


## **Level Test**

**Level Test**

* Check that the question number start at 1 and the correct question from the database and its four options are displayed.
* Check that the question layout changes from 2 columns to 1 column on mobile screens.
* Select the correct answer and check that the success message is displayed and the next question is loaded.
* Select the incorrect answer and check that error message is displayed and the next quesiton is loaded.
* Repeat the above process for each question.

GIFGIF


**Level Test Results Page**

* Check that the correct number of correct answers is displyed.
* Check that the number of correct answers matches with the correct level in accordance with the result key below.
       
        result_key ={
            range(0,4):'A1 - Beginner',
            range(4,7):'A2 - Elementary',
            range(7,10):'B1 - Pre-Intermediate',
            range(10,14):'B2 - Intermediate',
            range(14,17):'B2H - Upper Intermediate',
            range(17,20):'C1 - Advanced'}

* Check that the Retake Test button takes the user back to start of level test.
* Check the the Courses button takes the user to the All Courses View.
* Check that the Show Correct Answers dropdown button displays the correct answers.
* Check that for each card in the correct answers dropdown container every correct answer has a background colour of green. 
* Check that re-clcicking the show correct answers button closes the Correct Answer container. 


## **Blog**

**Blog Page Previews View**

* Check that for each post there is a title, short description, autho , date posted and likes.
* Check that clicking on the title or the short description takes the user to the blog details view if they are logged in.
* Check that if a user is not logged clicking on a blog post redirects the user to the login page.
* Check that the add post button appears at the bottom of blog post librayr for admin user only.

**Blog Post Details View**

* Check that the correct title , short description and post content are displayed.
* Check that posts are sorted from newest to oldest.
* Check that author and date posted information and number of likes are at the bottom of the post.
* Check that the like button increments the number of likes by 1 and reloads the page without the like button to prevent multiple likes by the same user.
* Check that if a user has previously liked a post that there is no like button displayed on initial page load. 
* Check that the edit post and delete post buttons are visible at the bottom of the page for admin users.
* Check that the edit post takes the admin user to the edit post form.
* Check that the delete post deletes the post from the databse and the blog post preview page.


## Allauth functionality 

* Check that custom styles on Allauth forms are displayed on all Alluth templates.
* Check that a new user can register and successfully recieve a confirmation email.
* Check that existing users can log in and log out succesfully. 
* Check that existing users can change passwords. 

## Profiles

* Check that user who is logged in can access the profile link in the navbar.
* Check that the update information button correctly updates the details in the user profile form.
* Check this information persists after logging out and back in again.
* Check that a user with no bookings has an empty booking history section.
* Check that a user that has made a booking has that booking showing in the booking history section.
* Check that the dropdown button show details reveals the correct details about the booking.


## Admin Functionality

**Add Course**

* Check that the add course nav link takes the admin user to the add course form.
* Check that the form does not submit with empty or invalid fields for course name input.
* Check that the form does not submit with empty or invalid fields for course description input.
* Check that the form does not submit with empty or invalid fields for maximum class size.
* Check that the form does not submit with empty or invalid fields for course hours.
* Check that the form does not submit with empty or invalid fields for minimum age.
* Check that the custom validator for minimum age is working by entering an age below five and triggering the error message.
* Check that the form does not submit with empty or invalid fields for course cost per week. 
* Check that the form does not submit with empty or invalid fields for timetable.
* Check that the add course button successfully adds a course to the databse and course library.
* Check that the cancel button takes the user back to the homepage. 


**Edit Course**

* Check that the edit course form loads with correct course information
* Check that the info toast is displayed confirming the admin user is editing the course details of the selected course.
* Check that the updated form does not submit with empty or invalid fields following the steps from above in the add course testing process.
* Check that the update course button brings the user back to the All courses page and a success message is displayed and the course details have been succesfully updated.

**Delete Course**

* Check that the delete course button successfully deletes the course from the course library and databse and a success message is displayed confirming the deletion. 

**Add Blog Post**

* Check that the add blog post form displays with the correct placeholders.
* Check that the form does not submit with any empty fields.
* Check that the Add Post button successfully uploads the post to the libray with the correct author and date posted.
* Check that the blog post content template has succesfully separted the post content into paragraphs tags at each linebreak. 
* Check that the cancel button takes the user back to the blog page.

**Edit Blog Post**

* Check that the edit blog post form displays with the current post content.
* Check that the info toast is displayed confirming the admin user is editing the post.
* Check that the form does not submit with any empty or invalid fields. 
* Chcek that the Update Post button successfully adds the updated post. 

**Delete Blog Post**

* Check that the delete post button successfully deletes the post from the blog post page and the database and a success message is displayed confirming the deletion. 

