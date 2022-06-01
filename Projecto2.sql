----Javier Valle Carnet 20159
----Hansel López 19026
select * from test;

insert into test(test) values('adios')

 delete from test where test = 'cccs'
 
 select * from test where test = 'adios'
  
drop table prueba;

--Tabla de los datos del usuario.
create table datos_usuario(
	nombre varchar(50), 
	apellido varchar(50),
	usuario varchar(50),
	contraseña varchar(200),
	correo varchar(50),
	plan varchar(50),
	tiempo varchar(80)
);

alter table datos_usuario alter column contraseña type varchar(200) using(contraseña::varchar(200));

alter table datos_usuario add column tiempo varchar(80);

drop table fracaso;

select * from datos_usuario du;

delete from datos_usuario ;

delete from fracaso;

delete from perfiles;

select * from admins a;

select * from fracaso;

select * from perfiles;

--Llave primaria de la tabla perfiles.
alter table perfiles 
add constraint perfil
primary key (perfil);

--Llave primaria de la tabla.
alter table datos_usuario
add constraint llave1
primary key (usuario);

select * from datos_usuario du;

insert into datos_usuario(usuario) values('Jav1') --Usuario de prueba

delete from datos_usuario; --Eliminando cosas que no sirven.

--Preparando el query para seleccionar perfiles
select du.usuario, p.perfil 
FROM datos_usuario du
	join perfiles p on du.usuario = p.usuario
WHERE du.usuario = 'Javs'
limit 1

select * from perfiles;

select * from datos_usuario du;

--Tabla de los perfiles del usuario.
create table perfiles(
	usuario varchar(50),
	perfil varchar(50)
);

--Llave foránea de perfiles, y de la tabla perfiles, que apunta hacia la tabla de datos_usuario en su columna de usuario.
alter table perfiles 
add constraint llave2
foreign key (usuario)
references datos_usuario(usuario);


--Seleccionando los perfiles.
select * from perfiles p;

--Eliminando basura.
delete from perfiles;

drop table perfiles;

--Tabla de administradores
create table admins(
	nombre varchar(50),
	apellido varchar(50),
	usuario varchar(50),
	contrasña varchar(200)
);

select * from admins;

delete from admins;

--Tabla para los videos.
create table videos(
	id serial,
	nombre varchar(50),
	genero varchar(50),
	director varchar(50),
	premio varchar(50), 
	fecha_streno date, 
	link varchar(200),
	duracion varchar(50), 
	primary key(id)
);


--Insertando dato de prueba.
insert into videos(nombre, genero, director, premio, fecha_streno, link, duracion) values 
('Mejor Película de Acción', 'Acción', 'John Cena', 'Óscar', '03-27-2022', 'https://www.youtube.com/watch?v=1UAgkBSGV_4&ab_channel=Stokan', '150');

insert into videos(nombre, genero, director, premio, fecha_streno, link, duracion) values 
('Solo en Casa', 'Comedia', 'Juan', 'Óscar', '04-12-2021', 'https://www.youtube.com/watch?v=8pxa3wDxo5E&ab_channel=PelisClásicas📺', '142');


alter table videos alter column duracion type integer using(duracion::integer);

select * from videos;

delete from videos where id = '3';

alter table videos add column id integer; 

alter table videos drop column actor;
drop table videos;

select * from historial h;

delete from videos;

select * from videos_actores;

select * from videos;

--Query para ver el nombre de la película en donde participa un actor.
select v.nombre 
from videos v
	join videos_actores va on va.id_pelicula = v.id
where va.nombre = 'Dwane Jhonson';

--Creando tabla para tener a los videos en los que aparecen los actores.
create table videos_actores(
	id serial,
	nombre varchar(50),
	id_pelicula int,
	id_actor int,
	primary key (id)
)

--Creando llaves foráneas.
--Llave foránea que apunta desde la columna de id_pelicula de la tabla videos_actores hacia la columna de videos en su columna de id.
alter table videos_actores 
add constraint idpel
foreign key (id_pelicula)
references videos(id);

--Llave foránea que apunta desde la columna de id_actor de la tabla videos_actores hacia la columna de actores en su columna de id.
alter table videos_actores 
add constraint idactor
foreign key (id_actor)
references actores(id);

--Creando tabla para almacenar a los actores.
create table actores (
	nombre varchar(50),
	id serial,
	primary key (id)
)

select * from videos;

insert into actores values ('Vin Diesel'), ('Dwane Jhonson'), ('Johnny Depp'), ('Brad Pitt');

select * from actores;

select * from videos v;
select * from videos_actores;


insert into videos_actores values('1','Vin Diesel', '1', '1'), 
('2','Dwane Jhonson', '1', '2'), ('3','Johnny Depp', '2', '3'), 
('4','Brad Pitt', '2', '4');


