from rest_framework import viewsets
from main.models.user import User
from main.seriallizers.user import UserSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    search_fields = '__all__'
    lookup_field = 'user_id' 