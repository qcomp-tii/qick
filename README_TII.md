# Software for custom Qick firmware with tProc_v2

This document provides a description of the hardware, firmware and software required to use multiple boards to control qubits using Qick and tProc_v2.

The firmware file should be: _'./216_tProc_v8.bit'_. Which has the following features:

- 3 Full Speed Signal Generators (axis_signal_gen_v6) at 9.58464 GSPS in DACs: 0_230, 1_230 & 2_230.
- 5 Interpolated Signal Generators (axis_sg_int4_v2) at 6.88128 GSPS in DACs: 0_228, 1_228, 2_228, 3_228 & 0_229.
- 1 Multiplex Readout (axis_sg_mixmux8_v1) at 6.88128 GSPS in DAC: 2_229.
- 1 Multiplex Readin (axis_pfb_readout_v4) at 2.4576 GSPS in ADC: 0_226.
- Multi-Tile Synchronization between tiles 228 & 229.
- SPI_0 output to control Bias Flux external Analog Front-end (+ driver 'TIDAC80508.py')
- GPIO_0 output to control start pulse of tProc from master to slaves (modifications in qick library + driver 'hello_GPIO.elf').
- LMK04828 configuration file for 'Nested Zero-Delay Dual-Loop' mode using external CLKin0 as reference.
- HMC7044 configuration file to distribute clocks to LMKs.