update videos set link = 'https://www.youtube.com/watch?v=pleMLkso4p8&ab_channel=sennguyen' where nombre = 'Mejor Película de Acción'

create table busquedas(
	perfil varchar(50),
	busqueda varchar(50),
	tiempo varchar(50)
);

select * from busquedas;


--Tabla para almacenar fracasos en la contraseña.
create table fracaso (
	usuario varchar(50)
);

--Llave foránea de fracaso que va desde usuario y que apunta hacia la tabla de registros, con llave primaria usuario.
alter table fracaso 
add constraint frac
foreign key (usuario)
references datos_usuario(usuario);

select * from fracaso;



--Lista de favoritos de la persona.
create table favoritos (
	 perfil varchar(50),
	 nombre varchar(50),
	 link varchar(200),
	 visto int, 
	 tiempo varchar(50)
);


--Historial
create table historial (
	perfil varchar(50),
	 nombre varchar(50),
	 link varchar(200),
	 visto int, 
	 tiempo varchar(50)
);

drop table historial;

select * from historial;

select * from favoritos;


create table anunciante(
	nombre varchar(50),  
	correo varchar(50),
	primary key (nombre)
);

select * from anunciante;

insert into anunciante(nombre, correo) values ('Coca-Cola', 'cocacola@gmail.com'),
											  ('Pepsi', 'pepsi@gmail.com'),
											  ('Ford', 'ford@gmail.com'),
											  ('Mercedes', 'pepsi@gmail.com')

insert into anunciante(nombre, correo) values ('Rolex', 'rolex@gmail.com');

insert into anunciante(nombre, correo) values ('Tissot', 'tissot@gmail.com');

--Creando tabla para los anuncios.
create table anuncio(
	nombre_anunciante varchar(50),
	link varchar(200),
	genero varchar(50),
	primary key(nombre_anunciante)
);

alter table anuncio  
add constraint anu
foreign key (nombre_anunciante)
references anunciante(nombre);

select * from datos_usuario du;

insert into anuncio(nombre_anunciante, link, genero) values('Coca-Cola', 'https://www.youtube.com/watch?v=BbjYY-xugKE&ab_channel=MarvelEspaña', 'Acción');

insert into anuncio(nombre_anunciante, link, genero) values ('Pepsi','https://www.youtube.com/watch?v=BQaz2dRsfQM&ab_channel=EstrellaDamm', 'Romance'), 
										 					('Ford', 'https://www.youtube.com/watch?v=gbkH3CpAt4Y&ab_channel=Marketing360', 'Comedia'),
										 					('Mercedes', 'https://www.youtube.com/watch?v=izMbNhfBI2I&ab_channel=IKEAEspaña', 'Suspenso')

insert into anunciante (nombre, correo) values ('Mustang', 'mustang@gmail.com');
insert into anuncio(nombre_anunciante, link, genero) values ('Rolex', 'https://www.youtube.com/watch?v=bwUGBtVf174&ab_channel=TopCine%26Tv', 'Ficción');


select * from anuncio;

select * from datos_usuario du;

select * from videos;

select * from historial h;

select * from busquedas;

select * from datos_usuario du;

select * from perfiles;

select * from busquedas b
where tiempo like '%2022-03-28';

--Select para la reportería.
--Select para el top 10 de géneros. 
select distinct v.genero, TO_DATE(substring(tiempo, 0,11), 'YYYY/MM/DD') as fecha, sum(v.duracion) as minutos_consumidos
from busquedas b
	join videos v on b.busqueda = v.nombre 
where tiempo >= '2022-03-28' and tiempo <= '2022-03-31'
group by v.genero, b.tiempo
limit 10;

select * from videos;

select * from busquedas b;

--Select para la cantidad de reproducciones por tipo de cuenta para un rango de fechas dado.
select v.genero, TO_DATE(substring(b.tiempo, 0,11), 'YYYY/MM/DD') as fecha, count(b.busqueda) as cantidad_reprodicciones, du.plan
from busquedas b
	join videos v on b.busqueda = v.nombre
	join perfiles p on p.perfil = b.perfil 
	join datos_usuario du on p.usuario = du.usuario 
where b.tiempo >= '2022-03-28' and b.tiempo <= '2022-03-31'
group by v.genero, b.tiempo, du.plan, p.perfil;

select tiempo from busquedas b;

select * from historial h;

select * from busquedas b;

--Select para la cantidad de reproducciones por tipo de cuenta para un rango de fechas dado.
select v.genero, count(b.busqueda) as cantidad_reprodicciones
from busquedas b
    join videos v on b.busqueda = v.nombre
    join perfiles p on p.perfil = b.perfil 
    join datos_usuario du on p.usuario = du.usuario 
where b.tiempo >= '2022-03-28' and b.tiempo <= '2022-03-31'
group by v.genero;

