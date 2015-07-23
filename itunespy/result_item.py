#!/usr/bin/python
# Made with <3 by Fran González (@spaceisstrange)
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# You should have received a
#  copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>

class ResultItem(object):
    def __init__(self, json):
        self.artist_name = json['artistName']
        self.artist_link_url = json['artistLinkUrl']
        self.artist_id = json['artistId']
        self.artist_genre_name = json['primaryGenreName']
        self.artist_radio_url = json['radioStationUrl']

        if 'primaryGenreId' in json:
            self.artist_genre_id = json['primaryGenreId']

        if 'amgArtistId' in json:
            self.artist_amg_id = json['amgArtistId']

        if 'artistViewUrl' in json:
            self.artist_view_url = json['artistViewUrl']

        if 'trackName' in json:
            self.track_name = json['trackName']

        if 'trackCensoredName' in json:
            self.track_censored_name = json['trackCensoredName']

        if 'trackViewUrl' in json:
            self.track_view_url = json['trackViewUrl']

        if 'trackCount' in json:
            self.track_count = json['trackCount']

        if 'trackNumber' in json:
            self.track_number = json['trackNumber']

        if 'previewUrl' in json:
            self.preview_url = json['previewUrl']

        if 'artworkUrl30' in json:
            self.artwork_url_30 = json['artworkUrl30']

        if 'artworkUrl60' in json:
            self.artwork_url_60 = json['artworkUrl60']

        if 'artworkUrl100' in json:
            self.artwork_url_100 = json['artworkUrl100']

        if 'collectionName' in json:
            self.collection_name = json['collectionName']

        if 'collectionCensoredName' in json:
            self.collection_censored_name = json['collectionCensoredName']

        if 'collectionViewUrl' in json:
            self.collection_view_url = json['collectionViewUrl']

        if 'collectionPrice' in json:
            self.collection_price = json['collectionPrice']

        if 'trackPrice' in json:
            self.track_price = json['trackPrice']

        if 'collectionHdPrice' in json:
            self.collection_hd_price = json['collectionHdPrice']

        if 'trackHdPrice' in json:
            self.track_hd_price = json['trackHdPrice']

        if 'releaseDate' in json:
            self.release_date = json['releaseDate']

        if 'collectionExplicitness' in json:
            self.collection_explicitness = json['collectionExplicitness']

        if 'trackExplicitness' in json:
            self.track_explicitness = json['trackExplicitness']

        if 'trackTimeMillis' in json:
            self.track_time = json['trackTimeMillis']

        if 'discCount' in json:
            self.disc_count = json['discCount']

        if 'discNumber' in json:
            self.disc_number = json['discNumber']

        if 'country' in json:
            self.country = json['country']

        if 'currency' in json:
            self.currency = json['currency']

        if 'copyright' in json:
            self.copyright = json['copyright']

        if 'contentAdvisoryRating' in json:
            self.content_advisory_rating = json['contentAdvisoryRating']

        if 'shortDescription' in json:
            self.short_description = json['shortDescription']

        if 'longDescription' in json:
            self.long_description = json['longDescription']

        if 'isStreamable' in json:
            self.is_streamable = json['isStreamable']
