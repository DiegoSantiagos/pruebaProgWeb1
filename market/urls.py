from django.urls import path
from . import views

urlpatterns = [
    # path('', views.menu, name='menu'),
    path('index', views.index, name='index'),
    path('', views.index, name='index'),
    path('listarProductos', views.listarProductos, name='listarProductos'),
    path('listarCarrito', views.listarCarrito, name='listarCarrito'),
    path('listarCategoria', views.listarCategoria, name='listarCategoria'),
    path('anadiProductoForm', views.anadirProductoForm, name='anadirProductoForm'),
    path('anadirCategoriaForm', views.anadirCategoriaForm, name='anadirCategoriaForm'),
    path('anadirCarrito/<int:pk>', views.anadirCarrito, name='anadirCarrito'),
    # path('anadirCarrito/<int:pk>/<int:total>/', views.anadirCarrito, name='anadirCarrito'),
    path('buscarCategoria/<int:pk>', views.buscarCategoria, name='buscarCategoria'),
    path('editarProducto/<int:pk>', views.editarProducto, name='editarProducto'),
    path('eliminarProducto/<int:pk>', views.eliminarProducto, name='eliminarProducto'),
    path('eliminarCategoria/<int:pk>', views.eliminarCategoria, name='eliminarCategoria'),
    path('eliminarCarrito/<int:pk>', views.eliminarCarrito, name='eliminarCarrito'),
    path('editarCategoria/<int:pk>', views.editarCategoria, name='editarCategoria'),
    path('verProducto/<int:pk>', views.verProducto, name='verProducto'),
    path('registrar/', views.registro_usuario, name="registrar"),
    path('actualizarCarrito/<int:pk>', views.actualizarCarrito, name='actualizarCarrito'),
]
