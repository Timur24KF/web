from django.urls import path, include
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Showroom API",
        default_version='v1',
        description="Test description",
    ),
    public=True,
)


urlpatterns = [
    path("posts/user/<str:username>", PostUserAPIView.as_view()),
    path("posts/category/<int:category>", PostCategoryAPIView.as_view()),
    path("posts", PostsAPIView.as_view()), 
    path("post/<int:pk>/comments", PostCommentsAPIView.as_view()), 
    path("favposts", FavPostsAPIView.as_view()),
    path("post/<int:pk>", PostDetailAPIView.as_view()),
    path("post/<int:pk>/like", LikeCreateAPIView.as_view()),
    path("post/<int:pk>/deletelike", LikeDeleteAPIView.as_view()),
    path("profile/change", UserUpdateAPIView.as_view()),
    path("profile/change-password", ChangePasswordAPIView.as_view()),
    path("register", CreateUserAPIView.as_view()),
    


    path("auth", include("rest_framework.urls")),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
