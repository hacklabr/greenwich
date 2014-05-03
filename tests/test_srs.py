import unittest
from osgeo import osr

from greenwich.srs import SpatialReference


class SpatialReferenceTestCase(unittest.TestCase):

    def test_wkt(self):
        sref = SpatialReference(osr.SRS_WKT_WGS84)
        self.assertEqual(sref.wkt, osr.SRS_WKT_WGS84)

    def test_epsg(self):
        epsg_id = 3310
        from_epsg = SpatialReference(epsg_id)
        self.assertEqual(from_epsg.srid, epsg_id)

    def test_proj4(self):
        p4 = SpatialReference(2805).ExportToProj4()
        from_proj4 = SpatialReference(p4)
        self.assertEqual(from_proj4.proj4, p4)

    def test_equality(self):
        self.assertEqual(SpatialReference(3857), SpatialReference(3857))
        self.assertNotEqual(SpatialReference(4326), SpatialReference(3857))