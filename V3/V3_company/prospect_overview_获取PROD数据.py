# Time : 2022/11/2 15:35
import json
import pickle
from datetime import datetime

import requests

import V1_get_Authorization

'''
[13, 17, 23, 51, 117, 136, 137, 139, 142, 147, 149, 150, 157, 158, 167, 170, 175, 176, 180, 187, 188, 191, 196, 197, 198, 199, 200, 202, 203, 207, 216, 217, 218, 219, 224, 225, 229, 230, 231, 232, 233, 235, 236, 237, 242, 243, 244, 246, 247, 249, 252, 253, 258, 259, 261, 272, 276, 279, 280, 282, 292, 299, 300, 316, 318, 319, 320, 321, 322, 323, 325, 328, 329, 331, 333, 334, 335, 336, 338, 340, 341, 343, 345, 351, 352, 355, 356, 357, 359, 360, 361, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 385, 386, 387, 388, 389, 390, 391, 392, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 411, 412, 413, 414, 415, 416, 417, 418, 419, 421, 424, 425, 426, 429, 431, 432, 433, 434, 435, 436, 437, 438, 439, 441, 443, 444, 445, 446, 449, 450, 451, 453, 454, 455, 456, 457, 458, 459, 461, 462, 463, 464, 466, 467, 469, 471, 472, 473, 476, 477, 479, 480, 481, 482, 483, 485, 486, 494, 498, 499, 501, 505, 510, 518, 519, 520, 521, 523, 524, 525, 529, 535, 536, 537, 539, 540, 543, 544, 545, 546, 547, 548, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 568, 569, 570, 572, 573, 574, 576, 577, 578, 580, 581, 582, 583, 584, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 661, 662, 663, 665, 666, 667, 668, 669, 672, 673, 674, 675, 676, 678, 679, 680, 685, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 745, 747, 748, 749, 750, 751, 752, 753, 754, 756, 757, 759, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 777, 778, 779, 780, 781, 783, 784, 785, 786, 787, 788, 789, 790, 793, 797, 799, 804, 808, 809, 810, 811, 813, 814, 816, 818, 819, 820, 821, 822, 824, 825, 826, 828, 829, 835, 836, 837, 838, 841, 842, 846, 847, 848, 849, 850, 856, 857, 859, 860, 862, 865, 868, 869, 870, 873, 875, 876, 878, 879, 880, 881, 883, 885, 888, 891, 894, 898, 899, 900, 901, 905, 906, 910, 911, 912, 914, 915, 916, 917, 918, 919, 920, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 940, 941, 944, 945, 946, 947, 948, 949, 950, 951, 952, 956, 957, 958, 960, 961, 965, 969, 971, 972, 973, 974, 975, 1027, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1067, 1069, 1070, 1071, 1072, 1074, 1075, 1076, 1077, 1080, 1081, 1082, 1086, 1087, 1088, 1089, 1090, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099, 1100, 1101, 1102, 1103, 1105, 1106, 1107, 1108, 1109, 1110, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1123, 1125, 1126, 1128, 1129, 1130, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139, 1140, 1142, 1143, 1145, 1146, 1147, 1148, 1149, 1150, 1152, 1153, 1154, 1155, 1157, 1158, 1161, 1162, 1163, 1164, 1165, 1166, 1167, 1169, 1170, 1172, 1173, 1174, 1175, 1178, 1179, 1180, 1181, 1182, 1184, 1188, 1189, 1190, 1191, 1192, 1193, 1196, 1198, 1199, 1200, 1201, 1202, 1203, 1204, 1206, 1211, 1212, 1213, 1216, 1217, 1219, 1220, 1221, 1222, 1223, 1224, 1225, 1226, 1227, 1228, 1229, 1230, 1231, 1233, 1234, 1235, 1239, 1240, 1241, 1245, 1249, 1253, 1257, 1258, 1265, 1266, 1274, 1277, 1279, 1282, 1283, 1284, 1299, 1300, 1310, 1340, 1343, 1367, 1369, 1371, 1373, 1376, 1385, 1386, 1390, 1392, 1394, 1409, 1411, 1415, 1416, 1417, 1419, 1424, 1431, 1435, 1444, 1449, 1457, 1461, 1464, 1466, 1467, 1472, 1485, 1491, 1492, 1507, 1508, 1509, 1514, 1516, 1518, 1521, 1524, 1530, 1539, 1553, 1560, 1572, 1578, 1581, 1586, 1589, 1599, 1600, 1601, 1604, 1605, 1612, 1616, 1627, 1630, 1643, 1644, 1648, 1650, 1654, 1655, 1664, 1677, 1689, 1693, 1695, 1699, 1714, 1719, 1720, 1724, 1725, 1726, 1727, 1728, 1729, 1730, 1731, 1733, 1734, 1735, 1736, 1737, 1738, 1745, 1751, 1757, 1761, 1770, 1771, 1775, 1777, 1785, 1811, 1836, 1837, 1856, 1866, 1867, 1868, 1869, 1872, 1875, 1877, 1883, 1884, 1886, 1890, 1891, 1899, 1904, 1914, 1918, 1921, 1923, 1924, 1931, 1932, 1936, 1937, 1941, 1942, 1953, 1955, 1959, 1966, 1967, 1968, 1969, 1970, 1975, 1976, 1977, 1978, 1983, 1984, 1988, 1992, 1995, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2014, 2017, 2024, 2026, 2028]

'''

