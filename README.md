# Magisk Modules Alt Repo

This repository stores modules for [MMRL](https://github.com/DerGoogler/MMRL).

To submit your modules, please go to the [submission](https://github.com/Magisk-Modules-Alt-Repo/submission) repository.

## Add to MMRL

```
https://magisk-modules-alt-repo.github.io/json-v2/
```

## Add to MMRL-CLI

```shell
mmrl repo add "https://magisk-modules-alt-repo.github.io/json-v2/json/modules.json"
```

## Developers

Enhance your modules visibility in MMRL and supported apps! Create a file named `common/repo.json` with the following contents

```jsonc
{
  "support": "",
  "donate": "",
  "cover": "",
  "icon": "",
  "license": "",
  "readme": "",
  "homepage": "",
  "screenshots": [],
  "category": "",
  "categories": [],
  "require": [],
  "note": {
    "title": "str", // optional
    "color": "red,blue,yellow,green", // optional
    "message": "str" // required if note is defined
  },
  "root": {
    "kernelsu": ">= 1.0.0",
    "magisk": ">= 24.0
  }
}
```


| Key          | Attribute | Type                                                                                                     | Description                                        |
| ------------ | --------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| homepage     | optional  | Str                                                                                                      | URL                                                |
| readme       | optional  | Str                                                                                                      | URL with e.g. description, instructions            |
| support      | optional  | Str                                                                                                      | URL to issue tracker/support forum                 |
| donate       | optional  | Str                                                                                                      | URL to donation page                               |
| cover        | optional  | Str                                                                                                      | URL to cover image (featureGraphic)                |
| icon         | optional  | Str                                                                                                      | URL to icon.png (squared, max 512x512 px)          |
| screenshots  | optional  | Str[]                                                                                                    | URLs to screenshots of the module                  |
| license      | optional  | Str                                                                                                      | SPDX identifier (see below)                        |
| antifeatures | optional  | Str[]                                                                                                    | potentially unwanted "features" (see below)        |
| category     | optional  | Str                                                                                                      | category the module belongs to (deprecated)        |
| categories   | optional  | Str[]                                                                                                    | array of categories the module belongs to          |
| require      | optional  | Str[]                                                                                                    | array of `module_id`s this module depends on       |
| note         | optional  | [Note](https://github.com/Googlers-Repo/magisk-modules-repo-util/blob/main/sync/model/ModuleNote.pyi)    | additional notes for the module                    |
| root         | optional  | [Root](https://github.com/Googlers-Repo/magisk-modules-repo-util/blob/main/sync/model/RootSolutions.pyi) | defined min version for Magisk, KernelSU or APatch |


> Non-array and non-object properties can also be placed inside the `module.prop` file

> [!IMPORTANT]
> When you're updating details don't forget to increase the version code otherwise it won't display

## How to update?

- [magisk-modules-repo-util](https://github.com/Googlers-Repo/magisk-modules-repo-util.git)

### For mods

1. Go to actions
2. Click on "sync-build-deploy"
3. Click on "Run workflow" and enter a repo that has been added to the **Magisk Modules Alt Repo**
4. Wait till the action has ended

![](assets/adding-guide.png)
