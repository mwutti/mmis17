from flickrapi import FlickrAPI
import keras as keras
import tensorflow

FLICKR_PUBLIC = '3ca61596336d9f3fec08b403f6967b76'
FLICKR_SECRET = 'bed674e575a17080'

flickr = FlickrAPI(FLICKR_PUBLIC, FLICKR_SECRET, format='parsed-json')
extras='url_sq,url_t,url_s,url_q,url_m,url_n,url_z,url_c,url_l,url_o'
cats = flickr.photos.search(text='kitten', per_page=5, extras=extras)
photos = cats['photos']
from pprint import pprint
pprint(photos)
