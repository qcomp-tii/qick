vlib questa_lib/work
vlib questa_lib/msim

vlib questa_lib/msim/xilinx_vip
vlib questa_lib/msim/xil_defaultlib
vlib questa_lib/msim/xpm
vlib questa_lib/msim/axis_infrastructure_v1_1_0
vlib questa_lib/msim/axi4stream_vip_v1_1_5

vmap xilinx_vip questa_lib/msim/xilinx_vip
vmap xil_defaultlib questa_lib/msim/xil_defaultlib
vmap xpm questa_lib/msim/xpm
vmap axis_infrastructure_v1_1_0 questa_lib/msim/axis_infrastructure_v1_1_0
vmap axi4stream_vip_v1_1_5 questa_lib/msim/axi4stream_vip_v1_1_5

vlog -work xilinx_vip -64 -sv -L axi_vip_v1_1_5 -L axi4stream_vip_v1_1_5 -L xilinx_vip "+incdir+/home/tools/Xilinx/Vivado/2019.1/data/xilinx_vip/include" \
"/home/tools/Xilinx/Vivado/2019.1/data/xilinx_vip/hdl/axi4stream_vip_axi4streampc.sv" \
"/home/tools/Xilinx/Vivado/2019.1/data/xilinx_vip/hdl/axi_vip_axi4pc.sv" \
"/home/tools/Xilinx/Vivado/2019.1/data/xilinx_vip/hdl/xil_common_vip_pkg.sv" \
"/home/tools/Xilinx/Vivado/2019.1/data/xilinx_vip/hdl/axi4stream_vip_pkg.sv" \
"/home/tools/Xilinx/Vivado/2019.1/data/xilinx_vip/hdl/axi_vip_pkg.sv" \
"/home/tools/Xilinx/Vivado/2019.1/data/xilinx_vip/hdl/axi4stream_vip_if.sv" \
"/home/tools/Xilinx/Vivado/2019.1/data/xilinx_vip/hdl/axi_vip_if.sv" \
"/home/tools/Xilinx/Vivado/2019.1/data/xilinx_vip/hdl/clk_vip_if.sv" \
"/home/tools/Xilinx/Vivado/2019.1/data/xilinx_vip/hdl/rst_vip_if.sv" \

vlog -work xil_defaultlib -64 -sv -L axi_vip_v1_1_5 -L axi4stream_vip_v1_1_5 -L xilinx_vip "+incdir+../../../ipstatic/hdl" "+incdir+/home/tools/Xilinx/Vivado/2019.1/data/xilinx_vip/include" \
"/home/tools/Xilinx/Vivado/2019.1/data/ip/xpm/xpm_cdc/hdl/xpm_cdc.sv" \

vcom -work xpm -64 -93 \
"/home/tools/Xilinx/Vivado/2019.1/data/ip/xpm/xpm_VCOMP.vhd" \

vlog -work axis_infrastructure_v1_1_0 -64 "+incdir+../../../ipstatic/hdl" "+incdir+/home/tools/Xilinx/Vivado/2019.1/data/xilinx_vip/include" \
"../../../ipstatic/hdl/axis_infrastructure_v1_1_vl_rfs.v" \

vlog -work xil_defaultlib -64 -sv -L axi_vip_v1_1_5 -L axi4stream_vip_v1_1_5 -L xilinx_vip "+incdir+../../../ipstatic/hdl" "+incdir+/home/tools/Xilinx/Vivado/2019.1/data/xilinx_vip/include" \
"../../../../../axis_mst_0/sim/axis_mst_0_pkg.sv" \

vlog -work axi4stream_vip_v1_1_5 -64 -sv -L axi_vip_v1_1_5 -L axi4stream_vip_v1_1_5 -L xilinx_vip "+incdir+../../../ipstatic/hdl" "+incdir+/home/tools/Xilinx/Vivado/2019.1/data/xilinx_vip/include" \
"../../../ipstatic/hdl/axi4stream_vip_v1_1_vl_rfs.sv" \

vlog -work xil_defaultlib -64 -sv -L axi_vip_v1_1_5 -L axi4stream_vip_v1_1_5 -L xilinx_vip "+incdir+../../../ipstatic/hdl" "+incdir+/home/tools/Xilinx/Vivado/2019.1/data/xilinx_vip/include" \
"../../../../../axis_mst_0/sim/axis_mst_0.sv" \

vlog -work xil_defaultlib \
"glbl.v"
