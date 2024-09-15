from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied

def role_required(*roles):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')  # Redirect to login page if user is not authenticated
            
            # Check if the user's role is in the list of allowed roles
            if request.user.user_type not in roles:
                raise PermissionDenied  # Raise error if user does not have the required role
            
            return view_func(request, *args, **kwargs)  # Call the original view function
        
        return _wrapped_view
    return decorator
