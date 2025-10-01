from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <h1>Welcome to ALX Project Nexus Backend 🚀</h1>
        <p>Here are some available routes:</p>
        <ul>
            <li><a href="/admin/">Admin Panel</a> (login with your admin username & password)</li>
        </ul>
    """)