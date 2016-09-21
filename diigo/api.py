from pydiigo import DiigoApi
from secrets import USERNAME, PASSWORD, APIKEY

diigo = DiigoApi(user=USERNAME, password=PASSWORD, apikey=APIKEY)

# Can post with created_at not being this moment

old_bookmark = diigo.bookmarks_find(filter='all', tags='asdf')

new_bookmark = diigo.bookmarks_find(filter='all', tags='asdf', users='jasalt')

# after annotation, tags added via script disappeared?
# updating tags seems to work fine

with_annotations = diigo.bookmarks_find(filter='all', tags='asdf', users='jasalt')
#'created_at': '2016/02/15 10:47:30 +0000',

new = diigo.bookmark_add(url='www.example.com', shared='yes', tags='asdf fdsa')

# update = diigo.bookmark_add(title='testing', description='foobar',url='www.example.com', shared='yes', tags='')


import ipdb; ipdb.set_trace()
