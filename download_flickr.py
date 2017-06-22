from flickrapi import FlickrAPI


class Flickr:
    FLICKR_PUBLIC = '3ca61596336d9f3fec08b403f6967b76'
    FLICKR_SECRET = 'bed674e575a17080'
    extras = 'url_q,url_o'

    def __init__(self):
        self.flickr = FlickrAPI(self.FLICKR_PUBLIC, self.FLICKR_SECRET, format='parsed-json')

    def loadImageData(self, keyword):
        return self.flickr.photos.search(text=keyword, per_page=100, extras=self.extras)
