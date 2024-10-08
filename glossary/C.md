# C

## CALO: Calorimeters {#CALO}

The entire calorimetry system at LHCb («SPD»/«PS», «ECAL», «HCAL» is often collectively referred to as CALO.
Its purpose is to discriminate between electrons, photons and hadrons as well as provide measurements of their energy and position.
In Runs 1 and 2, the CALO played an important role providing transverse energy measurements to the «L0» trigger.

## Castelao

High-level physics analysis software [repository](https://gitlab.cern.ch/lhcb/Castelao), similar to «Urania», but based on «DaVinci». This project hosts, among others, important packages used for the centralised production of «PID» and track calibration datasets (PIDCalibProduction, TrackCalibProduction). Any other packages which are based on «DaVinci» and need to be centrally distributed could be included in the project. Refer to the [repository](https://gitlab.cern.ch/lhcb/Castelao) for a list of available packages.

## CB: Collaboration Board {#CB}

The ultimate authority within LHCb representing all institutes within the collaboration.

## CC7: CentOS CERN 7 {#CC7}

The former "default" Linux operating system at CERN, default on lxplus since start of 2019 until June 30, 2024 when it ended service and got replaced by AlmaLinux.

## CE: Computing Element {#CE}

A service at a grid site that runs jobs. For example `LCG.CERN.cern`, `LCG.RAL.uk`.

## CLARO {#CLARO}

CLARO is a customized 8-channel «ASIC» CMOS chip used to read out «RICH» «MaPMT»s in Upgrade I. 
It is a digital board with a binary output. 
Each channel is calibrated separately to find the most optimal threshold.
The threshold defines whether 1 (signal) or 0 (no signal) will be transmitted.

## CVMFS: CERN Virtual Machine File System {#CVMFS}

[CVMFS](https://cernvm.cern.ch/portal/filesystem) is a network file system based on HTTP and optimised to deliver experiment software
in a fast, scalable, and reliable way through sophisticated caching strategies.
