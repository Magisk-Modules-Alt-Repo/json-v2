
### v1.0.5
  - change low_ram default value to false

### v1.0.4

  - fix a bug where XtremeBS would continually enable when `trigger=boot` is set
  - math changed in battery time prediction
  - process handling now ensures that the
  nice level doesnt get changed behind us
  - proc_file will now take a nice level per process
  if you dont change your file, nice is 10
  nice levels are 0 (normal) - 19 (very nice)
  - added `keep_on_charge` option, this leads to extremely fast charging speeds and is only needed if using `trigger=auto`

### v1.0.3

  - add battery time prediction
  - removed undocumented function
  - removed old function from pre-v0.0.1
  - made app handling faster (still needs to be faster. WIP)

### v1.0.2

  - make requested changes for MMAR
  - configs are now located in `/data/local/tmp/XtremeBS/`

### v1.0.1

  - Add manual control

### v1.0.0

  - FIRST OFFICIAL RELEASE
  - fixed daemon command handling
  - fixed a bug in process handling

### v0.0.3

  - fixed a bug that prevented powersave from starting

### v0.0.2

  - minor improvements
  - fixed a bug.

### v0.0.1

  - initial release
