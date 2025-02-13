from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login

def iniciar_sesion(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Autenticar al usuario
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Iniciar sesión
            login(request, user)
            messages.success(request, '¡Inicio de sesión exitoso!')
            return redirect('home')  # Redirigir a la página de inicio
        else:
            # Mostrar un mensaje de error si la autenticación falla
            messages.error(request, 'Usuario o contraseña incorrectos.')

    # Renderizar el formulario de inicio de sesión
    return render(request, 'credenciales/iniciar_sesion.html')

def registrar(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        username = request.POST['email']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['fullname']
        # last_name = request.POST['last_name']

        # Validar que el nombre de usuario no exista
        if User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya está en uso.')
            return redirect('registrar')

        # Crear el nuevo usuario
        try:
            nuevo_usuario = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=''
            )
            # Iniciar sesión automáticamente después del registro
            login(request, nuevo_usuario)
            messages.success(request, '¡Registro exitoso! Bienvenido.')
            return redirect('iniciar_sesion')  # Redirigir a la página de inicio
        except Exception as e:
            messages.error(request, f'Error al registrar el usuario: {e}')
            return redirect('registrar')

    # Si no es una solicitud POST, mostrar el formulario de registro
    return render(request, 'credenciales/registro.html')