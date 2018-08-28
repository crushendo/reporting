# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.6.32)
# Database: scouterdb
# Generation Time: 2017-02-17 13:21:05 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table auth_group
# ------------------------------------------------------------

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;

INSERT INTO `auth_group` (`id`, `name`)
VALUES
	(51,'Mature'),
	(190,'Young');

/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table auth_group_permissions
# ------------------------------------------------------------

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



# Dump of table auth_permission
# ------------------------------------------------------------

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_2f476e4b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
	(1,'Can add log entry',1,'add_logentry'),
	(2,'Can change log entry',1,'change_logentry'),
	(3,'Can delete log entry',1,'delete_logentry'),
	(4,'Can add permission',2,'add_permission'),
	(5,'Can change permission',2,'change_permission'),
	(6,'Can delete permission',2,'delete_permission'),
	(7,'Can add user',3,'add_user'),
	(8,'Can change user',3,'change_user'),
	(9,'Can delete user',3,'delete_user'),
	(10,'Can add group',4,'add_group'),
	(11,'Can change group',4,'change_group'),
	(12,'Can delete group',4,'delete_group'),
	(13,'Can add content type',5,'add_contenttype'),
	(14,'Can change content type',5,'change_contenttype'),
	(15,'Can delete content type',5,'delete_contenttype'),
	(16,'Can add session',6,'add_session'),
	(17,'Can change session',6,'change_session'),
	(18,'Can delete session',6,'delete_session'),
	(19,'Can add field',7,'add_field'),
	(20,'Can change field',7,'change_field'),
	(21,'Can delete field',7,'delete_field'),
	(22,'Can add labelle data',8,'add_labelledata'),
	(23,'Can change labelle data',8,'change_labelledata'),
	(24,'Can delete labelle data',8,'delete_labelledata'),
	(25,'Can add labelle field order',9,'add_labellefieldorder'),
	(26,'Can change labelle field order',9,'change_labellefieldorder'),
	(27,'Can delete labelle field order',9,'delete_labellefieldorder'),
	(28,'Can add scouting areas',10,'add_scoutingareas'),
	(29,'Can change scouting areas',10,'change_scoutingareas'),
	(30,'Can delete scouting areas',10,'delete_scoutingareas');

/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table auth_user
# ------------------------------------------------------------

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`)
VALUES
	(1,'pbkdf2_sha256$30000$qRuiwf4sz3BJ$yCTjIZRjJehIZMhbtxUZrTbilBpA8RwPCWMAggZQk/U=','2016-12-14 18:27:18.248449',1,'rackett','','','ryan.ackett@duda.com',1,1,'2016-11-11 15:07:36.669414'),
	(2,'pbkdf2_sha256$20000$KwYC6fKqbyxk$hdVo0s1Nnpu8Ah63z0ATUglAZTnblTcY98wlYcdyRiU=','2017-02-09 13:38:01.734698',0,'guest','Guest','','',0,1,'2016-11-11 15:08:50.000000');

/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table auth_user_groups
# ------------------------------------------------------------

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



# Dump of table auth_user_user_permissions
# ------------------------------------------------------------

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



# Dump of table django_admin_log
# ------------------------------------------------------------

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`)
VALUES
	(1,'2016-11-11 15:08:50.971487','2','guest',1,'[{\"added\": {}}]',3,1),
	(2,'2016-11-11 15:09:10.706615','2','guest',2,'[{\"changed\": {\"fields\": [\"first_name\"]}}]',3,1);

/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table django_content_type
# ------------------------------------------------------------

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;

INSERT INTO `django_content_type` (`id`, `app_label`, `model`)
VALUES
	(1,'admin','logentry'),
	(4,'auth','group'),
	(2,'auth','permission'),
	(3,'auth','user'),
	(7,'collection','field'),
	(8,'collection','labelledata'),
	(9,'collection','labellefieldorder'),
	(10,'collection','scoutingareas'),
	(5,'contenttypes','contenttype'),
	(6,'sessions','session');

/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table django_migrations
# ------------------------------------------------------------

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
	(1,'contenttypes','0001_initial','2016-08-10 17:26:31.507691'),
	(2,'auth','0001_initial','2016-08-10 17:26:31.850412'),
	(3,'admin','0001_initial','2016-08-10 17:26:31.902797'),
	(4,'admin','0002_logentry_remove_auto_add','2016-08-10 17:26:31.931023'),
	(5,'contenttypes','0002_remove_content_type_name','2016-08-10 17:26:32.022019'),
	(6,'auth','0002_alter_permission_name_max_length','2016-08-10 17:26:32.052940'),
	(7,'auth','0003_alter_user_email_max_length','2016-08-10 17:26:32.084056'),
	(8,'auth','0004_alter_user_username_opts','2016-08-10 17:26:32.098614'),
	(9,'auth','0005_alter_user_last_login_null','2016-08-10 17:26:32.122232'),
	(10,'auth','0006_require_contenttypes_0002','2016-08-10 17:26:32.125096'),
	(11,'auth','0007_alter_validators_add_error_messages','2016-08-10 17:26:32.143207'),
	(12,'auth','0008_alter_user_username_max_length','2016-08-10 17:26:32.174422'),
	(13,'sessions','0001_initial','2016-08-10 17:26:32.193834'),
	(14,'collection','0001_initial','2016-08-11 13:31:08.825832'),
	(15,'collection','0002_labelledata_test','2016-10-28 17:09:33.614695'),
	(16,'collection','0003_remove_labelledata_test','2016-11-09 18:32:20.078285'),
	(17,'collection','0004_auto_20161110_1509','2016-11-10 15:09:27.697018'),
	(18,'collection','0005_labellefieldorder','2016-11-11 18:41:32.582952'),
	(19,'collection','0006_labellefieldorder_age','2016-11-11 19:12:14.841161'),
	(20,'collection','0007_scoutingareas','2016-11-11 19:44:51.039598');

