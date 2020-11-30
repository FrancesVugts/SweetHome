<a href="https://imgbb.com/"><img src="https://i.ibb.co/jLDnW1t/logo.jpg" alt="logo" border="0"></a><br>
[This website](https://your-sweethome.herokuapp.com/) was created to let people find there dream rentalhome.<br>
As a user you can look for houses and subscribe to the ones you're interested in.<br>
As admin you can add houses, update house information or delete houses.<br>
## UX
* User stories
    * For a user
        * As a user I want to be able to read some basic instructions on how the website works.
        * As a user I want to be able to contact the owner of the website in case I have any questions.
        * As a user I want to be able to navigatie easelly between the pages.
        * As a user I want to be able to make my own account.
        * As a user I want to be able to have a look at the houses that are available.
        * As a user I want to be able to filter on houses with certain properties.
        * As a user I want to be able to sort the houses on a certain propertie.
        * As a user I want to be able to see more photos and details of a house I'm interested in.
        * As a user I want to be able to see where a house is located.
        * As a user I don't want to see any houses that are no longer available.
        * As a user I want to be able to subscribe to a house.
        * As a user I want to be able to unsubscribe to a house.
        * As a user I want to be able to see for which houses I have a subscription.
        * As a user I don't want to see subscriptions to houses that are no longer available.
        * As a user I want to bee able to see my personal details.
        * As a user I want to be able to change my personal details.
        * As a user I want to be able to easelly make a payment.
        * As a user I don't want to be able to accidentally make a dubble payment.
    * For the admin
        * As admin I want to be able to add avaialble houses.
        * As admin I want to be able to edit available houses.
        * As admin I want to be able to delete houses that are not available.
        * As admin I want to get a warning before a house is really deleted.
        * As admin I don't want the user to be able to subscribe more then once to a house.
        * As admin I don't want the user to see houses that are not available, but I do want to keep them in the database.
        * As admin I don't want other people to able to maken changes to houses or delete houses.
* Design
    * Color Scheme
        * I've chosen for 2 popping colors that go well together to make the company stand out.
        For the rest I've kept the color scheme simple to give the attention to the two main colors.
        I like to go for a darker and a bit of a lighter color for easy use, because you can use a lighter color to stand out on a darker background and visa versa.
    * Typography
        * For this site I've chosen to use two fonts.
        First of all I've used Open Sans for the main text for easy reading, because I want the user to be comfortable.
        The user is looking for a house to feel comfortable in, so the site should fit with this feeling.
        As my second font I've chosen  for Poiret One.
        With this font I want the important pieces of text and the logo to really stand out, to fit with a company that stands out.
        I want it to give the site a bit of a luxary feeling with this font as well.
        Offcourse I also wanted to combine to fonts that go well with each other.
    * Imagery
        * The images on this page would be from the houses that are up for rental.
        In case there is no team image, I've created a default images that fits well with the rest of the website.
* Wireframes
    * [Phone Wireframes](https://i.ibb.co/pKfHT6J/Telefoon.jpg)
    * [Tablet Wireframes](https://i.ibb.co/gDZy66H/Tablet.jpg)
    * [Screen Wireframes](https://i.ibb.co/TP6tTTt/laptop.jpg)
## Features
* I've made sure the site is responsive and easy to use on different devices.
* The site contains interactive elements like color changes when hovering over elements and a hamburger menu that changes when clicked on.
* The site contains a register, login and logout option.
* The site contains a profile page where the user can see it's personal details, and subscriptions.
* The site contains an admin option who has extra rights on the page.
* The site contains a contact form in case of problems.
## Technologies used
I have used the following technologys for this project:
* [Github](https://github.com), for version control.
* [Gitpod](https://gitpod.io), for my development environment.
* HTML5, because it is the standard markup language for Web Pages.
* CSS3, to style the website.
* Javascript, for the use of a contact form.
* [Python](https://www.python.org), for the backend.
* [Django](https://www.djangoproject.com/), for my framework.
* [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) To render forms.
* [Postgres SQL](https://www.postgresql.org/), for my database.
* [Heroku](https://heroku.com), to deploy my app.
* [EmailJS](https://www.emailjs.com/), to let the user be able to contact me.
* [Stripe](https://dashboard.stripe.com/register) for online payment.
* Unittest, for testing my Python code.
* PIP, to download tools.
* [JQuery](https://jquery.com) for DOM manipulation.
* [Bootstrap](https://getbootstrap.com/), to make my website responsive and mobile-first.
* [Font Awesome](https://fontawesome.com/) for the icons used on this website.
* [Google Developers](https://developers.google.com/) for adding a map with the houses location.
* [Google Fonts](https://fonts.google.com/), to choose and combine my fonts.
* [Coolors](https://coolors.co/), to choose my and combine my colors.
## Testing
To make sure there where nog syntax errors, I've used the following validators on my pages:
* [HTML validator](https://validator.w3.org/#validate_by_input)
* [CSS validator](https://jigsaw.w3.org/css-validator/)
* [Python validator](https://extendsclass.com/python-tester.html)
### Testing User Stories from User Experience (UX) Section
* User
    * As a user I want to be able to read some basic instructions on how the website works.
        * From the navigation menu the user can go to the "info" page.
    * As a user I want to be able to contact the owner of the website in case I have any questions.
        * From the navigation menu the user can go to the "contact" page.
        * Here the user can fill in name, emailaddress and a message and send the question to the owner of the site.
        * The user get's a pop up that tells the user that the message has been send. 
    * As a user I want to be able to navigatie easelly between the pages.
        * There is a Navigation menu on the top of the page with all the links displayed.
        * On smaller screens there is a hamburger menu on the top of the page where the user can click on. This will result in a dropdown menu with all the links displayed.
        * On certain actions the user gets linked to the most logical page. For instance, when subscribing to a house, the user gets linked to the profile page where it can see it's subscriptions.
    * As a user I want to be able to make my own account.
        * When navigating to the login page, there is a link that says "sign up".
        * On the sign up page the user kan create an account.
        * From there the user will be linked to the profile page.
        * On the profile page the user can add personal information.
    * As a user I want to be able to have a look at the houses that are available.
        * From the navigation menu the user can go to the "houses" page.
    * As a user I want to be able to filter on houses with certain properties.
        * When on the houses page, there is a subheader with a link to "Set Filters" in the top left.
        * When clicking on "Set filters", a modal pops up.
        * On the modal the user can filter on city, price, type and minimum amount of bedrooms.
        * When clicking "Save filters" the modal will close and the user can see the filterd list of houses.
        * The user can also click on "Clear filters", to once again get all the results.
    * As a user I want to be able to sort the houses on a certain propertie.
        * When on the houses page, there is a subheader with a link to "Set Filters" in the top left.
        * When clicking on "Set filters", a modal pops up.
        * On the modal the user can sort by price or cityname in ascending or descending order.
        * When clicking "Save filters" the modal will close and the user can see the sorted list of houses.
        * The user can also click on "Clear filters", to once again get all the results from new to old.
    * As a user I want to be able to see more photos and details of a house I'm interested in.
        * When the user is on the houses page, it can click on a card.
        * This will open up a new page with more photo's and details.
    * As a user I want to be able to see where a house is located.
        * When the user is on the houses page, it can click on a card.
        * This will open up a new page where the user can also find a google maps map with a marker at the address from the house.
    * As a user I don't want to see any houses that are no longer available.
        * The houses page will only display cards for houses where the current date is betweend the starting and the ending date.
    * As a user I want to be able to subscribe to a house.
        * When the user is logged in, the user can fill out the personal details on the profile page.
        * After that there will be a payment button available that the user can use to make a payment for one year.
        * Then the user can go to the houses page and click on the house they want to subscribe to. 
        * On the bottom of the page, there will be a subscribe button available. 
    * As a user I want to be able to unsubscribe to a house.
        * When a user is subscribed to a house, the user can unsubscribe with a button at the same place as the subscribe button.
        * Also, on the profile page the user can see the subscriptions and use a unsubscribe button as well.
    * As a user I want to be able to see for which houses I have a subscription.
        * The user can go to the profile page via the menu.
        * On the right side the user can see the subscriptions.
        * When the user subscribes to a house, they will also automatically go to the profile page to be able to see the subscriptions.
    * As a user I don't want to see subscriptions to houses that are no longer available.
        * Just like the houses overview, only subscriptions will be viewed when the current date is betweend the start and enddate of the house.
    * As a user I want to bee able to see my personal details.
        * On the profile page the user can fill in the personal details.
        * After the user has filled in the personal details, they will allways be viewed on the profile page.
    * As a user I want to be able to change my personal details.
        * On the profile page the user can fill in the personal details.
        * After the user has filled in the personal details, they will allways be viewed on the profile page.
        * When the user wants to change the personal details, the user can use the button on the bottom of the personal info.
    * As a user I want to be able to easelly make a payment.
        * When te user is logged in and the user has filled out the personal details, there will be a button for paymenty available at the bottom of the personal info.
    * As a user I don't want to be able to accidentally make a dubble payment.
        * When te user has made a payment, the payment button will nog longer be visible.
* Admin
    * As admin I want to be able to add avaialble houses.
        * When logged in as super user the admin can go to the manage page via the menu.
        * On this page the admin can fill out all the information and use the button to add the house.
    * As admin I want to be able to edit available houses.
        * When logged in the admin can go to the houses page and click on the house that needs to be adjusted.
        * Under the house information the admin can click on "edit".
        * Here the admin can change what needs to be changed and click on the button "Update house".
    * As admin I want to be able to delete houses that are not available.
        * When logged in the admin can go to the houses page and click on the house that needs to be adjusted.
        * Under the house information the admin can click on "delete".
        * A modal will pop up to ask the admin of the house really needs to be deleted as a safety check.
        * Here the admin can change what needs to be changed and click on the button "Update house".
    * As admin I want to get a warning before a house is really deleted.
        * Under the house information the admin can click on "delete".
        * A modal will pop up to ask the admin of the house really needs to be deleted as a safety check.
    * As admin I don't want the user to be able to subscribe more then once to a house.
        * When the user is subscribed to a house, the subscription button will no longer be visible.
        * Also there will be a background check if the subscription allready exists. If so, there will not be another subscription added.
    * As admin I don't want the user to see houses that are not available, but I do want to keep them in the database.
        * The houses page will only display cards for houses where the current date is betweend the starting and the ending date.
        * Alltough the houses will not be viewed, they are present in the database.
    * As admin I don't want other people to able to maken changes to houses or delete houses.
        * When someone is not logged in or the person is logged in but not as superuser, the links to update and delete houses are not visible.
### Further testing
* I've tested this Website on Google Chrome, Microsoft Edge and Firefox browsers.
* I've tested this Website on laptop and mobile.
* I've tested different devices using "inspect" in chrome.
* I've asked friends and family to look at the website and give feedback.
* I've written as much automated tests as I could in the given time.
* I've written automated tests for urls, views, models and forms.
### Known bugs
* There is one bug on the page where you can edit a house. When you hover over the "Select image" button, the mouse should turn in to a hand. It does do that, but not for the whole button as it should be.
* The same goes for the page where you can add a house.
## Deployment
This project was created using Github.<br>
From there I used Gitpod.io to write my code.<br>
Then I used commits to git followed by pushes to my GitHub repository.<br>
Later on I've deployed this project to Heroku and used automated pushes to make sure my pushes to GitHub were also made to Heroku.<br>
For deployment on Heroku I've used the following steps:
* Using the terminal command pip freeze > requirements.txt I have created a requirements.txt file.
* Using the terminal command echo web: python app.py > Procfile I have created a procfile.
* I've used git add, git commit and git push to push the requirements and procfile to GitHub.
* I've created a new app on the Heroku website by using the "new" button on my dashboard.
* I gave the app a name of your-sweethome and set the region to Europe.
* From the Heroku dashboard I've clicked "Deploy" > "Deployment method" and selected GitHub.
* Confirm the linking of the heroku app to the correct GitHub repository.
* In the heroku dashboard I've clicked "Settings" > "Reveal Config Vars".
* I've added the config vars for my AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, DATABASE_URL, EMAIL_HOST_PASS, EMAIL_HOST_USER, SECRET_KEY, STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY, STRIPE_WH_SECRET, USE_AWS.
* In the heroku dashboard I've clicked "Deploy".
* In the "Manual Deployment" section of this page I've made sure the master branch is selected and I've clicked "Deploy Branch".
* The site was now successfully deployed.
## Left to implement in the future
* I've implemented a payment system for the user to make a payment for one year. With that I've made my buttons so a user cannot make a dubble payment and a user cannot subscribe to a house without making a payment. But what's left to implement is that the payment should get a date of experiment, one year after the payment.
* I would like for the user to also be able to easelly see if they made a payment and what the date of experiment is.
* If there would have been more time, I would have liked to write more automated tests.
## Credits
### Content
* All the content for this website was writen by the devoloper herself.
### Media
* The no_photo image was created by the developer herself.
* I've used photos from Pexel to fill my database with some examples photos of houses.
### Acknowledgement
* I would like to thank my mentor for the feedback througout this project.
* I would like to thank tutor support for helping me where needed.
* I've added comments with links when using code from other people, I would like to thank these people as well for providing helpfull information on the internet.