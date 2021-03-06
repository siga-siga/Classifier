from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys

#APIキーの情報

key = "0f99edef6341808756306de016a5eed0"
secret = "80ca5d3cf069e5b8"
wait_time = 1

#保存フォルダの指定
manname = sys.argv[1]
savedir = "./" + manname

flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
        text = manname,
        per_page = 400,
        media = 'photos',
        sort = 'relivance',
        safe_search = 1,
        extras = 'url_q, licence'
)
photos = result['photos']
#返り値を表示
#pprint(photos)

for i, photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filepath = savedir + '/' + photo['id'] + '.jpg'
    if os.path.exists(filepath): continue
    urlretrieve(url_q,filepath)
    time.sleep(wait_time)
