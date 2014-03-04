========
Overview
========


django-mandrill is a Django email backend allowing MailChimp's
Mandrill as a backend.

This app is inspired by `Djrill <https://github.com/brack3t/Djrill>`_,
the difference being that this app wraps the official mandrill python
api (rather than reimplementing a client) and is primarily focused on
supporting Mandrill Templates.

Dependencies
============

django-mandrill was created and tested with Django 1.4.3, please let
me know if you have success with it in older or newer versions.

This package depends on `mandrill` package (available on pypi).

Installing
==========

Eventually `pip install django-mandrill` will get you there.

Usage
=====

Add 'django_mandrill' to your INSTALLED_APPS.

Add the following configuration values in your settings:

::

    EMAIL_BACKEND = 'django_mandrill.mail.backends.mandrillbackend.EmailBackend'
    MANDRILL_API_KEY = '************************'



Sending Email
=============

django-mandrill should transparently work with Django's `send_mail()`,
`send_mass_mail()`, and `EmailMessage` objects with no change required
to the code.

Send an email based on a Mandrill Template:

::

    # send user a forgot password containing a nonce
    subject = 'Reset Password'
    user = some_user_object
    nonce = some_nonce_value

    template_content = []
    message = {
        'from_email': 'info@sample.com',
        'from_name': 'Robot',
        'subject': subject,
        'to': [{'email': user.email, 'name': user.get_full_name()},],
        'global_merge_vars': [
            {'name':'SUBJECT', 'content': subject},
            {'name':'USER_NAME', 'content': user.first_name},
            {'name':'NONCE', 'content': nonce},
            # etc etc
        ],
    }
    mail = MandrillTemplateMail("Password Reset", template_content, message)
    mail.send()


See mandrill package for information as to what the available message
options are.


Contributors
============

  * `Shu Zong Chen`_

.. CONTRIBUTORS

.. _`Shu Zong Chen`: http://freelancedreams.com/
