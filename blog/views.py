from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView, FormView
from zinnia.models import Entry, Category
from zinnia.managers import PUBLISHED
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from forms import NewsletterForm

# Create your views here.

class BlogListView(ListView):
	model = Entry
	template_name = 'home.html'
	context_object_name = "entry_list"
	paginate_by = 8
	view_link = 'Blog'
	show_menu = True

	def get_queryset(self):
		super(BlogListView, self).get_queryset()
		category = self.kwargs.get('category', '')

		if category != '':
			category = get_object_or_404(Category, slug=category)
			options = Q(categories=category)
			self.category = category.title
			if category.parent != None:
				self.dtype = category.parent.slug
			else:
				self.dtype = category.slug
		else:
			options = Q()
			self.dtype = 'all'

			self.category = ''

		return Entry.objects.filter(options).filter(status=PUBLISHED)

	def get_context_data(self, **kwargs):
		context = super(BlogListView, self).get_context_data(**kwargs)
		context['categories'] = Category.objects.all()
		context['form'] = NewsletterForm()
		context['recent'] = Entry.objects.filter(status=PUBLISHED).order_by('-creation_date')[:8]

	    # try:
	    #     m = HomeMetaTags.objects.get(Q(location='B'))
	    #     context['meta_title'] = m.meta_title
	    #     context['meta_description'] = m.meta_description
	    #     context['meta_keywords'] = m.meta_keyword
	    # except HomeMetaTags.DoesNotExist:
	    #     context['meta_title'] = None
	    #     context['meta_description'] = None
	    #     context['meta_keywords'] = None
		return context

class PostView(DetailView):
    model = Entry
    template_name = "post.html"
    view_link = 'Post'
    def get_queryset(self):
        return Entry.objects.filter(slug=self.kwargs.get('slug')).filter(status=PUBLISHED)

    def get_context_data(self, **kwargs):
		context = super(PostView, self).get_context_data(**kwargs)
		context['categories'] = Category.objects.all()
		context['form'] = NewsletterForm()
		context['recent'] = Entry.objects.filter(status=PUBLISHED).order_by('-creation_date')[:8]

		return context