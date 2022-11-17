import requests
# import prod_client_list_data
import V1_get_Authorization


import json

# data = prod_client_list_data.get_client_list()
# id_prod = []
# for i in data:
#     id = i["id"]
#     id_prod.append(id)
# print(id_prod)

id_prod = [1, 3, 6, 7, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 90, 91, 92, 93, 94, 95, 96, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 133, 135, 138, 140, 141, 143, 144, 145, 146, 148, 151, 152, 153, 154, 155, 156, 159, 160, 161, 162, 163, 165, 166, 168, 169, 171, 172, 173, 174, 177, 178, 179, 181, 182, 184, 185, 186, 189, 190, 192, 194, 195, 201, 204, 205, 206, 209, 211, 213, 214, 215, 220, 221, 222, 223, 226, 227, 228, 234, 238, 239, 240, 241, 245, 248, 250, 251, 254, 255, 256, 257, 260, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 273, 274, 275, 277, 278, 281, 283, 284, 285, 286, 287, 288, 289, 290, 291, 293, 294, 295, 296, 297, 298, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 317, 324, 326, 327, 330, 332, 335, 337, 339, 342, 344, 346, 349, 350, 353, 354, 358, 361, 362, 363, 364, 379, 382, 384, 393, 410, 420, 422, 423, 427, 428, 430, 440, 442, 447, 448, 452, 460, 465, 468, 470, 474, 475, 478, 484, 487, 488, 489, 495, 496, 497, 499, 500, 502, 503, 504, 506, 507, 508, 509, 511, 512, 513, 514, 515, 516, 517, 522, 526, 527, 528, 530, 531, 532, 533, 534, 538, 539, 541, 542, 549, 550, 567, 571, 575, 579, 585, 586, 621, 633, 634, 660, 664, 670, 671, 677, 686, 687, 744, 746, 755, 758, 760, 761, 762, 776, 782, 791, 792, 793, 794, 795, 796, 800, 801, 802, 803, 805, 806, 807, 812, 815, 817, 823, 827, 830, 831, 832, 833, 834, 839, 840, 843, 844, 845, 847, 851, 852, 853, 854, 858, 861, 863, 864, 866, 867, 871, 872, 874, 877, 882, 884, 886, 887, 889, 890, 891, 892, 893, 895, 896, 897, 902, 903, 904, 907, 908, 909, 913, 921, 938, 939, 941, 942, 943, 953, 954, 955, 959, 962, 963, 964, 966, 967, 968, 970, 976, 977, 978, 1027, 1028, 1045, 1047, 1065, 1066, 1068, 1073, 1078, 1083, 1084, 1085, 1091, 1094, 1104, 1111, 1112, 1113, 1114, 1122, 1124, 1125, 1127, 1128, 1131, 1141, 1144, 1145, 1151, 1156, 1159, 1160, 1171, 1176, 1177, 1183, 1186, 1194, 1195, 1201, 1205, 1207, 1208, 1209, 1210, 1214, 1215, 1218, 1236, 1237, 1238, 1241, 1242, 1243, 1244, 1250, 1254, 1255, 1256, 1258, 1259, 1260, 1261, 1262, 1263, 1264, 1267, 1268, 1269, 1271, 1272, 1273, 1275, 1276, 1278, 1280, 1281, 1291, 1293, 1294, 1295, 1297, 1298, 1299, 1300, 1301, 1302, 1303, 1304, 1305, 1306, 1307, 1309, 1310, 1338, 1339, 1341, 1342, 1344, 1345, 1346, 1347, 1348, 1349, 1350, 1351, 1352, 1353, 1354, 1355, 1356, 1357, 1358, 1359, 1360, 1361, 1362, 1363, 1364, 1365, 1366, 1367, 1368, 1370, 1372, 1374, 1375, 1377, 1378, 1379, 1380, 1381, 1387, 1388, 1389, 1391, 1392, 1393, 1394, 1395, 1397, 1398, 1399, 1400, 1401, 1402, 1403, 1404, 1405, 1406, 1407, 1408, 1410, 1412, 1416, 1417, 1418, 1420, 1421, 1422, 1423, 1424, 1425, 1426, 1427, 1428, 1429, 1430, 1432, 1433, 1434, 1436, 1437, 1438, 1439, 1440, 1441, 1442, 1443, 1444, 1445, 1446, 1447, 1448, 1449, 1450, 1451, 1452, 1453, 1454, 1455, 1456, 1457, 1458, 1459, 1460, 1462, 1463, 1465, 1468, 1469, 1470, 1471, 1473, 1474, 1475, 1476, 1477, 1478, 1479, 1480, 1483, 1484, 1486, 1487, 1488, 1489, 1490, 1493, 1494, 1495, 1496, 1497, 1498, 1499, 1500, 1501, 1502, 1503, 1504, 1505, 1506, 1510, 1511, 1512, 1513, 1514, 1515, 1516, 1517, 1519, 1520, 1522, 1523, 1525, 1526, 1527, 1528, 1529, 1531, 1533, 1534, 1535, 1536, 1537, 1538, 1539, 1540, 1541, 1543, 1544, 1545, 1546, 1547, 1548, 1549, 1550, 1551, 1552, 1554, 1555, 1556, 1557, 1559, 1560, 1561, 1562, 1563, 1564, 1565, 1566, 1567, 1571, 1572, 1573, 1574, 1575, 1576, 1577, 1580, 1582, 1583, 1584, 1585, 1586, 1587, 1588, 1589, 1590, 1591, 1594, 1595, 1596, 1598, 1600, 1602, 1603, 1605, 1606, 1607, 1608, 1609, 1610, 1611, 1613, 1614, 1615, 1616, 1617, 1618, 1619, 1620, 1621, 1622, 1623, 1624, 1626, 1628, 1629, 1630, 1631, 1632, 1633, 1634, 1635, 1636, 1637, 1638, 1639, 1640, 1641, 1642, 1644, 1645, 1646, 1647, 1648, 1649, 1650, 1653, 1654, 1656, 1657, 1658, 1659, 1660, 1661, 1662, 1663, 1664, 1665, 1666, 1667, 1669, 1670, 1671, 1672, 1673, 1674, 1675, 1676, 1677, 1678, 1679, 1680, 1681, 1682, 1686, 1687, 1688, 1690, 1691, 1692, 1693, 1694, 1695, 1696, 1697, 1698, 1699, 1701, 1702, 1703, 1704, 1705, 1706, 1707, 1708, 1709, 1712, 1713, 1714, 1715, 1716, 1717, 1718, 1720, 1721, 1722, 1723, 1732, 1736, 1738, 1739, 1740, 1741, 1742, 1743, 1744, 1745, 1746, 1747, 1748, 1749, 1750, 1751, 1752, 1753, 1754, 1755, 1756, 1757, 1758, 1759, 1760, 1762, 1763, 1764, 1765, 1766, 1768, 1769, 1770, 1773, 1774, 1775, 1776, 1777, 1778, 1779, 1780, 1781, 1782, 1783, 1784, 1785, 1786, 1787, 1788, 1789, 1790, 1791, 1792, 1793, 1794, 1795, 1796, 1814, 1815, 1816, 1817, 1818, 1819, 1822, 1823, 1824, 1825, 1826, 1827, 1828, 1829, 1830, 1831, 1832, 1833, 1834, 1835, 1836, 1838, 1839, 1840, 1842, 1843, 1844, 1845, 1846, 1847, 1848, 1849, 1850, 1851, 1852, 1853, 1854, 1855, 1856, 1857, 1858, 1859, 1860, 1861, 1862, 1864, 1865, 1869, 1870, 1871, 1873, 1874, 1875, 1876, 1877, 1878, 1879, 1880, 1881, 1882, 1885, 1887, 1888, 1889, 1892, 1893, 1894, 1895, 1896, 1897, 1898, 1900, 1901, 1902, 1903, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1915, 1916, 1917, 1919, 1922, 1925, 1926, 1927, 1928, 1929, 1930, 1933, 1934, 1935, 1936, 1938, 1939, 1940, 1943, 1944, 1945, 1946, 1947, 1948, 1949, 1950, 1951, 1952, 1953, 1954, 1955]
proxies = {
    'http': 'http://127.0.0.1:4780',
    'https': 'http://127.0.0.1:4780'
}
Authorization = V1_get_Authorization.get_V1Authorization()
headers = {'Authorization': Authorization,
           'Content-Type': 'application/json'}
