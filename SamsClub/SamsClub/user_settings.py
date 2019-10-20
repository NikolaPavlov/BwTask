import os


CATEGORY_TO_SCRAP_URL = 'https://www.samsclub.com/b/energy-drinks/1504'

# the url received after click next button (paggination)
NEXT_PAGE_URL = 'https://www.samsclub.com/b/energy-drinks/1504?clubId=undefined&offset=48&searchCategoryId=1504&selectedFilter=all&sortKey=relevance&sortOrder=1'

# directory to store downloaded imgs
IMAGES_STORE = os.getcwd() + '/imgs'

# wait for JS setting
SPLASH_WAIT_TIME = 2

# not available msg if target is not present
NOT_AVAILABLE_MSG = 'not available'
