--
-- PostgreSQL database dump
--

-- Dumped from database version 13.0
-- Dumped by pg_dump version 13.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: libro; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.libro (
    id_libro integer NOT NULL,
    codigo character varying(20) NOT NULL,
    titulo character varying(100) NOT NULL,
    editorial character varying(100) NOT NULL,
    stock integer NOT NULL
);


ALTER TABLE public.libro OWNER TO postgres;

--
-- Name: libro_id_libro_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.libro_id_libro_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.libro_id_libro_seq OWNER TO postgres;

--
-- Name: libro_id_libro_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.libro_id_libro_seq OWNED BY public.libro.id_libro;


--
-- Name: prestamo; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.prestamo (
    id_prestamo integer NOT NULL,
    id_libro integer NOT NULL,
    id_usuario integer NOT NULL,
    fecha_prestamo timestamp without time zone NOT NULL,
    fecha_devolucion timestamp without time zone,
    devuelto boolean
);


ALTER TABLE public.prestamo OWNER TO postgres;

--
-- Name: prestamo_id_prestamo_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.prestamo_id_prestamo_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.prestamo_id_prestamo_seq OWNER TO postgres;

--
-- Name: prestamo_id_prestamo_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.prestamo_id_prestamo_seq OWNED BY public.prestamo.id_prestamo;


--
-- Name: usuario; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.usuario (
    id_usuario integer NOT NULL,
    tipo_doc character varying(50) NOT NULL,
    num_doc character varying(50) NOT NULL,
    codigo character varying(20) NOT NULL,
    nombre character varying(50) NOT NULL,
    ap_paterno character varying(50) NOT NULL,
    ap_materno character varying(50) NOT NULL
);


ALTER TABLE public.usuario OWNER TO postgres;

--
-- Name: usuario_id_usuario_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.usuario_id_usuario_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.usuario_id_usuario_seq OWNER TO postgres;

--
-- Name: usuario_id_usuario_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.usuario_id_usuario_seq OWNED BY public.usuario.id_usuario;


--
-- Name: libro id_libro; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.libro ALTER COLUMN id_libro SET DEFAULT nextval('public.libro_id_libro_seq'::regclass);


--
-- Name: prestamo id_prestamo; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.prestamo ALTER COLUMN id_prestamo SET DEFAULT nextval('public.prestamo_id_prestamo_seq'::regclass);


--
-- Name: usuario id_usuario; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuario ALTER COLUMN id_usuario SET DEFAULT nextval('public.usuario_id_usuario_seq'::regclass);


--
-- Data for Name: libro; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.libro (id_libro, codigo, titulo, editorial, stock) FROM stdin;
2	AP-202113120650	Apocalipsis	Umbrella	3
\.


--
-- Data for Name: prestamo; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.prestamo (id_prestamo, id_libro, id_usuario, fecha_prestamo, fecha_devolucion, devuelto) FROM stdin;
3	2	2	2021-02-01 10:41:51	2021-02-01 11:00:13	t
4	2	2	2021-02-01 10:51:48	2021-02-01 11:03:12	t
\.


--
-- Data for Name: usuario; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.usuario (id_usuario, tipo_doc, num_doc, codigo, nombre, ap_paterno, ap_materno) FROM stdin;
2	DNI	40880382	CR-2021131201351	omar	cruces	ortega
\.


--
-- Name: libro_id_libro_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.libro_id_libro_seq', 2, true);


--
-- Name: prestamo_id_prestamo_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.prestamo_id_prestamo_seq', 4, true);


--
-- Name: usuario_id_usuario_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.usuario_id_usuario_seq', 2, true);


--
-- Name: libro pk_libro; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.libro
    ADD CONSTRAINT pk_libro PRIMARY KEY (id_libro) INCLUDE (id_libro);


--
-- Name: prestamo pk_prestamo; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.prestamo
    ADD CONSTRAINT pk_prestamo PRIMARY KEY (id_prestamo) INCLUDE (id_prestamo);


--
-- Name: usuario pk_usuario; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT pk_usuario PRIMARY KEY (id_usuario) INCLUDE (id_usuario);


--
-- Name: prestamo fk_prestamo_1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.prestamo
    ADD CONSTRAINT fk_prestamo_1 FOREIGN KEY (id_libro) REFERENCES public.libro(id_libro) NOT VALID;


--
-- Name: prestamo fk_prestamo_2; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.prestamo
    ADD CONSTRAINT fk_prestamo_2 FOREIGN KEY (id_usuario) REFERENCES public.usuario(id_usuario) NOT VALID;


--
-- PostgreSQL database dump complete
--

