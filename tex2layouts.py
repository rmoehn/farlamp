import ast
import itertools
import re
import typing

from amplification import tb_layout


# Credits: itertools docs
def consume(iterator, n=None):
    """Advance the iterator n-steps ahead. If n is None, consume entirely."""
    # Use functions that consume iterators at C speed.
    if n is None:
        # feed the entire iterator into a zero-length deque
        collections.deque(iterator, maxlen=0)
    else:
        # advance to the empty slice starting at position n
        next(itertools.islice(iterator, n, n), None)

# Credits: Inspired by definition of `pairwise` in itertools docs.
def tuplewise(iterable, size):
    """Collect data into fixed-length chunks or blocks"""
    copies = itertools.tee(iterable, size)
    for shift_times, copy in enumerate(copies):
        consume(copy, shift_times)
    return zip(*copies)


tex_p = "/Users/erle/Projekte/JZKonferenzbeitrag/Farlamp-repo/tiny-supfail.tex"

with open(tex_p, "r") as f:
    lines_ = f.readlines()


def chartspecs(lines: [str]):
    for (l1, l2, l3) in tuplewise(lines, 3):
        if not l1.startswith("% LC"):
            continue
        patterns = ast.literal_eval(l1.replace("% LC ", "", 1))
        title_line = l2 if l2.startswith("\\") else l3
        match = re.match(r"\\LearningCurve[{](.*?)[}]", title_line)
        title = match.group(1)

        yield {"type": "multiline", "title": title, "patterns": patterns}


cat_spec = {"title": "for LaTeX", "charts": list(chartspecs(lines_)), "collapsed": True}

tb_layout.write(tb_layout.main_layout + [cat_spec], "../short-amp-exp/results/iterate")
