from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
import webnlp.sentiment_analysis as sent

# Create your views here.

def home(request): 
	return render(request,"home.html",{})

@ensure_csrf_cookie
def regex(request):
	import re
	if request.method=="POST":
		text_body = request.POST['regexform']
		print(text_body)

		sentiment_score, tokens = sent.sentiwordnet_analyze(text_body)
		color = [sent.get_sentiment_color(tok[1]) for tok in tokens]
		tokens = [(tokens[i][0], tokens[i][1], color[i]) for i in range(len(tokens))]

		
		context = {
		            'toks': tokens,
					'final_rating': sentiment_score,
		        }
		return render(request, 'regex.html', context)
