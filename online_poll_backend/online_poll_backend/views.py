from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <h1>Welcome to ALX Project Nexus Backend 🚀</h1>
        <p>Available routes:</p>
        <ul>
            <li><a href="/admin/">Admin Panel</a> 
                (login with username: <b>admin</b>, password: <b>jordi1993</b>)
            </li>
            
            <h3>🔑 Authentication</h3>
            <li><a href="/api/auth/register/">User Registration</a></li>
            <li><a href="/api/auth/login/">User Login (JWT)</a></li>
            <li><a href="/api/auth/refresh/">Refresh Token</a></li>
            <li><a href="/api/auth/logout/">Logout</a></li>
            
            <h3>📊 Polls</h3>
            <li><a href="/api/polls/">Polls (CRUD via API)</a></li>
            <li><a href="/api/vote/">Cast Vote</a></li>
            
            <h3>📖 API Docs</h3>
            <li><a href="/api/docs/">Swagger UI</a></li>
        </ul>
    """)