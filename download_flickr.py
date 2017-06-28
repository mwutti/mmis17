from flickrapi import FlickrAPI


class Flickr:
    FLICKR_PUBLIC = 'Enter your API Key'
    FLICKR_SECRET = 'Insert your API Secret'
    extras = 'url_q,url_o'

    def __init__(self):
        self.flickr = FlickrAPI(self.FLICKR_PUBLIC, self.FLICKR_SECRET, format='parsed-json')

    def loadImageData(self, keyword):
        return self.flickr.photos.search(text=keyword, per_page=100, extras=self.extras)
