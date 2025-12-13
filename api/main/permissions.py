from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAdminOrReadOnly(BasePermission):
    """
    Custom права доступа, позволяющие редактировать объекты только администраторам.
    Для любых запросов разрешены права только на чтение.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif request.method == "DELETE":
            return request.user.role == 'admin'
        return request.user and request.user.role in ['manager', 'support', 'admin']
    
    def has_object_permission(self, request, view, obj):
        
        return super().has_object_permission(request, view, obj)
    