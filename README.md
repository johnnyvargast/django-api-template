# Backend
Backend for the generic `Backend` project

## Project Config
1. Python `3.7`.
2. Django `3.2.4`.

# Installation
### Requirements
- Python 3.7 & up
- PIP (package manager) (pip v19.0.3)
- Virtual Environment (pipenv or virtualenv)

### Set up

Here is the step-by-step procedure to set up the `Backend project`

- Clone the Backend project from gitlab by following command:
```
git clone https://github.com/johnnyvargast/django-api-template.git
```
- Create a new virtualenv and activate it
- Into `backend` folder:
```
cd backend
```
- Install Dependencies:
```
pip install -r requirements.txt
```
- Create the `.env` file in the main project folder
- Set up the `.env` file with corresponding variables like `database, secrete_key`. You can use the `.env.example` file as a guide.
- Run the following command for migrations.
```
python manage.py migrate
```
- Create Super User 
```
python manage.py createsuperuser
```

- After all these steps , you can run this project with the command.

```
python manage.py runserver
```


## Convention commits
#### Format
type: Short description  
More description (if it is necessary)
Related issues (if it is necessary)

#### Types:
- feat:
    A new feature or improvement.
- fix:
    Fixed a bug.
- docs:
    Changes on the documentation files
- style:
    Changes on the styling on the code but not changes on the functionality

#### Example:
```shell
feat: Summarize changes in around 50 characters or less

More detailed explanatory text, if necessary. Wrap it to about 72
characters or so. In some contexts, the first line is treated as the
subject of the commit and the rest of the text as the body. The
blank line separating the summary from the body is critical (unless
you omit the body entirely); various tools like `log`, `shortlog`
and `rebase` can get confused if you run the two together.

Explain the problem that this commit is solving. Focus on why you
are making this change as opposed to how (the code explains that).
Are there side effects or other unintuitive consequenses of this
change? Here is the place to explain them.

Further paragraphs come after blank lines.

 - Bullet points are okay, too

 - Typically a hyphen or asterisk is used for the bullet, preceded
   by a single space, with blank lines in between, but conventions
   vary here

If you use an issue tracker, put references to them at the bottom,
like this:

Resolves: #123
See also: #456, #789
```

For more details you can review [this article](http://udacity.github.io/git-styleguide/) or [this one](https://www.conventionalcommits.org/en/v1.0.0/).


#
### Command executed to install the libraries used in this project
```sh
pip install django==3.2.4
pip install django-environ
pip install boto3
pip install django-storages
pip install djangorestframework
pip install djangorestframework-jsonapi
pip install django-filter
pip install drf-yasg
pip install djangorestframework-simplejwt
pip install django-cleanup
```