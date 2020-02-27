Esri welcomes contributions from anyone and everyone. Please see our [guidelines for contributing](https://github.com/esri/contributing). Please expect any pull requests to go through a peer review before being accepted.

### Before filing an issue

Please take a look at [previous issues](https://github.com/Esri/arcgis-python-api/issues?q=is%3Aissue+is%3Aclosed) that resolve common problems.

If you're just looking for help, you'll probably attract the most eyes if you post in the [GeoNet Forums](https://community.esri.com/groups/arcgis-python-api/).

If you think you're encountering a new bug, please feel free to log an [issue](https://github.com/Esri/arcgis-python-api/issues/new) and include the steps to reproduce the problem.

**Please include the following in your issue:**
* Your conda or pip environment (run `conda list` or `pip freeze` and copy/paste the output into the issue)
* Any code (or notebook) you executed that made you run into this issue

# Updating errors in existing notebooks

Do you see an error in an existing notebook? Is there a typo, a misnamed variable, and do you know how to fix it?
* Make the fix in the notebook
* If you made code changes, re-run the appropriate cells in the notebook (Don't re-run every cell in the notebook unless necessary)
* Make a copy of the `dev_site_current` branch on your local fork
* Add the updated notebook to your branch on your fork
* [Open a pull request](https://help.github.com/articles/creating-a-pull-request-from-a-fork/) from your fork's branch to this repository's `dev_site_current` branch

# Adding new sample notebooks

Do you have a notebook that shows off functionality of the API? Do you want to see that notebook released with the next version of the ArcGIS API for Python? We welcome your notebooks and workflows as it will benefit a large audience.

* Create a new notebook, make sure it runs consistently on its own on a few systems
    * Make sure the notebook filename is in an `all_lowercase_underscore_delimiter_convention.ipynb`
* Make a copy of the `dev_site_next_release` branch on your local fork
* Place the notebook in the correct folder in the `samples/` folder on your fork
* Add the notebook to your branch on your fork
* [Open a pull request](https://help.github.com/articles/creating-a-pull-request-from-a-fork/) from your fork's branch to this repository's `dev_site_current` branch
