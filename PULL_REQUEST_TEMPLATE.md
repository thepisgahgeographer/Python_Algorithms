\<insert pull request description here\>

-----

# Checklist

Please go through each entry in the below checklist and mark an 'X' if that condition has been met. Every entry should be marked with an 'X' to be get the Pull Request approved.


- [ ] All `import`s are in the first cell? First block of imports are standard libraries, second block are 3rd party libraries, third block are all `arcgis` imports?
- [ ] All `GIS` object instantiations are one of the following?
    - `gis = GIS('https://www.arcgis.com', 'arcgis_python', 'P@ssword123')`
    - `gis = GIS(profile="your_online_profile")`
    - `gis = GIS('https://pythonapi.playground.esri.com/portal', 'arcgis_python', 'amazing_arcgis_123')`
    - `gis = GIS(profile="your_enterprise_portal")`
- [ ] If this notebook requires setup or teardown, did you add the appropriate code to `./misc/setup.py` and/or `./misc/teardown.py`?
- [ ] If this notebook references any portal items that need to be staged on AGOL/Python API playground, did you coordinate with a Python API team member to stage the item the correct way with the api\_data\_owner user?
- [ ] Code refactored & split out across multiple cells, useful comments?
- [ ] Consistent voice/tense/narrative style? Thoroughly checked for typos?
- [ ] All images used like `<img src="base64str_here">` instead of `<img src="https://some.url">`? All map widgets contain a static image preview? (Call `mapview_inst.take_screenshot()` to do so)
- [ ] All file paths are constructed in an OS-agnostic fashion with `os.path.join()`? (Instead of `r"\foo\bar"`, `os.path.join(os.path.sep, "foo", "bar")`, etc.)
- [ ] **IF YOU WANT THIS SAMPLE TO BE DISPLAYED ON THE DEVELOPERS.ARCGIS.COM WEBSITE**, ping @ DavidJVitale so he can add it to the list for the next deploy 
