"""
georssy.decoder
~~~~~~~~~~~~
TODO
:copyright: (c) 2017 by Sergio Ferraresi.
:license: Apache2, see LICENSE for more details.
"""

import logging
import re

from .gml.gml_decoder import gml_decoder
from .simple.simple_decoder import simple_decoder

logger = logging.getLogger( __name__ )

class decoder( object ):
    '''
    GeoRss Parser.
    GeoRSS-Simple is meant as a very lightweight format that developers and users can quickly and easily add to their existing feeds with little effort. It supports basic geometries (point, line, box, polygon) and covers the typical use cases when encoding locations.
    GeoRSS GML is a formal GML Application Profile, and supports a greater range of features, notably coordinate reference systems other than WGS-84 latitude/longitude.

    Some publishers and users may prefer to separate lat/long pairs by a comma rather than whitespace. This is permissible in Simple; GeoRSS parsers should just treat commas as whitespace.

    See http://www.georss.org/ for more information.
    '''

    def __init__( self, parent_node = None, polygons_over_boxes = False ):
        '''
        Constructor
        '''

        if parent_node is None:
            msg = 'GeoRSS parent node NOT valid'
            logger.error( msg )

            raise ValueError( msg )

        logger.debug( 'georssy parameters:' )
        logger.debug( '  Polygons over Boxes: "%s"' % ( 'Y' if polygons_over_boxes else 'N' ) )

        sd = simple_decoder( parent_node = parent_node, polygons_over_boxes = polygons_over_boxes )
        gd = gml_decoder( parent_node = parent_node, polygons_over_boxes = polygons_over_boxes )

        self.point_list = []
        if sd.point_list:
            self.point_list.extend( sd.point_list )
        if gd.point_list:
            self.point_list.extend( gd.point_list )
        self.line_list = []
        if sd.line_list:
            self.line_list.extend( sd.line_list )
        if gd.line_list:
            self.line_list.extend( gd.line_list )
        self.polygon_list = []
        if sd.polygon_list:
            self.polygon_list.extend( sd.polygon_list )
        if gd.polygon_list:
            self.polygon_list.extend( gd.polygon_list )
        self.feature_type_list = sd.feature_type_list
        self.feature_name_list = sd.feature_name_list
        self.relationship_list = sd.relationship_list
        self.elevation_list = sd.elevation_list
        self.floor_list = sd.floor_list
        self.radius_list = sd.radius_list

        logger.debug( 'georssy decoded elements:' )
        if self.point_list:
            logger.debug( '  Points: "%s"' % str( self.point_list ) )
        if self.line_list:
            logger.debug( '  Lines: "%s"' % str( self.line_list ) )
        if self.polygon_list:
            logger.debug( '  Polygons: "%s"' % str( self.polygon_list ) )
        if self.feature_type_list:
            logger.debug( '  Feature Types: "%s"' % str( self.feature_type_list ) )
        if self.feature_name_list:
            logger.debug( '  Feature Names: "%s"' % str( self.feature_name_list ) )
        if self.relationship_list:
            logger.debug( '  Relationships: "%s"' % str( self.relationship_list ) )
        if self.elevation_list:
            logger.debug( '  Elevations: "%s"' % str( self.elevation_list ) )
        if self.floor_list:
            logger.debug( '  Floors: "%s"' % str( self.floor_list ) )
