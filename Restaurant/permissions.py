from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission to only allow admin users to edit objects.
    Read-only permissions are allowed for any request.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        
        return (
            request.user and 
            request.user.is_authenticated and
            request.user.groups.filter(name='Manager').exists()
        )
        
