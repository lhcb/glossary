# T

## T&A: Tracking and Alignment (and Vertexing) {#TandA}

LHCb physics performance working group for matters of Tracking, Alignment, and Vertexing.
Also represented in the «OPG» as Alignment and as Tracking.

## Tagging {#Tagging}

See «Flavour Tagging:Flavour-Tagging».

## TB: Technical Board {#TB}

Advisory body to the LHCb management on all aspects of detector design, optimization, safety and cost.

## TCK: Trigger Configuration Key {#TCK}

A unique 32-bit configuration value (in base 16) representing a given trigger configuration (sequence of algorithms and selection cuts).

## TDR: Technical Design Report {#TDR}

A document submitted to the «LHCC» of CERN describing the design of a subdetector or other subsystem (e.g. online, trigger, computing).
This document also describes the cost of the detector and which institutes will be responsible for which elements of the construction.
The TDRs of LHCb and the upgrades are collected [here](http://cdsweb.cern.ch/search?cc=LHCb+Reports&ln=en&jrec=11).
The document is reviewed by the «LHCC», with involvement from the «RRB» for financial aspects.

## Technical Proposal {#TP}

A document submitted to the «LHCC» of CERN describing the design of a new experiment or major upgrade,
outlining the physics case and detector design.
This document contains more detail than the «LoI», for example reporting on [R&D](https://en.wikipedia.org/wiki/Research_and_development)
that shows the feasibility of the project and possibly estimating the cost.
The «LHCC» reviews the document and determines if the collaboration should proceed to the next stage of approval,
typically «TDR»s for the individual subdetectors and systems of the experiment.
If costs are involved the «RRB» of CERN is involved in the approval.

For the original LHCb experiment this is [CERN-98-004](http://lhcb-tp.web.cern.ch/lhcb-tp/)
followed by an LHCb reoptimized detector design and performance «TDR» that is
[CERN/LHCC 2003-030](http://cds.cern.ch/record/630827/files/lhcc-2003-030.pdf).
For the LHCb Upgrade I the equivalent document is known as a Framework «TDR», and is
[CERN/LHCC-2012-007](http://cds.cern.ch/record/1443882/files/LHCB-TDR-012.pdf).
For the LHCb Upgrade II the equivalent document is due to be submitted around late 2020.

## TELL40 {#TELL40}

«Readout Boards:ReadoutBoard» in Upgrade I based on the Advanced Telecommunication Computer Architecture (ATCA) technology.
The TELL40s operate at 40 MHz and replace the previous TELL1 boards used in Runs 1 and 2.

## TFC: Timing and Fast Control system {#TFC}

A system responsible for controlling and distributing the clock, timing and trigger information,
synchronous and asynchronous commands to the entire data readout system,
see the [LHCb Trigger and Online TDR](https://cds.cern.ch/record/1701361/files/LHCB-TDR-016.pdf).

## Tier (Grid) {#Tier}

Grid sites are split into tiers depending on their resources. Tier 1 (i.e. RAL, PIC) and tier 2 sites (mostly universities) store data, the tier 1s in particular storing raw data. The tier 3 sites do not store data. See [here for details](http://wlcg-public.web.cern.ch/tier-centres).

## Timepix {#Timepix}

An «application specific integrated circuit:ASIC» (ASIC) used in hybrid pixel detectors,
which contains 256 x 256 pixels with a 55 $$\mu$$m pitch.
Timepix3 is based on the Medipix/Timepix family of «ASICs» and additionally offers the possibility to measure the time of arrival of particles.

## TISTOS

Trigger decisions can be classified into three categories:

- Trigger On Signal (TOS): a positive decision can be reached using information from the signal candidate.
- Trigger Independently of Signal (TIS): a positive decision can be reached using information from the rest of the event.
- Trigger on both (TOB): a positive decision requires the entire event.

Note that the TIS and TOS categories are not mutually exclusive.

## Track

The signature that is reconstructed when a charged particle travels through LHCb.
Split into 5 types depending on which parts of the tracking system are used:

* Downstream Track
* Long track (forward track or match track)
* T Track
* Upstream Track (in upgrade jargon also "Velo-UT track")
* Velo Track

[!["Track types in LHCb"](/figures/track_types.png)](/figures/track_types.png)

## Track Type

The type of the track used in `TupleToolTrackInfo`, and anything that includes it. See [Tracking strategies used in LHCb](https://twiki.cern.ch/twiki/bin/view/LHCb/LHCbTrackingStrategies#Track_types) or [TupleToolTrackInfo](https://twiki.cern.ch/twiki/bin/view/LHCb/TupleToolTrackInfo) for details. The types are:

| ID | Track type |
|----|------------|
| 0  |  Unknown   |
| 1  |  VELO track |
| 2  |  2D VELO track |
| 3  |  Long (or forward) track |
| 4  |  Upstream track |
| 5  |  Downstream track |
| 6  |  Seed track |
| 7  |  Muon track |
| 8  |  Calorimeter cosmic track |
| 9  |  TT track |

## TT: Tracker Turicensis {#TT}

The tracking station located immediately before the magnet in Runs 1 and 2. For the LHCb Upgrade I it will be replaced by the «Upstream Tracker:UT». 
It played an important role in reconstructing tracks that originate outside the «VELO», such as those that come from K-shorts and Lambda baryons.
Much like the «IT» stations, the TT consists of 4 layers of silicon strips, oriented at 0°, −5°, +5° and 0° from the vertical.

## Tracker-only {#TrackerOnly}

A fast simulation configuration that excludes calorimeter and muon geometries, but keeps the RICH geometry included. However, RICH physics lists are switched off.

## Tracking efficiency {#TrackingEfficiency}
Performance number of a tracking algorithm, defined as the amount of reconstructed tracks that can be matched to MC particles with respect to the amount of reconstructible tracks. In offline analysis usually calculated with data-driven tag-and-probe methods on dedicated calibration samples. See references in the [Tracking efficiency TWiki](https://twiki.cern.ch/twiki/bin/viewauth/LHCbInternal/LHCbTrackingEfficiencies) for details.

