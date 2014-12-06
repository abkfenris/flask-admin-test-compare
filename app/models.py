from . import db
from geoalchemy2 import Geometry
from geoalchemy2.shape import to_shape
from sqlalchemy import func

class POI(db.Model):
	# Maine around Baxter
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(40))
	point = db.Column(Geometry("POINT", srid=926919))
	
	#def point_shape(self):
	#	return to_shape(self.point)
	#
	#def point_shape_web(self):
	#	return to_shape(db.session.scalar(self.point.ST_Transform(4326)))

class Line(db.Model):
	# New Hampshire
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(40))
	line = db.Column(Geometry("LINESTRING", srid=32010))

class Polygon(db.Model):
	# Western Maine
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(40))
	polygon = db.Column(Geometry("POLYGON", srid=2802))

class MultiPoint(db.Model):
	# Maine around Baxter
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(40))
	multipoint = db.Column(Geometry("MULTIPOINT", srid=926919))

class MultiLine(db.Model):
	# New Hampshire
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(40))
	multiline = db.Column(Geometry("MULTILINESTRING", srid=32010))

class MultiPolygon(db.Model):
	# Western Maine
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(40))
	multipolygon = db.Column(Geometry("MULTIPOLYGON", srid=2802))

class Collection(db.Model):
	# Web
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(40))
	collection = db.Column(Geometry("GEOMETRYCOLLECTION", srid=4326))