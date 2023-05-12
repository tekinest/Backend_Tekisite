from rest_framework.permissions import BasePermission, SAFE_METHODS

# class IsOwnerOrReadOnly(BasePermission):
#     message = 'You must be the owner of this object.'
#     my_safe_method = [ 'HEAD', 'GET', 'OPTIONS', 'POST']
#     def has_object_permission(self, request, view, obj):
#         # member = Membership.objects.get(user=request.user)
#         # member.is_active
#         if request.method in self.my_safe_method:
#             return True
#         return obj.user == request.user
    



class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission to only allow owners of an object to retrieve it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the object.
        return obj.owner == request.user