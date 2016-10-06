# How long does the data spend at the routers?

#info given in question

total_time = 75 #milliseconds tracerout, round trip Birmingham -> Sundsvall
one_way_distance = 2500.0 # km, Birmingham -> Sundsvall, . added to rm rounding
optic_speed = 200000 #km/s
ms_per_second = 1000 # conversion from ms to seconds [ms/sec]

# Calculations
time_on_the_wires = 2*one_way_distance / optic_speed * ms_per_second # km / [km/sec] * [ms/s]
total_time_at_routers = total_time - time_on_the_wires
print total_time_at_routers 
