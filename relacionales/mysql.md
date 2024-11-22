# MySQL

MySQL es un sistema de gestión de bases de datos relacional desarrollado por Oracle Corporation. MySQL es un sistema de gestión de bases de datos de código abierto y es uno de los sistemas de gestión de bases de datos más populares en la actualidad.

## Instalación

Podemos instalar MySQL en diferentes sistemas operativos, como Windows, macOS y Linux. También podemos lanzar un docker o un servicio en la nube.

```bash
docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:tag
```

## Conexión

Podemos conectarnos a MySQL a través de la línea de comandos o a través de una interfaz gráfica como MySQL Workbench.

```bash
mysql -u root -p
```

Si es en docker:

```bash
docker exec -it some-mysql mysql -u root -p
```


