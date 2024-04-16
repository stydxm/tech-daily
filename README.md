# Tech Daily

A daily tech news generator on top of LLMs, spiders and RSS sources.

## Usage

```bash
pip3 install -r requirements.txt
python3 main.py
```
The program will generate a PDF file in directory `temp`.

```
OSError: cannot load library 'gobject-2.0-0': error 0x7e.  
Additionally, ctypes.util.find_library() did not manage to locate a library called 'gobject-2.0-0'
```
Note: if you get the error above, follow the [instruction](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#installation)
or disable `md2pdf` feature.

## Data Sources
- [GitHub Trending](https://github.com/trending)
- [Hacker News](https://news.ycombinator.com/)
- [arxiv](https://arxiv.org/) (rank by [Cool Papers](https://papers.cool/))
