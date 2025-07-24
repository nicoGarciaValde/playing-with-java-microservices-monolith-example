# Microservicios en Flask

Este directorio contiene dos microservicios sencillos implementados con Python y Flask:

- **products**: expone un API para consultar productos.
- **users**: expone un API para consultar usuarios.

Cada microservicio incluye un `Dockerfile` para facilitar su despliegue. También se provee un `docker-compose.yml` para levantar ambos servicios de forma local:

```bash
docker-compose up --build
```

Los servicios quedarán disponibles en:
- `http://localhost:5001` para el servicio de productos.
- `http://localhost:5002` para el servicio de usuarios.
