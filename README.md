The awesome Mr. Cesar project

Transforming the way High School students select universities.

The existing app, built during the hackathon is here:

[http://www2.mrcesar.co/app/index.html#home](http://www2.mrcesar.co/app/index.html#home)

mobile version is here:

[http://mobiletest.me/iphone_5_emulator/#u=http://www2.mrcesar.co/app/index.html%23home](http://mobiletest.me/iphone_5_emulator/#u=http://www2.mrcesar.co/app/index.html%23home)

"original" repo from hackathon

https://github.com/tsabend/collegecoach

To start development:

create a new virtualenv

then:

```
pip install -r requirements.txt
```

App uses Django 1.8 DRF 3.1 and PostgreSQL.

Setup a Postgresq database as per `mrcesar/settings.py`

Then

```
./manage.py migrate
```

```
./manage.py runserver
```

OAuth/Allauth setup:

As per: http://django-allauth.readthedocs.org/en/latest/installation.html

1) Add a Site for your domain, matching settings.SITE_ID (django.contrib.sites app).
2) For each OAuth based provider, add a Social App (socialaccount app).
3) Fill in the site and the OAuth app credentials obtained from the provider.

http://django-allauth.readthedocs.org/en/latest/providers.html

Most providers require you to sign up for a so called API client or app, containing a client ID and API secret. You must add a SocialApp record per provider via the Django admin containing these app credentials.

When creating the OAuth app on the side of the provider pay special attention to the callback URL (sometimes also referred to as redirect URL). If you do not configure this correctly, you will receive login failures when attempting to log in, such as:

An error occured while attempting to login via your social network account.
Use a callback URL of the form:

http://example.com/accounts/twitter/login/callback/
http://example.com/accounts/soundcloud/login/callback/
...
For local development, use the following:

http://127.0.0.1:8000/accounts/twitter/login/callback/

See:
    http://django-allauth.readthedocs.org/en/latest/providers.html#google
    and
    http://django-allauth.readthedocs.org/en/latest/providers.html#facebook

For Google and Facebook specific.


Have fun!

