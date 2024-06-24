from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('index', views.index, name='index'),
    path('listarProductos', views.listarProductos, name='listarProductos'),
    path('listarCarrito', views.listarCarrito, name='listarCarrito'),
    path('listarCategoria', views.listarCategoria, name='listarCategoria'),
    path('anadiProductoForm', views.anadirProductoForm, name='anadirProductoForm'),
    path('anadirCategoriaForm', views.anadirCategoriaForm, name='anadirCategoriaForm'),
    path('anadirCarrito/<int:pk>', views.anadirCarrito, name='anadirCarrito'),
    path('buscarCategoria/<int:pk>', views.buscarCategoria, name='buscarCategoria'),
    path('editarProducto/<int:pk>', views.editarProducto, name='editarProducto'),
    path('eliminarProducto/<int:pk>', views.eliminarProducto, name='eliminarProducto'),
    path('eliminarCategoria/<int:pk>', views.eliminarCategoria, name='eliminarCategoria'),
    path('eliminarCarrito/<int:pk>', views.eliminarCarrito, name='eliminarCarrito'),
    path('editarCategoria/<int:pk>', views.editarCategoria, name='editarCategoria'),
    # path('editarCarrito/<int:pk>', views.editarCarrito, name='editarCarrito'),
    # path('anadirDireccion', views.anadirDireccion, name='anadirDireccion'),
    # path('listarDireccion', views.listarDireccion, name='listarDireccion'),
    # path('editarDireccion/<int:pk>', views.editarDireccion, name='editarDireccion'),
    # path('eliminarDireccion/<int:pk>', views.eliminarDireccion, name='eliminarDireccion'),
    # path('anadirCompra', views.anadirCompra, name='anadirCompra'),
    # path('listarCompra', views.listarCompra, name='listarCompra'),
    # path('editarCompra/<int:pk>', views.editarCompra, name='editarCompra'),
    # path('eliminarCompra/<int:pk>', views.eliminarCompra, name='eliminarCompra'),
    path('verProducto/<int:pk>', views.verProducto, name='verProducto'),
    path('registro/', views.registroUsuario, name='registro'),
]