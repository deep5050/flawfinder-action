# flawfinder-action

<img alt="GitHub All Releases" src="https://img.shields.io/github/downloads/deep5050/flawfinder-action/total?style=flat-square">  <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/deep5050/flawfinder-action?style=flat-square">
[![HitCount](http://hits.dwyl.com/deep5050/flawfinder-action.svg)](http://hits.dwyl.com/deep5050/flawfinder-action)

A simple Github Action that checks for security flaws in your C/C++ codes and generates a report.

## what is flawfinder?
[flawfinder](http://doc.gnu-darwin.org/flawfinder/), a simple program that examines C/C++ source code and reports possible security weaknesses (“flaws”) sorted by risk level.

# Usage
Create a ``.yml`` file under ``.github/workflows`` with the following contents
### Default configuration

```yml
name: flawfinder
on: [push]

jobs:
  build:
    name: flawfinder-action
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: flawfinder-action 
        uses: deep5050/flawfinder-action@master
        with:
          github_token: ${{ secrets.GITHUB_TOKEN}}
```

### Advanced configuration
```yml
name: flawfinder
on: [push]

jobs:
  build:
    name: flawfinder-action
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: flawfinder-action 
        uses: deep5050/flawfinder-action@master
        with:
          github_token: ${{ secrets.GITHUB_TOKEN}}
          report_type:
          data_only:
          never_ignore:
          false_positive:
          inputs_flag:
          dot_directories:
          allow_link:
```

#### Input Options
``report type`` : ``html`` Which is default, generates an HTML report. ``text`` for plain text report.

``data_only`` : ``enable`` Don't display the headers and footers of the analysis.

``never_ignore`` : ``enable`` Never ignore security issues, even if they have an ``ignore'' directive in a comment.

``false_positive`` : ``enable`` Do not include hits that are likely to be false  positives.

``inputs_flag`` : ``enable`` Show only functions that obtain data from outside the program. this also sets minlevel to 0.

``dot_directories`` : ``enable`` Scan for files even in directories whose names begin with . (dot) 

``allow_link`` : ``enable`` Allow symbolic links

Please refer to the [flawfinder doumentation](http://doc.gnu-darwin.org/flawfinder/) for further details.

## License

>MIT License

>Copyright (c) 2020 Dipankar Pal

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
