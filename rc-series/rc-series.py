#!/user/bin/python3

import argparse
import matplotlib.pyplot as plt
import numpy as np

# Simulates the output of an RC (series) circuit 
#
# The following scenarios are possible: 
# 
# (1) C is charging since the input is attached to a
#   DC power supply (Vs), namely:
#
#                     R
#                  +-----+
#      +-----------|     |-----------+ Vo
#      |           +-----+           |
#      |                             |
#    ----- Vs                     ------- C 
#     ---                         -------
#      |                             |
#      |                             |
#    -----                         -----
#     ---                           ---
#      -                             -
#   
#   e.g.:
#   $ python3 rc-series.py --Vs 12.26 --Vo 6.0 --R 3300 --C 4.7 --t 5
#
# (2) C is discharging since the powser supply has been 
#   disattached, namely:
#
#                     R
#                  +-----+
#      +-----------|     |-----------+ Vo
#      |           +-----+           |
#      |                             |
#      |                          ------- C 
#      |                          -------
#      |                             |
#      |                             |
#    -----                         -----
#     ---                           ---
#      -                             -
#   
#   e.g.:
#   $ python3 rc-series.py --Vo 6.13 --R 3300 --C 4.7 --t 5

def parse_args():

    parser = argparse.ArgumentParser(
        prog="RC (series) circuit simulator",
        description="Simulates the output of an RC (series) circuit (both charging and discharging)"
    )

    parser.add_argument('--Vs', help='Source voltage [V] (required for charging)', default=0.0, type=float)
    parser.add_argument('--Vo', help='Initial voltage across C [V] (required for discharging, optional for charging)', default=0.0, type=float)
    parser.add_argument('--R', help='Resistance of R [Ω]', required=True, type=float)
    parser.add_argument('--C', help='Capacitance of C [µF]', required=True, type=float)
    parser.add_argument('--t', help='Simulation time [s]', default=120, type=int)

    args = parser.parse_args()

    return args 

def Vout(Vs, Vo, R, C, t):
    
    Vout = Vs + (Vo - Vs) * np.exp( -t / (R*C) )
    
    return Vout

def simulate(Vs, Vo, R, C, t):

    V_t = []
    _t = []

    step = 0.0
    while (step <= t):
        _t.append(step)
        V_t.append(Vout(Vs, Vo, R, C, step))
        step = step + t / 1000.0 # 1000 steps within simulation time 

    return V_t, _t

def main():

    args = parse_args()

    Vs = args.Vs
    Vo = args.Vo
    R = args.R
    C = args.C * 10E-6 # Input C is expressed in µF
    t = args.t

    V_t, _t = simulate(Vs, Vo, R, C, t)

    Vs_t = []
    Vo_t = []
    for step in _t:
        Vs_t.append(Vs)
        Vo_t.append(Vo)

    fig, ax = plt.subplots()
    ax.plot(_t, V_t, label='Vout(t)')
    ax.plot(_t, Vs_t, label='Vs', linestyle='dotted')
    ax.plot(_t, Vo_t, label='Vo', linestyle='dotted')
    ax.legend()
    
    plt.title('RC (series) output')
    plt.grid()
    plt.xlabel('t [s]')
    plt.ylabel('Voltage [V]')
    plt.show()

main() 
