from django.shortcuts import render

# Create your views here.

def home(request): 
	return render(request,"home.html",{})

def regex(request):
	import re
	if request.method=="POST":
		list1 = ["The", "House", "of", "Representatives", "shall", "be", "composed", "of", "Members", "chosen", "every", "second", "Year", "by", "the", "People", "of", "the", "several", "States", "and", "the", "Electors", "in", "each", "State", "shall", "have", "the", "Qualifications", "requisite", "for", "Electors"]
		list2 = [0.2,0.5,0.1,0.9,0.6,0.1,0.5,0.1,0.6,0.4,0.3,0.6,0.7,0.2,0.3,0.8,0.2,0.1,0.2,0.5,0.7,0.3,0.2,0.6,0.2,0.4,0.6,0.7,0.4,0.8,0.9,0.2,0.6]
		mylist = zip(list1, list2)
		context = {
		            'mylist': mylist,
		        }
		return render(request, 'regex.html', context)
