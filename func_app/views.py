from django.http import HttpResponse
import hashtags


# Create your views here.

def index(request, text):
    return HttpResponse(f"В тексте {text} хэштеги это {hashtags.extract_hashtags(text)}")