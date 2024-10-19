from django.shortcuts import render
from django.core.paginator import Paginator
from app.models import ClubInfo, Activity
from app.forms import LoginForm

# get infor of club
try:
    club_infor = ClubInfo.objects.first()
except ClubInfo.DoesNotExist:
    club_infor = None

# Create your views here.
def home(request):
    favourite_posts = [
        {
            'cards': [
                {'image_url': 'https://images.unsplash.com/photo-1719937206168-f4c829152b91?q=80&w=1770&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', 'title': 'Card Title 1', 'description': 'Some quick example text to build on the card title.'},
                {'image_url': 'https://images.unsplash.com/photo-1719937206168-f4c829152b91?q=80&w=1770&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', 'title': 'Card Title 2', 'description': 'Some quick example text to build on the card title.'},
                {'image_url': 'https://images.unsplash.com/photo-1719937206168-f4c829152b91?q=80&w=1770&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', 'title': 'Card Title 3', 'description': 'Some quick example text to build on the card title.'},
            ]
        },
        {
            'cards': [
                {'image_url': 'https://images.unsplash.com/photo-1719937206168-f4c829152b91?q=80&w=1770&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', 'title': 'Card Title 4', 'description': 'Some quick example text to build on the card title.'},
                {'image_url': 'https://images.unsplash.com/photo-1719937206168-f4c829152b91?q=80&w=1770&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', 'title': 'Card Title 5', 'description': 'Some quick example text to build on the card title.'},
                {'image_url': 'https://images.unsplash.com/photo-1719937206168-f4c829152b91?q=80&w=1770&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', 'title': 'Card Title 6', 'description': 'Some quick example text to build on the card title.'},
            ]
        },
        # Add more posts as needed
    ]
    
    activities = [
        {
            'image_url': 'https://images.unsplash.com/photo-1498050108023-c5249f4df085?q=80&w=1772&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
            'title': 'Bay tùm lum giữa các vì sao',
            'description': 'Quay đều\nQuay đều\nQuay đều\nQuay đều\nQuay đều\nQuay đều\nQuay đều',
        },
        
        {
            'image_url': 'https://images.unsplash.com/photo-1498050108023-c5249f4df085?q=80&w=1772&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
            'title': 'Bay tùm lum giữa các vì sao',
            'description': 'Quay đều\nQuay đều\nQuay đều\nQuay đều\nQuay đều\nQuay đều\nQuay đều',
        },
        
        {
            'image_url': 'https://images.unsplash.com/photo-1498050108023-c5249f4df085?q=80&w=1772&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
            'title': 'Bay tùm lum giữa các vì sao',
            'description': 'Quay đều\nQuay đều\nQuay đều\nQuay đều\nQuay đều\nQuay đều\nQuay đều',
        },
        # Add more activities here...
    ]
    
    return render(request, 'base_pages/index.html', {'club_infor': club_infor, 'favourite_posts': favourite_posts, 'activities': activities})
    
        

def about(request):
    return render(request, 'base_pages/about.html', {'club_infor': club_infor})

def contact(request):
    return render(request, 'base_pages/contact.html', {'club_infor': club_infor})

def activity(request):
    activity_list = Activity.objects.all()
    paginator = Paginator(activity_list, 3)  # Show 3 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'base_pages/activity.html', {'club_infor': club_infor, 'page_obj': page_obj})

def activity_detail(request, activity_id):
    activity = Activity.objects.get(activity_id=activity_id)    
    return render(request, 'base_pages/activity_detail.html', {'activity': activity})


def login(request):
    form = LoginForm()
    if request.method == 'POST':
        pass
    else:
        return render(request, 'auth_pages/login.html', {'club_infor': club_infor, 'form': form})