--Select para el top 10 de los direcotres y actores principales de las películas que los perfiles estándar y avanzados han visto.
select v.director, v.actor, h.nombre, TO_DATE(substring(h.tiempo, 0,11), 'YYYY/MM/DD') as fecha 
from historial h
	join videos v on h.nombre = v.nombre
	join perfiles p on p.perfil = h.perfil 
	join datos_usuario du on p.usuario = du.usuario 
where h.tiempo >= '2022-03-28' and h.tiempo <= '2022-03-31' and du.plan = 'Estándar' or du.plan = 'Avanzado'
limit 10;

select * from videos;

alter table videos add column esEstrella integer;

insert into videos(esestrella) values('1, 0') where nombre = 'Mejor Película de Acción'; 

update videos set esEstrella = '0' where nombre = 'Solo en Casa';

select * from datos_usuario du;

select * from busquedas b;

select * from perfiles;

select * from historial;

select * from anuncio;

select * from fracaso;

select * from datos_usuario du;

select * from favoritos f;

select * from actores a;

--Conteo de la cantidad de cuentas avanzadas creadas en los últimos seis meses.
select count(usuario), TO_DATE(substring(du.tiempo, 0,11), 'YYYY/MM/DD') as fecha 
from datos_usuario du
where plan = 'Avanzado' and du.tiempo >= '2022-03-28' and du.tiempo <= '2022-03-31'
group by du.tiempo;



--Hora pico del sistema.
select TO_DATE(substring(b.tiempo, 0,11), 'YYYY/MM/DD') as fecha, b.tiempo
from busquedas b
where b.tiempo > '2022-03-28'
order by TO_DATE(substring(b.tiempo, 0,11), 'YYYY/MM/DD')
desc;


select * from admins a;

select * from datos_usuario du;

select * from admins;

select * from videos v;

select * from actores a;

select * from videos_actores va;

select * from favoritos f;

select nombre, link from favoritos f
where perfil = 'Javier';


delete from videos where nombre = 'Solo en Casa';

select * from videos;

select * from videos_actores va;
 
select * from videos;

select * from datos_usuario du;

--insert into videos_actores values('5','Vin Diesel', '1', '1');

select * from historial h;

select * from busquedas b;

delete from videos where nombre = 'Matilda';

delete from actores where nombre = 'Vin Diesel';

-- Haciendo arreglos faltantes para la BD.

-- Primeros arreglos.

-- Búsqueda, favoritos e historial tiene llaves foráneas hacia perfiles.
select * from datos_usuario du;

select * from favoritos f;

select * from historial h;

delete from historial where perfil = 'Jan';

delete from busquedas where perfil = 'Jan';

select * from perfiles;

select * from busquedas;

-- Agregando la primera llave foránea. Esta va desde la columna de perfiles de la tabla busquedas hacia la columna de perfil de la tabla perfiles.
alter table busquedas 
add constraint llave
foreign key (perfil)
references perfiles(perfil)
on delete cascade;

alter table busquedas 
drop constraint llave;

-- Agregando la segunda llave foránea. Esta va desde la columna de perfiles de la tabla historial hacia la columna de perfil de la tabla perfiles.
alter table historial
add constraint llave2
foreign key (perfil)
references perfiles(perfil)
on delete cascade;

alter table historial 
drop constraint llave2;

-- Agregando la tercera llave foránea. Esta va desde la columna de perfiles de la tabla historial hacia la columna de perfil de la tabla perfiles.

alter table favoritos 
add constraint llave3
foreign key (perfil)
references perfiles(perfil)
on delete cascade;

alter table favoritos 
drop constraint llave3;

-- Segundos arreglos.

-- Llave foranea de historial a videos, igual con favoritos y con videos_actores (llaves foráneas desde las tablas hacia videos).

select * from historial h;
select * from videos v;

-- Revisar con detalle esta opción.

alter table videos
add constraint llave4
primary key (id);

select * from videos;

alter table videos 
drop constraint videos_pkey cascade;

-- Agregando columna para hacer una llave foránea.
alter table historial 
add column id_pelicula varchar(50);

select * from historial h;

select * from videos v;

delete from historial where nombre = 'Matilda';

update historial 
set id_pelicula = '4'
where nombre = 'Solo en Casa';

alter table historial 
add constraint llave5
foreign key (id_pelicula)
references videos(id)
on delete cascade 
on update cascade;

alter table historial alter column id_pelicula type int using(id_pelicula::int);

-- Agregar llave primara de favoritos a videos.

select * from favoritos f;

alter table favoritos 
add column id_pelicula varchar(50);

update favoritos 
set id_pelicula = '1'
where nombre = 'Mejor Película de Acción';

alter table favoritos 
add constraint llave8
foreign key (id_pelicula)
references videos(id)
on delete cascade
on update cascade;

alter table favoritos alter column id_pelicula type int using(id_pelicula::int);

-- Llave foránea de videos_actores hacia videos.

