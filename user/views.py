from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.exceptions import TokenError
from django.contrib.auth.hashers import check_password
from .models import MyCustomUser
from .serializers import UserSerializer
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from book_for_sell.models import BookForSell
from book_for_sell.serializers import BookForSellserializer
from book_for_fund.models import BookForFund
from book_for_fund.serializers import BoookForFundSerializer
from book_for_lend.models import BookForLend
from book_for_lend.serializers import BookForLendSerializer


def send_welcome_email(user):
    send_mail(
        subject='Welcome to BoiBondhu!',
        message=f'''
Hi {user.first_name},

Welcome to BoiBondhu! Your account has been created successfully.

Email: {user.email}

Happy reading!
— BoiBondhu Team
        ''',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        fail_silently=False,
    )


def get_tokens_for_user(user):
    refresh = RefreshToken()
    refresh['user_id'] = user.id
    refresh['email']   = user.email
    return {
        'refresh': str(refresh),
        'access' : str(refresh.access_token),
    }

def get_user_from_token(request):
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return None
    token     = AccessToken(auth_header.split(' ')[1])
    user_id   = token['user_id']
    return MyCustomUser.objects.get(id=user_id)


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            send_welcome_email(user)
            return Response(
                {'message': 'User created successfully'},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        email    = request.data.get('email')
        password = request.data.get('password')

        try:
            user = MyCustomUser.objects.get(email=email)
        except MyCustomUser.DoesNotExist:
            return Response(
                {'error': 'Invalid credentials'},
                status=status.HTTP_401_UNAUTHORIZED
            )

        if not check_password(password, user.password):
            return Response(
                {'error': 'Invalid credentials'},
                status=status.HTTP_401_UNAUTHORIZED
            )

        return Response({**get_tokens_for_user(user),'username':user.first_name}, status=status.HTTP_200_OK)


class ProfileView(APIView):
    def get(self, request):
        try:
            user = get_user_from_token(request)
            if not user:
                raise Exception
        except Exception:
            return Response(
                {'error': 'Unauthorized'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TokenRefreshView(APIView):
    def post(self, request):
        refresh_token = request.data.get('refresh')
        if not refresh_token:
            return Response(
                {'error': 'Refresh token required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            refresh = RefreshToken(refresh_token)
            return Response(
                {'access': str(refresh.access_token)},
                status=status.HTTP_200_OK
            )
        except TokenError:
            return Response(
                {'error': 'Invalid or expired token'},
                status=status.HTTP_401_UNAUTHORIZED
            )
class DashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        sell_books = BookForSell.objects.filter(seller=user)
        fund_books = BookForFund.objects.filter(donor=user)
        lend_books = BookForLend.objects.filter(lender=user)

        return Response({
            'user'      : UserSerializer(user).data,
            'sell_books': BookForSellserializer(sell_books, many=True, context={'request': request}).data,
            'fund_books': BoookForFundSerializer(fund_books, many=True, context={'request': request}).data,
            'lend_books': BookForLendSerializer(lend_books, many=True, context={'request': request}).data,
        })

    def patch(self, request):
        user       = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

