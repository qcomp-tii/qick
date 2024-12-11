from qick import *
from qick.averager_program import AveragerProgram, QickSweep, merge_sweeps
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.subplots as sp
import numpy as np
from tqdm import tqdm

# import xrfclk
# #xrfclk.set_ref_clks(lmk_freq=245.76, lmx_freq=491.52)

# from pynq.pl_server.global_state import clear_global_state
# clear_global_state()


################################
# Devices Configuration
#################################

### LOAD THE FIRMWARE #######

soc = QickSoc(bitfile='/home/xilinx/jupyter_notebooks/qick/TII/bitstreams/base_MTS_15.bit')
soc_cfg = soc




### INITIALIZE SPI DEVICES ###
### SET POWER FOR DACs ###
import sys
sys.path.append('/home/xilinx/jupyter_notebooks/qick/TII/drivers')

from TIDAC80508 import TIDAC80508
tidac = TIDAC80508()

#import HMC7044_768_SYSREF
#hmc = HMC7044_768_SYSREF()


### SET POWER FOR DACs ###
dac_2280 = soc_cfg.usp_rf_data_converter_0.dac_tiles[0].blocks[0]
dac_2280.SetDACVOP(40000)
dac_2281 = soc_cfg.usp_rf_data_converter_0.dac_tiles[0].blocks[1]
dac_2281.SetDACVOP(40000)
dac_2282 = soc_cfg.usp_rf_data_converter_0.dac_tiles[0].blocks[2]
dac_2282.SetDACVOP(40000)
dac_2283 = soc_cfg.usp_rf_data_converter_0.dac_tiles[0].blocks[3]
dac_2283.SetDACVOP(40000)

dac_2292 = soc_cfg.usp_rf_data_converter_0.dac_tiles[1].blocks[2]
dac_2292.SetDACVOP(40000)

dac_2230 = soc_cfg.usp_rf_data_converter_0.dac_tiles[2].blocks[0]
dac_2230.SetDACVOP(40000)
dac_2232 = soc_cfg.usp_rf_data_converter_0.dac_tiles[2].blocks[2]
dac_2232.SetDACVOP(40000)

### ENABLE MULTI TILE SYNCHRONIZATION ###

soc_cfg.usp_rf_data_converter_0.mts_dac_config.RefTile = 2
soc_cfg.usp_rf_data_converter_0.mts_dac_config.Tiles = 0b0001
soc_cfg.usp_rf_data_converter_0.mts_dac_config.SysRef_Enable = 1
soc_cfg.usp_rf_data_converter_0.mts_dac_config.Target_Latency = -1
soc_cfg.usp_rf_data_converter_0.mts_dac()

def reset_bias():
    tidac.set_bias(channel_cfg["DAC_bias"][0], bias_value=0)
    tidac.set_bias(channel_cfg["DAC_bias"][1], bias_value=0)
    tidac.set_bias(channel_cfg["DAC_bias"][2], bias_value=0)
    tidac.set_bias(channel_cfg["DAC_bias"][3], bias_value=0)
def set_sweetspots():
    tidac.set_bias(channel_cfg["DAC_bias"][0], bias_value=flux_cfg["Q6"]["sweetspot"])
    tidac.set_bias(channel_cfg["DAC_bias"][1], bias_value=flux_cfg["Q7"]["sweetspot"])
    tidac.set_bias(channel_cfg["DAC_bias"][2], bias_value=flux_cfg["Q8"]["sweetspot"])
    tidac.set_bias(channel_cfg["DAC_bias"][3], bias_value=flux_cfg["Q9"]["sweetspot"])
    
