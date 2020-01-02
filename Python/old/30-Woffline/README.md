# woffline

#### TODO:
- [ ] Fix `is_url_file` to work with plain file names without extensions
  **ex:** `return (rs < url.rindex(".") and (rs - ls > 1 or rs == ls))` throws ValueError: substring not found:
- [ ] add cli args
- [ ] resolve all `# TODO`s in code
- [ ] merge with master
- [ ] rename `temp` modules
- [ ] remove references to `temp`
- [ ] add cli args
- [x] download js from `<link>` tags
- [x] download images from cdns
- [x] download styles from cdns
- [x] download fonts from cdns
- [x] download js from cdns
- [x] download resources from inline styles inside elements. e.g: 
	`<div style="background-image: url("https://cdn-images-1.medium.com/max/2000/gradv/29/81/30/darken/25/1*INe6Cm7Ix34J-C7X_ZJ5Qw.png"); background-position: 50% 50% !important;"/>`
- [x] download resources from cds relative to that cdn url
- [ ] add tests for util.py
- [x] add recursive link wofflining
- [x] add depth to wofflining
- [x] add resource downloading from css (also fixes ligatures)
	- [x] images
	- [x] fonts
	- [x] local files
  - [x] local files in parent directories ex: `../../image.png` (test with jekyllrb.com)
- [x] fix same name case: `href="a/a.css"` and `href="a.css"` (inside `get_resource_url()`)
- [x] `@import`s in css 
	- [x] With `url()`
	- [x] With local file path
- [x] remove `config.RES_PATH` import from `util.py`
- [ ] use `stream_file_to` for all js downloads?
- [ ] use `stream_file_to` for all css downloads?
- [ ] download html using streams
- [ ] Figure out issue: `www.google.com/someimage.png` download works only with leading `www`
- [x] fix this:
	When downloading fonts like this:
	`<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato:400,900">`, everything after '?' is cut off. Determine name from query and download as `name.css`

# Installing
```
cd woffline
pip install -r requirements.txt
```

# Running tests
Must be in root directory:
```
$ pwd
/woffline/
```

#### Run every test:
```
python -m unittest
```

#### Run single test:
```
python -m unittest test.test_url_util.TestUrlUtil.test_goup
```
This runs the test method `test_goup` inside class `TestUrlUtil` located at 
`/woffline/test/test_url_util.py`

