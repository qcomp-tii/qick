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
    tidac.set_bias(channel_cfg["DAC_bias"][0], bias_value=flux_cfg["q6_sweetspot"])
    tidac.set_bias(channel_cfg["DAC_bias"][1], bias_value=flux_cfg["q7_sweetspot"])
    tidac.set_bias(channel_cfg["DAC_bias"][2], bias_value=flux_cfg["q8_sweetspot"])
    tidac.set_bias(channel_cfg["DAC_bias"][3], bias_value=flux_cfg["q9_sweetspot"])
    
    ### DEFINE INPUTS AND OUTPUTS ###

DC_FLUX     = [2,5,6,7] # Froentend channels - different from DACs
RF_FLUX     = [0,None,1, None]
DRIVE       = [2,3,4,5]
PROBE_CH    = 6
FEEDBACK_CH = [0,1,2,3] #ADC
MAX_GAIN    = 32766  
TOF         = 450
LAG         = 88  # ns

### CONFIG PARAMETERS   ###

channel_cfg = { "q6_flux_ch"    : RF_FLUX[0],
                "q8_flux_ch"    : RF_FLUX[1],
                "flux_ch_nqz"   : 1,
                "DAC_bias"      : DC_FLUX,
                "q6_drive_ch"   : DRIVE[0],
                "q7_drive_ch"   : DRIVE[1],
                "q8_drive_ch"   : DRIVE[2],
                "q9_drive_ch"   : DRIVE[3],
                "drive_ch_nqz"  : 2,
                "probe_ch"      : PROBE_CH,
                "probe_ch_nqz"  : 2,
                "feedback_ch"   : FEEDBACK_CH,
                "lag"          : LAG,  # ns
}

flux_cfg = {    "q6_sweetspot": 0.12, # update
                "q7_sweetspot": 0.14, # update
                "q8_sweetspot": 0.26, # update
                "q9_sweetspot": 0.24, # update
            
                "q6_flux_pulse_start": 0,            # [ns]
                "q6_flux_pulse_gain": 0.92,           # 0 to 1
                "q6_flux_pulse_length": 100,        # [ns]probe_c
                "q6_flux_pulse_frequency": 0.0, # [MHz] nqz 1
                "q6_flux_pulse_relative_phase": 0,   # [degrees]
                "q6_flux_pulse_shape": "const",        # constant
            
                "q8_flux_pulse_start": 0,            # [ns]
                "q8_flux_pulse_gain": 0.92,           # 0 to 1
                "q8_flux_pulse_length": 100,        # [ns]probe_c
                "q8_flux_pulse_frequency": 0.0, # [MHz] nqz 1
                "q8_flux_pulse_relative_phase": 0,   # [degrees]
                "q8_flux_pulse_shape": "const",        # constant            
} 

drive_cfg={ 
    "Q6" :{
        "drive_pulse_start": 0,            # [ns]
        "drive_pulse_gain": 0.3,           # 0 to 1
        "drive_pulse_length": 60,        # [ns]probe_c
        "drive_pulse_frequency": 4226.503, # [MHz] nqz #4135.0, #
        "drive_pulse_relative_phase": 0,   # [degrees]
        "drive_pulse_shape": "arb",        # gauss
        "sigma": 0.02, # [us]
    },
    "Q7":{

        "drive_pulse_start": 0,            # [ns]
        "drive_pulse_gain": 0.9,           # 0 to 1
        "drive_pulse_length": 60,        # [ns]probe_c
        "drive_pulse_frequency": 4766.1, #4864.151, #4760.1, #4864.151, # [MHz] nqz 1 
        "drive_pulse_relative_phase": 0,   # [degrees]
         "drive_pulse_shape": "arb",        # gauss
         "sigma": 0.02,                       # [us]
    },
    "Q8":{
        "drive_pulse_start": 0,            # [ns]
        "drive_pulse_gain": 0.3,           # 0 to 1
        "drive_pulse_length": 60,        # [ns]probe_c
        "drive_pulse_frequency": 4285.281, # [MHz] nqz 1 4190.0, #4190.0, #
        "drive_pulse_relative_phase": 0,   # [degrees]
        "drive_pulse_shape": "arb",        # gauss
        "sigma": 0.02,                       # [us]
    },
    "Q9":{
        "drive_pulse_start": 0,            # [ns]
        "drive_pulse_gain": 0.9,           # 0 to 1
        "drive_pulse_length": 80,        # [ns]probe_c
        "drive_pulse_frequency": 4750.0, #4850.869, # [MHz] nqz 1 #4755.0, #
        "drive_pulse_relative_phase": 0,   # [degrees]
        "drive_pulse_shape": "arb",        # gauss
        "sigma": 0.02, # [us]
    }
          }                       

readout_cfg={   "ro_pulse_start": 0,       # [ns]
#                "ro_pulse_gain" : [0.24, 0.45, 0.24, 0.6],
                "ro_pulse_gain" : [0.9, 0.9, 0.9, 0.9], #High power
                "ro_pulse_length": 3500,   # [ns]
                "ro_pulse_shape": "const", # rectangular
                "ro_pulse_frequency"    : [7490.8, 7551.0, 7581.39, 7439.64],
                "freq_original"         : [7490.8, 7551.0, 7581.39, 7439.64],
                "acquisition_frequency" : [7490.8, 7551.0, 7581.39, 7439.64],
                "acquisition_length": 3000,      # [ns]
                "delay_before_acquisition": TOF, # missing lags[ns]
                "reps": 2000,                     # Fixed
                "soft_avgs": 1,                  # [ns],
                "relaxation_time": 30000}        # [ns]  

print("Configuration and paramiters set")