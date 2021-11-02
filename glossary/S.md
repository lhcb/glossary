# S

## Sandbox {#Sandbox}

A small collection of files passed along with your job. The sandboxes are stored on the DIRAC server and removed after a limited time. The files they contain must be small.

## Scientific Linux CERN (SLC) {#SLC}

Former "default" Linux operating system at CERN (SLC6 default operating system on lxplus until end of 2018).

## SciFi: Scintillating Fibre Tracker {#SciFi}

Large area tracking detector installed for the Upgrade I of the LHCb detector, located between the magnet and the downstream «PID» detectors. Successor of the «OT»/«IT» tracking system. Consists of 3 stations with 4 layers in a «x-u-v-x configuration:XUVX» each.

## SE: Storage Element {#SE}

A service at a grid site that stores data. For example: `CERN-USER`, `GRIDKA_MC-DST`.

## Site (Grid)

A computing centre hosting grid computing services. For example: `IN2P3-LAPP`.

## SMOG: System for Measuring the Overlap with Gas {#SMOG}

The _System for Measuring the Overlap with Gas_ is a gas injection system designed to increase the pressure inside the LHCb «VELO» beam vacuum.
Only noble gases are injected. The gas spreads out +/- 20 m around the nominal proton-proton interaction point
and the pressure is approximately $$10^{-7}$$ mbar.
Originally designed for precise luminosity measurements, SMOG injections are also used for specific data takings,
allowing LHCb to be operated in fixed target mode.

## S-ODIN {#S_ODIN}

A [TFC]{#TFC} readout supervision module responsible for generating necessary information and commands, see [LHCb Trigger and Online TDR](https://cds.cern.ch/record/1701361/files/LHCB-TDR-016.pdf) and [ODIN](#ODIN).

## SOL40

A multiple interface board that connects frontend and backend readout electronics of the subdetector to [S-ODIN]{#S_ODIN} with a set of 3.2 Gb/s high-speed bidirectional optical links, see [LHCb Trigger and Online TDR](https://cds.cern.ch/record/1701361/files/LHCB-TDR-016.pdf).  

## SPD: Scintillating Pad Detector {#SPD}

The SPD consists of scintillating pads and is placed before the «PS».
The joint purpose of the SPD and PS is to reduce the background for the «L0» electron trigger.
The SPD, in conjunction with the «ECAL», helps distinguish between electrons and neutral particles like photons and neutral pions.

## ST: Silicon Tracker {#ST}

A term that collectively refers to the «TT» and «IT».

## Starterkit {#Starterkit}

One week introduction course into computer usage at LHCb for young students. With no prerequisites on Linux usage, teaching basic survival skills including Grid usage and ntuple production. You can find the online version [here](https://lhcb.github.io/starterkit-lessons/index.html).

## sWeights {#sWeights}

Also known as sPlot.
A signal/background discrimination technique, that utilizes information about distribution of signal and background events in one variable, called a discriminating variable, to get a distribution of signal and background events in the observed variable, called an observable.
From a discriminating variable, where signal and background distributions are known, a weight is computed per event, that represents signal-likeness or background-likeness.
Strictly speaking discriminating variable and observable should factorize in order to use this technique.
Several background species might be specified to compute the weights. 
See [sPlot paper](https://arxiv.org/abs/physics/0402083) and ROOT implementation [SPlot class](https://root.cern/doc/master/classRooStats_1_1SPlot.html).
