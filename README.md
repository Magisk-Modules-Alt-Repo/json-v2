# Magisk Modules Alt Repo

This repository stores modules for [MMRL](https://github.com/DerGoogler/MMRL).

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

```json
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
  "require": []
}
```

| Key           | Attribute | Description                             |
|---------------|-----------|-----------------------------------------|
| license       | optional  | [SPDX ID](https://spdx.org/licenses/)   |
| cover         | optional  | URL                                     |
| icon          | optional  | URL                                     |
| screenshots   | optional  | URL[]                                   |
| category      | optional  | Str                                     |
| readme        | optimal   | Str                                     |
| categories    | optional  | Str[]                                   |
| homepage      | optional  | URL                                     |
| support       | optional  | URL                                     |
| donate        | optional  | URL                                     |

> Non-array properties can also be placed inside the `module.prop` file

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
