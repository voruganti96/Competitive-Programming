# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After 
# some thought, we see that no matter what number we start with, when we keep replacing 
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n). 
# And that's top-down design! Here we go.... 
# Note: the autograder will grade each of the following functions, so they are required. 
# However, they also are here specifically because they are just the right helper 
# functions to make nthHappyNumber(n) easier to write!

def sumofsquaresofdigit(n):
    l = []
    string = str(n)
    for i in range(0,len(string)):	l.append((int(string[i]))**2)
    return sum(l)

def isprime(n):
	flag = 0
	for i in range(1, n+1,1):
		if n % i ==0:
			flag = flag +1
	if flag ==2:
		return True
	else:
		return False



def ishappynumber(n):
    sos =sumofsquaresofdigit(n)
    #print("Sum of Squares:",sos)
    while sos != 4 and sos != 1:sos = sumofsquaresofdigit(sos)
    if sos ==4:return False
    else:return True

def ishappyprimenumber(n):
    
    if isprime(n) and ishappynumber(n): return True
    
   

def nthHappyNumber(n):
    happy_list = []
    x=0
    for i in range(1,10000):
        if ishappynumber(i) == True: happy_list.append(i)
    #print("Happy Numbers List:\n",happy_list)
    #print("List_length:",len(happy_list))
    x+=(happy_list[n-1])
    #print(n,'th','Happy Number =>',x)
    return x


