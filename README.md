# Django Template Site 

A fully functional django based website. Heroku ready.

To see the site in action go to:
https://stormy-beach-15517.herokuapp.com/

This repo is meant to be a fully functional website suitable for an academic project, small business or similar.

--

I've spent a while now learning build websites- It's been a bit of a frustrating process. Webcoding relies on a lot of structure and a lot of conventions that experience web programmers can take for granted. For an experienced web programmers it's nice not to have to read tons of basic documentation everytime you use an app. For a novice programmer it can be extremely confusing not to understand what goes into making a website.

If your goal is to learn to build websites well this may not be the place for you. You should go read about how the web works, what frameworks can do, the difference between front-end and back-end, etc. That research will serve you well when you try to make your own, more complicated, websites.

If you're like me though you don't particularly care about building websites. You just want something that will look decent and serve as a public face for your project. You're in the right place. Let's get started.

--

#Rule Number One#

If you have a question about how something works, what something is, or how to make a change you need to ask.

Programming is easier when we work as a team. So if there's something you're not getting make an issue and let the community help you. Asking questions will also help me to improve documentation- as it is this is pretty minimal.

Conversely, if you're an experienced web programmer and you have a suggestion don't hesitate. As I said above I'm far from being an expert. I'd like this template site to be as good as possible but I can't follow best practices that i don't know.

--

##Set up the website
- Install Django
- Install the heroku toolbelt (and make a heroku account)
- clone the repo
- `cd django-site-template`
- `python manage.py runserver`
- Did everything work? If not open an issue and copy the traceback from your terminal.
- `grep -rl template_site_name . | grep -v .pyc | xargs sed -i .bak s/template_site_name/your-name/g`
- `grep -rl Template_Site_Name . | grep -v .pyc | xargs sed -i .bak s/Template_Site_Name/Your-Name/g`
- `mv template_site_name your-name`
- `cp your-name/settings_secret.py.template your-name/settings_secret.py`
- change the secret key
- `python manage.py runserver`
- Did everything work? If not open an issue and copy the traceback from your terminal.
- make a new app on heroku
- `heroku git:remote -a your-heroku-app-name`
- `git push heroku master`
- Did everything work? If not open an issue and copy the traceback from your terminal.
- `heroku open` at this point you SHOULD see an error - we are about to fix that


We need to migrate our tables and register an admin account 

- `heroku run python manage.py makemigrations`
- `heroku run python manage.py migrate`
- `heroku run python manage.py createsuperuser`

##Now we're ready to go!
- `heroku open` you should now be getting a 404 error. If you get anything else make an issue.
- add '/admin' to the end of you url
- log in with the superuser accoutn you just made
- if you don't see the admin dashboard make an issue

Now you need to provide info about all of your pages. This site is set up to use the Django Admin as a very simple Content Management Service.

For example click the '+ add' button on the 'HomeInfo' line. 
- Fill in the fields. 
- Hit save.
Now click on '+ add' next to banner line.
- Fill in the image field with the image url of your choice.
- Fill in the title field with anything - it doesn't show up yet.
- Hit save.
- Click view site.

You should now be able to see your homepage! You'll need to edit the info for all the other pages too or you'll get 404 errors for those as well.

--

##Acknowledgments

The front end is based on the modern-business bootstrap template using the sandstone bootstrap theme.

The back end is based on django.
