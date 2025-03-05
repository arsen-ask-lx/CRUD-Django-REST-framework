from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

from .models import CRUD_model
from .serializers import CRUD_serializer
from .permissions import IsOwner


class CRUDView(viewsets.ModelViewSet):
    """
    ViewSet для управления задачами (CRUD):
    - GET (list)    /tasks/
    - получить список задач текущего пользователя
    - GET (retrieve)/tasks/{id}/      - получить задачу по ID
    - POST          /tasks/          - создать новую задачу (для авторизованных)
    - PUT/PATCH     /tasks/{id}/      - изменить задачу (только владелец)
    - DELETE        /tasks/{id}/      - удалить задачу (только владелец)
    Дополнительно:    - Фильтрация по статусу и дате выполнения (status, due_date)
    """
    serializer_class = CRUD_serializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'due_date']

    def get_queryset(self):
        """
           Возвращает задачи, принадлежащие только текущему авторизованному пользователю.
        """
        return CRUD_model.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
            При создании новой задачи автоматически назначает текущего пользователя владельцем.
        """
        serializer.save(user=self.request.user)

    def get_permissions(self):
        """
        Для операций update, partial_update и destroy
        требуется быть владельцем задачи (IsOwner).
        """
        if self.action in ['update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), IsOwner()]
        return [permissions.IsAuthenticated()]
