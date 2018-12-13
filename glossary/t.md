# T

## T&A: Tracking and Alignment (and Vertexing) {#TandA}

LHCb physics performance working group for matters of Tracking, Alignment, and Vertexing.
Also represented in the [OPG](o.html#OPG) as Alignment and as Tracking.

## Tagging

See [Flavour Tagging](f.html#flavourtagging).

## TB: Technical Board {#TB}

Advisory body to the LHCb management on all aspects of detector design, optimization, safety and cost.

## TCK : Trigger Configuration Key {#TCK}

A unique 32-bit configuration value (in base 16) representing a given trigger configuration (sequence of algorithms and selection cuts).

## Tier (Grid) {#Tier}

Grid sites are split into tiers depending on their resources. Tier 1 (i.e. RAL, PIC) and tier 2 sites (mostly universities) store data, the tier 1s in particular storing raw data. The tier 3 sites do not store data. See [here for details]{http://wlcg-public.web.cern.ch/tier-centres}.

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
