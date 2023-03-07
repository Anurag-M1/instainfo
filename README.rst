.. image:: https://github.com/anurag-zzibzz/InstaInfo/master/docs/logo_heading.png

.. badges-start

|travis| |pypi| |pyversion| |license| |aur| |contributors| |downloads|

.. |travis| image:: https://img.shields.io/travis/instainfo/instainfo/master.svg
   :alt: Travis-CI Build Status
   :target: https://travis-ci.org/instainfo/instainfo

.. |pypi| image:: https://img.shields.io/pypi/v/instainfo.svg
   :alt: instainfo PyPI Project Page
   :target: https://pypi.org/project/instainfo/

.. |license| image:: https://img.shields.io/github/license/instainfo/instainfo.svg
   :alt: MIT License
   :target: https://github.com/instainfo/instainfo/blob/master/LICENSE

.. |pyversion| image:: https://img.shields.io/pypi/pyversions/instainfo.svg
   :alt: Supported Python Versions

.. |contributors| image:: https://img.shields.io/github/contributors/instainfo/instainfo.svg
   :alt: Contributor Count
   :target: https://github.com/anurag-zzibzz/InstaInfo

.. |aur| image:: https://img.shields.io/aur/version/instainfo.svg
   :alt: Arch User Repository Package
   :target: https://aur.archlinux.org/packages/instainfo/

.. |downloads| image:: https://pepy.tech/badge/instainfo/month
   :alt: PyPI Download Count
   :target: https://pepy.tech/project/instainfo

.. badges-end

::

    $ pip3 install instainfo

    $ instainfo profile [profile ...]

**instainfo**

- downloads **public and private profiles, hashtags, user stories,
  feeds and saved media**,

- downloads **comments, geotags and captions** of each post,

- automatically **detects profile name changes** and renames the target
  directory accordingly,

- allows **fine-grained customization** of filters and where to store
  downloaded media,

- automatically **resumes previously-interrupted** download iterations.

::

    instainfo [--comments] [--geotags]
                [--stories] [--highlights] [--tagged] [--igtv]
                [--login YOUR-USERNAME] [--fast-update]
                profile | "#hashtag" | :stories | :feed | :saved

`instainfo Documentation <https://instainfo.github.io/>`__


How to Automatically Download Pictures from Instagram
-----------------------------------------------------

To **download all pictures and videos of a profile**, as well as the
**profile picture**, do

::

    instainfo profile [profile ...]

where ``profile`` is the name of a profile you want to download. Instead
of only one profile, you may also specify a list of profiles.

To later **update your local copy** of that profiles, you may run

::

    instainfo --fast-update profile [profile ...]

If ``--fast-update`` is given, instainfo stops when arriving at the
first already-downloaded picture.

Alternatively, you can use ``--latest-stamps`` to have instainfo store
the time each profile was last downloaded and only download newer media:

::

    instainfo --latest-stamps -- profile [profile ...]

With this option it's possible to move or delete downloaded media and still keep
the archive updated.

When updating profiles, instainfo
automatically **detects profile name changes** and renames the target directory
accordingly.

instainfo can also be used to **download private profiles**. To do so,
invoke it with

::

    instainfo --login=your_username profile [profile ...]

When logging in, instainfo **stores the session cookies** in a file in your
temporary directory, which will be reused later the next time ``--login``
is given.  So you can download private profiles **non-interactively** when you
already have a valid session cookie file.

`instainfo Documentation <https://instainfo.github.io/basic-usage.html>`__

Contributing
------------

As an open source project, instainfo heavily depends on the contributions from
its community. See
`contributing <https://instainfo.github.io/contributing.html>`__
for how you may help instainfo to become an even greater tool.

Supporters
----------

.. current-sponsors-start

| instainfo is proudly sponsored by
|  `@anurag_zzibzz <https://github.com/anurag-zzibzz/InstaInfo>`__

See `Anurag' GitHub Sponsors <https://github.com/anurag-zzibzz/>`__ page for
how you can sponsor the development of instainfo!

.. current-sponsors-end

It is a pleasure for us to share our instainfo to the world, and we are proud
to have attracted such an active and motivating community, with so many users
who share their suggestions and ideas with us. Buying a community-sponsored beer
or coffee from time to time is very likely to further raise our passion for the
development of instainfo.

Disclaimer
----------

.. disclaimer-start

instainfo is in no way affiliated with, authorized, maintained or endorsed by Instagram or any of its affiliates or
subsidiaries. This is an independent and unofficial project. Use at your own risk.

instainfo is licensed under an MIT license. Refer to ``LICENSE`` file for more information.

.. disclaimer-end
