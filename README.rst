########
The Task
########


Build web spider using Python with the help of Scrapy. The spider should pull
all products from pre-defined category of the site.


Stack:
======

    * python2 or python3
    * Scrapy framework


Requirements
============

    * Scraping target - https://www.samsclub.com
    * Category - Energy Drinks - https://www.samsclub.com/b/energy-drinks/1504
    * Needed information:
       * Title
       * Price
       * Images
       * Item Number (#)
       * Description
    * Clean the price from letters and symbols and format it to 0.00 format
    * Get all the products from the category


-----


Assumptions
~~~~~~~~~~~

It's not clear if you want the urls of product's images or the images themselves. I assume we want the images downloaded to our pc. It's not clear if you want all products from the target category or only the available ones. For example this product: https://www.samsclub.com/p/red-bull-energy-drink-12-pk-16-oz-cans/prod711948?xid=plp_product_1_46 It's in 'Select club' and the price for this items isn't available. I assume we want all available info, and if the price isn't available we're going to put 'not available'.

-----

###########
My Solution
###########

My solution using only Scrapy is available on OnlyScrapy branch, but it
downloads only one image per product. In the master branch I'm using
scrapy-splash which allows me to get all the images from the product's gallery
with expense of loosing speed waiting for the JS to load.

How To Run
==========

1. Git clone the repo
2. cd REPO_DIR and install the dependencies (pipenv install)
3. Setup splash

   .. code-block:: bash

    docker pull scrapinghub/splash
    docker run -it -p 8050:8050 scrapinghub/splash

4. Activate the virutalenv (pipenv shell)
5. Setup *user_settings.py* if you want to change defaults.

   .. code-block:: bash

    cd REPO_DIR/SamsClub/SamsClub/user_settings.py

Settings in *user_settings.py*:

    * category to scrape (put category url from the website)
    * next page url (url received when you click next in the selected category)
    * images store location (where to store downloaded images)

6. Run from REPO_DIR/SamsClub direcory with:

   .. code-block:: bash

       scrapy crawl category_spider -L INFO -o output.jl

7. Analyse the results in the newley created JSON file output.jl, images are in
   newley created imgs folder in the same directory.
