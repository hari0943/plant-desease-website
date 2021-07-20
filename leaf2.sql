/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.5.20-log : Database - leaf
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`leaf` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `leaf`;

/*Table structure for table `agriculture` */

DROP TABLE IF EXISTS `agriculture`;

CREATE TABLE `agriculture` (
  `officer_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(15) DEFAULT NULL,
  `dob` varchar(15) DEFAULT NULL,
  `place` varchar(15) DEFAULT NULL,
  `pin` varchar(15) DEFAULT NULL,
  `qualification` varchar(15) DEFAULT NULL,
  `experience` varchar(15) DEFAULT NULL,
  `email` varchar(15) DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `login_id` int(15) DEFAULT NULL,
  `image` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`officer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `agriculture` */

insert  into `agriculture`(`officer_id`,`name`,`dob`,`place`,`pin`,`qualification`,`experience`,`email`,`phone`,`login_id`,`image`) values (3,'anju','2021-01-08','jhgjk','98789','sslc','7','anju@gmail.com','8798',18,'/static/officer/Capture.PNG'),(4,'aiswarya','2001-05-10','perambra','673525','bca','3','aiswaryakrishna','9745453569',22,'/static/officer/IMG_20200702_115905.jpg'),(5,'neethu','2000-05-01','yewtuygteyer','673525','asd','3','uieruzg','955855454',24,'/static/officer/IMG_20200702_115905.jpg'),(6,'officer1','2021-04-28','plc1','673005','qul1','expr1','officer1@gmail.','8547963021',30,'/static/officer/Capture.PNG'),(7,'officer2','2021-04-10','plc2','673005','qul2','expr2','officer1@gmail.','8547963021',32,'/static/officer/Capture.PNG');

/*Table structure for table `complaints` */

DROP TABLE IF EXISTS `complaints`;

CREATE TABLE `complaints` (
  `complaints_id` int(11) NOT NULL AUTO_INCREMENT,
  `farmer_id` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `replay` varchar(15) DEFAULT NULL,
  `complaints` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`complaints_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;

/*Data for the table `complaints` */

insert  into `complaints`(`complaints_id`,`farmer_id`,`date`,`replay`,`complaints`) values (1,123325,'0000-00-00',']',NULL),(2,454646,'0000-00-00','gfsadhj',NULL),(3,454646,'0000-00-00','gfsadhj',NULL),(4,23,'0000-00-00','ok','bad'),(5,6788,'0000-00-00','7hjh',NULL),(6,27,'2021-02-23','pending','vj'),(7,27,'2021-02-23','pending','hdhsjs'),(8,27,'2021-02-23','pending','hdhsjs'),(9,27,'2021-02-23','pending','hdhsjs'),(10,27,'2021-02-23','pending','hdhsjs'),(11,27,'2021-02-23','pending','hdhsjs'),(12,27,'2021-02-23','pending','hdhsjs'),(13,27,'2021-02-23','pending','adf'),(14,27,'2021-02-23','pending','aa'),(15,27,'2021-03-01','pending','not working'),(16,44,'2021-04-10','rplyhh','gsjsjjdjdjdd');

/*Table structure for table `doubts` */

DROP TABLE IF EXISTS `doubts`;

CREATE TABLE `doubts` (
  `doubts_id` int(11) NOT NULL AUTO_INCREMENT,
  `doubts` varchar(15) DEFAULT NULL,
  `date` varchar(15) DEFAULT NULL,
  `farmer_id` int(11) DEFAULT NULL,
  `replay` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`doubts_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `doubts` */

insert  into `doubts`(`doubts_id`,`doubts`,`date`,`farmer_id`,`replay`) values (1,'resery','12',27,'ok'),(2,'guitar','2021-02-27',27,'pending'),(3,'\"+doubts+\"','2021-02-27',0,'pending'),(4,'mkkj','2021-03-01',27,'pending'),(5,'yddyfigy','2021-04-10',44,'pending');

/*Table structure for table `farmer` */

DROP TABLE IF EXISTS `farmer`;

CREATE TABLE `farmer` (
  `farmer_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(15) DEFAULT NULL,
  `dob` varchar(15) DEFAULT NULL,
  `gender` varchar(15) DEFAULT NULL,
  `place` varchar(15) DEFAULT NULL,
  `pin` varchar(15) DEFAULT NULL,
  `email` varchar(15) DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `login_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`farmer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `farmer` */

insert  into `farmer`(`farmer_id`,`name`,`dob`,`gender`,`place`,`pin`,`email`,`phone`,`login_id`) values (1,'anu','10','f','perambra','673525','nkn@fg','9562853569',27),(2,'Likhil','Likhil','Male','Likhil','Likhil','Likhil','Likhil',43),(3,'aravind','2000-01-01','Male','kakkodi','673611','aravind@gmail.c','987645321',44);

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `farmer_id` int(12) DEFAULT NULL,
  `feedback` varchar(15) DEFAULT NULL,
  `date` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`farmer_id`,`feedback`,`date`) values (1,23,'bad',NULL),(2,27,'fffgggggggffg','2021-02-23'),(3,27,'fddd','2021-02-23'),(4,27,'good','2021-03-01'),(5,27,'good','2021-03-01'),(6,44,'chvug','2021-04-10');

/*Table structure for table `fertilizer` */

DROP TABLE IF EXISTS `fertilizer`;

CREATE TABLE `fertilizer` (
  `fertilizer_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(15) DEFAULT NULL,
  `pic` varchar(100) DEFAULT NULL,
  `descrription` varchar(15) DEFAULT NULL,
  KEY `fertilizer_id` (`fertilizer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;

/*Data for the table `fertilizer` */

insert  into `fertilizer`(`fertilizer_id`,`name`,`pic`,`descrription`) values (15,'fr4','/static/fertilizer/Capture.PNG','ds2'),(16,'fueradan','/static/fertilizer/Capture.PNG','ghjjjh');

/*Table structure for table `history` */

DROP TABLE IF EXISTS `history`;

CREATE TABLE `history` (
  `history_id` int(11) NOT NULL AUTO_INCREMENT,
  `file` varchar(15) DEFAULT NULL,
  `leaf_id` int(11) DEFAULT NULL,
  `farmer_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`history_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `history` */

/*Table structure for table `leaf` */

DROP TABLE IF EXISTS `leaf`;

CREATE TABLE `leaf` (
  `leaf_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `phtoto` varchar(200) DEFAULT NULL,
  `discreption` varchar(200) DEFAULT NULL,
  `disease` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`leaf_id`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=latin1;

/*Data for the table `leaf` */

insert  into `leaf`(`leaf_id`,`name`,`phtoto`,`discreption`,`disease`) values (18,'Apple','/static/images/0a5e9323-dbad-432d-ac58-d291718345d9___FREC_Scab 3417_90deg.JPG','Apple Scab','Apple___Apple_scab'),(19,'Apple','/static/images/00e909aa-e3ae-4558-9961-336bb0f35db3___JR_FrgE.S 8593.JPG','black rot','Apple___Black_rot'),(20,'apple','/static/images/0a41c25a-f9a6-4c34-8e5c-7f89a6ac4c40___FREC_C.Rust 9807.JPG','Cedar apple rus','Apple___Cedar_apple_rust'),(21,'Apple','/static/images/00a6039c-e425-4f7d-81b1-d6b0e668517e___RS_HL 7669.JPG','Healthy','Apple___healthy'),(22,'cherry','/static/images/0a0bd696-c093-47ef-866b-7f5a40af3edb___JR_HL 3952.JPG','Healthy','Cherry_(including_sour)___healthy'),(23,'cherry','/static/images/00b7df55-c789-43d6-a02e-a579ac9d07e6___FREC_Pwd.M 4748.JPG','Powdery_mildew','Cherry_(including_sour)___Powdery_mildew'),(24,'corn','/static/images/00a20f6f-e8bd-4453-9e25-36ea70feb626___RS_GLSp 4655.JPG','Gray_leaf_spot','Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot'),(25,'corn','/static/images/RS_Rust 1563.JPG','common rust','Corn_(maize)___Common_rust_'),(26,'corn','/static/images/0a1a49a8-3a95-415a-b115-4d6d136b980b___R.S_HL 8216 copy.jpg','Healthy','Corn_(maize)___healthy'),(27,'corn','/static/images/0a11f9e8-7357-48c2-8550-daeae59a1e76___RS_NLB 3588.JPG','Northern_Leaf_B','Corn_(maize)___Northern_Leaf_Blight'),(28,'grape','/static/images/00cab05d-e87b-4cf6-87d8-284f3ec99626___FAM_B.Rot 3244.JPG','Grape black rot','Grape___Black_rot'),(29,'grape','/static/images/00b65fe8-cee1-4b68-8ef4-1211814f2845___FAM_B.Msls 3990.JPG','esca','Grape___Esca_(Black_Measles)'),(30,'grape','/static/images/00e00912-bf75-4cf8-8b7d-ad64b73bea5f___Mt.N.V_HL 6067.JPG','Healthy','Grape___healthy'),(31,'grape','/static/images/00a962ad-573b-44b1-97ae-912a6bd6e0b0___FAM_L.Blight 1431.JPG','lsariopsis_Leaf','Grape___Leaf_blight_(Isariopsis_Leaf_Spot)'),(32,'orange','/static/images/3330bad2-38aa-40bd-9938-6128efd96327___UF.Citrus_HLB_Lab 1497.JPG','citrus greening','Orange___Haunglongbing_(Citrus_greening)'),(33,'peach','/static/images/00ddc106-692e-4c67-b2e8-569c924caf49___Rutg._Bact.S 1228.JPG','bacterial spot','Peach___Bacterial_spot'),(34,'peach','/static/images/0a2ed402-5d23-4e8d-bc98-b264aea9c3fb___Rutg._HL 2471.JPG','Healthy','Peach___healthy'),(35,'pepper bell','/static/images/00f2e69a-1e56-412d-8a79-fdce794a17e4___JR_B.Spot 3132.JPG','bacterial spot','Pepper,_bell___Bacterial_spot'),(36,'pepper bell','/static/images/0a3f2927-4410-46a3-bfda-5f4769a5aaf8___JR_HL 8275.JPG','Healthy','Pepper,_bell___healthy'),(37,'potato','/static/images/0a8a68ee-f587-4dea-beec-79d02e7d3fa4___RS_Early.B 8461.JPG','early blight','Potato___Early_blight'),(38,'potato','/static/images/00fc2ee5-729f-4757-8aeb-65c3355874f2___RS_HL 1864.JPG','Healthy','Potato___healthy'),(39,'potato','/static/images/00b1f292-23dd-44d4-aad3-c1ffb6a6ad5a___RS_LB 4479.JPG','late blight','Potato___Late_blight'),(40,'raspberry','/static/images/00a3fc0e-64cc-4e35-ac2f-aef04fda9b22___Mary_HL 9177.JPG','Healthy','Raspberry___healthy'),(41,'soyabean','/static/images/6033b6c1-a12a-4c11-9e19-d7ec164b151c___RS_HL 3916.JPG','Healthy','Soybean___healthy'),(42,'squash','/static/images/00a90bbc-a12c-426d-bcc8-fadb371ea6d0___UMD_Powd.M 0358_flipLR.JPG','Powdery_mildew','Squash___Powdery_mildew'),(43,'strawberry','/static/images/00e9a277-ca5e-4350-95ce-8b2918b69fb9___RS_HL 4667.JPG','Healthy','Strawberry___healthy'),(44,'strawberry','/static/images/0a08af15-adfe-447c-8ed4-17ed2702d810___RS_L.Scorch 0054.JPG','leaf scorch','Strawberry___Leaf_scorch'),(45,'tomato','/static/images/00a7c269-3476-4d25-b744-44d6353cd921___GCREC_Bact.Sp 5807.JPG','bacterial spot','Tomato___Bacterial_spot'),(46,'tomato','/static/images/00c5c908-fc25-4710-a109-db143da23112___RS_Erly.B 7778.JPG','early blight','Tomato___Early_blight'),(47,'tomato','/static/images/000bf685-b305-408b-91f4-37030f8e62db___GH_HL Leaf 308.1_new30degFlipLR.JPG','Healthy','Tomato___healthy'),(48,'tomato','/static/images/0a3f65fc-ef1c-4aed-b235-46bae4e5c0e7___GHLB2 Leaf 9065_flipLR.JPG','late blight','Tomato___Late_blight'),(49,'tomato','/static/images/0a9b3ff4-5343-4814-ac2c-fdb3613d4e4d___Crnl_L.Mold 6559.JPG','leaf mold','Tomato___Leaf_Mold'),(50,'tomato','/static/images/00f16858-f392-4d9e-ad9f-efab8049a13f___JR_Sept.L.S 8368.JPG','Septoria_leaf_s','Tomato___Septoria_leaf_spot'),(51,'tomato','/static/images/00bc7858-1dca-4bfb-a828-225f03bd72a5___Com.G_SpM_FL 9455_180deg.JPG','Two-spotted_spi','Tomato___Spider_mites Two-spotted_spider_mite'),(52,'tomato','/static/images/0a2de4c5-d688-4f9d-9107-ace1d281c307___Com.G_TgS_FL 7941.JPG','target spot','Tomato___Target_Spot'),(53,'tomato','/static/images/000ec6ea-9063-4c33-8abe-d58ca8a88878___PSU_CG 2169.JPG','mosaic virus','Tomato___Tomato_mosaic_virus'),(54,'tomato','/static/images/10239cd2-1e83-45d0-b40d-816316d705d4___YLCV_GCREC 2393.JPG','Yellow_Leaf_Cur','Tomato___Tomato_Yellow_Leaf_Curl_Virus'),(55,'Blueberry','/static/images/00fee259-67b7-4dd7-8b36-12503bbdba14___RS_HL 2681_180deg.JPG','Blueberry___healthy','Blueberry___healthy');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(25) DEFAULT NULL,
  `password` varchar(25) DEFAULT NULL,
  `type` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`user_name`,`password`,`type`) values (2,'sa','sa','subadmin'),(5,'adkjfvhdjkf','jhgju','subadmin'),(17,'anu@gmail.com','anu123','subadmin'),(18,'anju@gmail.com','a','officer'),(19,'admin','123','admin'),(20,'s','s','subadmin'),(21,'kmsreelakshimi@','123456','subadmin'),(22,'aiswaryakrishna','1421','officer'),(23,'grdhhgjf','appukuttan','subadmin'),(24,'uieruzg','7759','officer'),(25,'','','subadmin'),(26,'','','subadmin'),(27,'f','f','farmer'),(28,'gg','aaa','subadmin'),(29,'subadmin1@gmail.com','subadmin1','subadmin'),(30,'officer1@gmail.','2141','officer'),(31,'officer1@gmail.','offcr1','subadmin'),(32,'officer1@gmail.','9893','officer'),(33,'sub2','psw2','subadmin'),(34,'Likhil','Likhil','farmer'),(35,'sub3','psw3','subadmin'),(36,'Likhil','Likhil','farmer'),(37,'Likhil','Likhil','farmer'),(38,'Likhil','Likhil','farmer'),(39,'Likhil','Likhil','farmer'),(40,'Likhil','Likhil','farmer'),(41,'Likhil','Likhil','farmer'),(42,'Likhil','Likhil','farmer'),(43,'Likhil','Likhil','farmer'),(44,'aravind@gmail.c','a','farmer'),(45,'sub4@gmail.com','psw4','subadmin');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `noti_id` int(11) NOT NULL AUTO_INCREMENT,
  `subject` varchar(15) DEFAULT NULL,
  `content` varchar(15) DEFAULT NULL,
  `date` varchar(15) DEFAULT NULL,
  `type` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`noti_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`noti_id`,`subject`,`content`,`date`,`type`) values (10,'profile','add new','2021-01-23',NULL),(11,'profile','add new','2021-01-23',NULL),(12,'Subject','shfkjdshfksd','2021-04-10',NULL),(13,'sub11','cont11','2021-04-10',NULL);

/*Table structure for table `sub_admin` */

DROP TABLE IF EXISTS `sub_admin`;

CREATE TABLE `sub_admin` (
  `subadmin_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(15) DEFAULT NULL,
  `dob` varchar(15) DEFAULT NULL,
  `email` varchar(15) DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `login_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`subadmin_id`)
) ENGINE=InnoDB AUTO_INCREMENT=464 DEFAULT CHARSET=latin1;

/*Data for the table `sub_admin` */

insert  into `sub_admin`(`subadmin_id`,`name`,`dob`,`email`,`phone`,`login_id`) values (1,'sarang','12-08-200','appukuttan@gmai','9452542431',2),(457,'sarang','2000-12-03','grdhhgjf','86789686839',23),(460,'officer1 plc1','2021-04-10','officer1@gmail.','8547963021',31),(461,'sub2','2021-04-11','sub2','8520147963',33),(462,'sub3','2021-04-12','sub3','789542266426',35),(463,'sub4','2021-04-10','sub4@gmail.com','8520147963',45);

/*Table structure for table `tips` */

DROP TABLE IF EXISTS `tips`;

CREATE TABLE `tips` (
  `tips_id` int(11) NOT NULL AUTO_INCREMENT,
  `subject` varchar(15) DEFAULT NULL,
  `content` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`tips_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

/*Data for the table `tips` */

insert  into `tips`(`tips_id`,`subject`,`content`) values (15,'power saving mo','battary');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
