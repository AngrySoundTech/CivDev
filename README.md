# CivDev

A simple development environment for Civ Plugins.

# Setup

1. Make sure you have [git], [maven], and [python] installed.
2. Download Spigot [BuildTools], and follow the instructions to build
4. Run `pip install -r requirements.txt` to install dependencies
3. Run `./civ setup` on Windows, or `./civ.sh setup` on *nix. Alternatively, use `python civ.py setup`

Projects will be located in the [plugins folder], and can be modified at will.

# Building

Projects can be built individually, but I recommend building them all first.

This can be done by opening a terminal in the [plugins folder] and running `mvn clean install`

# Plugins not included

_This section was copied from https://github.com/civrepo/megarepo because_
I'm lazy and this is the challenge Orinnari presented me

BungeeGuard, ClearLag, HolographicDisplays, LuckPerms, ProtocolLib, SuperVanish, Vault, Votifier, and WorldEdit
are all plugins currently present within Civclassic's AnsibleSetup that aren't here.
They're missing because they're more general purpose libraries or admin tools rather than anything specific to Civ.

BetterChairs is a plugin currently present within Civclassics' roleplay, but not something specific to Civ.

Orebfuscator is a special case, it was made by a Civ player and server owner but designed to be server agnostic.
Also, the forks currently used by Civ servers are outdated compared to Imprex Development's fork which is significantly
updated but therefore might not be compatible with other Civ plugins or Civ setups.


[git]: https://git-scm.com/downloads
[maven]: https://maven.apache.org/download.cgi
[python]: https://www.python.org/downloads/

[BuildTools]: https://www.spigotmc.org/wiki/buildtools/

[plugins folder]: ./plugins