/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table django_session
# ------------------------------------------------------------

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`)
VALUES
	('15r893j77q16gzopxyi0f10cd09s9lr5','MDY2ZDMyZDk5NGU4YjhiMmQyNGZmMWY3OGIwYWMwNjViY2MyZDZjYjp7Il9hdXRoX3VzZXJfaGFzaCI6IjBlOWQwOWFiMjFiMGM1ODQ2NGVkNWYwMGU1NGRlZDBjNGNkMzExODgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=','2016-12-20 13:30:21.518133'),
	('18y9abjn0njkjf4elx3ryckk95iitsoe','ZmNkNDA4NmI3MjQ5MTY2MTcwYWJhMTZhNGRhMjNhNTExZDYxMGQyOTp7Il9hdXRoX3VzZXJfaGFzaCI6ImYzNWVlOTgxZTUxMmM0YTc3MmRlNmZjZmU1NzBiMWI1ODg3ZGEyYTgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=','2017-02-21 15:39:52.021826'),
	('1c9hbq7rlfi50z1gwucwz0y0z1n5b76n','MDY2ZDMyZDk5NGU4YjhiMmQyNGZmMWY3OGIwYWMwNjViY2MyZDZjYjp7Il9hdXRoX3VzZXJfaGFzaCI6IjBlOWQwOWFiMjFiMGM1ODQ2NGVkNWYwMGU1NGRlZDBjNGNkMzExODgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=','2016-11-25 15:35:30.970948'),
	('1n11fah1z4svuwb8fvy6r8uzkqzhtom4','ZmNkNDA4NmI3MjQ5MTY2MTcwYWJhMTZhNGRhMjNhNTExZDYxMGQyOTp7Il9hdXRoX3VzZXJfaGFzaCI6ImYzNWVlOTgxZTUxMmM0YTc3MmRlNmZjZmU1NzBiMWI1ODg3ZGEyYTgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=','2017-02-17 18:01:32.464455'),
	('407tdkwn31v205d7z6iax5dgwodozn4v','Mjc5ZWZkMDliMDkxNTJmOWJmYWZkNDVlN2I4MjI3OTkxNjViZGQyNTp7Il9hdXRoX3VzZXJfaGFzaCI6ImYzNWVlOTgxZTUxMmM0YTc3MmRlNmZjZmU1NzBiMWI1ODg3ZGEyYTgiLCJfYXV0aF91c2VyX2lkIjoiMiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-02-17 16:13:16.747312'),
	('fmiw1wcv01w9szqs9r4m83qu5xymynv7','ZmNkNDA4NmI3MjQ5MTY2MTcwYWJhMTZhNGRhMjNhNTExZDYxMGQyOTp7Il9hdXRoX3VzZXJfaGFzaCI6ImYzNWVlOTgxZTUxMmM0YTc3MmRlNmZjZmU1NzBiMWI1ODg3ZGEyYTgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=','2017-02-23 13:38:01.736776'),
	('h22iqkkhcpamuna0dflwqs3olr2j8tc8','ZmNkNDA4NmI3MjQ5MTY2MTcwYWJhMTZhNGRhMjNhNTExZDYxMGQyOTp7Il9hdXRoX3VzZXJfaGFzaCI6ImYzNWVlOTgxZTUxMmM0YTc3MmRlNmZjZmU1NzBiMWI1ODg3ZGEyYTgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=','2017-02-03 13:18:15.549546'),
	('l5z1jnvl164npnnxdf3ucquq9rvmcdio','MDY2ZDMyZDk5NGU4YjhiMmQyNGZmMWY3OGIwYWMwNjViY2MyZDZjYjp7Il9hdXRoX3VzZXJfaGFzaCI6IjBlOWQwOWFiMjFiMGM1ODQ2NGVkNWYwMGU1NGRlZDBjNGNkMzExODgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=','2016-12-19 18:33:42.601964'),
	('n2x3j6sr4j2umtrzglyqjh0kc25xnjbd','ZmNkNDA4NmI3MjQ5MTY2MTcwYWJhMTZhNGRhMjNhNTExZDYxMGQyOTp7Il9hdXRoX3VzZXJfaGFzaCI6ImYzNWVlOTgxZTUxMmM0YTc3MmRlNmZjZmU1NzBiMWI1ODg3ZGEyYTgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=','2017-02-18 15:32:56.030402'),
	('n8bhk3zpfc4bzfxv5c08r82tpyey9x6i','ZmNkNDA4NmI3MjQ5MTY2MTcwYWJhMTZhNGRhMjNhNTExZDYxMGQyOTp7Il9hdXRoX3VzZXJfaGFzaCI6ImYzNWVlOTgxZTUxMmM0YTc3MmRlNmZjZmU1NzBiMWI1ODg3ZGEyYTgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=','2017-02-22 20:03:06.481678'),
	('ojq6bgsexpgbp3jcwux1p394uyxiqkzv','ZmNkNDA4NmI3MjQ5MTY2MTcwYWJhMTZhNGRhMjNhNTExZDYxMGQyOTp7Il9hdXRoX3VzZXJfaGFzaCI6ImYzNWVlOTgxZTUxMmM0YTc3MmRlNmZjZmU1NzBiMWI1ODg3ZGEyYTgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=','2017-02-21 15:21:13.219973'),
	('pd3ho4p46o2r3n9j8hq9hvuroit9aum8','ZmNkNDA4NmI3MjQ5MTY2MTcwYWJhMTZhNGRhMjNhNTExZDYxMGQyOTp7Il9hdXRoX3VzZXJfaGFzaCI6ImYzNWVlOTgxZTUxMmM0YTc3MmRlNmZjZmU1NzBiMWI1ODg3ZGEyYTgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=','2017-02-22 20:05:14.757667'),
	('sqb29ypz45uzt3faj8nh67ko4h3f6jlm','ZmNkNDA4NmI3MjQ5MTY2MTcwYWJhMTZhNGRhMjNhNTExZDYxMGQyOTp7Il9hdXRoX3VzZXJfaGFzaCI6ImYzNWVlOTgxZTUxMmM0YTc3MmRlNmZjZmU1NzBiMWI1ODg3ZGEyYTgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=','2017-01-19 19:03:23.404587'),
	('uducfxy2n4ubmzc0121o021gol1mwa06','NGFjY2U0ZDA4NTllOTcyMTc4ZjZhMjc4NDhhOTllYTI2YmQ2MDA0Mzp7Il9hdXRoX3VzZXJfaGFzaCI6ImU1OGVjNDkwM2VhOWUxMTkzYTA1MjA4NDc4MGRlNTJkMWIzYjNlMGQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2016-12-19 18:48:03.081264'),
	('whbb3qmhqxuy8936utwzww138pk8nj81','NGFjY2U0ZDA4NTllOTcyMTc4ZjZhMjc4NDhhOTllYTI2YmQ2MDA0Mzp7Il9hdXRoX3VzZXJfaGFzaCI6ImU1OGVjNDkwM2VhOWUxMTkzYTA1MjA4NDc4MGRlNTJkMWIzYjNlMGQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2016-12-28 18:27:18.264368'),
	('z67fca1k3x085ibh1lhitev2sa3m1iau','ZmNkNDA4NmI3MjQ5MTY2MTcwYWJhMTZhNGRhMjNhNTExZDYxMGQyOTp7Il9hdXRoX3VzZXJfaGFzaCI6ImYzNWVlOTgxZTUxMmM0YTc3MmRlNmZjZmU1NzBiMWI1ODg3ZGEyYTgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=','2017-02-17 18:10:32.557445');

/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table scoutapp_field
# ------------------------------------------------------------

DROP TABLE IF EXISTS `scoutapp_field`;

CREATE TABLE `scoutapp_field` (
  `slug` int(11) DEFAULT NULL,
  `area` longtext CHARACTER SET latin1,
  `fieldName` longtext CHARACTER SET latin1,
  `variety` longtext CHARACTER SET latin1,
  `age` longtext CHARACTER SET latin1,
  `status` longtext CHARACTER SET latin1,
  `chemical` longtext CHARACTER SET latin1,
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `scoutapp_field` WRITE;
/*!40000 ALTER TABLE `scoutapp_field` DISABLE KEYS */;

INSERT INTO `scoutapp_field` (`slug`, `area`, `fieldName`, `variety`, `age`, `status`, `chemical`)
VALUES
	(1,'100','101 B','Valencia','Mature','Open',''),
	(2,'100','102 A','Valencia','Mature','Open',''),
	(3,'100','102 B H','Hamlin','Mature','Open',''),
	(4,'100','102 B V','Valencia','Mature','Open',''),
	(5,'100','103 South','Valencia','Mature','Open',''),
	(6,'100','104 A','Valencia','Mature','Open',''),
	(7,'100','104 B H','Hamlin','Mature','Open',''),
	(8,'100','104 B P','Pineapple','Mature','Open',''),
	(9,'100','105 A','Hamlin','Mature','Open',''),
	(10,'100','105 B ','Pineapple','Mature','Open',''),
	(11,'100','105 C','Pineapple','Mature','Open',''),
	(12,'100','105 D','Ruby Red','Mature','Open',''),
	(13,'53','53 C West 1','Valencia','Mature','Open',''),
	(14,'53','53 C West 2','Valencia','Mature','Open',''),
	(15,'53','53 D 1 (West)','Hamlin','Mature','Open',''),
	(16,'53','53 D 2 (East)','Hamlin','Mature','Open',''),
	(17,'53','53 E 1 (West)','Hamlin','Mature','Open',''),
	(18,'53','53 E 2 (East)','Hamlin','Mature','Open',''),
	(19,'53','53 F','Hamlin','Mature','Open',''),
	(20,'53','53 G','Hamlin/Valencia','Mature','Open',''),
	(21,'53','53 C east','Hamlin','Mature','Open',''),
	(22,'53','53 D east','Hamlin','Mature','Open',''),
	(23,'53','53 E east','Valencia','Mature','Open',''),
	(24,'53','53 F east','Valencia','Mature','Open',''),
	(25,'53','53 G east','Valencia','Mature','Open',''),
	(26,'9250','9250 A','Hamlin','Mature','Open',''),
	(27,'9250','9250 B','Hamlin','Mature','Open',''),
	(28,'9250','9250 C','Hamlin','Mature','Open',''),
	(29,'9250','9250 G','Valencia','Mature','Open',''),
	(30,'100','NO3 P','Pineapple','Mature','Open',''),
	(31,'100','NO3V','Valencia','Mature','Open',''),
	(32,'100','LL 1','','Mature','Open',''),
	(33,'100','LL 2','','Mature','Open',''),
	(34,'Old Grove','N 81','Pineapple','Mature','Open',''),
	(35,'Old Grove','QS','Valencia','Mature','Open',''),
	(36,'Old Grove','U 12 North','Valencia','Mature','Open',''),
	(37,'Old Grove','U 12 South','Valencia','Mature','Open',''),
	(38,'Old Grove','U 80','Pineapple','Mature','Open',''),
	(39,'Old Grove','U1 C','Valencia','Mature','Open',''),
	(40,'Old Grove','U3 B West','Hamlin','Mature','Open',''),
	(41,'Old Grove','U3 B East','Valencia','Mature','Open',''),
	(42,'Old Grove','U3 C','Hamlin','Mature','Open',''),
	(43,'Old Grove','U4 C','Valencia','Mature','Open',''),
	(44,'Old Grove','U5A','Hamlin','Mature','Open',''),
	(45,'Old Grove','U6 A','Valencia','Mature','Open',''),
	(46,'Old Grove','U6 B','Hamlin','Mature','Open',''),
	(47,'Old Grove','U6 C','Valencia','Mature','Open',''),
	(48,'Old Grove','U6 W 2','Valencia','Mature','Open',''),
	(49,'Old Grove','U7 A','Pineapple','Mature','Open',''),
	(50,'Old Grove','U7 C','Valencia','Mature','Open',''),
	(51,'Old Grove','U8 B','Valencia','Mature','Open',''),
	(52,'Old Grove','U8 C','Hamlin','Mature','Open',''),
	(53,'Old Grove','U8 W','Midsweet','Mature','Open',''),
	(54,'120','120 A East','Valencia','Mature','Open',''),
	(55,'120','120 A West','Valencia','Mature','Open',''),
	(56,'120','120 B East','Hamlin','Mature','Open',''),
	(57,'120','120 B West ','Valencia','Mature','Open',''),
	(58,'120','120 C East','Hamlin','Mature','Open',''),
	(59,'120','120 D East','Vernia','Mature','Open',''),
	(60,'120','120 D West','Midsweet','Mature','Open',''),
	(61,'120','120 E East','Hamlin','Mature','Open',''),
	(62,'120','120 G','Hamlin','Mature','Open',''),
	(63,'56','56 A','Hamlin','Mature','Open',''),
	(64,'56','56 B','Hamlin','Mature','Open',''),
	(65,'56','56 D East','Valencia','Mature','Open',''),
	(66,'56','56 D West','Hamlin','Mature','Open',''),
	(67,'56','56 E','Valencia','Mature','Open',''),
	(68,'56','56 F','Valencia','Mature','Open',''),
	(69,'56','56 G','Valencia','Mature','Open',''),
	(70,'56','56 H','Valencia','Mature','Open',''),
	(71,'NE','NEA East','Valencia','Mature','Open',''),
	(72,'NE','NE A West','Valencia','Mature','Open',''),
	(73,'NE','NE B ','Hamlin/Valencia','Mature','Open',''),
	(74,'NE','NE C','Valencia','Mature','Open',''),
	(75,'NE','NE D','Hamlin','Mature','Open',''),
	(76,'NE','NE C East','Hamlin','Mature','Open',''),
	(77,'NE','NE D East','Valencia','Mature','Open',''),
	(78,'NE','NE E MS','Honey Tangerine','Mature','Open',''),
	(79,'NE','NE E H','Hamlin','Mature','Open',''),
	(80,'NE','NE E East','Valencia','Mature','Open',''),
	(81,'NE','NE F','Hamlin','Mature','Open',''),
	(82,'NE','NE G HAM','Hamlin','Mature','Open',''),
	(83,'NE','NE G VAL','Valencia','Mature','Open',''),
	(84,'NE','NE H','Hamlin/Valencia','Mature','Open',''),
	(85,'NE','NE I H','Hamlin','Mature','Open',''),
	(86,'NE','NE I V','Valencia','Mature','Open',''),
	(87,'NE','NE J','Midsweet','Mature','Open',''),
	(88,'NE','NE K','Midsweet','Mature','Open',''),
	(89,'NW','NW C 1','Valencia','Mature','Open',''),
	(90,'NW','NW C 2','Valencia','Young','Open',''),
	(91,'NW','NW D 1','Hamlin','Young','Open',''),
	(92,'NW','NW D 2','Valencia','Mature','Open',''),
	(93,'NW','NW D 3','Ray Red','Mature','Open',''),
	(94,'NW','NW E','Valencia','Mature','Open',''),
	(95,'NW','NW E West','Valencia','Young','Open',''),
	(96,'NW','NW E East','Hamlin','Young','Open',''),
	(97,'NW','NW F VAL','Valencia','Young','Open',''),
	(98,'NW','NW F HAM','Hamlin','Young','Open',''),
	(99,'NW','NW G VAL','Valencia','Young','Open',''),
	(100,'NW','NW G HAM','Hamlin','Young','Open',''),
	(101,'NW','NW H VAL','Valencia','Young','Open',''),
	(102,'NW','NW H HAM','Hamlin','Young','Open',''),
	(103,'NW','NW I','Hamlin','Mature','Open',''),
	(104,'NW','NW J VAL','Valencia','Mature','Open',''),
	(105,'NW','NW J HAM','Hamlin','Mature','Open',''),
	(106,'NW','NW K VAL','Valencia','Mature','Open',''),
	(107,'NW','NW K HAM','Hamlin','Mature','Open',''),
	(108,'NW','NW K','Valencia','Mature','Open',''),
	(109,'NW','NW L 1','Valencia','Mature','Open',''),
	(110,'NW','NW L 2','Hamlin','Mature','Open',''),
	(111,'NW','NW L 3','Pineapple','Mature','Open',''),
	(112,'NW','NW M 1','Hamlin','Mature','Open',''),
	(113,'NW','NW M 2','Valencia','Mature','Open',''),
	(114,'NW','NW M 3','Hamlin','Mature','Open',''),
	(115,'NW','NW N','Hamlin','Mature','Open',''),
	(116,'NW','NW P','Hamlin','Mature','Open',''),
	(117,'NW','NWQ','Hamlin','Mature','Open',''),
	(118,'NW','NW R','Hamlin','Mature','Open',''),
	(119,'Nursury','107 NRS','Mixed','Mature','Open',''),
	(120,'Nursury','107 NRS West','Hamlin','Mature','Open',''),
	(121,'Old Grove','N81','Valencia','Young','Open',''),
	(122,'118','118A','Hamlin','Mature','Open',''),
	(123,'118','118B','Valencia','Mature','Open',''),
	(124,'118','118C','Hamlin','Mature','Open',''),
	(125,'118','118D','Hamlin','Mature','Open',''),
	(126,'118','118E','Valencia','Mature','Open',''),
	(127,'118','118F','Valencia','Mature','Open',''),
	(128,'118','118G','Valencia','Mature','Open',''),
	(129,'120','120C Reds','Ray Red','Mature','Open',''),
	(130,'Nursury','107 Li/Le','Lime/Lemon','Mature','Open',''),
	(131,'Old Grove','U5B','','Young','Open',''),
	(132,'120','120 D Young','','Young','Open','');

/*!40000 ALTER TABLE `scoutapp_field` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table scoutapp_labelledata
# ------------------------------------------------------------

DROP TABLE IF EXISTS `scoutapp_labelledata`;

CREATE TABLE `scoutapp_labelledata` (
  `id` int(11) DEFAULT NULL,
  `slug` int(11) DEFAULT NULL,
  `Field` text,
  `Age` text,
  `date` text,
  `stop` text,
  `adult` text,
  `eggs` text,
  `tapped` text,
  `flush` text,
  `OD` text,
  `LM` text,
  `SM` text,
  `Leafminer` longtext NOT NULL,
  `ODEggs` longtext NOT NULL,
  `ODLarva` longtext NOT NULL,
  `SpiderMites` longtext NOT NULL,
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `scoutapp_labelledata` WRITE;
/*!40000 ALTER TABLE `scoutapp_labelledata` DISABLE KEYS */;

INSERT INTO `scoutapp_labelledata` (`id`, `slug`, `Field`, `Age`, `date`, `stop`, `adult`, `eggs`, `tapped`, `flush`, `OD`, `LM`, `SM`, `Leafminer`, `ODEggs`, `ODLarva`, `SpiderMites`)
VALUES
	(1,1,'101 B',' ','2016-11-01','NW','0','0','0','0','OD','LM','SM',' ',' ',' ',' '),
	(2,2,'120 A East',' ','2016-11-02','C','4','3','2','1','OD','LM','SM',' ',' ',' ',' '),
	(3,3,'NE A West',' ','2016-11-02','SE','1','3','2','4','O','O','X',' ',' ',' ',' '),
	(4,4,'120 D Young','Mature','2016-11-09','NW','1','2','3','4','O','X','X',' ',' ',' ',' '),
	(5,5,'NW C 2','Mature','2016-11-10','NW','0','0','0','0','X','X','X',' ',' ',' ',' '),
	(6,6,'118B','Mature','2016-11-10','NW','0','0','0','0','X','X','X',' ',' ',' ',' '),
	(7,7,'120 D Young','Young','2016-11-10','NE','0','0',' ',' ',' ',' ',' ','0','0','0','none'),
	(8,8,'NW C 2','Young','2016-11-10','NE','0','1',' ',' ',' ',' ',' ','2','4','3','high'),
	(9,9,'NW E East','Young','2016-11-10','C','1','1',' ',' ',' ',' ',' ','1','0','0','high'),
	(10,10,'56 B','Mature','2016-11-10','NW','1','2','0','3','X','O','X',' ',' ',' ',' '),
	(11,11,'NW D 1','Young','2016-11-10','NW','1','3',' ',' ',' ',' ',' ','2','7','16','high'),
	(12,12,'101 B','Mature','2016-12-05','SE','3','4','5','6','O','O','O',' ',' ',' ',' '),
	(13,13,'102 A','Mature','2016-12-05','SE','1','2','3','4','X','X','X',' ',' ',' ',' '),
	(19,19,'101 B','Mature','2017-01-16','NW','3','0','0','0','X','X','X',' ',' ',' ',' '),
	(20,20,'120 A West','Mature','2016-12-05','SE','0','0','0','0','X','X','X',' ',' ',' ',' '),
	(21,21,'120 D Young','Young','2016-12-05','SE','0','0',' ',' ',' ',' ',' ','0','0','0','none'),
	(23,23,'118C','Mature','2016-12-06','NW','1','1','0','1','X','X','O',' ',' ',' ',' '),
	(18,18,'120 D Young','Young','2016-12-06','NW','0','0',' ',' ',' ',' ',' ','0','0','0','none'),
	(24,24,'107 NRS','Mature','2017-01-16','NW','0','0','0','0','X','X','X',' ',' ',' ',' '),
	(25,25,'102 B H','Mature','2017-01-17','NW','1','0','0','0','X','X','X',' ',' ',' ',' '),
	(26,26,'102 B H','Mature','2017-01-17','NE','2','0','0','0','X','X','X',' ',' ',' ',' '),
	(27,27,'101 B','Mature','2017-01-20','NW','1','0','0','0','X','X','X',' ',' ',' ',' '),
	(28,28,'101 B','Mature','2017-01-20','NE','2','0','0','0','X','X','X',' ',' ',' ',' '),
	(29,29,'101 B','Mature','2017-01-20','C','3','0','0','0','X','X','X',' ',' ',' ',' '),
	(30,30,'101 B','Mature','2017-01-20','SW','4','0','0','0','X','X','X',' ',' ',' ',' '),
	(31,31,'101 B','Mature','2017-01-20','SE','5','0','0','0','X','X','X',' ',' ',' ',' '),
	(32,32,'N 81','Mature','2017-02-02','NW','1','0','0','0','X','X','X',' ',' ',' ',' '),
	(33,33,'N 81','Mature','2017-02-02','NE','2','0','0','0','X','X','X',' ',' ',' ',' '),
	(34,34,'N 81','Mature','2017-02-02','C','3','0','0','0','X','X','X',' ',' ',' ',' '),
	(35,35,'N 81','Mature','2017-02-02','SW','4','0','0','0','X','X','X',' ',' ',' ',' '),
	(36,36,'N 81','Mature','2017-02-02','SE','5','0','0','0','X','X','X',' ',' ',' ',' '),
	(37,37,'120 D Young','Young','2017-02-02','NE','1','0',' ',' ',' ',' ',' ','0','0','0','none'),
	(38,38,'120 D Young','Young','2017-02-02','NW','2','0',' ',' ',' ',' ',' ','0','0','0','none'),
	(39,39,'120 D Young','Young','2017-02-02','C','0','0',' ',' ',' ',' ',' ','0','0','0','high'),
	(40,40,'120 D Young','Young','2017-02-02','SE','1','1',' ',' ',' ',' ',' ','1','1','1','medium'),
	(41,41,'120 D Young','Young','2017-02-02','SW','0','0',' ',' ',' ',' ',' ','5','11','0','none'),
	(42,42,'101 B','Mature','2017-02-03','NW','1','0','0','0','X','X','O',' ',' ',' ',' '),
	(43,43,'101 B','Mature','2017-02-03','NE','2','0','0','0','O','X','X',' ',' ',' ',' '),
	(44,44,'101 B','Mature','2017-02-03','C','3','0','0','0','X','X','X',' ',' ',' ',' '),
	(45,45,'101 B','Mature','2017-02-03','SW','4','0','0','5','X','X','X',' ',' ',' ',' '),
	(46,46,'101 B','Mature','2017-02-03','SE','0','3','1','20','X','X','O',' ',' ',' ',' '),
	(47,47,'120 D Young','Young','2017-02-03','NW','5','1',' ',' ',' ',' ',' ','1','1','1','medium'),
	(48,48,'120 D Young','Young','2017-02-03','NE','3','0',' ',' ',' ',' ',' ','0','0','0','low'),
	(49,49,'120 D Young','Young','2017-02-03','C','3','0',' ',' ',' ',' ',' ','0','0','0','none'),
	(50,50,'120 D Young','Young','2017-02-03','SW','0','0',' ',' ',' ',' ',' ','0','0','0','medium'),
	(51,51,'120 D Young','Young','2017-02-03','SE','0','9',' ',' ',' ',' ',' ','0','0','0','medium'),
	(52,52,'102 A','Mature','2017-02-03','','1','0','0','0','X','X','X',' ',' ',' ',' '),
	(53,53,'102 A','Mature','2017-02-03','NW','2','0','0','0','X','X','X',' ',' ',' ',' '),
	(54,54,'102 A','Mature','2017-02-03','NE','1','1','0','0','X','X','X',' ',' ',' ',' '),
	(55,55,'102 A','Mature','2017-02-03','C','9','0','0','0','X','X','X',' ',' ',' ',' '),
	(56,56,'102 A','Mature','2017-02-03','SW','0','0','0','12','X','X','X',' ',' ',' ',' '),
	(57,57,'102 A','Mature','2017-02-03','SE','0','0','1','0','X','X','X',' ',' ',' ',' '),
	(58,58,'102 B H','Mature','2017-02-03','NW','3','2','0','3','X','X','O',' ',' ',' ',' '),
	(59,59,'102 B H','Mature','2017-02-03','C','4','3','6','8','O','X','X',' ',' ',' ',' '),
	(60,60,'102 B H','Mature','2017-02-03','NE','0','0','0','0','X','X','X',' ',' ',' ',' '),
	(61,61,'NW C 2','Young','2017-02-03','NW','1','0',' ',' ',' ',' ',' ','0','0','0','none'),
	(62,62,'NW C 2','Young','2017-02-03','NE','4','0',' ',' ',' ',' ',' ','0','0','0','none'),
	(63,63,'NW C 2','Young','2017-02-03','C','0','3',' ',' ',' ',' ',' ','0','0','0','none'),
	(64,64,'NW C 2','Young','2017-02-03','SE','0','0',' ',' ',' ',' ',' ','0','0','0','none'),
	(65,65,'NW C 2','Young','2017-02-03','SW','0','0',' ',' ',' ',' ',' ','0','0','0','none'),
	(66,66,'101 B','Mature','2017-02-04','NW','3','1','2','2','X','X','O',' ',' ',' ',' '),
	(67,67,'101 B','Mature','2017-02-04','NE','2','2','2','2','X','X','X',' ',' ',' ',' '),
	(68,68,'101 B','Mature','2017-02-07','NW','7','23','0','20','X','X','X',' ',' ',' ',' '),
	(69,69,'120 A East','Mature','2017-02-08','NW','33','07','0','20','O','X','X',' ',' ',' ',' '),
	(70,70,'120 A East','Mature','2017-02-08','NE','3','3','3','3','X','X','O',' ',' ',' ',' '),
	(71,71,'120 A East','Mature','2017-02-08','C','0','0','09','0','X','X','X',' ',' ',' ',' '),
	(72,72,'120 A East','Mature','2017-02-08','SW','0','0','0','0','X','X','X',' ',' ',' ',' '),
	(73,73,'120 A East','Mature','2017-02-08','SE','1','1','1','1','X','X','X',' ',' ',' ',' '),
	(74,74,'120 A East','Mature','2017-02-09','NW','1','0','0','0','X','X','X',' ',' ',' ',' '),
	(75,75,'120 A East','Mature','2017-02-09','NE','1.0','0','0','0','X','X','X',' ',' ',' ',' ');

/*!40000 ALTER TABLE `scoutapp_labelledata` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table scoutapp_labellefieldorder
# ------------------------------------------------------------

DROP TABLE IF EXISTS `scoutapp_labellefieldorder`;

CREATE TABLE `scoutapp_labellefieldorder` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fieldName` longtext NOT NULL,
  `order` longtext NOT NULL,
  `age` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `scoutapp_labellefieldorder` WRITE;
