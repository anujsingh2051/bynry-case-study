from django.shortcuts import render, redirect
from .forms import ServiceRequestForm
from .models import ServiceRequest
from django.contrib.auth.decorators import login_required
def home(request):
    return render(request, 'home.html')
@login_required  # Ensure that the user is logged in before they can submit a request
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user  # Associate the request with the logged-in user
            service_request.save()
            return redirect('view_requests')  # Redirect to the view_requests page
    else:
        form = ServiceRequestForm()  # Create a new form instance if the request method is not POST

    return render(request, 'submit_request.html', {'form': form})  # Render the submit_request template with the form


@login_required  # Ensure that the user is logged in to view their requests
def view_requests(request):
    requests = ServiceRequest.objects.filter(user=request.user)  # Filter requests for the logged-in user
    return render(request, 'view_requests.html', {'requests': requests})  # Render the view_requests template with the requests
