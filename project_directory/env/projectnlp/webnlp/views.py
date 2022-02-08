from django.shortcuts import render

# Create your views here.

def home(request): 
	return render(request,"home.html",{})

def regex(request):
	import re
	if request.method=="POST":
		phonepattern = r'\d{3}-\d{3}-\d{4}'
		regex_area=request.POST['regexform']
		regex_phone=re.findall(phonepattern,regex_area)
		return render(request, "regex.html",{'phone':regex_phone})
	else:
		return render(request,"regex.html",{})

def lemma(request):
	import nltk
	nltk.download('punkt')
	nltk.download('wordnet')
	nltk.download('omw-1.4')
	from nltk.stem import WordNetLemmatizer
	wordnet_lemmatizer = WordNetLemmatizer()
	if request.method=="POST":
		lemma_area = request.POST['lemmaform']
		tokenization = nltk.word_tokenize(lemma_area)
		tokens = [i for i in tokenization]
		lemma_list = [wordnet_lemmatizer.lemmatize(i) for i in tokens]
		lemmas = [i for i in lemma_list]
		return render(request,"lemma.html",{'unprocessed':tokens,'lemmatized':lemmas})
	else:
		return render(request,"home.html",{})

def pos(request):
	return render(request,"pos.html",{})

def ner(request):
	return render(request,"ner.html",{})