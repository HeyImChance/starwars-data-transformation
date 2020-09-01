-- MySQL dump 10.13  Distrib 8.0.20, for macos10.15 (x86_64)
--
-- Host: 127.0.0.1    Database: swapi_data
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `characters`
--

DROP TABLE IF EXISTS `characters`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `characters` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `films` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `char_num` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `char_num_UNIQUE` (`char_num`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `characters`
--

LOCK TABLES `characters` WRITE;
/*!40000 ALTER TABLE `characters` DISABLE KEYS */;
INSERT INTO `characters` VALUES (1,'Cliegg Lars','\'Attack of the Clones\'',62),(2,'Shmi Skywalker','\'The Phantom Menace\', \'Attack of the Clones\'',43),(3,'Ric Olié','\'The Phantom Menace\'',39),(4,'Ayla Secura','\'The Phantom Menace\', \'Attack of the Clones\', \'Revenge of the Sith\'',46),(5,'Dooku','\'Attack of the Clones\', \'Revenge of the Sith\'',67),(6,'Wat Tambor','\'Attack of the Clones\'',76),(7,'Arvel Crynyd','\'Return of the Jedi\'',29),(8,'Beru Whitesun lars','\'A New Hope\', \'Attack of the Clones\', \'Revenge of the Sith\'',7),(9,'Gregar Typho','\'Attack of the Clones\'',60),(10,'Adi Gallia','\'The Phantom Menace\', \'Revenge of the Sith\'',55),(11,'Sly Moore','\'Attack of the Clones\', \'Revenge of the Sith\'',82),(12,'Bossk','\'The Empire Strikes Back\'',24),(13,'Watto','\'The Phantom Menace\', \'Attack of the Clones\'',40),(14,'Jek Tono Porkins','\'A New Hope\'',19),(15,'Grievous','\'Revenge of the Sith\'',79),(16,'Roos Tarpals','\'The Phantom Menace\'',37),(17,'Jocasta Nu','\'Attack of the Clones\'',74),(18,'Kit Fisto','\'The Phantom Menace\', \'Attack of the Clones\', \'Revenge of the Sith\'',53),(19,'Han Solo','\'A New Hope\', \'The Empire Strikes Back\', \'Return of the Jedi\'',14),(23,'Jango Fett','\'Attack of the Clones\'',69),(24,'Bib Fortuna','\'Return of the Jedi\'',45),(25,'Dormé','\'Attack of the Clones\'',66),(26,'Ratts Tyerel','\'The Phantom Menace\'',47),(27,'Zam Wesell','\'Attack of the Clones\'',70),(28,'Mon Mothma','\'Return of the Jedi\'',28);
/*!40000 ALTER TABLE `characters` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-09-01 10:05:34