/*!40000 ALTER TABLE `scoutapp_labellefieldorder` DISABLE KEYS */;

INSERT INTO `scoutapp_labellefieldorder` (`id`, `fieldName`, `order`, `age`)
VALUES
	(1,'101 B','1','Mature'),
	(2,'102 A','2','Mature'),
	(3,'102 B','3','Mature'),
	(4,'102 B ','4','Mature'),
	(5,'103 South','5','Mature'),
	(6,'104 A','6','Mature'),
	(7,'104 B','7','Mature'),
	(8,'104 B','8','Mature'),
	(9,'105 A','9','Mature'),
	(10,'105 B ','10','Mature'),
	(11,'105 C','11','Mature'),
	(12,'105 D','12','Mature'),
	(13,'53 C West 1','13','Mature'),
	(14,'53 C West 2','14','Mature'),
	(15,'53 D 1 (West)','15','Mature'),
	(16,'53 D 2 (East)','16','Mature'),
	(17,'53 E 1 (West)','17','Mature'),
	(18,'53 E 2 (East)','18','Mature'),
	(19,'53 F','19','Mature'),
	(20,'53 G','20','Mature'),
	(21,'53 C east','21','Mature'),
	(22,'53 D east','22','Mature'),
	(23,'53 E east','23','Mature'),
	(24,'53 F east','24','Mature'),
	(25,'53 G east','25','Mature'),
	(26,'9250 A','26','Mature'),
	(27,'9250 B','27','Mature'),
	(28,'9250 C','28','Mature'),
	(29,'9250 G','29','Mature'),
	(30,'NO3 ','30','Mature'),
	(31,'NO3','31','Mature'),
	(32,'LL 1','32','Mature'),
	(33,'LL 2','33','Mature'),
	(34,'N 81','34','Mature'),
	(35,'QS','35','Mature'),
	(36,'U 12 North','36','Mature'),
	(37,'U 12 South','37','Mature'),
	(38,'U 80','38','Mature'),
	(39,'U1 C','39','Mature'),
	(40,'U3 B East','40','Mature'),
	(41,'U3 C','41','Mature'),
	(42,'U4 C','42','Mature'),
	(43,'U5A','43','Mature'),
	(44,'U6 A','44','Mature'),
	(45,'U6 B','45','Mature'),
	(46,'U6 C','46','Mature'),
	(47,'U6 W 2','47','Mature'),
	(48,'U8W','48','Mature'),
	(49,'U7 A','49','Mature'),
	(50,'U7 C','50','Mature'),
	(51,'U8 B','51','Mature'),
	(52,'U8 C','52','Mature'),
	(53,'120 A East','53','Mature'),
	(54,'120 A West','54','Mature'),
	(55,'120 B East','55','Mature'),
	(56,'120 B West ','56','Mature'),
	(57,'120 C East','57','Mature'),
	(58,'120 D East','58','Mature'),
	(59,'120 D West','59','Mature'),
	(60,'120 E East','60','Mature'),
	(61,'120 G','61','Mature'),
	(62,'56 A','62','Mature'),
	(63,'56 B','63','Mature'),
	(64,'56 D','64','Mature'),
	(65,'56 D','65','Mature'),
	(66,'56 E','66','Mature'),
	(67,'56 F','67','Mature'),
	(68,'56 G','68','Mature'),
	(69,'56 H','69','Mature'),
	(70,'NE C East','70','Mature'),
	(71,'NE D East','71','Mature'),
	(72,'NE E','72','Mature'),
	(73,'NE E East','73','Mature'),
	(74,'NE G VAL','74','Mature'),
	(75,'NW C 2','75','Mature'),
	(76,'NW D','76','Mature'),
	(77,'NW D','77','Mature'),
	(78,'NW E 2','78','Mature'),
	(79,'NW L 2','79','Mature'),
	(80,'NW L 3','80','Mature'),
	(81,'NW M 1','81','Mature'),
	(82,'NW M 2','82','Mature'),
	(83,'NW M 3','83','Mature'),
	(84,'NW N','84','Mature'),
	(85,'NW P','85','Mature'),
	(86,'NWQ','86','Mature'),
	(87,'NW R','87','Mature'),
	(88,'NW I','88','Mature'),
	(89,'NW J VAL','89','Mature'),
	(90,'NW J HAM','90','Mature'),
	(91,'NW K 1','91','Mature'),
	(92,'NW K 2','92','Mature'),
	(93,'NW K 3','93','Mature'),
	(94,'NW L 1','94','Mature'),
	(95,'NE A ','95','Mature'),
	(96,'NE B ','96','Mature'),
	(97,'NE C','97','Mature'),
	(98,'NE D','98','Mature'),
	(99,'NE E','99','Mature'),
	(100,'NE F','100','Mature'),
	(101,'NE G HAM','101','Mature'),
	(102,'NE H','102','Mature'),
	(103,'NE I','103','Mature'),
	(104,'NE I','104','Mature'),
	(105,'NE J','105','Mature'),
	(106,'NE K','106','Mature'),
	(107,'118A','107','Mature'),
	(108,'118B','108','Mature'),
	(109,'118C','109','Mature'),
	(110,'118D','110','Mature'),
	(111,'118E','111','Mature'),
	(112,'118F','112','Mature'),
	(113,'118G','113','Mature'),
	(114,'120C Reds','114','Mature'),
	(115,'U8 W','115','Mature'),
	(116,'U3 B West','116','Mature'),
	(117,'107 NRS','117','Mature'),
	(118,'107 NRS West','118','Mature'),
	(119,'107 Li/Le','119','Mature'),
	(120,'N81 (V)','1','Young'),
	(121,'U5B','2','Young'),
	(122,'120 D','3','Young'),
	(123,'NWC (V) 1','4','Young'),
	(124,'NWD (H)','5','Young'),
	(125,'NWE (V) 1','6','Young'),
	(126,'NWE (H) 3','7','Young'),
	(127,'NWF  (H)','8','Young'),
	(128,'NWF (V)','9','Young'),
	(129,'NWG (V)','10','Young'),
	(130,'NWG (H)','11','Young'),
	(131,'NWH (V)','12','Young'),
	(132,'NWH (H)','13','Young');

