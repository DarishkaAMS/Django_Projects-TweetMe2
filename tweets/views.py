from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render

from .models import Tweet

# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "tweets/home.html", context={}, status=200)

def tweet_list_view(request, *args, **kwargs):
    """
    REST API VIEW
    Consume by JavaScript or Swift/Java/iOS/Android
    return json data
    """
    query_set = Tweet.objects.all()    
    tweets_list = [{"id": qs.id, "content": qs.content} for qs in query_set] 
    data = {
        "response": tweets_list
    }
    return JsonResponse(data)

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    """
    REST API VIEW
    Consume by JavaScript or Swift/Java/iOS/Android
    return json data
    """
    data = {
    "id": tweet_id,
    # "content": obj.content,
    # "image_path": obj.image.url
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = "Sorry. We have not found that page"
        status = 404
        # raise Http404

    return JsonResponse(data, status = status)
    # return HttpResponse(f"<h1> Hello {tweet_id} - {obj.content} </h1>")
