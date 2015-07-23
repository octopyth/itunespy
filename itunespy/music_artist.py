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

import itunespy
from itunespy import result_item

class MusicArtist(result_item.ResultItem):
    def __init__(self, json):
        result_item.ResultItem.__init__(self, json)

        if 'amgArtistId' in json:
            self.artist_amg_id = json['amgArtistId']
        else:
            self.artist_amg_id = None

    def get_albums(self):
        return itunespy.lookup(id=self.artist_id, entity=itunespy.entities['album'])[1:]

    # For debugging purposes
    def print_info(self):
        print(self.artist_name)
        print(self.artist_link_url)
        print(self.artist_id)
        print(self.artist_amg_id)
        print(self.artist_genre_name)
        print(self.artist_genre_id)
        print(self.artist_link_url)
        print()
