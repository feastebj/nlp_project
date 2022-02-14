from django.shortcuts import render
import webnlp.sentiment_analysis as sent

# Create your views here.

def home(request): 
	return render(request,"home.html",{})

def regex(request):
	import re
	if request.method=="POST":
		text_body = request.POST['regexform']
		print(text_body)

		sentiment_score, tokens = sent.sentiwordnet_analyze(text_body)
		
		context = {
		            'toks': tokens,
					'final_rating': sentiment_score,
		        }
		return render(request, 'regex.html', context)
