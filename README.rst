########
The Task
########


The task:
=========

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

Assumptions
~~~~~~~~~~~
It's not clear if you want the urls of Product's Images or the images
themselves. I assume we want the images downloaded to our pc.

It's not clear if you want all products from the target category or only the
available ones. For example this product:
https://www.samsclub.com/p/red-bull-energy-drink-12-pk-16-oz-cans/prod711948?xid=plp_product_1_46
It's in 'Select club' and the price for this items isn't available. I assume we
want all available info, and if the price isn't available we're going to put
'not available'.

###########
My Solution
###########

I couldn't find solution of the task with only Scrapy. 
