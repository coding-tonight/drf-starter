from rest_framework.views import APIView


class LoginApiView(APIView):
    permission_classes = []
    authentication_classes = []
    
    def post(self, request, format=None):
        pass