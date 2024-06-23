# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.2.1] - 2023-03-13

🎉 Support updating module via Magisk Manager

### Changed

- Add `updateJson` to `module.prop`

## [2.2.0] - 2023-03-13

🎉 Use GrapheneOS SUPL proxy ([thanks @ranton1990](https://github.com/PlqnK/magisk-supl-replacer/issues/2))

### Changed

- Use `supl.grapheneos.org` as `SUPL_HOST`

## [2.1.0] - 2023-01-17

🎉 Fix Google server being used ([thanks @ranton1990](https://github.com/PlqnK/magisk-supl-replacer/issues/2))

### Changed

- Use `agpss.orange.fr` as `SUPL_HOST`

## [2.0.0] - 2022-10-15

🎉 Maintenance changes

### Changed

- Use European time server
- Fix setting `SUPL_HOST` if it does not exist yet

## [1.0.0] - 2020-05-03

🎉 First release!

### Added

- Everything needed to make a standard Magisk module
- A `post-fs-data` script that replaces the values of `SUPL_HOST` and `NTP_SERVER` in Android's `gps.conf`
- A readme detailing everything needed to know before installing the module
- A license file
- GitHub workflows to lint the script as well as build and publish the module

[2.2.1]: https://github.com/Magisk-Modules-Alt-Repo/supl-replacer/releases/tag/v2.2.1
[2.2.0]: https://github.com/D3SOX/magisk-supl-replacer/releases/tag/v2.2.0
[2.1.0]: https://github.com/D3SOX/magisk-supl-replacer/releases/tag/v2.1.0
[2.0.0]: https://github.com/D3SOX/magisk-supl-replacer/releases/tag/v2.0.0
[1.0.0]: https://github.com/PlqnK/magisk-supl-replacer/releases/tag/v1.0.0
