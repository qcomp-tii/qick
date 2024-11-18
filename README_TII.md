# Software for custom Qick firmware with tProc_v1

This document provides a description of the hardware, firmware and software require to use multiple boards to control qubits using Qick and tProc_v1.

The firware file should be: _'./base_MTS_14.bit'_. Which has the following features:

- 6 Full Speed Signal Generators (axis_signal_gen_v6) at 6.144 GSPS in DACs 0_228, 1_228, 0_229, 1_229, 2_229 and 3_229.
- 1 Multiplex Readout (axis_sg_mux8_v1) at 9.8304 GSPS in DAC: 0_230
- 1 Multiplex Readin (axis_pfb_readout_v4) at 2.4576 GSPS in ADC: 0_226.

