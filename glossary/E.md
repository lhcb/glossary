# E

## EB

Abbreviation for:

 * Editorial Board
 * Event Builder

## Editorial Board

Entity responsible for ensuring that all LHCb publications are sound and consistent with the standards and style of the collaboration.
[_Website_](http://lhcb.web.cern.ch/lhcb/lhcb_page/collaboration/organization/editorial_board/default.html).

## Event Builder

Computers in the Online System that are in charge of receiving data from the detector and combining it into events.
See Section 3.5 in the [Trigger and Online Upgrade TDR](https://cds.cern.ch/record/1701361).

## ECAL: Electromagnetic Calorimeter {#ECAL}

The purpose of the ECAL is to measure the energy of electrons/photons and prevent them from travelling further through the detector.
Like the «HCAL», it is a sampling calorimeter made of layers of iron and plastic scintillator.

## ECGD: Early Career, Gender and Diversity {#ECGD}

The Early Career, Gender and Diversity office has been set up to help LHCb achieve a healthy working environment
with no discrimination on grounds of gender, sexual orientation, ethnicity, disability, creed, cultural background, etc.
See the [ECGD office webpages](http://lhcb.web.cern.ch/lhcb/ECGD_Office/ECGD-intro.html) for more information.

## ECS: Experiment Control System {#ECS}

The Experiment Control System is in charge of the configuration, control and monitoring of all the components of the online system.
This includes all devices in the areas of data acquisition, detector control (e.g. slow controls), trigger, timing,
and the interaction with the outside world.
Details in the Online System [webpages](http://lhcb-online.web.cern.ch/lhcb-online/ecs/default.htm).

## EDR: Engineering Design Review {#EDR}

A milestone during the construction of a subdetector.
The EDR is a meeting with accompanying documentation that describes the detailed design of a component system of the detector
(e.g. sensors, an [ASIC](https://en.wikipedia.org/wiki/Application-specific_integrated_circuit), high voltage system)
based on drawings and prototypes that have been produced.
Reviewers with relevant expertise from other subdetectors in LHCb and from other experiments
are usually appointed to conduct the review and make recommendations. The next major milestone is the «PRR».

## EMTF: Early Measurements Task Force {#EMTF}

The Early Measurements Task Force coordinates the earliest data analyses (in close collaboration with the software, simulation, commissioning, online and offline analysis teams including calibration, alignment, etc. experts) to ensure the rapid exploitation of the LHCb data that is taken at the start of a new Run. This may be for validation of a new detector, new readout systems, new reconstruction, a new trigger, and new running conditions, etc. 
The first and most important mission of the EMTF is to make sure that we are ready to do analysis efficiently as soon as we have the new data.
The second mission of the EMTF is to identify, prepare for, and help perform important analyses with the early Run data. Follow this [TWiki link]( https://twiki.cern.ch/twiki/bin/viewauth/LHCbPhysics/EarlyMeasurementsRun3)

## EoI: Expression of Interest {#EoI}

Please see the entry for «LoI».

## Erasmus

High-level physics analysis software [repository](https://gitlab.cern.ch/lhcb/Erasmus), similar to «Urania», but based on «Bender». Note that this project is now stopped, and retired from «CVMFS». All non-obsolete packages have been moved to the «Castelao» project, which is based instead on «DaVinci».

## eta

See «Pseudorapidity».

## EventType {#EvtType}

A uniquely defined 8-digit number attributed to a specific decay channel or final state (possibility of inclusion of resonances, etc.), used to identify «decay files:DecFile».

The first six digits describe the decay. The last two digits are reserved to distinguish between similar decays. The general form of the identifier is “gsdctnxu”.

* g: a general flag
* s: a selection flag
* d: a decay flag
* c: a charm and lepton flag
* t: a number of charged tracks flag
* n: a neutral particles flag
* x: an extra flag to distinguish between similar event types
* u: a user flag indicating different generator conditions

More about assigning EventType identifiers can be found in [this internal note](https://cds.cern.ch/record/855452/files/lhcb-2005-034.pdf).

## EvtGen

Software package for simulating the decays of heavy flavour particles using a wide range of decay models.
[_Website_](https://evtgen.hepforge.org).
