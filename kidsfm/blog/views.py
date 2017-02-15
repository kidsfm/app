from django.http		import HttpResponse
from django.template	import loader


def Index(request):
	"""
	Article index recheale from /blog/ URL
	"""
	template 	= loader.get_template('blog/index.html')
	context 	= {}
	return HttpResponse(template.render(context,request))


def Article(request, article_slug):
	'''
	Single article index recheale from /blog/<article-slug> URL
	'''
	template 	= loader.get_template('blog/post.html')
	context 	= {}
	return HttpResponse(template.render(context,request))



	