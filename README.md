# dotfiles

[![standard-readme compliant](https://img.shields.io/badge/standard--readme-OK-green.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

> This isn&#39;t the first, and it won&#39;t be the last. But it&#39;s myn, and therefore that makes it the greatest.

## Table of Contents

- [Install](#install)
- [Usage](#usage)
  - [PROFILE](#profile)
  - [CONFG](#config)
  - [THEME](#theme)
- [Examples](#examples)
- [Maintainers](#maintainers)
- [Contributing](#contributing)
- [License](#license)

## Install
### Requirements
- [git](https://git-scm.com/)
- [python ^2.7](https://www.python.org/)
- [poetry >= 0.12](https://github.com/sdispater/poetry#installation)

```shell
$ cd ~/.config/
$ git clone -b ubuntu https://github.com/mezerotm/dotfiles.git
$ cd dotfiles/
$ poetry install
```

Dotfiles are separated by branches, and will usually be named by the top distribution in a hierarchy. This means that a branch named debian should be compatible by it' sub-distributions. (Themes do not follow this pattern, more on this later)

```
         debian
            |
   /---- ubuntu ----\
  |         |        |
xubuntu  lubuntu  kubuntu
```

## Usage

### CONFIG
#### DESCRIPTION
Config files are dotbot yaml files which contain application specific configurations.
#### SYNOPSIS
poetry run invoke config ACTION CONFIG1[,CONFIG2,...[,CONFIGN]]
#### ACTION
  -i, --install

  Install the config(s)

  --remove

  Remove the config(s)
#### CONFIG
These are located in the [config folder](./config) they are referenced by folder name.

### PROFILE
#### DESCRIPTION
Profiles are collections of configs which are usually grouped together. You can only have one profile at a time, but this can easily be extended by adding standalone configs. Profiles also manage the interoperability of configs alongside themes.
#### SYNOPSIS
poetry run invoke profile ACTION PROFILE
#### ACTION
-i, --install

Install the profile

--remove

Remove the profile
### PROFILE
These are located in the [profile folder](./profile) they are referenced by folder name.

### THEME
#### DESCRIPTION
Themes are special. Each distribution has the ability to support multiple environments. Therefore themes are not tied to the distribution, but instead the environments. Compatibility with multiple distributions is therefore an inherited responsibility the theme must take into account. You can only have one theme at a time. Themes also get their own branch.
#### SYNOPSIS
poetry run invoke theme ACTION THEME
#### ACTION
-i, --install

Install the theme

--remove

Remove the theme
#### THEME
These are located in the [theme folder](./theme) they are referenced by folder name.

## Examples

```shell
$ poetry run invoke config -i zsh,zplug,zprezto
$ poetry run invoke config --remove zplug,zprezto
```

```shell
$ poetry run invoke profile -i minimum
$ poetry run invoke config -i ssh
```

```shell
$ git checkout themes
$ poetry run invoke theme -i rebecca
```

## Maintainers

[@mezerotm](https://github.com/mezerotm)

## License

GPl-3.0+ © 2019 Carlos Rincon