-- Esta llave apunta directamente desde id_pelicula de la videos_actores hacia id de la tabla videos.

alter table videos_actores 
add constraint llave6
foreign key (id_pelicula)
references videos(id)
on delete cascade;


select * from videos;

delete from videos_actores where id_pelicula = '2'

-- Terceros arreglos.
select * from videos_actores va;

insert into videos_actores values ('2', '1', '2');
-- Eliminando redundancia de videos actores.
alter table videos_actores 
drop column nombre;

select * from videos;

select * from historial;

alter table historial 
rename column title to nombre;

select * from favoritos;
select * from videos;

update favoritos 
set id_pelicula = '1'
where nombre = 'Mejor Película de Acción';


select * from videos;

select * from historial h;

select * from actores;

select * from videos_actores;

SELECT v.nombre, v.link, v.id FROM videos v JOIN videos_actores va ON va.id_pelicula = v.id JOIN actores a on va.id = a.id WHERE a.nombre = 'Vin Diesel'

SELECT nombre FROM videos WHERE genero = 'Acción'

select * from videos where director = 'Jon Watts';

select * from videos;

select * from favoritos;

select * from admins a;

select * from datos_usuario du;

select * from historial h;

select * from favoritos f;


SELECT nombre, id FROM videos WHERE nombre ILIKE '%mejor%'



-- Ampliación de la reportería.

-- Se deben aplicar índices y se deben especificar en el diccionario a entregar.

-- Top 5 contenido visto en cada hora entre 9:00 a.m. a 1:00 a.m. para un mes dado.

-- Jalando el nombre de las películas del historial.
select distinct tiempo::time 
from historial
group by tiempo::time
order by tiempo::time;

select * from historial h;

-- Probando sin subqueries.
select h.nombre, h.tiempo::time as hora
	from historial h
	where EXTRACT(MONTH FROM h.tiempo::date) = '5' and h.tiempo::time between '09:00:00' and '24:00:00'
group by h.tiempo, h.nombre 
order by h.tiempo;
--offset 20;
--limit 734;
--limit 5;

SELECT nombre, count(nombre) as total, tiempo::time
from historial
group by tiempo, nombre;


--Prueba con subqueries.

SELECT *
  FROM (
       SELECT distinct h.tiempo::time, h.nombre
         FROM historial h
         where EXTRACT(MONTH FROM tiempo::date) = '5'
         group by h.nombre, h.tiempo::time
         having count(h.nombre) >= 4
         order by h.tiempo::time
       ) as conta
 where tiempo::time not between '02:00:00' and '08:00:00' 
 order by tiempo::time
 asc;
 
-- Creando vista con el top de vistas.
create or replace view get_tops as
	SELECT *
	  FROM (
	       SELECT distinct tiempo::time, h.nombre, EXTRACT(MONTH FROM h.tiempo::date)
	         FROM historial h
	         --where EXTRACT(MONTH FROM tiempo::date) = '4'
	         group by h.nombre, h.tiempo::time, EXTRACT(MONTH FROM h.tiempo::date)
	         having count(h.nombre) >= 4
	         order by h.tiempo::time
	       ) as conta
	 where tiempo::time not between '02:00:00' and '08:00:00' 
	 order by tiempo::time
	 asc;
	
select * from get_tops;
select * from get_tops where EXTRACT(MONTH FROM tiempo::date) = '5';

-- Botando vista que no sirve.
drop view get_tops;

-- Segunda prueba con subqueries.
select
 *
from
  (select
     h.nombre,
     rank() over (order by count(h.nombre) desc) as my_rank
  from
     historial h
  where EXTRACT(MONTH FROM h.tiempo::date) = '5' and h.tiempo::time between '09:00:00' and '24:00:00'
  group by h.nombre) as subquery
where my_rank <= 5
limit 5;

-- Crear vista y en el where del select de la vista se jala el tiempo.
-- Función para el top 5 películas vistas por cada hora entre las 9:00 a.m. y la 1:00 a.m. para un mes.
create or replace function get_top(a integer)
returns table (nombre varchar, top bigint) as 
$body$
begin
	return query select
	 *
	from
	  (select
	     h.nombre,
	     rank() over (order by count(h.nombre) asc) as my_rank
	  from
	     historial h
	  where EXTRACT(MONTH FROM h.tiempo::date) = $1 and h.tiempo::time between '09:00:00' and '24:00:00'
	  group by h.nombre) as subquery
	where my_rank <= 5
	limit 5;
end;
$body$
language plpgsql;

drop function get_top;
	
-- Jalando el top con el número de mes.
select * from get_top(4);

select * from videos;

select * from videos_actores;

select * from historial;

select * from buscar;

-- Creando índice para que la búsqueda del mes sea más rápida.
create index dos 
on historial(tiempo);

-- Creando índice para que el ordenamiento y el agrupamiento sea más rápdio.
create index nombres 
on historial(nombre);

