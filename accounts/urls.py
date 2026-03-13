from django.urls import path
from accounts import views

urlpatterns = [
    path('api/utilisateurs/', views.ListeUtilisateursAPI.as_view(), name='liste_utilisateurs'),
    path('api/utilisateurs/<int:pk>/', views.DetailUtilisateurAPI.as_view(), name='detail_utilisateur'),
    path('api/utilisateurs/create/', views.CreateUtilisateurAPI.as_view(), name='create_utilisateur'),
    path('api/utilisateurs/<int:pk>/update/', views.UpdateUtilisateurAPI.as_view(), name='update_utilisateur'),
    path('api/utilisateurs/<int:pk>/delete/', views.DeleteUtilisateurAPI.as_view(), name='delete_utilisateur'),
    path('api/utilisateurs/<int:pk>/toggle-active/', views.ToggleActiveUtilisateurAPI.as_view(), name='toggle_active_utilisateur'),
]