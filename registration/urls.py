from django.urls import path
from .views import EditarPerfilUsuarioView, CrearUsuarioView, RegistroHuespedView, PerfilUsuarioView, ListaUsuariosView, EditarUsuarioParaAdminView, deshabilitar_usuario, habilitar_usuario

urlpatterns = [
    path('profile/', PerfilUsuarioView.as_view(), name='perfil'),
    path('crear_usuario/', CrearUsuarioView.as_view(), name='crear_usuario'),
    path('registro_huesped/', RegistroHuespedView.as_view(), name='signup'),
    path('editarUsuario/<int:pk>/', EditarPerfilUsuarioView.as_view(), name='editar_perfil_usuario'),
    path('listaUsuarios/', ListaUsuariosView.as_view(), name='Lista_usuarios'),
    path('deshabilitarUsuario/<int:user_id>/', deshabilitar_usuario, name='deshabilitar_usuario'),
    path('habilitarUsuario/<int:user_id>/', habilitar_usuario, name='habilitar_usuario'),
    path('editar_usuario_admin/<int:pk>/', EditarUsuarioParaAdminView.as_view(), name='editar_usuario_admin'),
]

