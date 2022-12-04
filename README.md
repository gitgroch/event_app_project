<!-- Insert Mobile responsiveness picture here -->

# **EventBoard**

![screenshot of site from https://ui.dev/amiresponsive.](/documents/images/home.jpg)


## **Overview**

EventBoard is a website where users can find events they might be interested in their local area. Users can view comment and create event posts. 

Target Audience:

- People looking for events to attend
- People who want to promote their event
- People who want to join the discussion on upcoming events

User Stories:

- As a Site User I can create and edit my event post so that I can bring awareness to my event.
- As a Site Admin/User I can create draft event posts so that I can finish writing the content later
- As a Site Admin I can create, read, update and delete posts so that I can moderate the sites content.
- As a user I can categorise my event posts so that other users can find my event easily.
- As a Site User I can register an account so that I can create event posts and comment on others.
- As a Site User / Admin I can comment on an individual event post so that I can join the conversation.
- As a Site User / Admin I can view comments on an individual event post so that I can read the conversation.
- As a user I can delete my comment so that I can have control on what I post to the website.
- As a Site User I can view a list of events so that I can choose one to view.
- As a user/poster I can delete my post so that I can control the information for the event that I posted.


The development Goals for the Website were to:

-  Create a website that is clean and simple and easy for users to read - ACHIEVED
-  Provide a method where users could create, reade upda and delete their own events - ACHIEVED
-  Provide a method where users could create, reade upda and delete their own comments- ACHIEVED
-  Provide a page that users can find a place to purchase related publications - ACHIEVED

The website can be accessed here: https://proj4-event-app.herokuapp.com/

## **Agile Methodology**

- Agile methodolgy was used in the development of the project in the form of a Kanbanboard available [here](https://github.com/users/gitgroch/projects/1/views/1)


### **Color Schemes** 

I wanted a clean look for the event board so decided to use a simple complementary colour scheme for this project 

![screenshot of chosen color scheme](/documents/images/scheme.jpg)
### **Typography**

I looked for fonts that complement each other, minimalist.

**Fonts:**
- Primary: Montserrat
- Secondary: Lato
- Backup font: Sans Serif

The fonts are sourced from Google fonts.


### **Features**

**Header Navigation Menus**

- The website employs two header navigation menus that include all front facing pages on the website. The navigation menus are fully responsive and change styles depending on the screen size. 
- The menus allow the user to easily navigate across the website, discouraging the use of browser back button.

**Post List View**

- The post list view generates an info card based on the information provided in the post form. 

![screenshot of postlist](/documents/images/postlist.jpg)

**Post Form View** 

- The post form takes data from the user and passes it to the Database. Fields in the form are created from fields availble in the database.

![screenshot of post form](/documents/images/postform.jpg)

**Modal** 


- A model was implemented to confirm deletion of both posts and comments to keep in line with defensive programming practices

![screenshot of modal](/documents/images/modal.jpg)

## **Testing:**



A seperate document has been created to detail Testing, Validation, Bugs and Fixes, which can be found [here](documents/TESTING.md)).

- [TESTING](documents/TESTING.md)

## **Future Enhancement**

The following features were considered nice to haves during development but not necessary for minimal viable project, and remained outside the scope for project submission.

- Add functionality to filter posts by county
- Add functionality to filter posts by category
- Add functionality to filter posts by county and category
- Implement SSO for popular social media accounts 
- Add functionality to mark events as finished once event date has passed.


## **Deployment** 

The site was deployed to Heroku pages. The steps to deploy are as follows:

- Log in to Heroku.
- From Dashboard > 'New' > 'Create New App'
- Name the project, select region
- Click 'Settings' then'Reveal Config Vars'.
- Add a value for 'SECRET_KEY' connecting to your django environment.
- Add a value for 'DATABASE_URL' connecting to your postgreSQL database.
- Add a value for 'ClOUDINARY_URL' connecting to cloudinary's cloud hosting service for media.
- Got to 'Buildpack'  select 'Add buildpack' then 'Save Changes'.
- Click 'Deploy' tab.
- Choose GitHub
- Connect to repository on GitHub.
- For final deployment ensure DEBUG = False in settings.py.
- In deploy settings click Deploy Branch
## **Credits**

- I used code from the "I think therefore I blog" tutorial project as a starting point for this project. Code 
has been altered or replaced throughout development to suit the project needs.
- Images for test posts are from Pexels
- Templates for form pages are from MDB Bootstrap.  Code 
has been altered or replaced throughout development to suit the project needs.
