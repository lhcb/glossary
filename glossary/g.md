# G

**Gaudi**
: The **LHCb** software framework, see the [Gaudi homepage](http://gaudi.web.cern.ch/gaudi/) and the [**Starterkit** high level overview](https://lhcb.github.io/starterkit-lessons/first-analysis-steps/davinci.html) for more details

**Grid Proxy**
: X509 authentication to use the grid. The proxy is generated from your grid certificate with the command `lhcb-proxy-init` and by default is valid for 24 hours. In Ganga you create the proxy with `credential_store.create(DiracProxy())`.

**Ganga**
: [**Ganga**](https://github.com/ganga-devs/ganga) is a job submission and management tool. It can submit and monitor jobs with several backends (local, batch, grid) without the need to customise scripts. Configure once, run anywhere! See the [docs](https://ganga.readthedocs.io/en/latest/) or [starterkit](https://lhcb.github.io/starterkit-lessons/first-analysis-steps/davinci-grid.html) for more details.