-- Top 10 de los térmios que los usuarios buscan.

select * from busquedas b;

select * from datos_usuario du;

-- Prueba sin subqueries.
select distinct busqueda
from busquedas b
group by busqueda
having count(busqueda) >= 2
order by busqueda
limit 10;

-- Prueba con subqueries.
select
 *
from
  (select
     distinct busqueda,
     rank() over (order by count(busqueda) asc) as ranking
  from
     busquedas b
    group by busqueda) subquery
  limit 10;

-- Creando la vista para ver el top 10 de los términos que los usuarios buscan.
create or replace view buscar
as
	select
	 *
	from
	  (select
	     distinct busqueda,
	     rank() over (order by count(busqueda) desc) as ranking
	  from
	     busquedas b
	    group by busqueda
	    order by ranking) subquery
	  limit 10;
	 
select * from busquedas;

select * from historial where perfil = 'Javier' and EXTRACT(MONTH FROM tiempo::date) = '5' and nombre = 'Días del Cielo'
order by tiempo::date;

select * from actores;

-- Ejecutando la vista.
select * from buscar;

drop view buscar;
-- Se creó un índice en la columna busqueda de la tabla busquedas para que la obtención de datos se más eficaz.
create index uno
on busquedas (busqueda);

select * from buscar;

-- El top 5 de los administradores que más modificaciones realizan en las cuentas de usuarios para un rango de fechas dado.

-- El top 20 de películas que comenzaron a verse pero que llevan más de 20 días sin finalizarse, para un rango de fechas dado.

select * from favoritos f;

-- Seleccionando películas sin terminar de ver en un rango de fechas determinado y que llevan más de 20 días sin terminarse de ver.

select distinct nombre, tiempo::date
from favoritos f
where tiempo::date > '04-17-2022' and tiempo::date < '05-22-2022' and (extract(days from (timestamp '05-22-2022' - timestamp '04-17-2022'))) > 20
limit 20;


create or replace function get_rangos (fechaInicial date, fechaFinal date)
returns table (nombre varchar(60), fecha2 date) as $$
	select distinct nombre, tiempo::date
	from favoritos f
	where tiempo::date > fechaInicial and tiempo::date < fechaFinal
		and date_part('day', fechaFinal::timestamp - fechaInicial::timestamp) > 20
		group by nombre, tiempo::date
		order by tiempo::date asc
		-- and (extract(days from (fechaFinal - fechaInicial)::timestamp)) > 20
	limit 20;
$$ language sql;


drop function get_rangos(date, date)

select * from get_rangos('03-17-2022', '05-30-2022');

-- Creando índice para poder optimizar la búsqueda de tiempos.
create index tres
on favoritos(tiempo);

-- Índice para poder obtener más rápido los nombres de las películas.
create index nombresF
on favoritos(nombre);

select * from favoritos;

select * from datos_usuario du;

delete from datos_usuario 
where usuario = 'Rob';

select * from busquedas;

select * from perfiles p;

select * from datos_usuario du;

select * from historial;

select * from favoritos f;

select * from busquedas b;

select * from fracaso f;

select * from videos;

select * from actores a;

-- Leonardo DiCaprio con id 5.

select * from videos_actores va;

insert into videos_actores values ('3', '9', '5');

delete from videos_actores where id = '3';

delete from actores where id = '5';

select * from admins;

alter table admins
add constraint llave10
primary key (usuario);

-- Tabla para insertar las modificaciones que los administradores hacen.
create table modificaciones_administradores(
	usuario varchar(50),
	modificacion varchar(50),
	fecha varchar(50)
)

-- Agregando llave foránea por si acaso.
alter table modificaciones_administradores
add constraint llave9
foreign key (usuario)
references admins(usuario)
on delete cascade
on update cascade;

select * from modificaciones_administradores;

select * from datos_usuario du;

select * from perfiles p;

select * from admins a;

-- Top 5 de los administradores que más modificaciones hicieron en las cuentas de usuarios para un rango de fechas dado.
select distinct username, fecha_hora::date
from bitacora b
where fecha_hora::date > '04-17-2022' and fecha_hora::date < '05-16-2022'
limit 5;

select * from bitacora b;

select
 *
from
  (select
     b.username,
     rank() over (order by count(operation) desc) as my_rank
  from
     bitacora b 
  where EXTRACT(MONTH FROM b.fecha_hora::date) = '6' and b.fecha_hora::date > '04-17-2022' and b.fecha_hora::date < '05-16-2022'
  group by b.username) as subquery
where my_rank > 10;

select distinct b.username, b.fecha_hora::date, count(b.operation)
from bitacora b
where fecha_hora::date = '2022-05-30' and fecha_hora::date < '2022-06-01' and es_admin = '1'
group by b.username, b.fecha_hora
order by count(b.operation) desc
limit 5;

