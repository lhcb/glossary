# G

## Ganga

[Ganga](https://github.com/ganga-devs/ganga) is a job submission and management tool. It can submit and monitor jobs with several backends (local, batch, grid) without the need to customise scripts. Configure once, run anywhere! See the [docs](https://ganga.readthedocs.io/en/latest/) or [starterkit](https://lhcb.github.io/starterkit-lessons/first-analysis-steps/davinci-grid.html) for more details.

## Gaudi

The **LHCb** software framework, see the [Gaudi homepage](http://gaudi.web.cern.ch/gaudi/) and the [**Starterkit** high level overview](https://lhcb.github.io/starterkit-lessons/first-analysis-steps/davinci.html) for more details.

## Gauss

The LHCb simulation application. [Project website](http://lhcbdoc.web.cern.ch/lhcbdoc/gauss/).

## GEANT4: GEometry ANd Tracking 4 {#GEANT4}

A software package which is used for simulating the processes that occur between as particles move through matter.
[_Website_](https://geant4.web.cern.ch/).


## GLIMOS: Group Leader In Matters Of Safety {#GLIMOS}

Each collaboration has one of its members designated as the authority in safety matters.
At CERN, the Group Leader In Matters Of Safety has complete authority over personnel and equipment in all matters that concern safety of the experiment,
independently of what home institute the personnel or equipment belongs.

## GPD: General Purpose Detector {#GPD}

Collective term for detectors capable of performing various types of studies.
The ATLAS and CMS experiments at the LHC are GPDs.


## Grid Certificate

Certificate required to access grid services. Can be [obtained from CERN](https://ca.cern.ch/ca/). To be useable you must be a member of a VO.

## Grid Proxy

X509 authentication to use the grid. The proxy is generated from your grid certificate with the command `lhcb-proxy-init` and by default is valid for 24 hours. In Ganga you create the proxy with `credential_store.create(DiracProxy())`.
