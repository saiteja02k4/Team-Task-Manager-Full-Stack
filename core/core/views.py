from django.http import HttpResponse

def home(request):
    return HttpResponse("""
    <h1>Smart Invitation 🚀</h1>
    <p>Backend is running successfully</p>
    """)