select count(b.operation), b.username, b.fecha_hora::date 
from bitacora b
group by b.username, b.fecha_hora::date
order by count(b.operation);

-- Preguntar acerca de esta función.
drop function get_mods;
create or replace function get_mods(
 a date,
 b date
 )
returns table (usuario varchar(50), fecha date, modificaciones bigint) as 
$body$
begin
	return query
	select distinct b.username, b.fecha_hora::date, count(b.operation)
	from bitacora b
	where fecha_hora::date = $1 and fecha_hora::date < $2
	group by b.username, b.fecha_hora
	order by count(b.operation) asc
	limit 5;
end;
$body$
language plpgsql;

-- Se creó un índice sobre las columnas operation y username, para que el sort que se genera en la función de 
-- get_mods sea más rápida y eficaz.
create index mods1 on bitacora(operation);
create index mods2 on bitacora(username);

select * from bitacora;

drop function get_mods(date, date)

select * from get_mods('2022-05-30', '2022-06-1');


-- Simulación de operaciones: Hay que preguntarle a los administradores una fecha y la cantidad de visualizaciones de películas.
select * from historial h;

select * from datos_usuario du;

select * from perfiles p;


create table prueba(
	nombre varchar(50),
	apellido varchar(50),
	usuario varchar(100),
	contrasena varchar(50),
	correo varchar(10),
	id_plan varchar(50),
	tiempo varchar(50)
);

create table prueba2(
	usuario varchar(50),
	perfil varchar(50)
)

-- Validando la data.
select * from prueba;

select * from prueba2;

alter table prueba 
add constraint cons
primary key (usuario)

alter table prueba2 
add constraint prueba
foreign key (usuario)
references prueba (usuario)

select * from perfiles p;

delete from prueba;

delete from prueba2;

drop table prueba cascade;
drop table prueba2;

select count(*) from historial h;

-- Contando las visualizaciones
select count(*) from historial h
where tiempo::date = '2022-04-27';

delete from historial where tiempo::date = '2022-04-30';

-- Validando las horas.
select * from historial h
where tiempo::date = '2022-04-27';

select * from videos;

-- Selección random de una película.
-- Referencia: https://como.help/programacion/postgresql/como-seleccionarordenar-aleatoriamente-elementos-en-postgresql#:~:text=Si%20queremos%20solo%20obtener%20un,la%20mayoría%20de%20los%20casos.

SELECT RANDOM() AS orden, id, nombre, link FROM videos ORDER BY orden limit 1


-- Selección random de un perfil.
SELECT RANDOM() AS orden, perfil FROM perfiles ORDER BY orden limit 1

select * from historial h;

select * from videos;

