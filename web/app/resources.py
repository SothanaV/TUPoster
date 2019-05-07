from import_export import resources
from .models import Score

class ScoreResource(resources.ModelResource):
  class Meta:
    model = Score