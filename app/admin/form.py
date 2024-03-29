from flask.ext.admin.model.form import converts
from flask.ext.admin.contrib.sqla.form import AdminModelConverter as SQLAAdminConverter
from .fields import GeoJSONField


class AdminModelConverter(SQLAAdminConverter):
    @converts('Geometry')
    def convert_geom(self, column, field_args, **extra):
        field_args['geometry_type'] = column.type.geometry_type
        field_args['srid'] = column.type.srid
        return GeoJSONField(**field_args)
