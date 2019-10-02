# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.1]
### Changed
- clean up README.md, remove info + language left over
  from when repository was `vocalization-annotation-formats`
- organize .gitignore

## [0.1.0]
### Changed
- change name to `pollyglot` from `vocalization-annotation-formats`

### Added
- `pollymake` function that makes subsets from source datasets,
which can then be uploaded to `pollyglot` repository on figshare
- `pollyglot.fetch` then fetches those subsets, for use by other
  programs
