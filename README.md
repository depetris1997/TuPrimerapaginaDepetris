# TuPrimeraPaginaDepetris

Proyecto Django (patrón **MVT**) estilo blog con **herencia de plantillas**, **3 modelos**, **formularios de alta** y **búsqueda en la BD**.

## ✅ Requisitos de la consigna (cumplidos)
- Herencia de HTML (`base.html` + templates que extienden).
- 3 clases en `models.py` (`Autor`, `Categoria`, `Post`).
- Un formulario para insertar datos de **cada** modelo.
- Un formulario para **buscar** posts por título o contenido.
- Proyecto listo para subir a GitHub.
- README con instrucciones y orden de prueba.

---

## 🚀 Cómo ejecutar

```bash
# 1) Crear entorno (opcional pero recomendado)
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
# source venv/bin/activate

# 2) Instalar dependencias
pip install -r requirements.txt

# 3) Migraciones (crea la base de datos)
python manage.py migrate

# 4) (Opcional) Crear superusuario para /admin
python manage.py createsuperuser

# 5) Ejecutar servidor
python manage.py runserver
```

Abrí: <http://127.0.0.1:8000/>

---

## 🧭 Orden sugerido para probar
1. **Crear Autor** → `/crear-autor/`
2. **Crear Categoría** → `/crear-categoria/`
3. **Crear Post** → `/crear-post/` (usa el Autor y la Categoría creados)
4. **Ver Posts** → `/posts/`
5. **Buscar** → `/buscar/` (por título o contenido)

También podés usar el **admin** en `/admin/` (si creaste superusuario).

---

## 🧱 Estructura

```
TuPrimeraPaginaDepetris/
├─ manage.py
├─ requirements.txt
├─ README.md
├─ blog/
│  ├─ __init__.py
│  ├─ settings.py
│  ├─ urls.py
│  ├─ asgi.py
│  └─ wsgi.py
├─ core/
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ forms.py
│  ├─ models.py
│  ├─ views.py
│  └─ migrations/
│     └─ __init__.py
└─ templates/
   ├─ base.html
   ├─ home.html
   ├─ lista_posts.html
   ├─ autor_form.html
   ├─ categoria_form.html
   ├─ post_form.html
   └─ buscar_post.html
```

---

## 🌎 Config regional
- **Idioma:** `es-ar`
- **Zona horaria:** `America/Argentina/Cordoba`

---

## 💡 Notas
- El proyecto usa **SQLite** por defecto (no requiere configuración extra).
- Si no aparecen autores/categorías al crear posts, crealos primero.
- Este es un proyecto base simple, ideal para extender en la entrega final.