final_overview_data = []
for id in id_prod:
    print(id)
    url = "https://api.hitalentech.com/api/v1/company/{}".format(id) + "?type=0"
    while True:
        try:
            res = requests.get(url=url, headers=headers,proxies=proxies)
            break
        except Exception as e:
            print(e)


    original_data = res.json()
    #print(original_data)
    try:
        original_sals = original_data["salesLead"]
    except:
        print(str(id) + 'wrong')
        print(original_data)

    if original_sals != None:
        salesLeadDetails = []
        for sales_ele in original_sals:  ### 获取am

            am_original = sales_ele["accountManager"]
            am = []
            for i in am_original:
                am_id = i["id"]
                am.append(am_id)
### 获取bd
        bd_original = sales_ele["bdManagers"]
        bd = []
        for j in bd_original:
            bd_ele = {"salesLeadId":j["salesLeadId"],"userId":j["userId"],"contribution":j["percentage"]}
            bd.append(bd_ele)
### 获取sales owner
        owners_original = sales_ele["owners"]
        owner = []
        for owner_yuansu in owners_original:
            owner_ele = {"salesLeadId":owner_yuansu["salesLeadId"],"userId":owner_yuansu["userId"],"contribution":owner_yuansu["percentage"]}
            owner.append(owner_ele)
        sales_yuansu = {"id":sales_ele["salesLeadId"],"accountManagers":am,"businessDevelopmentOwner":bd,"salesLeadsOwner":owner}
    else :
        am = []
        bd = []
        owner = []

