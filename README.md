<a href="https://imgbb.com/"><img src="https://i.ibb.co/jLDnW1t/logo.jpg" alt="logo" border="0"></a><br>
[This website](https://your-sweethome.herokuapp.com/) was created to let people find there dream rentalhome.<br>
As a user you can look for houses and subscribe to the ones you're interested in.<br>
As admin you can add houses, update house information or delete houses.<br>
## UX
* User stories
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
### Testing User Stories from User Experience (UX) Section
### Further testing
### Known bugs
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