#happy_list =[1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100, 103, 109, 129, 130, 133, 139, 167, 176, 188, 190, 192, 193, 203, 208, 219, 226, 230, 236, 239, 262, 263, 280, 291, 293, 301, 302, 310, 313, 319, 320, 326, 329, 331, 338, 356, 362, 365, 367, 368, 376, 379, 383, 386, 391, 392, 397, 404, 409, 440, 446, 464, 469, 478, 487, 490, 496, 536, 556, 563, 565, 566, 608, 617, 622, 623, 632, 635, 637, 638, 644, 649, 653, 655, 656, 665, 671, 673, 680, 683, 694, 700, 709, 716, 736, 739, 748, 761, 763, 784, 790, 
#793, 802, 806, 818, 820, 833, 836, 847, 860, 863, 874, 881, 888, 899, 901, 904, 907, 910, 912, 913, 921, 923, 931, 932, 937, 940, 946, 964, 970, 973, 989, 998, 1000, 1003, 1009, 1029, 1030, 1033, 1039, 1067, 1076, 1088, 1090, 1092, 1093, 1112, 1114, 1115, 1121, 1122, 1125, 1128, 1141, 1148, 1151, 1152, 1158, 1177, 1182, 1184, 1185, 1188, 1209, 1211, 1212, 1215, 1218, 1221, 1222, 1233, 1247, 1251, 1257, 1258, 1274, 1275, 1277, 1281, 1285, 1288, 1290, 1299, 1300, 1303, 1309, 1323, 1330, 1332, 1333, 1335, 1337, 1339, 1353, 1366, 1373, 1390, 1393, 1411, 1418, 1427, 1444, 1447, 1448, 1457, 1472, 1474, 1475, 1478, 1481, 1484, 1487, 1511, 1512, 1518, 1521, 1527, 1528, 1533, 1547, 1557, 1572, 1574, 1575, 1578, 1581, 1582, 1587, 1599, 1607, 1636, 1663, 1666, 1670, 1679, 1697, 1706, 1717, 1724, 1725, 1727, 1733, 1742, 1744, 1745, 1748, 1752, 1754, 1755, 1758, 1760, 1769, 1771, 1772, 1784, 1785, 1796, 1808, 1812, 1814, 1815, 1818, 1821, 1825, 1828, 1841, 1844, 1847, 1851, 1852, 1857, 1874, 1875, 1880, 1881, 1882, 1888, 1900, 1902, 1903, 1920, 1929, 1930, 1933, 1959, 1967, 1976, 1992, 1995, 2003, 2008, 2019, 2026, 2030, 2036, 2039, 2062, 2063, 2080, 2091, 2093, 2109, 2111, 2112, 2115, 2118, 2121, 2122, 2133, 2147, 2151, 2157, 2158, 2174, 2175, 2177, 2181, 2185, 2188, 2190, 2199, 2206, 2211, 2212, 2221, 2224, 2242, 2245, 2254, 2257, 2258, 2260, 2275, 2285, 2300, 2306, 2309, 2313, 2331, 2333, 2338, 2339, 2360, 2369, 2383, 2390, 2393, 2396, 2417, 2422, 2425, 2448, 2452, 2455, 2457, 2458, 2471, 2475, 2478, 2484, 2485, 2487, 2511, 2517, 2518, 2524, 2527, 2528, 2542, 2545, 2547, 2548, 2554, 2555, 2557, 2568, 2571, 2572, 2574, 2575, 2581, 2582, 2584, 2586, 2602, 2603, 2620, 2630, 2639, 2658, 2685, 2693, 2714, 2715, 2717, 2725, 2741, 2745, 2748, 2751, 2752, 2754, 2755, 2771, 2784, 2800, 2811, 2815, 2818, 2825, 2833, 2844, 2845, 2847, 2851, 2852, 2854, 2856, 2865, 2874, 2881, 2899, 2901, 2903, 2910, 2919, 2930, 2933, 2936, 2963, 2989, 2991, 2998, 3001, 3002, 3010, 3013, 3019, 3020, 3026, 3029, 3031, 3038, 3056, 3062, 3065, 3067, 3068, 3076, 3079, 3083, 3086, 3091, 3092, 3097, 3100, 3103, 3109, 3123, 3130, 3132, 3133, 3135, 3137, 3139, 3153, 3166, 3173, 3190, 3193, 3200, 3206, 3209, 3213, 3231, 3233, 3238, 3239, 3260, 3269, 3283, 3290, 3293, 3296, 3301, 3308, 3310, 3312, 3313, 3315, 3317, 3319, 3321, 3323, 3328, 3329, 3331, 3332, 3338, 3346, 3351, 3355, 3356, 3364, 3365, 3367, 3371, 3376, 3380, 3382, 3383, 3391, 3392, 3436, 3456, 3463, 3465, 3466, 3506, 3513, 3531, 3535, 3536, 3546, 3553, 3560, 3563, 3564, 3602, 3605, 3607, 3608, 3616, 3620, 3629, 3634, 3635, 3637, 3643, 3645, 3646, 3650, 3653, 3654, 3661, 3664, 3667, 3670, 3673, 3676, 3680, 3689, 3692, 3698, 3706, 3709, 3713, 3731, 3736, 3760, 3763, 3766, 3779, 3789, 3790, 3797, 3798, 3803, 3806, 3823, 3830, 3832, 3833, 3860, 3869, 3879, 3896, 3897, 3901, 3902, 3907, 3910, 3913, 3920, 3923, 3926, 3931, 3932, 3962, 3968, 3970, 3977, 3978, 3986, 3987, 4004, 4009, 4040, 4046, 4064, 4069, 4078, 4087, 4090, 4096, 4111, 4118, 4127, 4144, 4147, 4148, 4157, 4172, 4174, 4175, 4178, 4181, 4184, 4187, 4217, 4222, 4225, 4248, 4252, 4255, 4257, 4258, 4271, 4275, 4278, 4284, 4285, 4287, 4336, 4356, 4363, 4365, 4366, 4400, 4406, 4414, 4417, 4418, 4428, 4441, 4447, 4449, 4455, 4460, 4471, 4474, 4477, 4481, 4482, 4494, 4517, 4522, 4525, 4527, 4528, 4536, 4545, 4552, 4554, 4555, 4558, 4563, 4571, 4572, 4577, 4582, 4585, 4599, 4604, 4609, 4633, 4635, 4636, 4640, 4653, 4663, 4690, 4708, 4712, 4714, 4715, 4718, 4721, 4725, 4728, 4741, 4744, 4747, 4751, 4752, 4757, 4774, 4775, 4780, 4781, 4782, 4788, 4807, 4811, 4814, 4817, 4824, 4825, 4827, 4841, 4842, 4852, 4855, 4870, 4871, 4872, 4878, 4887, 4888, 4900, 4906, 4944, 4959, 4960, 4995, 5036, 5056, 5063, 5065, 5066, 5111, 5112, 5118, 5121, 5127, 5128, 5133, 5147, 5157, 5172, 5174, 5175, 5178, 5181, 5182, 5187, 5199, 5211, 5217, 5218, 5224, 5227, 5228, 5242, 5245, 5247, 5248, 5254, 5255, 5257, 5268, 5271, 5272, 5274, 5275, 5281, 5282, 5284, 5286, 5306, 5313, 5331, 5335, 5336, 5346, 5353, 5360, 5363, 5364, 5417, 5422, 5425, 5427, 5428, 5436, 5445, 5452, 5454, 5455, 5458, 5463, 5471, 5472, 5477, 5482, 5485, 5499, 5506, 5517, 5524, 5525, 5527, 5533, 5542, 5544, 5545, 5548, 5552, 5554, 5555, 5558, 5560, 5569, 5571, 5572, 5584, 5585, 5596, 5603, 5605, 5606, 5628, 5630, 5633, 5634, 5643, 5650, 5659, 5660, 5666, 5682, 5695, 5712, 5714, 5715, 5718, 5721, 5722, 5724, 5725, 5741, 5742, 5747, 5751, 5752, 5774, 5781, 5789, 5798, 5799, 5811, 5812, 5817, 5821, 5822, 5824, 5826, 5842, 5845, 5854, 5855, 5862, 5871, 5879, 5897, 5919, 5949, 5956, 5965, 5978, 5979, 5987, 5991, 5994, 5997, 6008, 6017, 6022, 6023, 6032, 6035, 6037, 6038, 6044, 6049, 6053, 6055, 6056, 6065, 6071, 6073, 6080, 6083, 6094, 6107, 6136, 6163, 6166, 6170, 6179, 6197, 6202, 6203, 6220, 6230, 6239, 6258, 6285, 6293, 6302, 6305, 6307, 6308, 6316, 6320, 6329, 6334, 6335, 6337, 6343, 6345, 6346, 6350, 6353, 6354, 6361, 6364, 6367, 6370, 6373, 6376, 6380, 6389, 6392, 6398, 6404, 6409, 6433, 6435, 6436, 6440, 6453, 6463, 6490, 6503, 6505, 6506, 6528, 6530, 6533, 6534, 6543, 6550, 6559, 6560, 6566, 6582, 6595, 6605, 6613, 6616, 6631, 6634, 6637, 6643, 6650, 6656, 6661, 6665, 6673, 6701, 6703, 6710, 6719, 6730, 6733, 6736, 6763, 6789, 6791, 6798, 6800, 6803, 6825, 6830, 6839, 6852, 6879, 6893, 6897, 6899, 6904, 6917, 6923, 6932, 6938, 6940, 6955, 6971, 6978, 6983, 6987, 6989, 6998, 7000, 7009, 7016, 7036, 7039, 7048, 7061, 7063, 7084, 7090, 7093, 7106, 7117, 7124, 7125, 7127, 7133, 7142, 7144, 7145, 7148, 7152, 7154, 7155, 7158, 7160, 7169, 7171, 7172, 7184, 7185, 7196, 7214, 7215, 7217, 7225, 7241, 7245, 7248, 7251, 7252, 7254, 7255, 7271, 7284, 7306, 7309, 7313, 7331, 7336, 7360, 7363, 7366, 7379, 7389, 7390, 7397, 7398, 7408, 7412, 7414, 7415, 7418, 7421, 7425, 7428, 7441, 7444, 7447, 7451, 7452, 7457, 7474, 7475, 7480, 7481, 7482, 7488, 7512, 7514, 7515, 7518, 7521, 7522, 7524, 7525, 7541, 7542, 7547, 7551, 7552, 7574, 7581, 7589, 7598, 7599, 7601, 7603, 7610, 7619, 7630, 7633, 7636, 7663, 7689, 7691, 7698, 7711, 7712, 7721, 7739, 7744, 7745, 7754, 7788, 7793, 7804, 7814, 7815, 7824, 7839, 7840, 7841, 7842, 7848, 7851, 7859, 7869, 7878, 7884, 7887, 7893, 7895, 7896, 7900, 7903, 7916, 7930, 7937, 7938, 7958, 7959, 7961, 7968, 7973, 7983, 7985, 7986, 7995, 8002, 8006, 8018, 8020, 8033, 8036, 8047, 8060, 8063, 8074, 8081, 8088, 8099, 8108, 8112, 8114, 8115, 8118, 8121, 8125, 8128, 8141, 8144, 8147, 8151, 8152, 8157, 8174, 8175, 8180, 8181, 8182, 8188, 8200, 8211, 8215, 8218, 8225, 8233, 8244, 8245, 8247, 8251, 8252, 8254, 8256, 8265, 8274, 8281, 8299, 8303, 8306, 8323, 8330, 8332, 8333, 8360, 8369, 8379, 8396, 8397, 8407, 8411, 8414, 8417, 8424, 8425, 8427, 8441, 8442, 8452, 8455, 8470, 8471, 8472, 8478, 8487, 8488, 8511, 8512, 8517, 8521, 8522, 8524, 8526, 8542, 8545, 8554, 8555, 8562, 8571, 8579, 8597, 8600, 8603, 8625, 8630, 8639, 8652, 8679, 8693, 8697, 8699, 8704, 8714, 8715, 8724, 8739, 8740, 8741, 8742, 8748, 8751, 8759, 8769, 8778, 8784, 8787, 8793, 8795, 8796, 8801, 8808, 8810, 8811, 8812, 8818, 8821, 8847, 8848, 8874, 8877, 8880, 8881, 8884, 8909, 8929, 8936, 8937, 8957, 8963, 8967, 8969, 8973, 8975, 8976, 8990, 8992, 8996, 9001, 9004, 9007, 9010, 9012, 9013, 9021, 9023, 9031, 9032, 9037, 9040, 9046, 9064, 9070, 9073, 9089, 9098, 9100, 9102, 9103, 9120, 9129, 9130, 9133, 9159, 9167, 9176, 9192, 9195, 9201, 9203, 9210, 9219, 9230, 9233, 9236, 9263, 9289, 9291, 9298, 9301, 9302, 9307, 9310, 9313, 9320, 9323, 9326, 9331, 9332, 9362, 9368, 9370, 9377, 9378, 9386, 9387, 9400, 9406, 9444, 9459, 9460, 9495, 9519, 9549, 9556, 9565, 9578, 9579, 9587, 9591, 9594, 9597, 9604, 9617, 9623, 9632, 9638, 9640, 9655, 9671, 9678, 9683, 9687, 9689, 9698, 9700, 9703, 9716, 9730, 9737, 9738, 9758, 9759, 9761, 9768, 9773, 9783, 9785, 9786, 9795, 9809, 9829, 9836, 9837, 9857, 9863, 9867, 9869, 9873, 9875, 9876, 9890, 9892, 9896, 9908, 9912, 9915, 9921, 9928, 9945, 9951, 9954, 9957, 9968, 9975, 9980, 9982, 9986]

#position = int(input("Please enter a value for 'n':"))
#nthHappyNumber(position)
#print(nthHappyNumber(6))

print(ishappynumber(904))



