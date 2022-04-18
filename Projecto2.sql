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



