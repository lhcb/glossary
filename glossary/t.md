# T

## Track

The signature that is reconstructed when a charged particle travels through LHCb.
Split into 5 types depending on which parts of the tracking system are used:

* Downstream Track
* Long track
* T Track
* Upstream Track
* Velo Track

[!["Track types in LHCb"](/figures/track_types.png)](/figures/track_types.png)

## Track Type

The type of the track used in TupleToolTrackInfo, and anything that includes it. See [Tracking strategies used in LHCb](https://twiki.cern.ch/twiki/bin/view/LHCb/LHCbTrackingStrategies#Track_types) or [TupleToolTrackInfo](https://twiki.cern.ch/twiki/bin/view/LHCb/TupleToolTrackInfo) for details. The types are:

| ID | Track type |
|----|------------|
| 0  |  Unknown   |
| 1  |  Velo track |
| 2  |  2D Velo track |
| 3  |  Long (or forward) track |
| 4  |  Upstream track |
| 5  |  Downstream track |
| 6  |  Seed track |
| 7  |  Muon track |
| 8  |  Calorimeter cosmic track |
| 9  |  TT track |

