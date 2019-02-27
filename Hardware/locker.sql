-- phpMyAdmin SQL Dump
-- version 4.8.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 22, 2019 at 06:22 AM
-- Server version: 10.1.31-MariaDB
-- PHP Version: 7.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `locker`
--

-- --------------------------------------------------------

--
-- Table structure for table `access`
--

CREATE TABLE `access` (
  `Access_Id` int(7) NOT NULL,
  `DLK_Id_User` int(5) NOT NULL,
  `DLK_RFID` varchar(100) NOT NULL,
  `DLK_Position_User` varchar(10) NOT NULL,
  `DLK_RFID_START` datetime NOT NULL,
  `DLK_RFID_EXP` datetime NOT NULL,
  `DLK_Id_Blacklist` int(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `access`
--

INSERT INTO `access` (`Access_Id`, `DLK_Id_User`, `DLK_RFID`, `DLK_Position_User`, `DLK_RFID_START`, `DLK_RFID_EXP`, `DLK_Id_Blacklist`) VALUES
(1, 1, 'DRF1879TR5', 'admin', '2018-08-30 00:00:00', '2022-10-04 00:00:00', NULL),
(2, 2, 'TU874F5OP3', 'Student', '2018-05-31 00:00:00', '2022-03-31 00:00:00', NULL),
(3, 3, 'SU410OCT39', 'Student', '2018-12-10 00:00:00', '2022-06-30 00:00:00', NULL),
(4, 4, 'N4MD5EW548', 'Student', '2018-05-31 00:00:00', '2022-05-31 00:00:00', 1),
(5, 5, 'OM48D16PQ2', 'Student', '2018-05-31 00:00:00', '2022-05-31 00:00:00', 2),
(6, 6, 'TWP15LO3U7', 'Student', '2018-05-31 00:00:00', '2023-05-31 00:00:00', NULL),
(7, 7, '1', 'admin', '2018-08-31 00:00:00', '2023-05-31 00:00:00', NULL),
(8, 8, '2', 'student', '2019-01-01 00:00:00', '2022-05-31 00:00:00', NULL),
(9, 9, '3', 'admin', '2018-08-31 00:00:00', '2023-05-31 00:00:00', NULL),
(10, 10, '4', 'student', '2019-01-01 00:00:00', '2022-05-31 00:00:00', NULL);

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
(0, 'ตู้ความเสียหาย'),
(4, 'ไม่บอกหรอก'),
(5, 'ไม่รู้ อยากยกเลิก'),
(6, 'ไม่มีเงินมาเปิดตู้เล่น'),
(8, 'ตู้สกปรก555'),
(9, 'อื่น ๆ');

-- --------------------------------------------------------

--
-- Table structure for table `details`
--

CREATE TABLE `details` (
  `DLK_Id_Detail` int(10) NOT NULL,
  `DLK_Id_User` int(5) NOT NULL,
  `DLK_RFID` varchar(100) NOT NULL,
  `DLK_Number_Locker` int(5) NOT NULL,
  `DLK_id_Result` int(5) NOT NULL,
  `DLK_Id_condi` int(5) DEFAULT NULL,
  `DLK_Date_Detail` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `DLK_Date_Curent` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `MQTT_Status` int(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `details`
--

INSERT INTO `details` (`DLK_Id_Detail`, `DLK_Id_User`, `DLK_RFID`, `DLK_Number_Locker`, `DLK_id_Result`, `DLK_Id_condi`, `DLK_Date_Detail`, `DLK_Date_Curent`, `MQTT_Status`) VALUES
(33, 8, '2', 3, 8, NULL, '2019-01-18 22:10:58', '2019-01-21 08:48:34', 1),
(34, 8, '2', 6, 8, NULL, '2019-01-21 14:04:18', '2019-01-21 08:48:36', 1),
(35, 8, '2', 2, 8, NULL, '2019-01-21 14:11:09', '2019-01-21 08:48:38', 1),
(36, 8, '2', 9, 8, NULL, '2019-01-21 14:38:29', '2019-01-21 08:48:40', 1),
(37, 8, '2', 3, 1, NULL, '2019-01-21 15:50:20', '2019-01-21 09:01:56', 1);

-- --------------------------------------------------------

--
-- Table structure for table `lockers`
--

CREATE TABLE `lockers` (
  `DLK_Id_Locker` int(10) NOT NULL,
  `DLK_Number_Locker` int(5) NOT NULL,
  `DLK_Name_Locker` varchar(255) NOT NULL,
  `DLK_Status_Locker` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `lockers`
--

INSERT INTO `lockers` (`DLK_Id_Locker`, `DLK_Number_Locker`, `DLK_Name_Locker`, `DLK_Status_Locker`) VALUES
(1, 1, 'Computer Science floor 6th', 3),
(2, 2, 'Computer Science floor 6th', 2),
(3, 3, 'Computer Science floor 6th', 4),
(4, 4, 'Computer Science floor 6th', 4),
(5, 5, 'Computer Science floor 6th', 5),
(6, 6, 'Computer Science floor 6th', 3),
(7, 7, 'Computer Science floor 6th', 4),
(8, 8, 'Computer Science floor 6th', 3),
(9, 9, 'Computer Science floor 6th', 3);

-- --------------------------------------------------------

--
-- Table structure for table `log_status_locker`
--

CREATE TABLE `log_status_locker` (
  `log_Id` int(10) NOT NULL,
  `DLK_Id_User` int(5) NOT NULL,
  `DLK_RFID` varchar(100) NOT NULL,
  `DLK_Number_Locker` int(5) NOT NULL,
  `DLK_Status_Locker` int(5) NOT NULL,
  `Time_update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `MQTT_Status` int(5) NOT NULL,
  `MQTT_Mass` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `log_status_locker`
--

INSERT INTO `log_status_locker` (`log_Id`, `DLK_Id_User`, `DLK_RFID`, `DLK_Number_Locker`, `DLK_Status_Locker`, `Time_update`, `MQTT_Status`, `MQTT_Mass`) VALUES
(196, 2, 'TU874F5OP3', 9, 2, '2019-01-16 08:50:55', 1, NULL),
(197, 2, 'TU874F5OP3', 9, 2, '2019-01-16 08:50:57', 1, NULL),
(198, 2, 'TU874F5OP3', 9, 1, '2019-01-16 08:51:00', 1, NULL),
(199, 2, 'TU874F5OP3', 9, 1, '2019-01-16 08:51:03', 1, NULL),
(200, 2, 'TU874F5OP3', 9, 1, '2019-01-16 08:51:05', 1, NULL),
(201, 2, 'TU874F5OP3', 8, 2, '2019-01-16 08:51:07', 1, NULL),
(202, 2, 'TU874F5OP3', 5, 2, '2019-01-16 08:51:10', 1, NULL),
(203, 2, 'TU874F5OP3', 5, 1, '2019-01-16 08:51:12', 1, NULL),
(204, 2, 'TU874F5OP3', 6, 2, '2019-01-16 08:51:15', 1, NULL),
(205, 2, 'TU874F5OP3', 6, 1, '2019-01-16 08:51:17', 1, NULL),
(206, 2, 'TU874F5OP3', 3, 2, '2019-01-16 08:51:20', 1, NULL),
(207, 2, 'TU874F5OP3', 3, 1, '2019-01-16 08:51:22', 1, NULL),
(208, 2, 'TU874F5OP3', 4, 2, '2019-01-16 08:51:24', 1, NULL),
(209, 2, 'TU874F5OP3', 4, 1, '2019-01-16 08:51:27', 1, NULL),
(210, 2, 'TU874F5OP3', 4, 2, '2019-01-16 08:51:29', 1, NULL),
(211, 2, 'TU874F5OP3', 4, 1, '2019-01-16 08:51:32', 1, NULL),
(212, 2, 'TU874F5OP3', 4, 4, '2019-01-16 08:51:34', 1, NULL),
(213, 2, 'TU874F5OP3', 4, 2, '2019-01-16 08:51:36', 1, NULL),
(214, 2, 'TU874F5OP3', 4, 1, '2019-01-16 08:51:39', 1, NULL),
(215, 2, 'TU874F5OP3', 4, 3, '2019-01-16 08:51:41', 1, NULL),
(216, 2, 'TU874F5OP3', 7, 2, '2019-01-16 08:51:44', 1, NULL),
(217, 2, 'TU874F5OP3', 7, 1, '2019-01-16 08:51:46', 1, NULL),
(218, 2, 'TU874F5OP3', 7, 3, '2019-01-16 08:51:48', 1, NULL),
(219, 2, 'TU874F5OP3', 1, 2, '2019-01-16 08:51:51', 1, NULL),
(220, 2, 'TU874F5OP3', 1, 1, '2019-01-16 08:51:53', 1, NULL),
(221, 2, 'TU874F5OP3', 1, 3, '2019-01-16 08:51:56', 1, NULL),
(222, 2, 'TU874F5OP3', 1, 2, '2019-01-16 09:05:03', 1, NULL),
(223, 2, 'TU874F5OP3', 1, 1, '2019-01-16 09:05:06', 1, NULL),
(224, 2, 'TU874F5OP3', 9, 2, '2019-01-16 09:05:08', 1, NULL),
(225, 2, 'TU874F5OP3', 9, 1, '2019-01-16 09:05:10', 1, NULL),
(226, 2, 'TU874F5OP3', 9, 4, '2019-01-16 09:05:13', 1, NULL),
(227, 2, 'TU874F5OP3', 9, 2, '2019-01-16 09:05:15', 1, NULL),
(228, 2, 'TU874F5OP3', 9, 1, '2019-01-16 09:05:18', 1, NULL),
(229, 2, 'TU874F5OP3', 9, 2, '2019-01-16 09:07:04', 1, NULL),
(230, 2, 'TU874F5OP3', 9, 1, '2019-01-16 09:07:07', 1, NULL),
(231, 2, 'TU874F5OP3', 9, 4, '2019-01-16 09:07:09', 1, NULL),
(232, 2, 'TU874F5OP3', 9, 2, '2019-01-16 09:07:11', 1, NULL),
(233, 2, 'TU874F5OP3', 9, 1, '2019-01-16 09:07:14', 1, NULL),
(234, 2, 'TU874F5OP3', 9, 3, '2019-01-16 09:07:16', 1, NULL),
(235, 2, 'TU874F5OP3', 4, 2, '2019-01-16 09:07:19', 1, NULL),
(236, 2, 'TU874F5OP3', 4, 1, '2019-01-16 09:07:21', 1, NULL),
(237, 2, 'TU874F5OP3', 4, 4, '2019-01-16 09:07:24', 1, NULL),
(238, 1, 'DRF1879TR5', 4, 2, '2019-01-16 09:07:27', 1, NULL),
(239, 1, 'DRF1879TR5', 4, 1, '2019-01-16 09:07:29', 1, NULL),
(240, 1, 'DRF1879TR5', 4, 4, '2019-01-16 09:07:32', 1, NULL),
(241, 1, 'DRF1879TR5', 4, 2, '2019-01-16 09:07:34', 1, NULL),
(242, 1, 'DRF1879TR5', 4, 1, '2019-01-16 09:07:36', 1, NULL),
(243, 1, 'DRF1879TR5', 4, 1, '2019-01-16 09:07:39', 1, NULL),
(244, 1, 'DRF1879TR5', 1, 2, '2019-01-16 09:07:41', 1, NULL),
(245, 1, 'DRF1879TR5', 1, 2, '2019-01-16 09:07:43', 1, NULL),
(246, 1, 'DRF1879TR5', 1, 1, '2019-01-16 09:07:46', 1, NULL),
(247, 1, 'DRF1879TR5', 1, 3, '2019-01-16 09:07:48', 1, NULL),
(248, 1, 'DRF1879TR5', 4, 2, '2019-01-16 09:07:50', 1, NULL),
(249, 1, 'DRF1879TR5', 4, 1, '2019-01-16 09:07:53', 1, NULL),
(250, 1, 'DRF1879TR5', 4, 3, '2019-01-16 09:07:55', 1, NULL),
(251, 1, 'DRF1879TR5', 1, 5, '2019-01-16 09:07:58', 1, NULL),
(252, 1, 'DRF1879TR5', 1, 5, '2019-01-16 09:08:00', 1, NULL),
(253, 1, 'DRF1879TR5', 1, 3, '2019-01-16 09:08:03', 1, NULL),
(258, 7, '1', 1, 2, '2019-01-16 09:08:05', 1, NULL),
(259, 7, '1', 1, 1, '2019-01-16 09:08:07', 1, NULL),
(260, 7, '1', 1, 3, '2019-01-16 09:08:10', 1, NULL),
(261, 7, '1', 1, 2, '2019-01-16 09:08:12', 1, NULL),
(262, 7, '1', 1, 1, '2019-01-16 09:08:14', 1, NULL),
(263, 7, '1', 1, 3, '2019-01-16 09:08:17', 1, NULL),
(264, 7, '1', 1, 3, '2019-01-16 09:08:19', 1, NULL),
(265, 8, '2', 2, 2, '2019-01-16 09:08:22', 1, NULL),
(266, 8, '2', 2, 1, '2019-01-16 09:08:24', 1, NULL),
(267, 8, '2', 2, 4, '2019-01-16 09:08:26', 1, NULL),
(280, 7, '1', 2, 2, '2019-01-16 09:08:29', 1, NULL),
(281, 7, '1', 2, 1, '2019-01-16 09:08:31', 1, NULL),
(282, 7, '1', 2, 3, '2019-01-16 09:08:33', 1, NULL),
(283, 8, '2', 6, 2, '2019-01-16 09:08:36', 1, NULL),
(284, 8, '2', 6, 1, '2019-01-16 09:08:38', 1, NULL),
(285, 8, '2', 6, 4, '2019-01-16 09:08:40', 1, NULL),
(286, 7, '1', 6, 2, '2019-01-16 09:08:43', 1, NULL),
(287, 7, '1', 6, 1, '2019-01-16 09:08:45', 1, NULL),
(288, 7, '1', 6, 4, '2019-01-16 09:10:47', 1, NULL),
(289, 7, '1', 6, 2, '2019-01-16 09:10:49', 1, NULL),
(290, 7, '1', 6, 1, '2019-01-16 09:11:06', 1, NULL),
(291, 7, '1', 6, 3, '2019-01-16 09:11:19', 1, NULL),
(292, 9, '3', 5, 5, '2019-01-16 09:11:22', 1, NULL),
(293, 10, '4', 1, 2, '2019-01-16 09:11:24', 1, NULL),
(294, 10, '4', 1, 1, '2019-01-16 09:11:26', 1, NULL),
(295, 10, '4', 1, 4, '2019-01-16 09:11:29', 1, NULL),
(296, 8, '2', 2, 2, '2019-01-16 09:11:31', 1, NULL),
(297, 8, '2', 2, 1, '2019-01-16 09:11:33', 1, NULL),
(298, 8, '2', 2, 4, '2019-01-16 09:11:36', 1, NULL),
(299, 7, '1', 2, 2, '2019-01-16 09:11:38', 1, NULL),
(300, 7, '1', 2, 1, '2019-01-16 09:11:41', 1, NULL),
(301, 7, '1', 2, 4, '2019-01-16 09:11:43', 1, NULL),
(302, 8, '2', 2, 2, '2019-01-16 09:11:45', 1, NULL),
(303, 8, '2', 2, 1, '2019-01-16 09:11:48', 1, NULL),
(304, 8, '2', 2, 3, '2019-01-16 09:11:50', 1, NULL),
(305, 10, '4', 1, 2, '2019-01-16 09:12:53', 1, NULL),
(306, 10, '4', 1, 1, '2019-01-16 09:12:57', 1, NULL),
(307, 10, '4', 1, 3, '2019-01-16 09:12:59', 1, NULL),
(308, 10, '4', 7, 2, '2019-01-16 09:18:17', 1, NULL),
(309, 10, '4', 7, 1, '2019-01-16 09:18:20', 1, NULL),
(310, 10, '4', 7, 4, '2019-01-16 09:18:22', 1, NULL),
(311, 10, '4', 7, 2, '2019-01-16 09:26:27', 1, NULL),
(312, 10, '4', 7, 1, '2019-01-16 09:26:30', 1, NULL),
(313, 10, '4', 7, 3, '2019-01-16 09:26:32', 1, NULL),
(314, 10, '4', 4, 2, '2019-01-16 09:36:12', 1, NULL),
(315, 10, '4', 4, 1, '2019-01-16 09:36:14', 1, NULL),
(316, 10, '4', 4, 4, '2019-01-16 09:36:17', 1, NULL),
(317, 8, '2', 7, 2, '2019-01-16 09:36:40', 1, NULL),
(318, 8, '2', 7, 1, '2019-01-16 09:36:43', 1, NULL),
(319, 8, '2', 7, 4, '2019-01-16 09:36:45', 1, NULL),
(320, 8, '2', 3, 2, '2019-01-21 08:10:15', 1, NULL),
(321, 8, '2', 3, 1, '2019-01-21 08:10:17', 1, NULL),
(322, 8, '2', 3, 4, '2019-01-21 08:10:20', 1, NULL),
(323, 8, '2', 3, 2, '2019-01-21 08:10:22', 1, NULL),
(324, 8, '2', 3, 1, '2019-01-21 08:10:24', 1, NULL),
(325, 8, '2', 3, 4, '2019-01-21 08:10:26', 1, NULL),
(326, 7, '1', 3, 2, '2019-01-21 08:10:28', 1, NULL),
(327, 7, '1', 3, 1, '2019-01-21 08:10:31', 1, NULL),
(328, 7, '1', 3, 3, '2019-01-21 08:10:33', 1, NULL),
(329, 8, '2', 6, 2, '2019-01-21 08:10:35', 1, NULL),
(330, 8, '2', 6, 1, '2019-01-21 08:10:37', 1, NULL),
(331, 8, '2', 6, 3, '2019-01-21 08:10:40', 1, NULL),
(332, 8, '2', 2, 2, '2019-01-21 08:10:42', 1, NULL),
(333, 8, '2', 2, 1, '2019-01-21 08:10:44', 1, NULL),
(334, 8, '2', 2, 4, '2019-01-21 08:10:46', 1, NULL),
(335, 8, '2', 2, 2, '2019-01-21 08:10:48', 1, NULL),
(336, 8, '2', 3, 2, '2019-01-21 08:50:02', 1, NULL),
(337, 8, '2', 3, 1, '2019-01-21 08:50:25', 1, NULL),
(338, 8, '2', 3, 4, '2019-01-21 08:50:27', 1, NULL);

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
(5, 'ฝากไม่ปิด'),
(6, 'ไม่ปิดตู้'),
(7, 'ยกเลิกการใช้งาน'),
(8, 'สำเร็จ');

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

--
-- Indexes for dumped tables
--

--
-- Indexes for table `access`
--
ALTER TABLE `access`
  ADD PRIMARY KEY (`Access_Id`);

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
  ADD KEY `DLK_Id_Locker` (`DLK_Number_Locker`),
  ADD KEY `DLK_id_Result` (`DLK_id_Result`),
  ADD KEY `DLK_Id_condi` (`DLK_Id_condi`);

--
-- Indexes for table `lockers`
--
ALTER TABLE `lockers`
  ADD PRIMARY KEY (`DLK_Id_Locker`);

--
-- Indexes for table `log_status_locker`
--
ALTER TABLE `log_status_locker`
  ADD PRIMARY KEY (`log_Id`);

--
-- Indexes for table `result`
--
ALTER TABLE `result`
  ADD PRIMARY KEY (`DLK_id_Result`);

--
-- Indexes for table `time`
--
ALTER TABLE `time`
  ADD PRIMARY KEY (`DLK_Id_Time`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `access`
--
ALTER TABLE `access`
  MODIFY `Access_Id` int(7) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `conditions`
--
ALTER TABLE `conditions`
  MODIFY `DLK_Id_Condi` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `details`
--
ALTER TABLE `details`
  MODIFY `DLK_Id_Detail` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- AUTO_INCREMENT for table `lockers`
--
ALTER TABLE `lockers`
  MODIFY `DLK_Id_Locker` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `log_status_locker`
--
ALTER TABLE `log_status_locker`
  MODIFY `log_Id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=339;

--
-- AUTO_INCREMENT for table `result`
--
ALTER TABLE `result`
  MODIFY `DLK_id_Result` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `time`
--
ALTER TABLE `time`
  MODIFY `DLK_Id_Time` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `details`
--
ALTER TABLE `details`
  ADD CONSTRAINT `details_ibfk_2` FOREIGN KEY (`DLK_Number_Locker`) REFERENCES `lockers` (`DLK_Id_Locker`),
  ADD CONSTRAINT `details_ibfk_3` FOREIGN KEY (`DLK_id_Result`) REFERENCES `result` (`DLK_id_Result`),
  ADD CONSTRAINT `details_ibfk_4` FOREIGN KEY (`DLK_Id_condi`) REFERENCES `conditions` (`DLK_Id_Condi`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
