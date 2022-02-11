# Changelog

<!--next-version-placeholder-->

## v0.3.3 (2022-02-11)
### Fix
* **setup:** Introduce Python 3.9 and 3.10 into allowed versions and remove 3.6 ([`fdfc14d`](https://github.com/BjoernLudwigPTB/pyxml2pdf/commit/fdfc14d78f092820c1757b1fea973cc1fe795578))

### Documentation
* **README:** Update image after changing the font ([`5cbcfd9`](https://github.com/BjoernLudwigPTB/pyxml2pdf/commit/5cbcfd92cf51737c6a8561f8c3bdd301151713b6))

**[See all commits in this version](https://github.com/BjoernLudwigPTB/pyxml2pdf/compare/v0.3.2...v0.3.3)**

## v0.3.2 (2021-09-19)
### Fix
* **main:** Insert actual raw template.xml download url as default value and refine command line help ([`6743dc5`](https://github.com/BjoernLudwigPTB/pyxml2pdf/commit/6743dc5cf0ffeee1396ad4eb107aea89f1600870))
* **input:** Reintroduce input into newly packaged project structure ([`4b3b91a`](https://github.com/BjoernLudwigPTB/pyxml2pdf/commit/4b3b91ad0bf3c1e516ef84f310b6dd4bad6be42d))

**[See all commits in this version](https://github.com/BjoernLudwigPTB/pyxml2pdf/compare/v0.3.1...v0.3.2)**

## v0.3.1 (2021-09-19)
### Fix
* **fonts:** Include fonts in release ([`493bb6a`](https://github.com/BjoernLudwigPTB/pyxml2pdf/commit/493bb6aa5cfaf6989a30ba38e5d0bf45002ac441))

**[See all commits in this version](https://github.com/BjoernLudwigPTB/pyxml2pdf/compare/v0.3.0...v0.3.1)**

## v0.3.0 (2021-05-10)
### Feature
* **properties:** Refurbish properties' use and enable easy overwriting via _properties_custom.py_ ([`cb0a755`](https://github.com/BjoernLudwigPTB/pyxml2pdf/commit/cb0a75579183fb2d12eb9710a926eb7fac547710))

### Documentation
* Greatly improve docs and fix README example call ([`7e5e1dd`](https://github.com/BjoernLudwigPTB/pyxml2pdf/commit/7e5e1dd94583391b8625753967357b637c7f2d74))

**[See all commits in this version](https://github.com/BjoernLudwigPTB/pyxml2pdf/compare/v0.2.0...v0.3.0)**

## v0.2.0 (2021-02-22)
### Feature
* **XML:** Allow for processing general XML files and prepare examples ([`2a3b7e9`](https://github.com/BjoernLudwigPTB/pyxml2pdf/commit/2a3b7e9dec9301840176408b0e36036725ef1b9a))

### Fix
* **TableStyles:** Turn background in colorful again ([`90bc427`](https://github.com/BjoernLudwigPTB/pyxml2pdf/commit/90bc427f9386dc625107035084e213bd85de2145))
* **XMLRow:** Introduce mandatory call to create full row representation ([`799c870`](https://github.com/BjoernLudwigPTB/pyxml2pdf/commit/799c87050231a4be79cf9d92ea25f17207619ff0))
* **TableBuilder:** Fix an issue with the stylesheet reference ([`3f65a96`](https://github.com/BjoernLudwigPTB/pyxml2pdf/commit/3f65a9634ca9ec6aef591988ac5451d1816b8def))

### Documentation
* **events:** Reintroduce events into docs ([`b2654ee`](https://github.com/BjoernLudwigPTB/pyxml2pdf/commit/b2654ee25adbe6761a17dba30c3bc8c61c27acf8))
* **README:** Improve README ([`8eff47a`](https://github.com/BjoernLudwigPTB/pyxml2pdf/commit/8eff47a76a810d087ce6720c674db622100389e5))
* **README:** Introduce more descriptions ([`adaefa4`](https://github.com/BjoernLudwigPTB/pyxml2pdf/commit/adaefa421a8888f9325fac8e4cdeb9df203cfb0b))
* **README:** Adapt command in README to new version ([`9eca5ad`](https://github.com/BjoernLudwigPTB/pyxml2pdf/commit/9eca5ad3c6b1d6c33d91271bca1d3b381b354e53))

**[See all commits in this version](https://github.com/BjoernLudwigPTB/pyxml2pdf/compare/v0.1.0...v0.2.0)**

## v0.1.0 (2021-02-09)
### Feature
* **EventTable:** Introduce extend method for `EventTable.py` und use it in `TableBuilder.py` ([`f205071`](https://github.com/BjoernLudwigPTB/pyxml2pdf/commit/f2050712137bb0d4011895e517e6b2158c91ed8e))
* **properties:** Parse and process fonts from `properties.py` ([`07edc8a`](https://github.com/BjoernLudwigPTB/pyxml2pdf/commit/07edc8a94e7126963dba395150e3d160455493a5))

### Documentation
* **README:** Improve documentation of commandline parameters ([`86d1734`](https://github.com/BjoernLudwigPTB/pyxml2pdf/commit/86d1734f9b77e01c1a63797147d96b0b115aebca))
* **readthedocs:** Refine code block in docstring of `table_styles.py::custom_styles()` ([`4ea2e62`](https://github.com/BjoernLudwigPTB/pyxml2pdf/commit/4ea2e62b4121c6378ffad3262ccabf73e234541c))
* **readthedocs:** Refine code block in docstring of `table_styles.py::custom_styles()` ([`e931524`](https://github.com/BjoernLudwigPTB/pyxml2pdf/commit/e931524bd4dc8cc6f4c4579266da8a14174b331c))
* **readthedocs:** Refine code block in docstring of `table_styles.py::custom_styles()` ([`c7d900e`](https://github.com/BjoernLudwigPTB/pyxml2pdf/commit/c7d900e9cf74ff17a5f35d63d1a54fa5d1306ce1))
* **readthedocs:** Repair code block in docstring of `table_styles.py::custom_styles()` ([`1aac9ad`](https://github.com/BjoernLudwigPTB/pyxml2pdf/commit/1aac9ad15d3517f338a5f60de95ebeeb9bf45da3))
* **readthedocs:** Improve code block in docstring of `table_styles.py::custom_styles()` ([`f39a82b`](https://github.com/BjoernLudwigPTB/pyxml2pdf/commit/f39a82bd078036cb5bc5182318ab077ca491cd2d))
* **readthedocs:** Improve docstrings of `table_styles.py::custom_styles()` ([`0c4fbc2`](https://github.com/BjoernLudwigPTB/pyxml2pdf/commit/0c4fbc2f246f0d9b7686383cefe3ad872dd5b9e8))
* **readthedocs:** Improve docstrings of `post_processor.py` and `table_styles.py` ([`25a2774`](https://github.com/BjoernLudwigPTB/pyxml2pdf/commit/25a277437164b7e5bee7424470cffd0b43645c66))
* **readthedocs:** Improve docstrings of `events.py::Event.get_table_row()` ([`3862d53`](https://github.com/BjoernLudwigPTB/pyxml2pdf/commit/3862d534c6e7f576673def2dde5ed02657b19322))
* **readthedocs:** Improve docstrings of `events.py`, `parser.py` and `table_styles.py` ([`79068eb`](https://github.com/BjoernLudwigPTB/pyxml2pdf/commit/79068eb6ed5a56c4c16ee40c9d0fd39fbedba817))
* **readthedocs:** Improve docstrings of `events.py::Event` ([`6031852`](https://github.com/BjoernLudwigPTB/pyxml2pdf/commit/60318528832080789990260c2554e5b3fa3f2e11))
* **Event:** Refine docstring of `events.py::Event.get_full_row` ([`30d5daa`](https://github.com/BjoernLudwigPTB/pyxml2pdf/commit/30d5daa6d659b142243e24763e5f23e0a4091e22))
* **Event:** Refine docstring of `events.py::Event._init_reduced_row()` ([`dd76c10`](https://github.com/BjoernLudwigPTB/pyxml2pdf/commit/dd76c104cba6514d451d2b982415c5c25bda5e04))
* **readthedocs:** Reinsert sphinx docs for all packages and modules ([`860282c`](https://github.com/BjoernLudwigPTB/pyxml2pdf/commit/860282c50b5423dc4a0a3a26516cdaa266b848b6))
* **readthedocs:** Remove hint about end of 2019 from ReadTheDocs ([`5843554`](https://github.com/BjoernLudwigPTB/pyxml2pdf/commit/5843554bfa8732302b05ac564974f2da8cd52933))
* **readme:** Include hint on scheduled Heroku deployment into `README.md` ([`287ee95`](https://github.com/BjoernLudwigPTB/pyxml2pdf/commit/287ee958bb53d46f819c6a7406099c528f6325dd))
* **readme:** Correct s typo in the `README.md` ([`d42106c`](https://github.com/BjoernLudwigPTB/pyxml2pdf/commit/d42106c7c2698f5966fa60975d722f8e61bc5ca6))
* **readme:** Introduce new badges to `README.md` with release number and compatible Python versions ([`78dd7b4`](https://github.com/BjoernLudwigPTB/pyxml2pdf/commit/78dd7b4c0c543ae42c10594d3a6d923099da7c67))
* **setup:** Specify Python versions as classifiers in `setup.py` to make them more visible ([`e71b768`](https://github.com/BjoernLudwigPTB/pyxml2pdf/commit/e71b7687781a29ef1c604eccd5804cc269a9cedc))
