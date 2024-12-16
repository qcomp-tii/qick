#SETUP FOR CONTROLLING THE CHIP SPINQ10Q QUBITS 6,7,8,9


### DEFINE INPUTS AND OUTPUTS ###

DC_FLUX     = [2,5,6,7] # Frontend channels - different from DACs
RF_FLUX     = [0,None,1, None]
DRIVE       = [2,3,4,5] # Qick drive channels for qubits 6,7,8,9
PROBE_CH    = 6
FEEDBACK_CH = [0,1,2,3] #ADC
MAX_GAIN    = 32766  
TOF         = 450
LAG         = 88  # ns

### CONFIG PARAMETERS   ###

channel_cfg = { "qubits"        : ["Q6","Q7","Q8","Q9"],
                "flux_ch"    : RF_FLUX, # Channel 6 -> RF_FLUX[0]=0, Channel 8 -> RF_FLUX[2]=1
                "flux_ch_nqz"   : 1,
                "DAC_bias"      : DC_FLUX,
                "drive_ch"   : DRIVE,
                "drive_ch_nqz"  : 2,
                "probe_ch"      : PROBE_CH,
                "probe_ch_nqz"  : 2,
                "feedback_ch"   : FEEDBACK_CH,
                "lag"          : LAG,  # ns
}

qubit_cfg = {
      "Q6":{"drive_ch":DRIVE[0],
            "flux_ch": RF_FLUX[0],
            "sweetspot": -0.156, # update
            "flux_pulse_start": 0,            # [ns]
            "flux_pulse_gain": 0.92,           # 0 to 1
            "flux_pulse_length": 100,        # [ns]probe_c
            "flux_pulse_frequency": 0.0, # [MHz] nqz 1
            "flux_pulse_relative_phase": 0,   # [degrees]
            "flux_pulse_shape": "const",        # constant  
            "drive_pulse_start": 0,            # [ns]
            "drive_pulse_gain": 0.0, #0.3,           # 0 to 1
            "drive_pulse_length": 60,        # [ns]probe_c
            "drive_pulse_frequency": 4814.4, # [MHz] nqz #4135.0, #
            "drive_pulse_relative_phase": 0,   # [degrees]
            "drive_pulse_shape": "arb",        # gauss
            "sigma": 0.02, # [us]           
           },   
     "Q7":{ "drive_ch":DRIVE[1],
            "flux_ch": RF_FLUX[2],           
            "sweetspot": -0.187,# update
            "drive_pulse_start": 0,            # [ns]
            "drive_pulse_gain": 0.0, #0.9,           # 0 to 1
            "drive_pulse_length": 100,        # [ns]probe_c
            "drive_pulse_frequency": 4141.0, #4864.151, #4760.1, #4864.151, # [MHz] nqz 1 
            "drive_pulse_relative_phase": 0,   # [degrees]
            "drive_pulse_shape": "arb",        # gauss
            "sigma": 0.02,                       # [us]          
          },
    "Q8":{"drive_ch":DRIVE[2],
         "flux_ch": RF_FLUX[2],          
        "sweetspot": -0.2, # update
        "flux_pulse_start": 0,            # [ns]
        "flux_pulse_gain": 0.92,           # 0 to 1
        "flux_pulse_length": 100,        # [ns]probe_c
        "flux_pulse_frequency": 0.0, # [MHz] nqz 1
        "flux_pulse_relative_phase": 0,   # [degrees]
        "flux_pulse_shape": "const",        # constant  
        "drive_pulse_start": 0,            # [ns]
        "drive_pulse_gain": 0.3,           # 0 to 1
        "drive_pulse_length": 60,        # [ns]probe_c
        "drive_pulse_frequency": 4781.0, # [MHz] nqz 1 4190.0, #4190.0, #
        "drive_pulse_relative_phase": 0,   # [degrees]
        "drive_pulse_shape": "arb",        # gauss
        "sigma": 0.02,                       # [us]        
    },
    "Q9":{"drive_ch":DRIVE[3],
        "flux_ch": RF_FLUX[3],          
        "sweetspot": -0.22, # update            "q6_flux_pulse_start": 0,            # [ns]
        "drive_pulse_start": 0,            # [ns]
        "drive_pulse_gain": 0.0, #0.9,           # 0 to 1
        "drive_pulse_length": 60,        # [ns]probe_c
        "drive_pulse_frequency": 4142.0, #4850.869, # [MHz] nqz 1 #4755.0, #
        "drive_pulse_relative_phase": 0,   # [degrees]
        "drive_pulse_shape": "arb",        # gauss
        "sigma": 0.02, # [us]        
    },
            
} 

                     

readout_cfg={   "ro_pulse_start": 0,       # [ns]
                "ro_pulse_gain" : [0.07, 0.017, 0.06, 0.04],  # Low power
#                "ro_pulse_gain" : [0.9, 0.9, 0.9, 0.9], #High power
                "ro_pulse_length": 3500,   # [ns]
                "ro_pulse_shape": "const", # rectangular
                "ro_pulse_frequency"    : [7491.732, 7552.237, 7582.338, 7436.382],
                "freq_original"         : [7491.732, 7552.237, 7582.338, 7436.382],
                "acquisition_frequency" : [7491.732, 7552.237, 7582.338, 7436.382],
                "acquisition_length": 3000,      # [ns]
                "delay_before_acquisition": TOF, # missing lags[ns]
                "reps": 2000,                     # Fixed
                "soft_avgs": 1,                  # [ns],
                "relaxation_time": 30000}        # [ns]  

print("Configuration and parameters set")