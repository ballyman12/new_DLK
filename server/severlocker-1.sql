-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 25, 2019 at 07:32 AM
-- Server version: 10.1.36-MariaDB
-- PHP Version: 7.2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `severlocker`
--

-- --------------------------------------------------------

--
-- Stand-in structure for view `access`
-- (See below for the actual view)
--
CREATE TABLE `access` (
`DLK_Id_Blacklist` int(10)
,`DLK_Id_User` int(10)
,`DLK_Name_User` varchar(255)
,`DLK_Position_User` varchar(100)
,`DLK_RFID` varchar(30)
,`DLK_RFID_START` datetime
,`DLK_RFID_EXP` datetime
);

-- --------------------------------------------------------

--
-- Table structure for table `blacklist`
--

CREATE TABLE `blacklist` (
  `DLK_Id_Blacklist` int(10) NOT NULL,
  `DLK_Id_User` int(5) NOT NULL,
  `DLK_Id_Locker` int(5) NOT NULL,
  `DLK_Id_Detail` int(10) DEFAULT NULL,
  `DLK_Id_condi` int(11) NOT NULL,
  `DLK_Time_Blacklist` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `conditions`
--

CREATE TABLE `conditions` (
  `DLK_Id_Condi` int(5) NOT NULL,
  `DLK_Name_Condi` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `conditions`
--

INSERT INTO `conditions` (`DLK_Id_Condi`, `DLK_Name_Condi`) VALUES
(1, 'ตู้เสียหาย'),
(2, 'มีธุระเร่งด่วน'),
(3, 'ตู้สกปรก'),
(4, 'ต้องการทดสอบ'),
(7, 'อื่นๆ');

-- --------------------------------------------------------

--
-- Table structure for table `details`
--

CREATE TABLE `details` (
  `DLK_Id_Detail` int(10) NOT NULL,
  `DLK_Id_RFID` int(25) NOT NULL,
  `DLK_RFID` varchar(255) DEFAULT NULL,
  `DLK_Id_User` int(2) NOT NULL,
  `DLK_Id_Locker` int(5) NOT NULL,
  `DLK_id_Result` int(5) NOT NULL,
  `DLK_Id_condi` int(5) DEFAULT NULL,
  `DLK_Date_Detail` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `DLK_Date_Curent` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `DLK_TimeUse_Detail` time DEFAULT NULL,
  `DLK_Price_Detail` int(7) NOT NULL,
  `DLK_Id_Price` int(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `details`
--

INSERT INTO `details` (`DLK_Id_Detail`, `DLK_Id_RFID`, `DLK_RFID`, `DLK_Id_User`, `DLK_Id_Locker`, `DLK_id_Result`, `DLK_Id_condi`, `DLK_Date_Detail`, `DLK_Date_Curent`, `DLK_TimeUse_Detail`, `DLK_Price_Detail`, `DLK_Id_Price`) VALUES
(1, 1, '9875642315', 1, 19, 1, NULL, '2018-12-28 14:52:50', '2019-02-14 07:40:15', '838:59:59', 354, 1);

-- --------------------------------------------------------

--
-- Table structure for table `location`
--

CREATE TABLE `location` (
  `Location_Id` int(5) NOT NULL,
  `Location_Name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

--
-- Dumping data for table `location`
--

INSERT INTO `location` (`Location_Id`, `Location_Name`) VALUES
(1, 'MeajoUniversity'),
(2, 'MaejoUniversity แพร่');

-- --------------------------------------------------------

--
-- Table structure for table `lockers`
--

CREATE TABLE `lockers` (
  `DLK_Id_Locker` int(10) NOT NULL,
  `DLK_Number_Locker` int(5) NOT NULL,
  `DLK_Status_Locker` int(2) NOT NULL,
  `DLK_Name_Locker` varchar(255) NOT NULL,
  `Location_Id` int(25) NOT NULL,
  `Site_Id` int(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `lockers`
--

INSERT INTO `lockers` (`DLK_Id_Locker`, `DLK_Number_Locker`, `DLK_Status_Locker`, `DLK_Name_Locker`, `Location_Id`, `Site_Id`) VALUES
(19, 1, 4, 'CS Floor 6', 1, 1),
(20, 2, 4, 'CS Floor 6', 1, 1),
(21, 3, 4, 'CS Floor 6', 1, 1),
(22, 4, 4, 'CS Floor 6', 1, 1),
(23, 5, 4, 'CS Floor 6', 1, 1),
(24, 6, 4, 'CS Floor 6', 1, 1),
(25, 7, 4, 'CS Floor 6', 1, 1),
(26, 8, 4, 'CS Floor 6', 1, 1),
(27, 9, 4, 'CS Floor 6', 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `locker_status`
--

CREATE TABLE `locker_status` (
  `DLK_Status_Id` int(55) NOT NULL,
  `DLK_Status_Name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

--
-- Dumping data for table `locker_status`
--

INSERT INTO `locker_status` (`DLK_Status_Id`, `DLK_Status_Name`) VALUES
(1, 'ปิด'),
(2, 'เปิด'),
(3, 'พร้อมใช้งาน'),
(4, 'ใช้งานอยู่'),
(5, 'ระงับการใช้งาน');

-- --------------------------------------------------------

--
-- Table structure for table `log_open`
--

CREATE TABLE `log_open` (
  `Log_Id` int(10) NOT NULL,
  `DLK_Id_RFID` int(25) DEFAULT NULL,
  `Location_Id` int(5) NOT NULL,
  `Site_Id` int(5) NOT NULL,
  `DLK_Id_Locker` int(5) NOT NULL,
  `DLK_Status_Locker` int(5) NOT NULL,
  `Time_Open` datetime DEFAULT NULL,
  `Time_Update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `MQTT_Status` int(2) DEFAULT NULL,
  `MQTT_Mas` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

-- --------------------------------------------------------

--
-- Table structure for table `log_sync`
--

CREATE TABLE `log_sync` (
  `Log_Id` int(5) NOT NULL,
  `User_Id` int(5) NOT NULL,
  `Date_Update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `Log_Status` int(5) NOT NULL,
  `Old_date` text,
  `New_date` text NOT NULL,
  `Table_name` varchar(255) NOT NULL,
  `Sync_Status` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

CREATE TABLE `payment` (
  `DLK_Id_Pay` int(5) NOT NULL,
  `DLK_Id_Detail` int(5) NOT NULL,
  `MQTT_Status` int(2) NOT NULL,
  `MQTT_Mass` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

-- --------------------------------------------------------

--
-- Table structure for table `price`
--

CREATE TABLE `price` (
  `DLK_Id_Price` int(5) NOT NULL,
  `DLK_2hour_Price` int(5) NOT NULL,
  `DLK_6hour_Price` int(5) NOT NULL,
  `DLK_12hour_Price` int(5) NOT NULL,
  `DLK_18hour_Price` int(5) NOT NULL,
  `DLK_24hour_Price` int(5) NOT NULL,
  `DLK_Id_Locker` int(5) DEFAULT NULL,
  `Location_Id` int(5) DEFAULT NULL,
  `Site_Id` int(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `price`
--

INSERT INTO `price` (`DLK_Id_Price`, `DLK_2hour_Price`, `DLK_6hour_Price`, `DLK_12hour_Price`, `DLK_18hour_Price`, `DLK_24hour_Price`, `DLK_Id_Locker`, `Location_Id`, `Site_Id`) VALUES
(1, 4, 5, 6, 7, 8, NULL, 1, 1),
(4, 3, 4, 5, 6, 7, NULL, NULL, NULL),
(5, 4, 5, 6, 7, 8, NULL, NULL, NULL),
(6, 4, 5, 6, 7, 8, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `report`
--

CREATE TABLE `report` (
  `DLK_Id_Report` int(5) NOT NULL,
  `DLK_Id_User` int(5) DEFAULT NULL,
  `DLK_Id_RFID` int(25) DEFAULT NULL,
  `DLK_Id_Price` int(5) NOT NULL,
  `DLK_Time_Report` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `DLK_2hour_New` int(5) NOT NULL,
  `DLK_6hour_New` int(5) NOT NULL,
  `DLK_12hour_New` int(5) NOT NULL,
  `DLK_18hour_New` int(5) NOT NULL,
  `DLK_24hour_New` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `report`
--

INSERT INTO `report` (`DLK_Id_Report`, `DLK_Id_User`, `DLK_Id_RFID`, `DLK_Id_Price`, `DLK_Time_Report`, `DLK_2hour_New`, `DLK_6hour_New`, `DLK_12hour_New`, `DLK_18hour_New`, `DLK_24hour_New`) VALUES
(1, NULL, NULL, 1, '2018-12-28 08:03:33', 3, 4, 5, 6, 7),
(2, NULL, NULL, 4, '2018-12-28 08:03:59', 4, 5, 6, 7, 8),
(3, NULL, NULL, 5, '2019-01-31 06:47:19', 4, 5, 6, 7, 8);

-- --------------------------------------------------------

--
-- Table structure for table `result`
--

CREATE TABLE `result` (
  `DLK_id_Result` int(5) NOT NULL,
  `DLK_Name_Result` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

--
-- Dumping data for table `result`
--

INSERT INTO `result` (`DLK_id_Result`, `DLK_Name_Result`) VALUES
(1, 'กำลังใช้งาน'),
(2, 'ไม่มีสิทธิใช้งาน'),
(3, 'ไม่ชำระค่าเทอม'),
(4, 'ค้างชำระ'),
(5, 'เงินไม่พอ'),
(6, 'แตะไม่ฝาก'),
(7, 'ยกเลิกการใช้งาน'),
(8, 'สำเร็จ');

-- --------------------------------------------------------

--
-- Table structure for table `rfid`
--

CREATE TABLE `rfid` (
  `DLK_Id_RFID` int(25) NOT NULL,
  `DLK_RFID` varchar(30) NOT NULL,
  `DLK_Id_User` int(25) NOT NULL,
  `DLK_RFID_START` datetime NOT NULL,
  `DLK_RFID_EXP` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

--
-- Dumping data for table `rfid`
--

INSERT INTO `rfid` (`DLK_Id_RFID`, `DLK_RFID`, `DLK_Id_User`, `DLK_RFID_START`, `DLK_RFID_EXP`) VALUES
(1, '9875642315', 1, '2018-12-28 00:00:00', '2019-09-25 00:00:00'),
(2, '8F89B4N5H6', 10, '2018-12-28 00:00:00', '2019-04-25 00:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `site`
--

CREATE TABLE `site` (
  `Site_Id` int(5) NOT NULL,
  `Site` varchar(255) NOT NULL,
  `Location_Id` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

--
-- Dumping data for table `site`
--

INSERT INTO `site` (`Site_Id`, `Site`, `Location_Id`) VALUES
(1, 'ตึก60ปี คณะวิทยาศาสตร์', 1),
(2, 'สนามฟีฬาอินทนิล', 1);

-- --------------------------------------------------------

--
-- Table structure for table `sync_status`
--

CREATE TABLE `sync_status` (
  `Sync_Status_Id` int(5) NOT NULL,
  `User_Id` int(5) NOT NULL,
  `Text` varchar(255) NOT NULL,
  `Log_Status` int(11) NOT NULL,
  `Date_Update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `Sync_Status` int(11) NOT NULL,
  `Log_Id` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

-- --------------------------------------------------------

--
-- Table structure for table `time`
--

CREATE TABLE `time` (
  `DLK_Id_Time` int(5) NOT NULL,
  `DLK_Open_Time` time NOT NULL,
  `DLK_Close_Time` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `time`
--

INSERT INTO `time` (`DLK_Id_Time`, `DLK_Open_Time`, `DLK_Close_Time`) VALUES
(1, '11:19:34', '23:19:36');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `DLK_Id_User` int(10) NOT NULL,
  `DLK_Name_User` varchar(255) NOT NULL,
  `DLK_NumberPhone_User` int(25) NOT NULL,
  `DLK_Position_User` varchar(100) NOT NULL,
  `DLK_Citizen_User` int(13) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`DLK_Id_User`, `DLK_Name_User`, `DLK_NumberPhone_User`, `DLK_Position_User`, `DLK_Citizen_User`) VALUES
(1, 'Fam', 0, 'Student', 1150),
(2, 'Ball', 0, 'Student', 0),
(3, 'Pete', 0, 'Student', 0),
(4, 'Nun', 0, 'Student', 0),
(5, 'Ice', 0, 'Student', 0),
(6, 'Matoom', 0, 'Student', 0),
(7, 'Mos', 0, 'Student', 0),
(8, 'Four', 0, 'Student', 0),
(9, 'Bale', 0, 'Student', 0),
(10, 'Dome', 0, 'Student', 0),
(11, 'Aum', 0, 'Student', 0),
(12, 'Print', 0, 'Student', 0),
(13, 'Am', 0, 'Student', 0),
(14, 'AunWhite', 0, 'Student', 0);

-- --------------------------------------------------------

--
-- Stand-in structure for view `usesing`
-- (See below for the actual view)
--
CREATE TABLE `usesing` (
`time_ok` time
,`DLK_Id_Detail` int(10)
,`DLK_Id_User` int(2)
,`DLK_Id_Locker` int(5)
,`DLK_id_Result` int(5)
,`DLK_Id_condi` int(5)
,`DLK_Date_Detail` datetime
,`DLK_Date_Curent` timestamp
,`DLK_TimeUse_Detail` time
,`DLK_Price_Detail` int(7)
,`DLK_Id_Price` int(5)
,`DLK_Name_User` varchar(255)
,`DLK_Number_Locker` int(5)
,`DLK_Status_Locker` int(2)
,`DLK_2hour_Price` int(5)
,`DLK_6hour_Price` int(5)
,`DLK_12hour_Price` int(5)
,`DLK_18hour_Price` int(5)
,`DLK_24hour_Price` int(5)
);

-- --------------------------------------------------------

--
-- Structure for view `access`
--
DROP TABLE IF EXISTS `access`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `access`  AS  select `blacklist`.`DLK_Id_Blacklist` AS `DLK_Id_Blacklist`,`users`.`DLK_Id_User` AS `DLK_Id_User`,`users`.`DLK_Name_User` AS `DLK_Name_User`,`users`.`DLK_Position_User` AS `DLK_Position_User`,`rfid`.`DLK_RFID` AS `DLK_RFID`,`rfid`.`DLK_RFID_START` AS `DLK_RFID_START`,`rfid`.`DLK_RFID_EXP` AS `DLK_RFID_EXP` from ((`rfid` join `users` on((`rfid`.`DLK_Id_User` = `users`.`DLK_Id_User`))) join `blacklist` on((`blacklist`.`DLK_Id_User` = `users`.`DLK_Id_User`))) ;

-- --------------------------------------------------------

--
-- Structure for view `usesing`
--
DROP TABLE IF EXISTS `usesing`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `usesing`  AS  select timediff(`details`.`DLK_Date_Curent`,`details`.`DLK_Date_Detail`) AS `time_ok`,`details`.`DLK_Id_Detail` AS `DLK_Id_Detail`,`details`.`DLK_Id_User` AS `DLK_Id_User`,`details`.`DLK_Id_Locker` AS `DLK_Id_Locker`,`details`.`DLK_id_Result` AS `DLK_id_Result`,`details`.`DLK_Id_condi` AS `DLK_Id_condi`,`details`.`DLK_Date_Detail` AS `DLK_Date_Detail`,`details`.`DLK_Date_Curent` AS `DLK_Date_Curent`,`details`.`DLK_TimeUse_Detail` AS `DLK_TimeUse_Detail`,`details`.`DLK_Price_Detail` AS `DLK_Price_Detail`,`details`.`DLK_Id_Price` AS `DLK_Id_Price`,`users`.`DLK_Name_User` AS `DLK_Name_User`,`lockers`.`DLK_Number_Locker` AS `DLK_Number_Locker`,`lockers`.`DLK_Status_Locker` AS `DLK_Status_Locker`,`price`.`DLK_2hour_Price` AS `DLK_2hour_Price`,`price`.`DLK_6hour_Price` AS `DLK_6hour_Price`,`price`.`DLK_12hour_Price` AS `DLK_12hour_Price`,`price`.`DLK_18hour_Price` AS `DLK_18hour_Price`,`price`.`DLK_24hour_Price` AS `DLK_24hour_Price` from (((`details` join `price` on((`details`.`DLK_Id_Price` = `price`.`DLK_Id_Price`))) join `users` on((`details`.`DLK_Id_User` = `users`.`DLK_Id_User`))) join `lockers` on(((`details`.`DLK_Id_Locker` = `lockers`.`DLK_Id_Locker`) and (`price`.`DLK_Id_Price` = 1) and (`details`.`DLK_id_Result` = 1)))) ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `blacklist`
--
ALTER TABLE `blacklist`
  ADD PRIMARY KEY (`DLK_Id_Blacklist`),
  ADD KEY `DLK_Id_User` (`DLK_Id_User`),
  ADD KEY `DLK_Id_Locker` (`DLK_Id_Locker`),
  ADD KEY `DLK_Id_condi` (`DLK_Id_condi`),
  ADD KEY `DLK_Id_Detail` (`DLK_Id_Detail`);

--
-- Indexes for table `conditions`
--
ALTER TABLE `conditions`
  ADD PRIMARY KEY (`DLK_Id_Condi`);

--
-- Indexes for table `details`
--
ALTER TABLE `details`
  ADD PRIMARY KEY (`DLK_Id_Detail`),
  ADD KEY `DLK_Id_Locker` (`DLK_Id_Locker`),
  ADD KEY `DLK_id_Result` (`DLK_id_Result`),
  ADD KEY `DLK_Id_condi` (`DLK_Id_condi`),
  ADD KEY `DLK_Id_Price` (`DLK_Id_Price`),
  ADD KEY `DLK_Id_User` (`DLK_Id_User`),
  ADD KEY `DLK_RFID` (`DLK_Id_RFID`);

--
-- Indexes for table `location`
--
ALTER TABLE `location`
  ADD PRIMARY KEY (`Location_Id`);

--
-- Indexes for table `lockers`
--
ALTER TABLE `lockers`
  ADD PRIMARY KEY (`DLK_Id_Locker`),
  ADD KEY `Location_Id` (`Location_Id`),
  ADD KEY `DLK_Number_Locker` (`DLK_Number_Locker`),
  ADD KEY `DLK_Status_Locker` (`DLK_Status_Locker`),
  ADD KEY `Site_Id` (`Site_Id`);

--
-- Indexes for table `locker_status`
--
ALTER TABLE `locker_status`
  ADD PRIMARY KEY (`DLK_Status_Id`);

--
-- Indexes for table `log_open`
--
ALTER TABLE `log_open`
  ADD PRIMARY KEY (`Log_Id`),
  ADD KEY `Location_Id` (`Location_Id`),
  ADD KEY `Site_Id` (`Site_Id`),
  ADD KEY `DLK_Id_Locker` (`DLK_Id_Locker`),
  ADD KEY `DLK_RFID` (`DLK_Id_RFID`),
  ADD KEY `DLK_Status_Locker` (`DLK_Status_Locker`);

--
-- Indexes for table `log_sync`
--
ALTER TABLE `log_sync`
  ADD PRIMARY KEY (`Log_Id`);

--
-- Indexes for table `payment`
--
ALTER TABLE `payment`
  ADD PRIMARY KEY (`DLK_Id_Pay`);

--
-- Indexes for table `price`
--
ALTER TABLE `price`
  ADD PRIMARY KEY (`DLK_Id_Price`),
  ADD KEY `DLK_Id_Locker` (`DLK_Id_Locker`),
  ADD KEY `DLK_Id_Price` (`DLK_Id_Price`),
  ADD KEY `Location_Id` (`Location_Id`),
  ADD KEY `Site_Id` (`Site_Id`);

--
-- Indexes for table `report`
--
ALTER TABLE `report`
  ADD PRIMARY KEY (`DLK_Id_Report`),
  ADD KEY `DLK_Id_User` (`DLK_Id_User`),
  ADD KEY `DLK_Id_Price` (`DLK_Id_Price`),
  ADD KEY `DLK_RFID` (`DLK_Id_RFID`);

--
-- Indexes for table `result`
--
ALTER TABLE `result`
  ADD PRIMARY KEY (`DLK_id_Result`);

--
-- Indexes for table `rfid`
--
ALTER TABLE `rfid`
  ADD PRIMARY KEY (`DLK_Id_RFID`),
  ADD KEY `DLK_Id_User` (`DLK_Id_User`);

--
-- Indexes for table `site`
--
ALTER TABLE `site`
  ADD PRIMARY KEY (`Site_Id`),
  ADD KEY `Location_Id` (`Location_Id`);

--
-- Indexes for table `sync_status`
--
ALTER TABLE `sync_status`
  ADD PRIMARY KEY (`Sync_Status_Id`),
  ADD KEY `Log_Id` (`Log_Id`);

--
-- Indexes for table `time`
--
ALTER TABLE `time`
  ADD PRIMARY KEY (`DLK_Id_Time`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`DLK_Id_User`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `blacklist`
--
ALTER TABLE `blacklist`
  MODIFY `DLK_Id_Blacklist` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `details`
--
ALTER TABLE `details`
  MODIFY `DLK_Id_Detail` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `location`
--
ALTER TABLE `location`
  MODIFY `Location_Id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `lockers`
--
ALTER TABLE `lockers`
  MODIFY `DLK_Id_Locker` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `locker_status`
--
ALTER TABLE `locker_status`
  MODIFY `DLK_Status_Id` int(55) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `log_open`
--
ALTER TABLE `log_open`
  MODIFY `Log_Id` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `log_sync`
--
ALTER TABLE `log_sync`
  MODIFY `Log_Id` int(5) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `payment`
--
ALTER TABLE `payment`
  MODIFY `DLK_Id_Pay` int(5) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `price`
--
ALTER TABLE `price`
  MODIFY `DLK_Id_Price` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `report`
--
ALTER TABLE `report`
  MODIFY `DLK_Id_Report` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `result`
--
ALTER TABLE `result`
  MODIFY `DLK_id_Result` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `rfid`
--
ALTER TABLE `rfid`
  MODIFY `DLK_Id_RFID` int(25) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `site`
--
ALTER TABLE `site`
  MODIFY `Site_Id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `sync_status`
--
ALTER TABLE `sync_status`
  MODIFY `Sync_Status_Id` int(5) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `time`
--
ALTER TABLE `time`
  MODIFY `DLK_Id_Time` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `DLK_Id_User` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `blacklist`
--
ALTER TABLE `blacklist`
  ADD CONSTRAINT `blacklist_ibfk_1` FOREIGN KEY (`DLK_Id_User`) REFERENCES `users` (`DLK_Id_User`),
  ADD CONSTRAINT `blacklist_ibfk_2` FOREIGN KEY (`DLK_Id_Locker`) REFERENCES `lockers` (`DLK_Id_Locker`),
  ADD CONSTRAINT `blacklist_ibfk_4` FOREIGN KEY (`DLK_Id_Detail`) REFERENCES `details` (`DLK_Id_Detail`),
  ADD CONSTRAINT `blacklist_ibfk_5` FOREIGN KEY (`DLK_Id_condi`) REFERENCES `conditions` (`DLK_Id_Condi`);

--
-- Constraints for table `details`
--
ALTER TABLE `details`
  ADD CONSTRAINT `details_ibfk_10` FOREIGN KEY (`DLK_Id_condi`) REFERENCES `conditions` (`DLK_Id_Condi`),
  ADD CONSTRAINT `details_ibfk_2` FOREIGN KEY (`DLK_Id_Locker`) REFERENCES `lockers` (`DLK_Id_Locker`),
  ADD CONSTRAINT `details_ibfk_3` FOREIGN KEY (`DLK_id_Result`) REFERENCES `result` (`DLK_id_Result`),
  ADD CONSTRAINT `details_ibfk_5` FOREIGN KEY (`DLK_Id_Price`) REFERENCES `price` (`DLK_Id_Price`),
  ADD CONSTRAINT `details_ibfk_8` FOREIGN KEY (`DLK_Id_User`) REFERENCES `users` (`DLK_Id_User`),
  ADD CONSTRAINT `details_ibfk_9` FOREIGN KEY (`DLK_Id_RFID`) REFERENCES `rfid` (`DLK_Id_RFID`);

--
-- Constraints for table `lockers`
--
ALTER TABLE `lockers`
  ADD CONSTRAINT `lockers_ibfk_1` FOREIGN KEY (`Location_Id`) REFERENCES `location` (`Location_Id`),
  ADD CONSTRAINT `lockers_ibfk_3` FOREIGN KEY (`DLK_Status_Locker`) REFERENCES `locker_status` (`DLK_Status_Id`),
  ADD CONSTRAINT `lockers_ibfk_4` FOREIGN KEY (`Site_Id`) REFERENCES `site` (`Site_Id`);

--
-- Constraints for table `log_open`
--
ALTER TABLE `log_open`
  ADD CONSTRAINT `log_open_ibfk_3` FOREIGN KEY (`Location_Id`) REFERENCES `location` (`Location_Id`),
  ADD CONSTRAINT `log_open_ibfk_5` FOREIGN KEY (`DLK_Id_Locker`) REFERENCES `lockers` (`DLK_Id_Locker`),
  ADD CONSTRAINT `log_open_ibfk_6` FOREIGN KEY (`DLK_Id_RFID`) REFERENCES `rfid` (`DLK_Id_RFID`),
  ADD CONSTRAINT `log_open_ibfk_7` FOREIGN KEY (`DLK_Status_Locker`) REFERENCES `lockers` (`DLK_Status_Locker`),
  ADD CONSTRAINT `log_open_ibfk_8` FOREIGN KEY (`Site_Id`) REFERENCES `site` (`Site_Id`);

--
-- Constraints for table `price`
--
ALTER TABLE `price`
  ADD CONSTRAINT `price_ibfk_1` FOREIGN KEY (`DLK_Id_Locker`) REFERENCES `lockers` (`DLK_Id_Locker`),
  ADD CONSTRAINT `price_ibfk_2` FOREIGN KEY (`Location_Id`) REFERENCES `location` (`Location_Id`),
  ADD CONSTRAINT `price_ibfk_3` FOREIGN KEY (`Site_Id`) REFERENCES `site` (`Site_Id`);

--
-- Constraints for table `report`
--
ALTER TABLE `report`
  ADD CONSTRAINT `report_ibfk_1` FOREIGN KEY (`DLK_Id_User`) REFERENCES `users` (`DLK_Id_User`),
  ADD CONSTRAINT `report_ibfk_2` FOREIGN KEY (`DLK_Id_Price`) REFERENCES `price` (`DLK_Id_Price`),
  ADD CONSTRAINT `report_ibfk_3` FOREIGN KEY (`DLK_Id_RFID`) REFERENCES `rfid` (`DLK_Id_RFID`);

--
-- Constraints for table `rfid`
--
ALTER TABLE `rfid`
  ADD CONSTRAINT `rfid_ibfk_1` FOREIGN KEY (`DLK_Id_User`) REFERENCES `users` (`DLK_Id_User`);

--
-- Constraints for table `site`
--
ALTER TABLE `site`
  ADD CONSTRAINT `site_ibfk_1` FOREIGN KEY (`Location_Id`) REFERENCES `location` (`Location_Id`);

--
-- Constraints for table `sync_status`
--
ALTER TABLE `sync_status`
  ADD CONSTRAINT `sync_status_ibfk_1` FOREIGN KEY (`Log_Id`) REFERENCES `log_sync` (`Log_Id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