proxies = {
    'http': 'http://127.0.0.1:4780',
    'https': 'http://127.0.0.1:4780'
}

def getV1prospectids(header):
    url = 'https://api.hitalentech.com/api/v1/companies?type=2'
    while True:
        try:
            resp = requests.get(url, headers=header, proxies=proxies)
            break
        except Exception as e:
            print(e)
    print(resp.status_code)
    compIDs = []
    for j in resp.json()['clients']:
        compIDs.append(j['id'])

    #print(compIDs)
    #print(len(compIDs))
    return compIDs


def getV1prospectdetails(id_, header):
    url = f'https://api.hitalentech.com/api/v1/company/{id_}?type=1'
    while True:
        try:
            resp = requests.get(url, headers=header, proxies=proxies)
            break
        except Exception as e:
            print(e)
    print(resp.status_code)

    comp = {}
    comp['id'] = resp.json()['id']
    comp['companyName'] = resp.json()['name']
    comp['industry'] = resp.json()['industry']
    comp['website'] = resp.json()['website']
    comp['fortuneRank'] = resp.json()['fortuneRank']
    comp['staffSizeType'] = resp.json()['staffSizeType']
    comp['businessRevenue'] = resp.json()['businessRevenue']
    comp['linkedinCompanyProfile'] = resp.json()['linkedinCompanyProfile']
    comp['crunchbaseCompanyProfile'] = resp.json()['crunchbaseCompanyProfile']
    comp['logo'] = resp.json()['logo']




    address = []
    address.append(resp.json()['primaryAddress']['address'])
    for i in resp.json()['additionalAddress']:
        address.append(i['address'])
    comp['address'] = address

    addressStr = []
    addressStr.append({
        'city' : resp.json()['primaryAddress']['city'],
        'province' : resp.json()['primaryAddress']['province'],
        'country' : resp.json()['primaryAddress']['country']
    })

    for i in resp.json()['additionalAddress']:
        addressStr.append({
        'city' : i['city'],
        'province' : i['province'],
        'country' : i['country']
    })

    comp['addressStr'] = addressStr

    clientContact = []
    estimatedDealTime = []
    accountProgress = []
    serviceTypeNames = []
    leadSource = []
    saleLeadOwners = []
    for i in resp.json()['salesLead']:
        estimatedDealTime.append(i['estimatedDealTime'])
        accountProgress.append(i['accountProgress'])
        leadSource.append(i['leadSource'])
        for s in i['serviceTypeNames']:
            serviceTypeNames.append(s)
        for c in i['contacts']:
            clientContact.append(c['name'])
        for slo in i['saleLeadOwners']:
            saleLeadOwners.append(slo)
    comp['saleLeadOwners'] = saleLeadOwners
    comp['clientContact'] = clientContact
    comp['estimatedDealTime'] = estimatedDealTime
    comp['accountProgress'] = accountProgress
    comp['serviceTypeNames'] = serviceTypeNames
    comp['leadSource'] = leadSource

    teamMembers = []
    for t in resp.json()['teamNumbers']:
        teamMembers.append(t['firstName'] + ' ' + t['lastName'])
    comp['teamMembers'] = teamMembers

    #print(json.dumps(comp, indent=4))
    return comp

if __name__ == '__main__':
    while True:
        try:
            Authorization = V1_get_Authorization.get_V1Authorization()
            break
        except Exception as e:
            print(e)

    header = {'Authorization': Authorization}
    compIDs = getV1prospectids(header)
    #compIDs = [1100,1221]

    datas = []
    for id_ in compIDs:
        print(f'处理中 : {id_} ..')
        datas.append(getV1prospectdetails(id_, header))


    f = open('Prod_prospect.txt', 'w', encoding='utf-8')

    json.dump(datas,f, indent=4, ensure_ascii=False)
