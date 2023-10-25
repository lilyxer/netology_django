from rest_framework import permissions
  

class IsOwnerOrReadOnly(permissions.BasePermission):
    """Ограничение для владельца поста. Вдладелец и админ имеют права,
    все остальные могут только читать
    """
    def has_object_permission(self, request, view, obj):            # уровень объекта/1 запись
        if request in permissions.SAFE_METHODS:
            return True
        return obj.creator == request.user or request.user.is_staff