/*!40000 ALTER TABLE `scoutapp_labellefieldorder` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table scoutapp_scoutingareas
# ------------------------------------------------------------

DROP TABLE IF EXISTS `scoutapp_scoutingareas`;

CREATE TABLE `scoutapp_scoutingareas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `location` longtext NOT NULL,
  `scoutedItem` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `scoutapp_scoutingareas` WRITE;
/*!40000 ALTER TABLE `scoutapp_scoutingareas` DISABLE KEYS */;

INSERT INTO `scoutapp_scoutingareas` (`id`, `location`, `scoutedItem`)
VALUES
	(1,'Labelle','Psyllids');

/*!40000 ALTER TABLE `scoutapp_scoutingareas` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table test2
# ------------------------------------------------------------

DROP TABLE IF EXISTS `test2`;

CREATE TABLE `test2` (
  `id` varchar(255) DEFAULT NULL,
  `slug` int(11) DEFAULT NULL,
  `area` varchar(255) DEFAULT NULL,
  `fieldName` varchar(255) DEFAULT NULL,
  `variety` varchar(255) DEFAULT NULL,
  `age` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `chemical` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `test2` WRITE;
/*!40000 ALTER TABLE `test2` DISABLE KEYS */;

INSERT INTO `test2` (`id`, `slug`, `area`, `fieldName`, `variety`, `age`, `status`, `chemical`)
VALUES
	('',1,'100','101 B','Valencia','Mature','Open',''),
	('',2,'100','102 A','Valencia','Mature','Open',''),
	('',3,'100','102 B H','Hamlin','Mature','Open',''),
	('',4,'100','102 B V','Valencia','Mature','Open',''),
	('',5,'100','103 South','Valencia','Mature','Open',''),
	('',6,'100','104 A','Valencia','Mature','Open',''),
	('',7,'100','104 B H','Hamlin','Mature','Open',''),
	('',8,'100','104 B P','Pineapple','Mature','Open',''),
	('',9,'100','105 A','Hamlin','Mature','Open',''),
	('',10,'100','105 B ','Pineapple','Mature','Open',''),
	('',11,'100','105 C','Pineapple','Mature','Open',''),
	('',12,'100','105 D','Ruby Red','Mature','Open',''),
	('',13,'53','53 C West 1','Valencia','Mature','Open',''),
	('',14,'53','53 C West 2','Valencia','Mature','Open',''),
	('',15,'53','53 D 1 (West)','Hamlin','Mature','Open',''),
	('',16,'53','53 D 2 (East)','Hamlin','Mature','Open',''),
	('',17,'53','53 E 1 (West)','Hamlin','Mature','Open',''),
	('',18,'53','53 E 2 (East)','Hamlin','Mature','Open',''),
	('',19,'53','53 F','Hamlin','Mature','Open',''),
	('',20,'53','53 G','Hamlin/Valencia','Mature','Open',''),
	('',21,'53','53 C east','Hamlin','Mature','Open',''),
	('',22,'53','53 D east','Hamlin','Mature','Open',''),
	('',23,'53','53 E east','Valencia','Mature','Open',''),
	('',24,'53','53 F east','Valencia','Mature','Open',''),
	('',25,'53','53 G east','Valencia','Mature','Open',''),
	('',26,'9250','9250 A','Hamlin','Mature','Open',''),
	('',27,'9250','9250 B','Hamlin','Mature','Open',''),
	('',28,'9250','9250 C','Hamlin','Mature','Open',''),
	('',29,'9250','9250 G','Valencia','Mature','Open',''),
	('',30,'100','NO3 P','Pineapple','Mature','Open',''),
	('',31,'100','NO3V','Valencia','Mature','Open',''),
	('',32,'100','LL 1','','Mature','Open',''),
	('',33,'100','LL 2','','Mature','Open',''),
	('',34,'Old Grove','N 81','Pineapple','Mature','Open',''),
	('',35,'Old Grove','QS','Valencia','Mature','Open',''),
	('',36,'Old Grove','U 12 North','Valencia','Mature','Open',''),
	('',37,'Old Grove','U 12 South','Valencia','Mature','Open',''),
	('',38,'Old Grove','U 80','Pineapple','Mature','Open',''),
	('',39,'Old Grove','U1 C','Valencia','Mature','Open',''),
	('',40,'Old Grove','U3 B West','Hamlin','Mature','Open',''),
	('',41,'Old Grove','U3 B East','Valencia','Mature','Open',''),
	('',42,'Old Grove','U3 C','Hamlin','Mature','Open',''),
	('',43,'Old Grove','U4 C','Valencia','Mature','Open',''),
	('',44,'Old Grove','U5A','Hamlin','Mature','Open',''),
	('',45,'Old Grove','U6 A','Valencia','Mature','Open',''),
	('',46,'Old Grove','U6 B','Hamlin','Mature','Open',''),
	('',47,'Old Grove','U6 C','Valencia','Mature','Open',''),
	('',48,'Old Grove','U6 W 2','Valencia','Mature','Open',''),
	('',49,'Old Grove','U7 A','Pineapple','Mature','Open',''),
	('',50,'Old Grove','U7 C','Valencia','Mature','Open',''),
	('',51,'Old Grove','U8 B','Valencia','Mature','Open',''),
	('',52,'Old Grove','U8 C','Hamlin','Mature','Open',''),
	('',53,'Old Grove','U8 W','Midsweet','Mature','Open',''),
	('',54,'120','120 A East','Valencia','Mature','Open',''),
	('',55,'120','120 A West','Valencia','Mature','Open',''),
	('',56,'120','120 B East','Hamlin','Mature','Open',''),
	('',57,'120','120 B West ','Valencia','Mature','Open',''),
	('',58,'120','120 C East','Hamlin','Mature','Open',''),
	('',59,'120','120 D East','Vernia','Mature','Open',''),
	('',60,'120','120 D West','Midsweet','Mature','Open',''),
	('',61,'120','120 E East','Hamlin','Mature','Open',''),
	('',62,'120','120 G','Hamlin','Mature','Open',''),
	('',63,'56','56 A','Hamlin','Mature','Open',''),
	('',64,'56','56 B','Hamlin','Mature','Open',''),
	('',65,'56','56 D East','Valencia','Mature','Open',''),
	('',66,'56','56 D West','Hamlin','Mature','Open',''),
	('',67,'56','56 E','Valencia','Mature','Open',''),
	('',68,'56','56 F','Valencia','Mature','Open',''),
	('',69,'56','56 G','Valencia','Mature','Open',''),
	('',70,'56','56 H','Valencia','Mature','Open',''),
	('',71,'NE','NEA East','Valencia','Mature','Open',''),
	('',72,'NE','NE A West','Valencia','Mature','Open',''),
	('',73,'NE','NE B ','Hamlin/Valencia','Mature','Open',''),
	('',74,'NE','NE C','Valencia','Mature','Open',''),
	('',75,'NE','NE D','Hamlin','Mature','Open',''),
	('',76,'NE','NE C East','Hamlin','Mature','Open',''),
	('',77,'NE','NE D East','Valencia','Mature','Open',''),
	('',78,'NE','NE E MS','Honey Tangerine','Mature','Open',''),
	('',79,'NE','NE E H','Hamlin','Mature','Open',''),
	('',80,'NE','NE E East','Valencia','Mature','Open',''),
	('',81,'NE','NE F','Hamlin','Mature','Open',''),
	('',82,'NE','NE G HAM','Hamlin','Mature','Open',''),
	('',83,'NE','NE G VAL','Valencia','Mature','Open',''),
	('',84,'NE','NE H','Hamlin/Valencia','Mature','Open',''),
	('',85,'NE','NE I H','Hamlin','Mature','Open',''),
	('',86,'NE','NE I V','Valencia','Mature','Open',''),
	('',87,'NE','NE J','Midsweet','Mature','Open',''),
	('',88,'NE','NE K','Midsweet','Mature','Open',''),
	('',89,'NW','NW C 1','Valencia','Mature','Open',''),
	('',90,'NW','NW C 2','Valencia','Young','Open',''),
	('',91,'NW','NW D 1','Hamlin','Young','Open',''),
	('',92,'NW','NW D 2','Valencia','Mature','Open',''),
	('',93,'NW','NW D 3','Ray Red','Mature','Open',''),
	('',94,'NW','NW E','Valencia','Mature','Open',''),
	('',95,'NW','NW E West','Valencia','Young','Open',''),
	('',96,'NW','NW E East','Hamlin','Young','Open',''),
	('',97,'NW','NW F VAL','Valencia','Young','Open',''),
	('',98,'NW','NW F HAM','Hamlin','Young','Open',''),
	('',99,'NW','NW G VAL','Valencia','Young','Open',''),
	('',100,'NW','NW G HAM','Hamlin','Young','Open',''),
	('',101,'NW','NW H VAL','Valencia','Young','Open',''),
	('',102,'NW','NW H HAM','Hamlin','Young','Open',''),
	('',103,'NW','NW I','Hamlin','Mature','Open',''),
	('',104,'NW','NW J VAL','Valencia','Mature','Open',''),
	('',105,'NW','NW J HAM','Hamlin','Mature','Open',''),
	('',106,'NW','NW K VAL','Valencia','Mature','Open',''),
	('',107,'NW','NW K HAM','Hamlin','Mature','Open',''),
	('',108,'NW','NW K','Valencia','Mature','Open',''),
	('',109,'NW','NW L 1','Valencia','Mature','Open',''),
	('',110,'NW','NW L 2','Hamlin','Mature','Open',''),
	('',111,'NW','NW L 3','Pineapple','Mature','Open',''),
	('',112,'NW','NW M 1','Hamlin','Mature','Open',''),
	('',113,'NW','NW M 2','Valencia','Mature','Open',''),
	('',114,'NW','NW M 3','Hamlin','Mature','Open',''),
	('',115,'NW','NW N','Hamlin','Mature','Open',''),
	('',116,'NW','NW P','Hamlin','Mature','Open',''),
	('',117,'NW','NWQ','Hamlin','Mature','Open',''),
	('',118,'NW','NW R','Hamlin','Mature','Open',''),
	('',119,'Nursury','107 NRS','Mixed','Mature','Open',''),
	('',120,'Nursury','107 NRS West','Hamlin','Mature','Open',''),
	('',121,'Old Grove','N81','Valencia','Young','Open',''),
	('',122,'118','118A','Hamlin','Mature','Open',''),
	('',123,'118','118B','Valencia','Mature','Open',''),
	('',124,'118','118C','Hamlin','Mature','Open',''),
	('',125,'118','118D','Hamlin','Mature','Open',''),
	('',126,'118','118E','Valencia','Mature','Open',''),
	('',127,'118','118F','Valencia','Mature','Open',''),
	('',128,'118','118G','Valencia','Mature','Open',''),
	('',129,'120','120C Reds','Ray Red','Mature','Open',''),
	('',130,'Nursury','107 Li/Le','Lime/Lemon','Mature','Open',''),
	('',131,'Old Grove','U5B','','Young','Open',''),
	('',132,'120','120 D Young','','Young','Open','');

/*!40000 ALTER TABLE `test2` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
