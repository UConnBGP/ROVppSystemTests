import sys
sys.path.append('./lib_bgp_data')
from lib_bgp_data import ROVPP_Simulator as Sim

Sim({"stream_level": 20}).simulate(percents=[5, 10, 15, 20, 25, 30], trials=1, exr_test=True, exr_bash="/usr/bin/rovpp-rovtest-extrapolator -v 1 -t rovpp_top_100_ases -t rovpp_etc_ases -t rovpp_edge_ases")

#Sim().simulate(percents=[5,10,15,20,25,30], trials=10)

#Sim({"stream_level": 20}).simulate(percents=[50], trials=5, exr_test=True, exr_bash="/usr/bin/rovpp-extrapolator -v 1 -t rovpp_top_100_ases -t rovpp_etc_ases -t rovpp_edge_ases")

#Sim({"stream_level": 20}).simulate(percents=[0], trials=1)
