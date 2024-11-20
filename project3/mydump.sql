-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: pro
-- ------------------------------------------------------
-- Server version	8.0.40

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
-- Table structure for table `cpp`
--

DROP TABLE IF EXISTS `cpp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cpp` (
  `qno` int NOT NULL AUTO_INCREMENT,
  `question` varchar(100) DEFAULT NULL,
  `option1` varchar(50) DEFAULT NULL,
  `option2` varchar(50) DEFAULT NULL,
  `option3` varchar(50) DEFAULT NULL,
  `option4` varchar(50) DEFAULT NULL,
  `answer` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`qno`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cpp`
--

LOCK TABLES `cpp` WRITE;
/*!40000 ALTER TABLE `cpp` DISABLE KEYS */;
INSERT INTO `cpp` VALUES (1,'Which of the following is the correct syntax for defining a function in C++?','void function_name();','function_name() void;','void function_name{};','function_name() {void};','A'),(2,'What is the output of the following code?\n`int x = 10; cout << x++;`','10','11','Error','None of the above','A'),(3,'Which operator is used for memory deallocation in C++?','delete','free','delete[]','dealloc','A'),(4,'Which of the following is not a valid data type in C++?','int','float','double','character','D'),(5,'Which keyword is used to prevent a class from being inherited in C++?','final','sealed','static','private','A'),(6,'What will be the result of `cout << 10 / 3;` in C++?','3.33','3','3.0','1','B'),(7,'What does `cin` stand for in C++?','Character Input','Console Input','Character Input Number','Console Input Number','B'),(8,'Which of the following is the default access modifier for class members?','private','protected','public','None of the above','A'),(9,'How can you define a constant in C++?','const int x = 10;','int x = 10 const;','constant int x = 10;','constant x = 10;','A'),(10,'What is the purpose of a destructor in C++?','To initialize an object','To free up resources used by an object','To allocate memory','To call the constructor','B'),(11,'Which type of inheritance is used when a class is derived from multiple base classes?','Single Inheritance','Multiple Inheritance','Multilevel Inheritance','Hierarchical Inheritance','B'),(12,'What is the default constructor in C++?','A constructor that takes arguments','A constructor that does not take any arguments','A constructor that initializes the data members','A constructor that deletes objects','B'),(13,'How do you call a function defined inside a class in C++?','object.function_name();','function_name();','function_name.object();','None of the above','A'),(14,'What will happen if you use the `delete` operator on a non-pointer variable?','It will cause an error','It will delete the variable','It will free memory','Nothing will happen','A'),(15,'Which of the following is used to handle exceptions in C++?','try-catch','throw-catch','catch-finally','try-finally','A'),(16,'Which type of class is used to define objects that have specific behaviors and properties?','Abstract Class','Concrete Class','Base Class','Derived Class','B'),(17,'What is the purpose of the `new` keyword in C++?','To create an array','To create a new object in heap memory','To create a new instance of a class','To create a new function','B'),(18,'How do you access a private member of a class in C++?','Using public getter and setter functions','Directly','Using friend functions','Both A and C','D'),(19,'Which operator is used to access members of a class through a pointer in C++?','.','->','::','&','B'),(20,'Which statement is true about the `virtual` function in C++?','It allows for function overriding','It prevents function overriding','It is used to declare constructors','None of the above','A'),(21,'What is the output of `cout << \'A\' + 1;`?','66','65','A','B','A');
/*!40000 ALTER TABLE `cpp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `java`
--

DROP TABLE IF EXISTS `java`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `java` (
  `qno` int NOT NULL AUTO_INCREMENT,
  `question` varchar(100) DEFAULT NULL,
  `option1` varchar(50) DEFAULT NULL,
  `option2` varchar(50) DEFAULT NULL,
  `option3` varchar(50) DEFAULT NULL,
  `option4` varchar(50) DEFAULT NULL,
  `answer` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`qno`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `java`
--

LOCK TABLES `java` WRITE;
/*!40000 ALTER TABLE `java` DISABLE KEYS */;
INSERT INTO `java` VALUES (1,'Which of the following is not a Java feature?','Object-Oriented','Use of pointers','Platform-Independent','Dynamic','B'),(2,'What is the size of an int variable in Java?','4 bytes','8 bytes','2 bytes','1 byte','A'),(3,'Which of these is a reserved keyword in Java?','object','strictfp','main','system','B'),(4,'Which of the following is not an access modifier in Java?','protected','void','public','private','B'),(5,'Which of the following correctly declares an array in Java?','int arr[] = new int[5];','int arr[5];','arr{5};','int arr(5);','A'),(6,'Which of these is the correct syntax for the main method in Java?','public void main(String[] args)','public static void main(String[] args)','static public main(String[] args)','None of the above','B'),(7,'What is the default value of a boolean variable in Java?','true','false','1','null','B'),(8,'Which of these are selection statements in Java?','if()','for()','continue','break','A'),(9,'What does `System.out.println()` do?','Prints data to the screen','Outputs data to a file','Sends data to a network','None of the above','A'),(10,'What is an interface in Java?','A class','An abstract class','A collection of abstract methods','A collection of variables','C'),(11,'Which keyword is used to inherit a class in Java?','implement','inherits','extends','None of the above','C'),(12,'Which exception is thrown when dividing by zero in Java?','NullPointerException','NumberFormatException','ArithmeticException','IOException','C'),(13,'What is the output of `System.out.println(4 + 5 + \"test\");`?','9test','45test','test9','test45','A'),(14,'How many types of constructors are there in Java?','1','2','3','4','B'),(15,'Which operator is used to concatenate strings in Java?','+','&','%','#','A'),(16,'Which of the following is the correct syntax to create an object in Java?','MyClass obj = new MyClass();','MyClass obj = MyClass();','MyClass obj = class MyClass();','MyClass obj = class.new MyClass();','A'),(17,'What is the range of the `short` data type in Java?','-128 to 127','-32,768 to 32,767','-2,147,483,648 to 2,147,483,647','None of the above','B'),(18,'What is the output of `System.out.println(\"Java\" + 1 + 2);`?','Java3','Java12','Java1Java2','Java21','B'),(19,'What will be the output of `System.out.print(\"Hello \" + \"World\");`?','Hello World','HelloWorld','Hello + World','World Hello','A'),(20,'Which package contains the Random class in Java?','java.util','java.lang','java.io','java.net','A');
/*!40000 ALTER TABLE `java` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `python`
--

DROP TABLE IF EXISTS `python`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `python` (
  `qno` int NOT NULL AUTO_INCREMENT,
  `question` varchar(100) DEFAULT NULL,
  `option1` varchar(50) DEFAULT NULL,
  `option2` varchar(50) DEFAULT NULL,
  `option3` varchar(50) DEFAULT NULL,
  `option4` varchar(50) DEFAULT NULL,
  `answer` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`qno`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `python`
--

LOCK TABLES `python` WRITE;
/*!40000 ALTER TABLE `python` DISABLE KEYS */;
INSERT INTO `python` VALUES (1,'Which keyword is used to define a function in Python?','function','define','def','lambda','C'),(2,'Which of the following is used to create a comment in Python?','//','#','/* */','<!-- -->','B'),(3,'What is the output of `print(2 ** 3)` in Python?','5','6','8','9','C'),(4,'Which of the following data types is immutable in Python?','list','set','dictionary','tuple','D'),(5,'Which function is used to get the length of a list in Python?','length()','size()','len()','count()','C'),(6,'Which keyword is used to handle exceptions in Python?','try','catch','finally','except','D'),(7,'How do you start a for loop in Python?','for i in range()','for (i=0; i<n; i++)','for i=0 to n','foreach(i)','A'),(8,'Which of the following is used to take input from the user in Python?','scanf()','input()','cin','gets()','B'),(9,'Which module in Python is used for regular expressions?','regex','re','regexp','pattern','B'),(10,'What is the output of `print(\'Hello\' + \'World\')`?','Hello World','HelloWorld','Hello+World','Hello','B'),(11,'Which operator is used for exponentiation in Python?','^','**','//','%','B'),(12,'Which of the following is a built-in function in Python?','sum()','add()','plus()','total()','A'),(13,'Which data type is used to store True/False values in Python?','boolean','bool','int','logical','B'),(14,'Which method is used to remove whitespace from the beginning and end of a string?','trim()','strip()','remove()','cut()','B'),(15,'How do you create a set in Python?','{1, 2, 3}','[1, 2, 3]','(1, 2, 3)','<1, 2, 3>','A'),(16,'What is the output of `print(10 // 3)` in Python?','3','3.33','4','Error','A'),(17,'Which statement is used to end a loop prematurely?','stop','exit','break','terminate','C'),(18,'Which Python keyword is used to define a class?','object','struct','define','class','D'),(19,'What is the output of `len(\'Python\')`?','5','6','7','Error','B'),(20,'Which of the following can be used to open a file in read mode?','open(\'file.txt\', \'r\')','open(\'file.txt\', \'w\')','open(\'file.txt\')','openfile(\'file.txt\')','A');
/*!40000 ALTER TABLE `python` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `result`
--

DROP TABLE IF EXISTS `result`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `result` (
  `sno` int NOT NULL AUTO_INCREMENT,
  `uname` varchar(50) DEFAULT NULL,
  `results` varchar(50) DEFAULT NULL,
  `dateTime` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`sno`),
  KEY `uname` (`uname`),
  CONSTRAINT `result_ibfk_1` FOREIGN KEY (`uname`) REFERENCES `user` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `result`
--

LOCK TABLES `result` WRITE;
/*!40000 ALTER TABLE `result` DISABLE KEYS */;
INSERT INTO `result` VALUES (19,'Abhi7974','CPP 2/5 ','2024-11-10 11:19:35'),(20,'Abhi7974','Java 1/5 ','2024-11-10 11:19:47'),(21,'Abhi7974','Python 0/5 ','2024-11-10 11:20:03'),(22,'Abhi7974','CPP 2/5 ','2024-11-10 11:20:12'),(23,'Sahil8','Java 4/5 ','2024-11-10 11:28:46');
/*!40000 ALTER TABLE `result` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `uid` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`uid`),
  UNIQUE KEY `idx_user_username_unique` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (6,'Abhi7974','Abhijeet@12','Abhijeet'),(7,'Sahil8','Sahil8770@','sa');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-12 21:48:40
