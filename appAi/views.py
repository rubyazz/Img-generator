from django.shortcuts import render
import openai 
from django.http import HttpResponse, JsonResponse	

# put here your own api from openai 
# https://platform.openai.com/docs/api-reference/introduction
openai.api_key = ""

def generate_images(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        n = int(request.POST.get('n'))
        size = request.POST.get('size')
        image_resp = openai.Image.create(prompt=prompt, n=n, size=size)
        urls = []
        for data in image_resp["data"]:
            url = data["url"]
            urls.append(url)
        print(f"Generated image URLs: {urls}")
        context = {'urls': urls}
        return render(request, "ai.html", context)
    else:
        return render(request, "ai.html")




def home(request):
	return render(request, "home.html")

def about(request):
	return render(request, "about.html")

def contact(request):
	return render(request, "contact.html")

def docs(request):
    return render(request, "docs.html")