-- Insertando 50 películas.
insert into videos(nombre, genero, director, premio, fecha_streno, link, duracion) values 
('Brokeback Mountain', 'Acción', 'Ang Lee', 'Óscar', '2020-05-15', 'https://www.youtube.com/watch?v=bgGp9c6ks-8&ab_channel=virgoprimaveral', '200'),
('Chicas Malas', 'Comedia', 'Tina Fey', 'Golden Award', '2000-08-16', 'https://www.youtube.com/watch?v=tfSYGgqHqds', '250'),
('El Padrino', 'Suspenso', 'Francis Ford', 'Óscar', '2012-09-05', 'https://www.youtube.com/watch?v=W65GZkn4g6Q&ab_channel=CarlosRodriguez', '240'),
('En el Calor de la Noche', 'Suspenso', 'Sidney Poittier', 'César Awards', '2010-12-04', 'https://www.youtube.com/watch?v=mD0j47AICi4&ab_channel=CinefórumFilm', '170'),
('Fellini Ocho y Medio', 'Suspenso', 'Fellini', 'Raspberry', '2014-05-05', 'https://www.youtube.com/watch?v=R59zZj_h2BU&ab_channel=FilmsEs', '140'),
('Iron Man', 'Acción', 'Jon Favreau', 'Óscar', '2008-04-14', 'https://www.youtube.com/watch?v=dGK_qH_-Hes&ab_channel=JonathanUbiera', '150'),
('Mad Max: Furia en la Carretera', 'Acción', 'George Miller', 'Academy Awards', '2010-08-16', 'https://www.youtube.com/watch?v=2ISWs5rB1q4&ab_channel=UPlayNetwork', '180'),
('Moon Light', 'Suspenso', 'Barry Jenkins', 'César Awards', '2021-07-22', 'https://www.youtube.com/watch?v=VzetxI2f22Y&ab_channel=TrailersInSpanish', '150'),
('Parasite', 'Suspenso', 'Bong Joon-ho', 'European Awards', '2019-08-10', 'https://www.youtube.com/watch?v=tQBlgeQqUdQ&ab_channel=KLER.conectado', '120'),
('Salvad al Tigre', 'Suspenso', 'John G. Avildsen', 'Óscar', '2015-03-14', 'https://www.youtube.com/watch?v=ZprLkE4gn8A&ab_channel=Wendox033', '80'),
('Doce Hombre sin Piedad', 'Miedo', 'Sidney Lumet', 'British Academy', '2009-07-12', 'https://www.youtube.com/watch?v=jO3kJ8w_1L8&ab_channel=RTVE', '270'),
('Con la Muerte en los Talones', 'Acción', 'Alfred Hitchcock', 'David di Donatello', '2013-01-04', 'https://www.youtube.com/watch?v=GI4dYdkwTMg&ab_channel=CINEENTREAMIGOS', '240'),
('Déjenme Salir', 'Ficción', 'Jordan Bale', 'Satellite Awards', '2017-06-27', 'https://www.youtube.com/watch?v=fmGY8rC69Kk&ab_channel=WassonBebe', '115'),
('Días del Cielo', 'Amor', 'Terrence Malick', 'European Films', '2018-04-30', 'https://www.youtube.com/watch?v=EZY_swecdAw&ab_channel=FilmotecaSantJoand%27Alacant', '105'),
('El bueno, el feo y el malo', 'Acción', 'Sergio Leone', 'Raspberry', '2005-10-15', 'https://www.youtube.com/watch?v=wCnHzRNq1G8&ab_channel=PulaskyProducciones', '225'),
('Fitzcarraldo', 'Comedia', 'Werner Herzog', 'Satellite Awards', '2003-03-17', 'https://www.youtube.com/watch?v=AuMb5xZBJkk&ab_channel=PeliculasUniversales', '180'),
('Los Cazafantasmas', 'Suspenso', 'Ivan Reitman', 'Óscar', '2006-05-12', 'https://www.youtube.com/watch?v=_drViVoIq14&ab_channel=CineenEspañol', '165'),
('Roma', 'Suspenso', 'Alfonso Cuarón', 'Grammy', '2008-06-05', 'https://www.youtube.com/watch?v=vOQxH7wrdHY&ab_channel=DaniloArroyotv', '155'),
('Selma', 'Amor', 'Ava DuVernay', 'Golden Globe', '2011-07-13', 'https://www.youtube.com/watch?v=z7uNlzdDF4o&ab_channel=albertocordalpeliculas', '135'),
('Tiempos de gloria', 'Ficción', 'Edward Zwick', 'Satellite Awards', '2013-05-19', 'https://www.youtube.com/watch?v=Ppzsz-WgYxo&ab_channel=PelículasCompletasHD', '95'),
('Al Filo de la Noticia', 'Comedia', 'James L. Brooks', 'Golden Globe', '2010-07-24', 'https://www.youtube.com/watch?v=tR4g0FdT7M8&ab_channel=VideoCult', '79'),
('El Exorcista', 'Terror', 'William Friedkin', 'European Films', '2004-02-10', 'https://www.youtube.com/watch?v=NclLgx_qI88&ab_channel=PelículasCompletas🎬HD🎬', '215'),
('Ladrón que roba ladrón', 'Comedia', 'Joe Menendez', 'Golden Globe', '2010-04-16', 'https://www.youtube.com/watch?v=KY93KXaASI8&ab_channel=MaryMardorre', '180'),
('La gran evasión', 'Acción', 'John Sturges', 'César Awards', '2001-12-12', 'https://www.youtube.com/watch?v=ahaCO_xJW-Q&ab_channel=Cinecinéfilosfilms', '120'),
('Muerte entre las Flores', 'Acción', 'Joel Coen', 'British Academy', '2002-11-09', 'https://www.youtube.com/watch?v=IAqW9w25n7A&ab_channel=JoanTeixidóPau', '110'),
('Acorralado (Rambo)', 'Ficción', 'Ted Kotcheff', 'Academy Awards', '2005-09-14', 'https://www.youtube.com/watch?v=S-hx4IPifA8&ab_channel=KhairulChannel', '105'),
('Terminator', 'Acción', 'James Cameron', 'British Academy', '1997-06-01', 'https://www.youtube.com/watch?v=Vj9vPLXFhfc&ab_channel=MUNDOTV', '75'),
('Toro Salvaje', 'Acción', 'Martin Scorsese', 'Satellite Awards', '1999-02-03', 'https://www.youtube.com/watch?v=P1mv7kLnzfA&ab_channel=Tokopilla18', '147'),
('Tres colores', 'Ficción', 'Krzysztof Kieślowski', 'Óscar', '2014-04-05', 'https://www.youtube.com/watch?v=93XYUr10r2g&ab_channel=delamilonga', '101'),
('Zombi', 'Acción', 'Paul Hoen', 'British Academy', '1997-06-25', 'https://www.youtube.com/watch?v=Aq8M_XX9FjQ&ab_channel=DarkLordZero', '78'),
('Alien: El octavo pasajero', 'Aventura', 'Ridley Scott', 'Golden Globe', '1970-08-10', 'https://www.youtube.com/watch?v=foOCRvwiAlY&ab_channel=TusSeriesyPelículasClásicas-TSPC', '130'),
('Blade Runner', 'Acción', 'Ridley Scott', 'Golden Globe', '2000-12-04', 'https://www.youtube.com/watch?v=WVNeBGVWfBE&ab_channel=SNediser', '140'),
('Centauros del desierto', 'Drama', 'John Ford', 'British Academy', '2005-01-31', 'https://www.youtube.com/watch?v=C-hhUALuLZE&ab_channel=MariodelaRubia', '100'),
('Ciudadano Kane', 'Misterio', 'Orson Welles', 'César Awards', '2006-04-20', 'https://www.youtube.com/watch?v=Z5MogqGgB1U&ab_channel=losinsecticidas', '105'),
('El puente sobre el río Kwai', 'Drama', 'David Lean', 'César Awards', '2021-08-09', 'https://www.youtube.com/watch?v=lzC_i3CFXds&ab_channel=DouglasRich', '127'),
('El resplandor', 'Drama', 'Stanley Kubrick', 'Raspberry', '2005-04-05', 'https://www.youtube.com/watch?v=0LSnh2KhfrI&ab_channel=PeliculasDonMolina', '114'),
('Haz lo que debas', 'Drama', 'Spike Lee', 'Golden Globe', '2014-05-17', 'https://www.youtube.com/watch?v=YS0j01r0MvI&ab_channel=DanielDíazCasanueva', '107'),
('Los amos de la noche (The Warriors)', 'Thriller', 'Walter Hill', 'Golden Globe', '2001-01-07', 'https://www.youtube.com/watch?v=PDiSBH7HhGk&ab_channel=BubenFlax', '102'),
('M*A*S*H', 'Drama', 'Robert Altman', 'Golden Globe', '2001-01-07', 'https://www.youtube.com/watch?v=JUFhDU2oXYI&ab_channel=ElbauldeLaCineteca', '106'),
('Agente 007 contra el Dr. No', 'Suspenso', 'Terence Young', 'British Academy', '1950-06-14', 'https://www.youtube.com/watch?v=yv2b1NC24mI&ab_channel=DarkHunterTV', '111'),
('Amor a quemarropa', 'Aventura', 'Tony Scott', 'Satellite Awards', '2012-07-14', 'https://www.youtube.com/watch?v=v4QbZC7rCfw&list=PLmrEspL7-NCpiDbmPMauKLjsYgyRQemyd&ab_channel=madmax', '220');

