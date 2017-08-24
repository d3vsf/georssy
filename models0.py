from __future__ import unicode_literals

from django.db import models

class EnvSettings( models.Model ):
    group = models.CharField( max_length = 100, primary_key = True )
    name  = models.CharField( max_length = 100, primary_key = True )
    value = models.CharField( max_length = 100 )
    type  = models.CharField( max_length = 100 )
    desc  = models.CharField( max_length = 200, null = True, blank = True )

    class Meta:
        db_table = u'settings'
