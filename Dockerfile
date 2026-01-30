# Usar nginx como servidor web base
FROM nginx:alpine

# Etiquetas de metadatos
LABEL maintainer="antoniotomast"
LABEL description="DevOps Web Application for Deployment Management"

# Copiar archivos de la aplicación al directorio de nginx
COPY index.html /usr/share/nginx/html/
COPY styles.css /usr/share/nginx/html/
COPY script.js /usr/share/nginx/html/

# Copiar configuración personalizada de nginx (opcional)
# COPY nginx.conf /etc/nginx/nginx.conf

# Exponer el puerto 80
EXPOSE 80

# Comando para iniciar nginx
CMD ["nginx", "-g", "daemon off;"]