select * from videos;

select * from actores a;

-- Insertando a más actores.
insert into actores(nombre) values 
('Felipe Londoño'),
('Monica Lopez'),
('Douglas Falconer'),
('Antonio Resines'),
('Laura Ramos'),
('José Coronado'),
('Edgar Vittorino'),
('Amanda Rios'),
('Lola Rodríguez'),
('Lucía Veiga'),
('Anthony Hopkins'),
('Manolo Caro'),
('Berta Ojea'),
('Diego Garisa'),
('Jared Leto'),
('Jason Momoa'),
('William Levy'),
('Alan Ritchson'),
('Álex Pastrana'),
('Franky Martín'),
('Gerard Butler'),
('Colin Firth'),
('Lucas Wainraich')
;

insert into actores(nombre) values('Russell Crowe');

select * from videos_actores va
where id_pelicula = '50';

select distinct genero from videos;

select * from videos_actores va;

select * from historial h;

select * from videos v;

select h.nombre, v.genero 
from historial h
	join videos v on h.id_pelicula = v.id;

select * from buscar;

select * from videos_actores;

select * from actores where id = '27';

-- Creando tabla para detectar e ingresar el login de los perfiles comerciales.
create table ingreso_comercial(
	perfil varchar(50),
	tiempo varchar(50),
	foreign key (perfil)
	references perfiles(perfil)
);

alter table ingreso_comercial
drop column ingreso;

drop table ingreso_comercial;

select * from perfiles p
where ingreso = '1';

alter table perfiles
add column ingreso int;

update perfiles 
set ingreso = '0';

select * from datos_usuario du
where plan = 'Estándar';

select * from videos where nombre ilike '%mejor%';

select * from videos;

select * from actores a;
select * from videos_actores va;

SELECT v.nombre, v.link FROM videos v 
JOIN videos_actores va ON va.id_pelicula = v.id 
JOIN actores a on va.id_actor = a.id WHERE a.nombre ILIKE '%Robert%'


select * from historial h where perfil = 'Javier' and tiempo::date = '2022-06-01';

select * from perfiles;

select * from buscar;

select * from favoritos 
where perfil = 'Javier' and tiempo::date = '2022-06-01';

select * from admins;

alter table admins 
add column ingreso int;

update admins
set ingreso = '0';


-- Bitácora: Hansel López






















