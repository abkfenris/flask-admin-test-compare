from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView as SQLAModelView

from .. import db
from ..models import POI

from . import form, typefmt

class ModelView(SQLAModelView):
    model_form_converter = form.AdminModelConverter
    column_type_formatters = typefmt.DEFAULT_FORMATTERS

class POIView(ModelView):
	pass

view = POIView(POI, db.session)

admin = Admin(name="flask-admin.contrib.geoa testing")
admin.add_view(view)