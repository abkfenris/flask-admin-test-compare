from . import db
from geoalchemy2 import Geometry
from geoalchemy2.shape import to_shape
from sqlalchemy import func

class POI(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(40))
	point = db.Column(Geometry("POINT", srid=926919))
	
	#def point_shape(self):
	#	return to_shape(self.point)
	#
	#def point_shape_web(self):
	#	return to_shape(db.session.scalar(self.point.ST_Transform(4326)))