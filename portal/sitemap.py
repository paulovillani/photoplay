from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
import datetime

class PortalSitemap(Sitemap):
	changefreq = "weekly"
	priority = 0.5

	def __init__(self, names):
	    self.names = names

	def items(self):
	    return self.names

	def changefreq(self, obj):
	    return 'weekly'

	def lastmod(self, obj):
	    return datetime.datetime.now()

	def location(self, obj):
	    return reverse(obj)