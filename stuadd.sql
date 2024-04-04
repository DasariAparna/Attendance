-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: stuattds
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `name` varchar(150) DEFAULT NULL,
  `email` varchar(150) NOT NULL,
  `passcode` varchar(16) DEFAULT NULL,
  `password` varchar(16) DEFAULT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES ('anusha','anushabaditha1999@gmail.com','bxttllbeybipaktx','123');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `records`
--

DROP TABLE IF EXISTS `records`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `records` (
  `date` date DEFAULT NULL,
  `id` int DEFAULT NULL,
  `name` varchar(150) DEFAULT NULL,
  `checkin` datetime DEFAULT NULL,
  `checkout` datetime DEFAULT NULL,
  `target` int DEFAULT NULL,
  `day_present` int DEFAULT '1',
  KEY `id` (`id`),
  CONSTRAINT `records_ibfk_1` FOREIGN KEY (`id`) REFERENCES `student` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `records`
--

LOCK TABLES `records` WRITE;
/*!40000 ALTER TABLE `records` DISABLE KEYS */;
INSERT INTO `records` VALUES ('2023-06-26',20201,'a','2023-06-26 15:53:52','2023-06-26 15:53:53',27,1),('2023-06-26',20202,'b','2023-06-26 16:09:10','2023-06-26 16:09:11',27,1),('2023-06-26',20203,'c','2023-06-26 16:13:19','2023-06-26 16:13:20',27,1),('2023-07-05',20201,'a','2023-07-05 11:50:29','2023-07-05 11:50:31',27,1),('2023-07-05',20202,'b','2023-07-05 11:54:26','2023-07-05 11:54:31',27,1),('2023-07-05',20203,'c','2023-07-05 11:58:55','2023-07-05 11:58:57',27,1),('2023-07-05',20205,'mobbu','2023-07-05 12:35:33','2023-07-05 12:36:26',27,1);
/*!40000 ALTER TABLE `records` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `id` int NOT NULL,
  `name` varchar(150) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `mobileno` varchar(10) DEFAULT NULL,
  `mail` varchar(150) DEFAULT NULL,
  `password` varchar(15) DEFAULT NULL,
  `address` varchar(20) DEFAULT NULL,
  `dept` varchar(20) DEFAULT NULL,
  `Target` int DEFAULT NULL,
  `addedby` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `project1` (`addedby`),
  CONSTRAINT `project1` FOREIGN KEY (`addedby`) REFERENCES `admin` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (20201,'a','Female','123455556','anusha@codegnan.com','123','dfghj','pmc',NULL,NULL),(20202,'b','male','234578943','eswar@codegnan.com','123','vijayawada','Physics',NULL,NULL),(20203,'c','Female','1235432343','swapna@codegnan.com','123','Vij','pmcs',NULL,NULL),(20205,'mobbu','female','1234569876','anusha@codegnan.com','123','sdfghj','MPC',27,'anushabaditha1999@gmail.com');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `work`
--

DROP TABLE IF EXISTS `work`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `work` (
  `Target` int DEFAULT '30',
  `added_by` varchar(150) DEFAULT NULL,
  KEY `added_by` (`added_by`),
  CONSTRAINT `work_ibfk_1` FOREIGN KEY (`added_by`) REFERENCES `admin` (`email`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `work`
--

LOCK TABLES `work` WRITE;
/*!40000 ALTER TABLE `work` DISABLE KEYS */;
INSERT INTO `work` VALUES (27,'anushabaditha1999@gmail.com'),(27,'anushabaditha1999@gmail.com');
/*!40000 ALTER TABLE `work` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-07 11:39:40
