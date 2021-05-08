#
#  2020 Traffic Analyzer
#  By Jonathan Rivera
#
#  Description:
#    Working with the assumption that more accidents correlate with more traffic
#    And using historical accident data from Bing Maps API, we can approximate the
#    Amount of traffic per month. Using this data we can see whether or not more
#    People have been travelling overtime, and seeing whether or not people are
#    Travelling more or less.
#  
#  EDIT #1: 
#    The API only gives current traffic data, which means I need to hard
#    code some data.
#
#    Luckily, I was able to find lots of data
# 
#    Traffic Volume (In Billion Vehicle-Miles) (For 2021, I went to their "weekly reports")
#    https://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm
#

Months = [ "Janurary", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ]

TrafficVolume2019 = [ 270.9, 266.7, 269.6, 272.3, 270.5, 270.4, 272.4, 272, 272.9, 272.1, 272.8, 273.4 ]

TrafficVolume2020 = [ 274.8, 274.3, 221.1, 160.9, 199.8, 231.3, 239.7, 239.7, 247.2, 246.8, 244.8, 244.5 ]

# Estimate based off percentage drop from last year
TrafficVolume2021 = [ TrafficVolume2020[0]*.90,  TrafficVolume2020[0]*.91 ]

# Percentage differences from previous month
differences = []

print("\nAn Analysis of Traffic from March 2020 - March 2021")
print("By Jonathan Rivera\n")


# Calculate change in traffic per month for 2020
for i in range(len(TrafficVolume2020)):
    if i == 0:
        differenceFromLastMonth = ((TrafficVolume2020[i]-TrafficVolume2019[11])/TrafficVolume2019[11]) * 100
    
    else:
        differenceFromLastMonth = ((TrafficVolume2020[i]-TrafficVolume2020[i-1])/TrafficVolume2020[i-1]) * 100

    differenceFromLastMonth = format(differenceFromLastMonth, '.1f')
    differences.append(differenceFromLastMonth)


# Calculate change in traffic per month for 2021
for i in range(len(TrafficVolume2021)):
    if i == 0:
        differenceFromLastMonth = ((TrafficVolume2021[i]-TrafficVolume2020[11])/TrafficVolume2020[11]) * 100
    
    else:
        differenceFromLastMonth = ((TrafficVolume2021[i]-TrafficVolume2021[i-1])/TrafficVolume2021[i-1]) * 100

    differenceFromLastMonth = format(differenceFromLastMonth, '.1f')
    differences.append(differenceFromLastMonth)


for i in range(len(differences)):
    isIncrease = True

    if(float(differences[i]) < 0):
        isIncrease = False

    if( i < 12 ):
        print("   ", f'{Months[i]:10}', "2020    Change in traffic: ", f'{str("+ " + differences[i]):>6}' if isIncrease else f'{str("- " + str(abs(float(differences[i])))):>6}', "%  increase" if isIncrease else "%  decrease", "from last month  (", f'{TrafficVolume2020[i]:.1f}' if i < 12 else f'{TrafficVolume2021[i-12]:.1f)}', ")  Bil. Miles")

    else:
        print("   ", f'{Months[i-12]:10}', "2021    Change in traffic: ", f'{str("+ " + differences[i]):>6}' if isIncrease else f'{str("- " + str(abs(float(differences[i])))):>6}', "%  increase" if isIncrease else "%  decrease", "from last month  (", f'{TrafficVolume2020[i]:.1f}' if i < 12 else f'{TrafficVolume2021[i-12]:.1f}', ")  Bil. Miles")

    differences[i] = float(differences[i])


changeIn3Months = ((TrafficVolume2021[1] - TrafficVolume2020[11])/TrafficVolume2020[11]) * 100
changeIn6Months = ((TrafficVolume2021[1] - TrafficVolume2020[8])/TrafficVolume2020[8]) * 100
changeInYear = ((TrafficVolume2021[1] - TrafficVolume2020[2])/TrafficVolume2020[2]) * 100

print("\nChange over past 3 months:  ", f'{changeIn3Months:>6.1f}', " %")
print("Change over past 6 months:  ", f'{changeIn6Months:>6.1f}', " %")
print("Change over past 12 months: ", f'{changeInYear:>6.1f}', " %")

print("\nAnalysis:")
print("\nTraffic has slowly but steadily increased since the initial quarantine.")
print("This signifies that people are becoming more confident in leaving their homes, and proves the hypothesis.\n")

    