###### 获取primary adress

        # print(sales_ele)
    primary_adress_original = original_data["primaryAddress"]
    companyAddresses_primary =  {"address":primary_adress_original["address"],"address2":primary_adress_original["address2"],"geoInfoEN":{"cityId":primary_adress_original["cityId"],"city":primary_adress_original["city"],"province":primary_adress_original["province"],"country":primary_adress_original["country"]},"companyAddressType":"PRIMARY"}

    oters_adress_original = original_data["additionalAddresses"]
    if len(oters_adress_original) <1 :
        oters_adress = []
        for oters in oters_adress_original:
            othes_ele ={"address":oters["address"],"address2":oters["address2"],"geoInfoEN":{"cityId":oters["cityId"],"city":oters["city"],"province":oters["province"],"country":oters["country"]},"companyAddressType":"OTHER"}
            oters_adress.append(owner_ele)
    else:
        oters_adress = []

    overview_data = {
	"id": original_data["id"],
	"logo": original_data["logo"],
	"name": original_data["name"],
	"industry": original_data["industry"],
	"website": original_data["website"],
	"fortuneRank": original_data["fortuneRank"],
	"sourceLink": None,
	"businessRevenue": original_data["businessRevenue"],
	"staffSizeType": original_data["staffSizeType"],
	"linkedinCompanyProfile": original_data["linkedinCompanyProfile"],
	"crunchbaseCompanyProfile": original_data["crunchbaseCompanyProfile"],
	"type": "CLIENT",
	"companyClientLevelType": original_data["type"],
	"active": original_data["active"],
	"tenantId": 4,
	"description": original_data["description"],
	"s3_link": None,
	"organizationName": None,
	"am":am,
    "bd":bd,
    "owner":owner,
	"companyAddresses_primary": companyAddresses_primary,
	"oters_adress" : oters_adress
}

    final_overview_data.append(overview_data)

print(final_overview_data)
f = open('client_overview_prod_jsonlist.py','w', encoding='utf-8')
f.write(json.dumps(final_overview_data, ensure_ascii=False,indent=4))


