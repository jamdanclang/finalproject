from django.db import models

class Campus(models.Model):
    name = models.CharField(max_length=255)
    name_slug = models.SlugField()
    def __unicode__(self):
        return self.name
#    def get_absolute_url(self):
#        return "/reports/%s/" % self.name_slug


class Building(models.Model):
    name = models.CharField(max_length=255)
    name_slug = models.SlugField()
    def __unicode__(self):
        return self.name
    def get_absolute_url(self):
        return "/reports/%s/" % self.name_slug  


#class Building(models.Model):
#    name = models.CharField(max_length=255)
#    name_slug = models.SlugField()
#    campus = models.ForeignKey(Campus)
    
#    def __unicode__(self):
#        return self.name
#    def get_absolute_url(self):
#        return "/reports/%s/%s/" % (self.campus.name_slug, self.name_slug)



class Reports(models.Model):
    building = models.ForeignKey(Building)
    date = models.DateField()
    access = models.IntegerField()


