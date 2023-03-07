.. meta::
   :description:
      Free command line tool to download photos from Instagram.
      Scrapes public and private profiles, hashtags, stories, feeds,
      saved media, and their metadata, comments and captions.
      Written in Python.

.. title:: instainfo — Download Instagram Photos and Metadata

instainfo
===========

.. highlight:: none

**instainfo** is a tool to download pictures (or videos) along with
their captions and other metadata from Instagram.

.. include:: ../README.rst
   :start-after: badges-start
   :end-before: badges-end

With `Python <https://www.python.org/>`__ installed, do::

    $ pip3 install instainfo

    $ instainfo profile [profile ...]

See :ref:`install` for more options on how to install instainfo.

**instainfo**

- downloads **public and private profiles, hashtags, user stories,
  feeds and saved media**,

- downloads **comments, geotags and captions** of each post,

- automatically **detects profile name changes** and renames the target
  directory accordingly,

- allows **fine-grained customization** of filters and where to store
  downloaded media,

- automatically **resumes previously-interrupted** download iterations,

- is free `open source <https://github.com/instainfo/instainfo>`__
  software written in Python.

::

    instainfo [--comments] [--geotags]
                [--stories] [--highlights] [--tagged] [--igtv]
                [--login YOUR-USERNAME] [--fast-update]
                profile | "#hashtag" | %location_id |
                :stories | :feed | :saved

See :ref:`download-pictures-from-instagram` for a detailed introduction on how
to use instainfo to download pictures from Instagram.

instainfo Documentation
-------------------------

.. toctree::
   :maxdepth: 2

   installation
   basic-usage
   cli-options
   as-module
   codesnippets
   troubleshooting
   contributing

Contributing
------------

As an open source project, instainfo heavily depends on the contributions from
its community. See :ref:`contributing` for how you may help instainfo to
become an even greater tool.

Supporters
----------

.. include:: sponsors.rst
   :start-after: donations-start
   :end-before: donations-end

Disclaimer
----------

.. include:: ../README.rst
   :start-after: disclaimer-start
   :end-before: disclaimer-end

..
   * :ref:`genindex`
   * :ref:`modindex`
   * :ref:`search`

