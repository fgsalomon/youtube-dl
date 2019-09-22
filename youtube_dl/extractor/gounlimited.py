from youtube_dl.extractor.common import InfoExtractor


class GounlimitedIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?gounlimited\.to/'
    # url https://gounlimited.to/embed-osq228uoqy7e.html  https://gounlimited.to/embed-ekxpxyw9wf86.html
    _TEST = {
        'url': 'https://gounlimited.to/embed-osq228uoqy7e.html',
        'md5': 'TODO: md5 sum of the first 10241 bytes of the video file (use --test)',
        'info_dict': {
            'id': '1',
            'ext': 'mp4',
            'title': 'No title',
            # TODO more properties, either as:
            # * A value
            # * MD5 checksum; start the string with md5:
            # * A regular expression; start the string with re:
            # * Any Python type (for example int or float)
        }
    }

    def _real_extract(self, url):

        webpage = self._download_webpage(url, video_id=None)

        video_id = self._html_search_regex(r'(preload\|mp4\|)(.+?)\|(.*?)(\|sources)', string=webpage, name='id', group=2)
        server = self._html_search_regex(r'(preload\|mp4\|)(.+?)\|(.*?)(\|sources)', string=webpage, name='id',
                                           group=3)
        title = "No title"
        video_url = "https://{}.gounlimited.to/{}/v.mp4".format(server, video_id)

        return {
            'id': "1",
            'title': title,
            'url': video_url
        }