
CREATE TABLE phoneshop.manufacturers (
	id BIGINT UNSIGNED auto_increment NOT NULL,
	name varchar(100) NOT NULL,
	deleted_at TIMESTAMP NULL,
	created_at TIMESTAMP NULL,
	updated_at TIMESTAMP NULL,
	CONSTRAINT manufacturers_PK PRIMARY KEY (id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8
COLLATE=utf8_general_ci;

CREATE TABLE phoneshop.models (
	id BIGINT UNSIGNED auto_increment NOT NULL,
	name varchar(100) NOT NULL,
	deleted_at TIMESTAMP NULL,
	created_at TIMESTAMP NULL,
	updated_at TIMESTAMP NULL,
	CONSTRAINT models_PK PRIMARY KEY (id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8
COLLATE=utf8_general_ci;

CREATE TABLE phoneshop.phones (
	id BIGINT UNSIGNED auto_increment NOT NULL,
	imei varchar(100) NOT NULL,
	memory SMALLINT UNSIGNED NOT NULL,
	manufacture_year SMALLINT UNSIGNED NOT NULL,
	os_version varchar(100) NOT NULL,
	body_color varchar(100) NULL,
	price varchar(100) NULL,
	deleted_at TIMESTAMP NULL,
	created_at TIMESTAMP NULL,
	updated_at TIMESTAMP NULL,
	manufacturer_id BIGINT UNSIGNED NULL,
	model_id BIGINT UNSIGNED NULL,
	CONSTRAINT phones_PK PRIMARY KEY (id),
	CONSTRAINT phones_manufacturers_FK FOREIGN KEY (manufacturer_id) REFERENCES phoneshop.manufacturers(id),
	CONSTRAINT phones_models_FK FOREIGN KEY (model_id) REFERENCES phoneshop.models(id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8
COLLATE=utf8_general_ci;


insert into manufacturers(name, created_at, updated_at) 
values('Apple', now(), now()), ('Samsung', now(), now())

insert into models(name, created_at, updated_at) 
values('iPhone 14 Promax', now(), now()), ('iPhone 13', now(), now()),
('Galaxy 10', now(), now()), ('Galaxy 12', now(), now())

