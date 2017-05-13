def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])

def lookup(index, keyword):
    for e in index:
        if e[0] == keyword:
            return e[1]
            break
    return []

def add_pages_to_index(index, url,content):
    words = content.split()
    for word in words:
        add_to_index(index,word,url)

def crawel_web(seed):
    tocrawl = [seed]
    crawled = []
    index = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_pages_to_index(index, page, content)
            union(tocrawl, get_all_links(content))
            crawled.append(page)
    return index


seed = """


<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">


<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

    <title>4. Built-in Types &mdash; Python 3.6.1 documentation</title>

    <link rel="stylesheet" href="../_static/pydoctheme.css" type="text/css" />
    <link rel="stylesheet" href="../_static/pygments.css" type="text/css" />

    <script type="text/javascript">
      var DOCUMENTATION_OPTIONS = {
        URL_ROOT:    '../',
        VERSION:     '3.6.1',
        COLLAPSE_INDEX: false,
        FILE_SUFFIX: '.html',
        HAS_SOURCE:  true
      };
    </script>
    <script type="text/javascript" src="../_static/jquery.js"></script>
    <script type="text/javascript" src="../_static/underscore.js"></script>
    <script type="text/javascript" src="../_static/doctools.js"></script>
    <script type="text/javascript" src="../_static/sidebar.js"></script>
    <link rel="search" type="application/opensearchdescription+xml"
          title="Search within Python 3.6.1 documentation"
          href="../_static/opensearch.xml"/>
    <link rel="author" title="About these documents" href="../about.html" />
    <link rel="copyright" title="Copyright" href="../copyright.html" />
    <link rel="top" title="Python 3.6.1 documentation" href="../contents.html" />
    <link rel="up" title="The Python Standard Library" href="index.html" />
    <link rel="next" title="5. Built-in Exceptions" href="exceptions.html" />
    <link rel="prev" title="3. Built-in Constants" href="constants.html" />
    <link rel="shortcut icon" type="image/png" href="../_static/py.png" />
    <link rel="canonical" href="https://docs.python.org/3/library/stdtypes.html" />

    <script type="text/javascript" src="../_static/copybutton.js"></script>
    <script type="text/javascript" src="../_static/version_switch.js"></script>




  </head>
  <body role="document">
    <div class="related" role="navigation" aria-label="related navigation">
      <h3>Navigation</h3>
      <ul>
        <li class="right" style="margin-right: 10px">
          <a href="../genindex.html" title="General Index"
             accesskey="I">index</a></li>
        <li class="right" >
          <a href="../py-modindex.html" title="Python Module Index"
             >modules</a> |</li>
        <li class="right" >
          <a href="exceptions.html" title="5. Built-in Exceptions"
             accesskey="N">next</a> |</li>
        <li class="right" >
          <a href="constants.html" title="3. Built-in Constants"
             accesskey="P">previous</a> |</li>
        <li><img src="../_static/py.png" alt=""
                 style="vertical-align: middle; margin-top: -1px"/></li>
        <li><a href="https://www.python.org/">Python</a> &raquo;</li>
        <li>
          <span class="version_switcher_placeholder">3.6.1</span>
          <a href="../index.html">Documentation </a> &raquo;
        </li>

          <li class="nav-item nav-item-1"><a href="index.html" accesskey="U">The Python Standard Library</a> &raquo;</li>
    <li class="right">


    <div class="inline-search" style="display: none" role="search">
        <form class="inline-search" action="../search.html" method="get">
          <input placeholder="Quick search" type="text" name="q" />
          <input type="submit" value="Go" />
          <input type="hidden" name="check_keywords" value="yes" />
          <input type="hidden" name="area" value="default" />
        </form>
    </div>
    <script type="text/javascript">$('.inline-search').show(0);</script>
         |
    </li>

      </ul>
    </div>

    <div class="document">
      <div class="documentwrapper">
        <div class="bodywrapper">
          <div class="body" role="main">

  <div class="section" id="built-in-types">
<span id="bltin-types"></span><h1>4. Built-in Types<a class="headerlink" href="#built-in-types" title="Permalink to this headline">¶</a></h1>
<p>The following sections describe the standard types that are built into the
interpreter.</p>
<p id="index-0">The principal built-in types are numerics, sequences, mappings, classes,
instances and exceptions.</p>
<p>Some collection classes are mutable.  The methods that add, subtract, or
rearrange their members in place, and don&#8217;t return a specific item, never return
the collection instance itself but <code class="docutils literal"><span class="pre">None</span></code>.</p>
<p>Some operations are supported by several object types; in particular,
practically all objects can be compared, tested for truth value, and converted
to a string (with the <a class="reference internal" href="functions.html#repr" title="repr"><code class="xref py py-func docutils literal"><span class="pre">repr()</span></code></a> function or the slightly different
<a class="reference internal" href="#str" title="str"><code class="xref py py-func docutils literal"><span class="pre">str()</span></code></a> function).  The latter function is implicitly used when an object is
written by the <a class="reference internal" href="functions.html#print" title="print"><code class="xref py py-func docutils literal"><span class="pre">print()</span></code></a> function.</p>
<div class="section" id="truth-value-testing">
<span id="truth"></span><h2>4.1. Truth Value Testing<a class="headerlink" href="#truth-value-testing" title="Permalink to this headline">¶</a></h2>
<p id="index-1">Any object can be tested for truth value, for use in an <a class="reference internal" href="../reference/compound_stmts.html#if"><code class="xref std std-keyword docutils literal"><span class="pre">if</span></code></a> or
<a class="reference internal" href="../reference/compound_stmts.html#while"><code class="xref std std-keyword docutils literal"><span class="pre">while</span></code></a> condition or as operand of the Boolean operations below. The
following values are considered false:</p>
<blockquote>
<div></div></blockquote>
<ul id="index-2">
<li><p class="first"><code class="docutils literal"><span class="pre">None</span></code></p>
</li>
<li id="index-3"><p class="first"><code class="docutils literal"><span class="pre">False</span></code></p>
</li>
<li><p class="first">zero of any numeric type, for example, <code class="docutils literal"><span class="pre">0</span></code>, <code class="docutils literal"><span class="pre">0.0</span></code>, <code class="docutils literal"><span class="pre">0j</span></code>.</p>
</li>
<li><p class="first">any empty sequence, for example, <code class="docutils literal"><span class="pre">''</span></code>, <code class="docutils literal"><span class="pre">()</span></code>, <code class="docutils literal"><span class="pre">[]</span></code>.</p>
</li>
<li><p class="first">any empty mapping, for example, <code class="docutils literal"><span class="pre">{}</span></code>.</p>
</li>
<li><p class="first">instances of user-defined classes, if the class defines a <a class="reference internal" href="../reference/datamodel.html#object.__bool__" title="object.__bool__"><code class="xref py py-meth docutils literal"><span class="pre">__bool__()</span></code></a> or
<a class="reference internal" href="../reference/datamodel.html#object.__len__" title="object.__len__"><code class="xref py py-meth docutils literal"><span class="pre">__len__()</span></code></a> method, when that method returns the integer zero or
<a class="reference internal" href="functions.html#bool" title="bool"><code class="xref py py-class docutils literal"><span class="pre">bool</span></code></a> value <code class="docutils literal"><span class="pre">False</span></code>. <a class="footnote-reference" href="#id11" id="id1">[1]</a></p>
</li>
</ul>
<p id="index-4">All other values are considered true &#8212; so objects of many types are always
true.</p>
<p id="index-5">Operations and built-in functions that have a Boolean result always return <code class="docutils literal"><span class="pre">0</span></code>
or <code class="docutils literal"><span class="pre">False</span></code> for false and <code class="docutils literal"><span class="pre">1</span></code> or <code class="docutils literal"><span class="pre">True</span></code> for true, unless otherwise stated.
(Important exception: the Boolean operations <code class="docutils literal"><span class="pre">or</span></code> and <code class="docutils literal"><span class="pre">and</span></code> always return
one of their operands.)</p>
</div>
<div class="section" id="boolean-operations-and-or-not">
<span id="boolean"></span><h2>4.2. Boolean Operations &#8212; <a class="reference internal" href="../reference/expressions.html#and"><code class="xref std std-keyword docutils literal"><span class="pre">and</span></code></a>, <a class="reference internal" href="../reference/expressions.html#or"><code class="xref std std-keyword docutils literal"><span class="pre">or</span></code></a>, <a class="reference internal" href="../reference/expressions.html#not"><code class="xref std std-keyword docutils literal"><span class="pre">not</span></code></a><a class="headerlink" href="#boolean-operations-and-or-not" title="Permalink to this headline">¶</a></h2>
<p id="index-6">These are the Boolean operations, ordered by ascending priority:</p>
<table border="1" class="docutils">
<colgroup>
<col width="25%" />
<col width="62%" />
<col width="13%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Operation</th>
<th class="head">Result</th>
<th class="head">Notes</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><code class="docutils literal"><span class="pre">x</span> <span class="pre">or</span> <span class="pre">y</span></code></td>
<td>if <em>x</em> is false, then <em>y</em>, else
<em>x</em></td>
<td>(1)</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">x</span> <span class="pre">and</span> <span class="pre">y</span></code></td>
<td>if <em>x</em> is false, then <em>x</em>, else
<em>y</em></td>
<td>(2)</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">not</span> <span class="pre">x</span></code></td>
<td>if <em>x</em> is false, then <code class="docutils literal"><span class="pre">True</span></code>,
else <code class="docutils literal"><span class="pre">False</span></code></td>
<td>(3)</td>
</tr>
</tbody>
</table>
<p id="index-7">Notes:</p>
<ol class="arabic simple">
<li>This is a short-circuit operator, so it only evaluates the second
argument if the first one is false.</li>
<li>This is a short-circuit operator, so it only evaluates the second
argument if the first one is true.</li>
<li><code class="docutils literal"><span class="pre">not</span></code> has a lower priority than non-Boolean operators, so <code class="docutils literal"><span class="pre">not</span> <span class="pre">a</span> <span class="pre">==</span> <span class="pre">b</span></code> is
interpreted as <code class="docutils literal"><span class="pre">not</span> <span class="pre">(a</span> <span class="pre">==</span> <span class="pre">b)</span></code>, and <code class="docutils literal"><span class="pre">a</span> <span class="pre">==</span> <span class="pre">not</span> <span class="pre">b</span></code> is a syntax error.</li>
</ol>
</div>
<div class="section" id="comparisons">
<span id="stdcomparisons"></span><h2>4.3. Comparisons<a class="headerlink" href="#comparisons" title="Permalink to this headline">¶</a></h2>
<p id="index-8">There are eight comparison operations in Python.  They all have the same
priority (which is higher than that of the Boolean operations).  Comparisons can
be chained arbitrarily; for example, <code class="docutils literal"><span class="pre">x</span> <span class="pre">&lt;</span> <span class="pre">y</span> <span class="pre">&lt;=</span> <span class="pre">z</span></code> is equivalent to <code class="docutils literal"><span class="pre">x</span> <span class="pre">&lt;</span> <span class="pre">y</span> <span class="pre">and</span>
<span class="pre">y</span> <span class="pre">&lt;=</span> <span class="pre">z</span></code>, except that <em>y</em> is evaluated only once (but in both cases <em>z</em> is not
evaluated at all when <code class="docutils literal"><span class="pre">x</span> <span class="pre">&lt;</span> <span class="pre">y</span></code> is found to be false).</p>
<p>This table summarizes the comparison operations:</p>
<table border="1" class="docutils">
<colgroup>
<col width="32%" />
<col width="68%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Operation</th>
<th class="head">Meaning</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><code class="docutils literal"><span class="pre">&lt;</span></code></td>
<td>strictly less than</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">&lt;=</span></code></td>
<td>less than or equal</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">&gt;</span></code></td>
<td>strictly greater than</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">&gt;=</span></code></td>
<td>greater than or equal</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">==</span></code></td>
<td>equal</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">!=</span></code></td>
<td>not equal</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">is</span></code></td>
<td>object identity</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">is</span> <span class="pre">not</span></code></td>
<td>negated object identity</td>
</tr>
</tbody>
</table>
<p id="index-9">Objects of different types, except different numeric types, never compare equal.
Furthermore, some types (for example, function objects) support only a degenerate
notion of comparison where any two objects of that type are unequal.  The <code class="docutils literal"><span class="pre">&lt;</span></code>,
<code class="docutils literal"><span class="pre">&lt;=</span></code>, <code class="docutils literal"><span class="pre">&gt;</span></code> and <code class="docutils literal"><span class="pre">&gt;=</span></code> operators will raise a <a class="reference internal" href="exceptions.html#TypeError" title="TypeError"><code class="xref py py-exc docutils literal"><span class="pre">TypeError</span></code></a> exception when
comparing a complex number with another built-in numeric type, when the objects
are of different types that cannot be compared, or in other cases where there is
no defined ordering.</p>
<p id="index-10">Non-identical instances of a class normally compare as non-equal unless the
class defines the <a class="reference internal" href="../reference/datamodel.html#object.__eq__" title="object.__eq__"><code class="xref py py-meth docutils literal"><span class="pre">__eq__()</span></code></a> method.</p>
<p>Instances of a class cannot be ordered with respect to other instances of the
same class, or other types of object, unless the class defines enough of the
methods <a class="reference internal" href="../reference/datamodel.html#object.__lt__" title="object.__lt__"><code class="xref py py-meth docutils literal"><span class="pre">__lt__()</span></code></a>, <a class="reference internal" href="../reference/datamodel.html#object.__le__" title="object.__le__"><code class="xref py py-meth docutils literal"><span class="pre">__le__()</span></code></a>, <a class="reference internal" href="../reference/datamodel.html#object.__gt__" title="object.__gt__"><code class="xref py py-meth docutils literal"><span class="pre">__gt__()</span></code></a>, and <a class="reference internal" href="../reference/datamodel.html#object.__ge__" title="object.__ge__"><code class="xref py py-meth docutils literal"><span class="pre">__ge__()</span></code></a> (in
general, <a class="reference internal" href="../reference/datamodel.html#object.__lt__" title="object.__lt__"><code class="xref py py-meth docutils literal"><span class="pre">__lt__()</span></code></a> and <a class="reference internal" href="../reference/datamodel.html#object.__eq__" title="object.__eq__"><code class="xref py py-meth docutils literal"><span class="pre">__eq__()</span></code></a> are sufficient, if you want the
conventional meanings of the comparison operators).</p>
<p>The behavior of the <a class="reference internal" href="../reference/expressions.html#is"><code class="xref std std-keyword docutils literal"><span class="pre">is</span></code></a> and <a class="reference internal" href="../reference/expressions.html#is-not"><code class="xref std std-keyword docutils literal"><span class="pre">is</span> <span class="pre">not</span></code></a> operators cannot be
customized; also they can be applied to any two objects and never raise an
exception.</p>
<p id="index-11">Two more operations with the same syntactic priority, <a class="reference internal" href="../reference/expressions.html#in"><code class="xref std std-keyword docutils literal"><span class="pre">in</span></code></a> and
<a class="reference internal" href="../reference/expressions.html#not-in"><code class="xref std std-keyword docutils literal"><span class="pre">not</span> <span class="pre">in</span></code></a>, are supported only by sequence types (below).</p>
</div>
<div class="section" id="numeric-types-int-float-complex">
<span id="typesnumeric"></span><h2>4.4. Numeric Types &#8212; <a class="reference internal" href="functions.html#int" title="int"><code class="xref py py-class docutils literal"><span class="pre">int</span></code></a>, <a class="reference internal" href="functions.html#float" title="float"><code class="xref py py-class docutils literal"><span class="pre">float</span></code></a>, <a class="reference internal" href="functions.html#complex" title="complex"><code class="xref py py-class docutils literal"><span class="pre">complex</span></code></a><a class="headerlink" href="#numeric-types-int-float-complex" title="Permalink to this headline">¶</a></h2>
<p id="index-12">There are three distinct numeric types: <em class="dfn">integers</em>, <em class="dfn">floating
point numbers</em>, and <em class="dfn">complex numbers</em>.  In addition, Booleans are a
subtype of integers.  Integers have unlimited precision.  Floating point
numbers are usually implemented using <code class="xref c c-type docutils literal"><span class="pre">double</span></code> in C; information
about the precision and internal representation of floating point
numbers for the machine on which your program is running is available
in <a class="reference internal" href="sys.html#sys.float_info" title="sys.float_info"><code class="xref py py-data docutils literal"><span class="pre">sys.float_info</span></code></a>.  Complex numbers have a real and imaginary
part, which are each a floating point number.  To extract these parts
from a complex number <em>z</em>, use <code class="docutils literal"><span class="pre">z.real</span></code> and <code class="docutils literal"><span class="pre">z.imag</span></code>. (The standard
library includes additional numeric types, <a class="reference internal" href="fractions.html#module-fractions" title="fractions: Rational numbers."><code class="xref py py-mod docutils literal"><span class="pre">fractions</span></code></a> that hold
rationals, and <a class="reference internal" href="decimal.html#module-decimal" title="decimal: Implementation of the General Decimal Arithmetic  Specification."><code class="xref py py-mod docutils literal"><span class="pre">decimal</span></code></a> that hold floating-point numbers with
user-definable precision.)</p>
<p id="index-13">Numbers are created by numeric literals or as the result of built-in functions
and operators.  Unadorned integer literals (including hex, octal and binary
numbers) yield integers.  Numeric literals containing a decimal point or an
exponent sign yield floating point numbers.  Appending <code class="docutils literal"><span class="pre">'j'</span></code> or <code class="docutils literal"><span class="pre">'J'</span></code> to a
numeric literal yields an imaginary number (a complex number with a zero real
part) which you can add to an integer or float to get a complex number with real
and imaginary parts.</p>
<p id="index-14">Python fully supports mixed arithmetic: when a binary arithmetic operator has
operands of different numeric types, the operand with the &#8220;narrower&#8221; type is
widened to that of the other, where integer is narrower than floating point,
which is narrower than complex.  Comparisons between numbers of mixed type use
the same rule. <a class="footnote-reference" href="#id12" id="id2">[2]</a> The constructors <a class="reference internal" href="functions.html#int" title="int"><code class="xref py py-func docutils literal"><span class="pre">int()</span></code></a>, <a class="reference internal" href="functions.html#float" title="float"><code class="xref py py-func docutils literal"><span class="pre">float()</span></code></a>, and
<a class="reference internal" href="functions.html#complex" title="complex"><code class="xref py py-func docutils literal"><span class="pre">complex()</span></code></a> can be used to produce numbers of a specific type.</p>
<p>All numeric types (except complex) support the following operations, sorted by
ascending priority (all numeric operations have a higher priority than
comparison operations):</p>
<table border="1" class="docutils">
<colgroup>
<col width="25%" />
<col width="40%" />
<col width="11%" />
<col width="24%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Operation</th>
<th class="head">Result</th>
<th class="head">Notes</th>
<th class="head">Full documentation</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><code class="docutils literal"><span class="pre">x</span> <span class="pre">+</span> <span class="pre">y</span></code></td>
<td>sum of <em>x</em> and <em>y</em></td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">x</span> <span class="pre">-</span> <span class="pre">y</span></code></td>
<td>difference of <em>x</em> and <em>y</em></td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">x</span> <span class="pre">*</span> <span class="pre">y</span></code></td>
<td>product of <em>x</em> and <em>y</em></td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">x</span> <span class="pre">/</span> <span class="pre">y</span></code></td>
<td>quotient of <em>x</em> and <em>y</em></td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">x</span> <span class="pre">//</span> <span class="pre">y</span></code></td>
<td>floored quotient of <em>x</em> and
<em>y</em></td>
<td>(1)</td>
<td>&nbsp;</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">x</span> <span class="pre">%</span> <span class="pre">y</span></code></td>
<td>remainder of <code class="docutils literal"><span class="pre">x</span> <span class="pre">/</span> <span class="pre">y</span></code></td>
<td>(2)</td>
<td>&nbsp;</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">-x</span></code></td>
<td><em>x</em> negated</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">+x</span></code></td>
<td><em>x</em> unchanged</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">abs(x)</span></code></td>
<td>absolute value or magnitude of
<em>x</em></td>
<td>&nbsp;</td>
<td><a class="reference internal" href="functions.html#abs" title="abs"><code class="xref py py-func docutils literal"><span class="pre">abs()</span></code></a></td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">int(x)</span></code></td>
<td><em>x</em> converted to integer</td>
<td>(3)(6)</td>
<td><a class="reference internal" href="functions.html#int" title="int"><code class="xref py py-func docutils literal"><span class="pre">int()</span></code></a></td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">float(x)</span></code></td>
<td><em>x</em> converted to floating point</td>
<td>(4)(6)</td>
<td><a class="reference internal" href="functions.html#float" title="float"><code class="xref py py-func docutils literal"><span class="pre">float()</span></code></a></td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">complex(re,</span> <span class="pre">im)</span></code></td>
<td>a complex number with real part
<em>re</em>, imaginary part <em>im</em>.
<em>im</em> defaults to zero.</td>
<td>(6)</td>
<td><a class="reference internal" href="functions.html#complex" title="complex"><code class="xref py py-func docutils literal"><span class="pre">complex()</span></code></a></td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">c.conjugate()</span></code></td>
<td>conjugate of the complex number
<em>c</em></td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">divmod(x,</span> <span class="pre">y)</span></code></td>
<td>the pair <code class="docutils literal"><span class="pre">(x</span> <span class="pre">//</span> <span class="pre">y,</span> <span class="pre">x</span> <span class="pre">%</span> <span class="pre">y)</span></code></td>
<td>(2)</td>
<td><a class="reference internal" href="functions.html#divmod" title="divmod"><code class="xref py py-func docutils literal"><span class="pre">divmod()</span></code></a></td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">pow(x,</span> <span class="pre">y)</span></code></td>
<td><em>x</em> to the power <em>y</em></td>
<td>(5)</td>
<td><a class="reference internal" href="functions.html#pow" title="pow"><code class="xref py py-func docutils literal"><span class="pre">pow()</span></code></a></td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">x</span> <span class="pre">**</span> <span class="pre">y</span></code></td>
<td><em>x</em> to the power <em>y</em></td>
<td>(5)</td>
<td>&nbsp;</td>
</tr>
</tbody>
</table>
<p id="index-15">Notes:</p>
<ol class="arabic">
<li><p class="first">Also referred to as integer division.  The resultant value is a whole
integer, though the result&#8217;s type is not necessarily int.  The result is
always rounded towards minus infinity: <code class="docutils literal"><span class="pre">1//2</span></code> is <code class="docutils literal"><span class="pre">0</span></code>, <code class="docutils literal"><span class="pre">(-1)//2</span></code> is
<code class="docutils literal"><span class="pre">-1</span></code>, <code class="docutils literal"><span class="pre">1//(-2)</span></code> is <code class="docutils literal"><span class="pre">-1</span></code>, and <code class="docutils literal"><span class="pre">(-1)//(-2)</span></code> is <code class="docutils literal"><span class="pre">0</span></code>.</p>
</li>
<li><p class="first">Not for complex numbers.  Instead convert to floats using <a class="reference internal" href="functions.html#abs" title="abs"><code class="xref py py-func docutils literal"><span class="pre">abs()</span></code></a> if
appropriate.</p>
</li>
<li><p id="index-16">Conversion from floating point to integer may round or truncate
as in C; see functions <a class="reference internal" href="math.html#math.floor" title="math.floor"><code class="xref py py-func docutils literal"><span class="pre">math.floor()</span></code></a> and <a class="reference internal" href="math.html#math.ceil" title="math.ceil"><code class="xref py py-func docutils literal"><span class="pre">math.ceil()</span></code></a> for
well-defined conversions.</p>
</li>
<li><p class="first">float also accepts the strings &#8220;nan&#8221; and &#8220;inf&#8221; with an optional prefix &#8220;+&#8221;
or &#8220;-&#8221; for Not a Number (NaN) and positive or negative infinity.</p>
</li>
<li><p class="first">Python defines <code class="docutils literal"><span class="pre">pow(0,</span> <span class="pre">0)</span></code> and <code class="docutils literal"><span class="pre">0</span> <span class="pre">**</span> <span class="pre">0</span></code> to be <code class="docutils literal"><span class="pre">1</span></code>, as is common for
programming languages.</p>
</li>
<li><p class="first">The numeric literals accepted include the digits <code class="docutils literal"><span class="pre">0</span></code> to <code class="docutils literal"><span class="pre">9</span></code> or any
Unicode equivalent (code points with the <code class="docutils literal"><span class="pre">Nd</span></code> property).</p>
<p>See <a class="reference external" href="http://www.unicode.org/Public/8.0.0/ucd/extracted/DerivedNumericType.txt">http://www.unicode.org/Public/8.0.0/ucd/extracted/DerivedNumericType.txt</a>
for a complete list of code points with the <code class="docutils literal"><span class="pre">Nd</span></code> property.</p>
</li>
</ol>
<p>All <a class="reference internal" href="numbers.html#numbers.Real" title="numbers.Real"><code class="xref py py-class docutils literal"><span class="pre">numbers.Real</span></code></a> types (<a class="reference internal" href="functions.html#int" title="int"><code class="xref py py-class docutils literal"><span class="pre">int</span></code></a> and <a class="reference internal" href="functions.html#float" title="float"><code class="xref py py-class docutils literal"><span class="pre">float</span></code></a>) also include
the following operations:</p>
<table border="1" class="docutils">
<colgroup>
<col width="31%" />
<col width="69%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Operation</th>
<th class="head">Result</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><a class="reference internal" href="math.html#math.trunc" title="math.trunc"><code class="xref py py-func docutils literal"><span class="pre">math.trunc(x)</span></code></a></td>
<td><em>x</em> truncated to <a class="reference internal" href="numbers.html#numbers.Integral" title="numbers.Integral"><code class="xref py py-class docutils literal"><span class="pre">Integral</span></code></a></td>
</tr>
<tr class="row-odd"><td><a class="reference internal" href="functions.html#round" title="round"><code class="xref py py-func docutils literal"><span class="pre">round(x[,</span>
<span class="pre">n])</span></code></a></td>
<td><em>x</em> rounded to <em>n</em> digits,
rounding half to even. If <em>n</em> is
omitted, it defaults to 0.</td>
</tr>
<tr class="row-even"><td><a class="reference internal" href="math.html#math.floor" title="math.floor"><code class="xref py py-func docutils literal"><span class="pre">math.floor(x)</span></code></a></td>
<td>the greatest <a class="reference internal" href="numbers.html#numbers.Integral" title="numbers.Integral"><code class="xref py py-class docutils literal"><span class="pre">Integral</span></code></a>
&lt;= <em>x</em></td>
</tr>
<tr class="row-odd"><td><a class="reference internal" href="math.html#math.ceil" title="math.ceil"><code class="xref py py-func docutils literal"><span class="pre">math.ceil(x)</span></code></a></td>
<td>the least <a class="reference internal" href="numbers.html#numbers.Integral" title="numbers.Integral"><code class="xref py py-class docutils literal"><span class="pre">Integral</span></code></a> &gt;= <em>x</em></td>
</tr>
</tbody>
</table>
<p>For additional numeric operations see the <a class="reference internal" href="math.html#module-math" title="math: Mathematical functions (sin() etc.)."><code class="xref py py-mod docutils literal"><span class="pre">math</span></code></a> and <a class="reference internal" href="cmath.html#module-cmath" title="cmath: Mathematical functions for complex numbers."><code class="xref py py-mod docutils literal"><span class="pre">cmath</span></code></a>
modules.</p>
<div class="section" id="bitwise-operations-on-integer-types">
<span id="bitstring-ops"></span><h3>4.4.1. Bitwise Operations on Integer Types<a class="headerlink" href="#bitwise-operations-on-integer-types" title="Permalink to this headline">¶</a></h3>
<p id="index-17">Bitwise operations only make sense for integers.  Negative numbers are treated
as their 2&#8217;s complement value (this assumes that there are enough bits so that
no overflow occurs during the operation).</p>
<p>The priorities of the binary bitwise operations are all lower than the numeric
operations and higher than the comparisons; the unary operation <code class="docutils literal"><span class="pre">~</span></code> has the
same priority as the other unary numeric operations (<code class="docutils literal"><span class="pre">+</span></code> and <code class="docutils literal"><span class="pre">-</span></code>).</p>
<p>This table lists the bitwise operations sorted in ascending priority:</p>
<table border="1" class="docutils">
<colgroup>
<col width="22%" />
<col width="59%" />
<col width="19%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Operation</th>
<th class="head">Result</th>
<th class="head">Notes</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><code class="docutils literal"><span class="pre">x</span> <span class="pre">|</span> <span class="pre">y</span></code></td>
<td>bitwise <em class="dfn">or</em> of <em>x</em> and
<em>y</em></td>
<td>&nbsp;</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">x</span> <span class="pre">^</span> <span class="pre">y</span></code></td>
<td>bitwise <em class="dfn">exclusive or</em> of
<em>x</em> and <em>y</em></td>
<td>&nbsp;</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">x</span> <span class="pre">&amp;</span> <span class="pre">y</span></code></td>
<td>bitwise <em class="dfn">and</em> of <em>x</em> and
<em>y</em></td>
<td>&nbsp;</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">x</span> <span class="pre">&lt;&lt;</span> <span class="pre">n</span></code></td>
<td><em>x</em> shifted left by <em>n</em> bits</td>
<td>(1)(2)</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">x</span> <span class="pre">&gt;&gt;</span> <span class="pre">n</span></code></td>
<td><em>x</em> shifted right by <em>n</em> bits</td>
<td>(1)(3)</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">~x</span></code></td>
<td>the bits of <em>x</em> inverted</td>
<td>&nbsp;</td>
</tr>
</tbody>
</table>
<p>Notes:</p>
<ol class="arabic simple">
<li>Negative shift counts are illegal and cause a <a class="reference internal" href="exceptions.html#ValueError" title="ValueError"><code class="xref py py-exc docutils literal"><span class="pre">ValueError</span></code></a> to be raised.</li>
<li>A left shift by <em>n</em> bits is equivalent to multiplication by <code class="docutils literal"><span class="pre">pow(2,</span> <span class="pre">n)</span></code>
without overflow check.</li>
<li>A right shift by <em>n</em> bits is equivalent to division by <code class="docutils literal"><span class="pre">pow(2,</span> <span class="pre">n)</span></code> without
overflow check.</li>
</ol>
</div>
<div class="section" id="additional-methods-on-integer-types">
<h3>4.4.2. Additional Methods on Integer Types<a class="headerlink" href="#additional-methods-on-integer-types" title="Permalink to this headline">¶</a></h3>
<p>The int type implements the <a class="reference internal" href="numbers.html#numbers.Integral" title="numbers.Integral"><code class="xref py py-class docutils literal"><span class="pre">numbers.Integral</span></code></a> <a class="reference internal" href="../glossary.html#term-abstract-base-class"><span class="xref std std-term">abstract base
class</span></a>. In addition, it provides a few more methods:</p>
<dl class="method">
<dt id="int.bit_length">
<code class="descclassname">int.</code><code class="descname">bit_length</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#int.bit_length" title="Permalink to this definition">¶</a></dt>
<dd><p>Return the number of bits necessary to represent an integer in binary,
excluding the sign and leading zeros:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">n</span> <span class="o">=</span> <span class="o">-</span><span class="mi">37</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">bin</span><span class="p">(</span><span class="n">n</span><span class="p">)</span>
<span class="go">&#39;-0b100101&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">n</span><span class="o">.</span><span class="n">bit_length</span><span class="p">()</span>
<span class="go">6</span>
</pre></div>
</div>
<p>More precisely, if <code class="docutils literal"><span class="pre">x</span></code> is nonzero, then <code class="docutils literal"><span class="pre">x.bit_length()</span></code> is the
unique positive integer <code class="docutils literal"><span class="pre">k</span></code> such that <code class="docutils literal"><span class="pre">2**(k-1)</span> <span class="pre">&lt;=</span> <span class="pre">abs(x)</span> <span class="pre">&lt;</span> <span class="pre">2**k</span></code>.
Equivalently, when <code class="docutils literal"><span class="pre">abs(x)</span></code> is small enough to have a correctly
rounded logarithm, then <code class="docutils literal"><span class="pre">k</span> <span class="pre">=</span> <span class="pre">1</span> <span class="pre">+</span> <span class="pre">int(log(abs(x),</span> <span class="pre">2))</span></code>.
If <code class="docutils literal"><span class="pre">x</span></code> is zero, then <code class="docutils literal"><span class="pre">x.bit_length()</span></code> returns <code class="docutils literal"><span class="pre">0</span></code>.</p>
<p>Equivalent to:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="k">def</span> <span class="nf">bit_length</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
    <span class="n">s</span> <span class="o">=</span> <span class="nb">bin</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>       <span class="c1"># binary representation:  bin(-37) --&gt; &#39;-0b100101&#39;</span>
    <span class="n">s</span> <span class="o">=</span> <span class="n">s</span><span class="o">.</span><span class="n">lstrip</span><span class="p">(</span><span class="s1">&#39;-0b&#39;</span><span class="p">)</span> <span class="c1"># remove leading zeros and minus sign</span>
    <span class="k">return</span> <span class="nb">len</span><span class="p">(</span><span class="n">s</span><span class="p">)</span>       <span class="c1"># len(&#39;100101&#39;) --&gt; 6</span>
</pre></div>
</div>
<div class="versionadded">
<p><span class="versionmodified">New in version 3.1.</span></p>
</div>
</dd></dl>

<dl class="method">
<dt id="int.to_bytes">
<code class="descclassname">int.</code><code class="descname">to_bytes</code><span class="sig-paren">(</span><em>length</em>, <em>byteorder</em>, <em>*</em>, <em>signed=False</em><span class="sig-paren">)</span><a class="headerlink" href="#int.to_bytes" title="Permalink to this definition">¶</a></dt>
<dd><p>Return an array of bytes representing an integer.</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="p">(</span><span class="mi">1024</span><span class="p">)</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="n">byteorder</span><span class="o">=</span><span class="s1">&#39;big&#39;</span><span class="p">)</span>
<span class="go">b&#39;\x04\x00&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="p">(</span><span class="mi">1024</span><span class="p">)</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="n">byteorder</span><span class="o">=</span><span class="s1">&#39;big&#39;</span><span class="p">)</span>
<span class="go">b&#39;\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="p">(</span><span class="o">-</span><span class="mi">1024</span><span class="p">)</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="n">byteorder</span><span class="o">=</span><span class="s1">&#39;big&#39;</span><span class="p">,</span> <span class="n">signed</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="go">b&#39;\xff\xff\xff\xff\xff\xff\xff\xff\xfc\x00&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">x</span> <span class="o">=</span> <span class="mi">1000</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">x</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">((</span><span class="n">x</span><span class="o">.</span><span class="n">bit_length</span><span class="p">()</span> <span class="o">+</span> <span class="mi">7</span><span class="p">)</span> <span class="o">//</span> <span class="mi">8</span><span class="p">,</span> <span class="n">byteorder</span><span class="o">=</span><span class="s1">&#39;little&#39;</span><span class="p">)</span>
<span class="go">b&#39;\xe8\x03&#39;</span>
</pre></div>
</div>
<p>The integer is represented using <em>length</em> bytes.  An <a class="reference internal" href="exceptions.html#OverflowError" title="OverflowError"><code class="xref py py-exc docutils literal"><span class="pre">OverflowError</span></code></a>
is raised if the integer is not representable with the given number of
bytes.</p>
<p>The <em>byteorder</em> argument determines the byte order used to represent the
integer.  If <em>byteorder</em> is <code class="docutils literal"><span class="pre">&quot;big&quot;</span></code>, the most significant byte is at the
beginning of the byte array.  If <em>byteorder</em> is <code class="docutils literal"><span class="pre">&quot;little&quot;</span></code>, the most
significant byte is at the end of the byte array.  To request the native
byte order of the host system, use <a class="reference internal" href="sys.html#sys.byteorder" title="sys.byteorder"><code class="xref py py-data docutils literal"><span class="pre">sys.byteorder</span></code></a> as the byte order
value.</p>
<p>The <em>signed</em> argument determines whether two&#8217;s complement is used to
represent the integer.  If <em>signed</em> is <code class="docutils literal"><span class="pre">False</span></code> and a negative integer is
given, an <a class="reference internal" href="exceptions.html#OverflowError" title="OverflowError"><code class="xref py py-exc docutils literal"><span class="pre">OverflowError</span></code></a> is raised. The default value for <em>signed</em>
is <code class="docutils literal"><span class="pre">False</span></code>.</p>
<div class="versionadded">
<p><span class="versionmodified">New in version 3.2.</span></p>
</div>
</dd></dl>

<dl class="classmethod">
<dt id="int.from_bytes">
<em class="property">classmethod </em><code class="descclassname">int.</code><code class="descname">from_bytes</code><span class="sig-paren">(</span><em>bytes</em>, <em>byteorder</em>, <em>*</em>, <em>signed=False</em><span class="sig-paren">)</span><a class="headerlink" href="#int.from_bytes" title="Permalink to this definition">¶</a></dt>
<dd><p>Return the integer represented by the given array of bytes.</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="nb">int</span><span class="o">.</span><span class="n">from_bytes</span><span class="p">(</span><span class="n">b</span><span class="s1">&#39;</span><span class="se">\x00\x10</span><span class="s1">&#39;</span><span class="p">,</span> <span class="n">byteorder</span><span class="o">=</span><span class="s1">&#39;big&#39;</span><span class="p">)</span>
<span class="go">16</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">int</span><span class="o">.</span><span class="n">from_bytes</span><span class="p">(</span><span class="n">b</span><span class="s1">&#39;</span><span class="se">\x00\x10</span><span class="s1">&#39;</span><span class="p">,</span> <span class="n">byteorder</span><span class="o">=</span><span class="s1">&#39;little&#39;</span><span class="p">)</span>
<span class="go">4096</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">int</span><span class="o">.</span><span class="n">from_bytes</span><span class="p">(</span><span class="n">b</span><span class="s1">&#39;</span><span class="se">\xfc\x00</span><span class="s1">&#39;</span><span class="p">,</span> <span class="n">byteorder</span><span class="o">=</span><span class="s1">&#39;big&#39;</span><span class="p">,</span> <span class="n">signed</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="go">-1024</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">int</span><span class="o">.</span><span class="n">from_bytes</span><span class="p">(</span><span class="n">b</span><span class="s1">&#39;</span><span class="se">\xfc\x00</span><span class="s1">&#39;</span><span class="p">,</span> <span class="n">byteorder</span><span class="o">=</span><span class="s1">&#39;big&#39;</span><span class="p">,</span> <span class="n">signed</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
<span class="go">64512</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">int</span><span class="o">.</span><span class="n">from_bytes</span><span class="p">([</span><span class="mi">255</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">],</span> <span class="n">byteorder</span><span class="o">=</span><span class="s1">&#39;big&#39;</span><span class="p">)</span>
<span class="go">16711680</span>
</pre></div>
</div>
<p>The argument <em>bytes</em> must either be a <a class="reference internal" href="../glossary.html#term-bytes-like-object"><span class="xref std std-term">bytes-like object</span></a> or an
iterable producing bytes.</p>
<p>The <em>byteorder</em> argument determines the byte order used to represent the
integer.  If <em>byteorder</em> is <code class="docutils literal"><span class="pre">&quot;big&quot;</span></code>, the most significant byte is at the
beginning of the byte array.  If <em>byteorder</em> is <code class="docutils literal"><span class="pre">&quot;little&quot;</span></code>, the most
significant byte is at the end of the byte array.  To request the native
byte order of the host system, use <a class="reference internal" href="sys.html#sys.byteorder" title="sys.byteorder"><code class="xref py py-data docutils literal"><span class="pre">sys.byteorder</span></code></a> as the byte order
value.</p>
<p>The <em>signed</em> argument indicates whether two&#8217;s complement is used to
represent the integer.</p>
<div class="versionadded">
<p><span class="versionmodified">New in version 3.2.</span></p>
</div>
</dd></dl>

</div>
<div class="section" id="additional-methods-on-float">
<h3>4.4.3. Additional Methods on Float<a class="headerlink" href="#additional-methods-on-float" title="Permalink to this headline">¶</a></h3>
<p>The float type implements the <a class="reference internal" href="numbers.html#numbers.Real" title="numbers.Real"><code class="xref py py-class docutils literal"><span class="pre">numbers.Real</span></code></a> <a class="reference internal" href="../glossary.html#term-abstract-base-class"><span class="xref std std-term">abstract base
class</span></a>. float also has the following additional methods.</p>
<dl class="method">
<dt id="float.as_integer_ratio">
<code class="descclassname">float.</code><code class="descname">as_integer_ratio</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#float.as_integer_ratio" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a pair of integers whose ratio is exactly equal to the
original float and with a positive denominator.  Raises
<a class="reference internal" href="exceptions.html#OverflowError" title="OverflowError"><code class="xref py py-exc docutils literal"><span class="pre">OverflowError</span></code></a> on infinities and a <a class="reference internal" href="exceptions.html#ValueError" title="ValueError"><code class="xref py py-exc docutils literal"><span class="pre">ValueError</span></code></a> on
NaNs.</p>
</dd></dl>

<dl class="method">
<dt id="float.is_integer">
<code class="descclassname">float.</code><code class="descname">is_integer</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#float.is_integer" title="Permalink to this definition">¶</a></dt>
<dd><p>Return <code class="docutils literal"><span class="pre">True</span></code> if the float instance is finite with integral
value, and <code class="docutils literal"><span class="pre">False</span></code> otherwise:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="p">(</span><span class="o">-</span><span class="mf">2.0</span><span class="p">)</span><span class="o">.</span><span class="n">is_integer</span><span class="p">()</span>
<span class="go">True</span>
<span class="gp">&gt;&gt;&gt; </span><span class="p">(</span><span class="mf">3.2</span><span class="p">)</span><span class="o">.</span><span class="n">is_integer</span><span class="p">()</span>
<span class="go">False</span>
</pre></div>
</div>
</dd></dl>

<p>Two methods support conversion to
and from hexadecimal strings.  Since Python&#8217;s floats are stored
internally as binary numbers, converting a float to or from a
<em>decimal</em> string usually involves a small rounding error.  In
contrast, hexadecimal strings allow exact representation and
specification of floating-point numbers.  This can be useful when
debugging, and in numerical work.</p>
<dl class="method">
<dt id="float.hex">
<code class="descclassname">float.</code><code class="descname">hex</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#float.hex" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a representation of a floating-point number as a hexadecimal
string.  For finite floating-point numbers, this representation
will always include a leading <code class="docutils literal"><span class="pre">0x</span></code> and a trailing <code class="docutils literal"><span class="pre">p</span></code> and
exponent.</p>
</dd></dl>

<dl class="classmethod">
<dt id="float.fromhex">
<em class="property">classmethod </em><code class="descclassname">float.</code><code class="descname">fromhex</code><span class="sig-paren">(</span><em>s</em><span class="sig-paren">)</span><a class="headerlink" href="#float.fromhex" title="Permalink to this definition">¶</a></dt>
<dd><p>Class method to return the float represented by a hexadecimal
string <em>s</em>.  The string <em>s</em> may have leading and trailing
whitespace.</p>
</dd></dl>

<p>Note that <a class="reference internal" href="#float.hex" title="float.hex"><code class="xref py py-meth docutils literal"><span class="pre">float.hex()</span></code></a> is an instance method, while
<a class="reference internal" href="#float.fromhex" title="float.fromhex"><code class="xref py py-meth docutils literal"><span class="pre">float.fromhex()</span></code></a> is a class method.</p>
<p>A hexadecimal string takes the form:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="p">[</span><span class="n">sign</span><span class="p">]</span> <span class="p">[</span><span class="s1">&#39;0x&#39;</span><span class="p">]</span> <span class="n">integer</span> <span class="p">[</span><span class="s1">&#39;.&#39;</span> <span class="n">fraction</span><span class="p">]</span> <span class="p">[</span><span class="s1">&#39;p&#39;</span> <span class="n">exponent</span><span class="p">]</span>
</pre></div>
</div>
<p>where the optional <code class="docutils literal"><span class="pre">sign</span></code> may by either <code class="docutils literal"><span class="pre">+</span></code> or <code class="docutils literal"><span class="pre">-</span></code>, <code class="docutils literal"><span class="pre">integer</span></code>
and <code class="docutils literal"><span class="pre">fraction</span></code> are strings of hexadecimal digits, and <code class="docutils literal"><span class="pre">exponent</span></code>
is a decimal integer with an optional leading sign.  Case is not
significant, and there must be at least one hexadecimal digit in
either the integer or the fraction.  This syntax is similar to the
syntax specified in section 6.4.4.2 of the C99 standard, and also to
the syntax used in Java 1.5 onwards.  In particular, the output of
<a class="reference internal" href="#float.hex" title="float.hex"><code class="xref py py-meth docutils literal"><span class="pre">float.hex()</span></code></a> is usable as a hexadecimal floating-point literal in
C or Java code, and hexadecimal strings produced by C&#8217;s <code class="docutils literal"><span class="pre">%a</span></code> format
character or Java&#8217;s <code class="docutils literal"><span class="pre">Double.toHexString</span></code> are accepted by
<a class="reference internal" href="#float.fromhex" title="float.fromhex"><code class="xref py py-meth docutils literal"><span class="pre">float.fromhex()</span></code></a>.</p>
<p>Note that the exponent is written in decimal rather than hexadecimal,
and that it gives the power of 2 by which to multiply the coefficient.
For example, the hexadecimal string <code class="docutils literal"><span class="pre">0x3.a7p10</span></code> represents the
floating-point number <code class="docutils literal"><span class="pre">(3</span> <span class="pre">+</span> <span class="pre">10./16</span> <span class="pre">+</span> <span class="pre">7./16**2)</span> <span class="pre">*</span> <span class="pre">2.0**10</span></code>, or
<code class="docutils literal"><span class="pre">3740.0</span></code>:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="nb">float</span><span class="o">.</span><span class="n">fromhex</span><span class="p">(</span><span class="s1">&#39;0x3.a7p10&#39;</span><span class="p">)</span>
<span class="go">3740.0</span>
</pre></div>
</div>
<p>Applying the reverse conversion to <code class="docutils literal"><span class="pre">3740.0</span></code> gives a different
hexadecimal string representing the same number:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="nb">float</span><span class="o">.</span><span class="n">hex</span><span class="p">(</span><span class="mf">3740.0</span><span class="p">)</span>
<span class="go">&#39;0x1.d380000000000p+11&#39;</span>
</pre></div>
</div>
</div>
<div class="section" id="hashing-of-numeric-types">
<span id="numeric-hash"></span><h3>4.4.4. Hashing of numeric types<a class="headerlink" href="#hashing-of-numeric-types" title="Permalink to this headline">¶</a></h3>
<p>For numbers <code class="docutils literal"><span class="pre">x</span></code> and <code class="docutils literal"><span class="pre">y</span></code>, possibly of different types, it&#8217;s a requirement
that <code class="docutils literal"><span class="pre">hash(x)</span> <span class="pre">==</span> <span class="pre">hash(y)</span></code> whenever <code class="docutils literal"><span class="pre">x</span> <span class="pre">==</span> <span class="pre">y</span></code> (see the <a class="reference internal" href="../reference/datamodel.html#object.__hash__" title="object.__hash__"><code class="xref py py-meth docutils literal"><span class="pre">__hash__()</span></code></a>
method documentation for more details).  For ease of implementation and
efficiency across a variety of numeric types (including <a class="reference internal" href="functions.html#int" title="int"><code class="xref py py-class docutils literal"><span class="pre">int</span></code></a>,
<a class="reference internal" href="functions.html#float" title="float"><code class="xref py py-class docutils literal"><span class="pre">float</span></code></a>, <a class="reference internal" href="decimal.html#decimal.Decimal" title="decimal.Decimal"><code class="xref py py-class docutils literal"><span class="pre">decimal.Decimal</span></code></a> and <a class="reference internal" href="fractions.html#fractions.Fraction" title="fractions.Fraction"><code class="xref py py-class docutils literal"><span class="pre">fractions.Fraction</span></code></a>)
Python&#8217;s hash for numeric types is based on a single mathematical function
that&#8217;s defined for any rational number, and hence applies to all instances of
<a class="reference internal" href="functions.html#int" title="int"><code class="xref py py-class docutils literal"><span class="pre">int</span></code></a> and <a class="reference internal" href="fractions.html#fractions.Fraction" title="fractions.Fraction"><code class="xref py py-class docutils literal"><span class="pre">fractions.Fraction</span></code></a>, and all finite instances of
<a class="reference internal" href="functions.html#float" title="float"><code class="xref py py-class docutils literal"><span class="pre">float</span></code></a> and <a class="reference internal" href="decimal.html#decimal.Decimal" title="decimal.Decimal"><code class="xref py py-class docutils literal"><span class="pre">decimal.Decimal</span></code></a>.  Essentially, this function is
given by reduction modulo <code class="docutils literal"><span class="pre">P</span></code> for a fixed prime <code class="docutils literal"><span class="pre">P</span></code>.  The value of <code class="docutils literal"><span class="pre">P</span></code> is
made available to Python as the <code class="xref py py-attr docutils literal"><span class="pre">modulus</span></code> attribute of
<a class="reference internal" href="sys.html#sys.hash_info" title="sys.hash_info"><code class="xref py py-data docutils literal"><span class="pre">sys.hash_info</span></code></a>.</p>
<div class="impl-detail compound">
<p><strong>CPython implementation detail:</strong> Currently, the prime used is <code class="docutils literal"><span class="pre">P</span> <span class="pre">=</span> <span class="pre">2**31</span> <span class="pre">-</span> <span class="pre">1</span></code> on machines with 32-bit C
longs and <code class="docutils literal"><span class="pre">P</span> <span class="pre">=</span> <span class="pre">2**61</span> <span class="pre">-</span> <span class="pre">1</span></code> on machines with 64-bit C longs.</p>
</div>
<p>Here are the rules in detail:</p>
<ul class="simple">
<li>If <code class="docutils literal"><span class="pre">x</span> <span class="pre">=</span> <span class="pre">m</span> <span class="pre">/</span> <span class="pre">n</span></code> is a nonnegative rational number and <code class="docutils literal"><span class="pre">n</span></code> is not divisible
by <code class="docutils literal"><span class="pre">P</span></code>, define <code class="docutils literal"><span class="pre">hash(x)</span></code> as <code class="docutils literal"><span class="pre">m</span> <span class="pre">*</span> <span class="pre">invmod(n,</span> <span class="pre">P)</span> <span class="pre">%</span> <span class="pre">P</span></code>, where <code class="docutils literal"><span class="pre">invmod(n,</span>
<span class="pre">P)</span></code> gives the inverse of <code class="docutils literal"><span class="pre">n</span></code> modulo <code class="docutils literal"><span class="pre">P</span></code>.</li>
<li>If <code class="docutils literal"><span class="pre">x</span> <span class="pre">=</span> <span class="pre">m</span> <span class="pre">/</span> <span class="pre">n</span></code> is a nonnegative rational number and <code class="docutils literal"><span class="pre">n</span></code> is
divisible by <code class="docutils literal"><span class="pre">P</span></code> (but <code class="docutils literal"><span class="pre">m</span></code> is not) then <code class="docutils literal"><span class="pre">n</span></code> has no inverse
modulo <code class="docutils literal"><span class="pre">P</span></code> and the rule above doesn&#8217;t apply; in this case define
<code class="docutils literal"><span class="pre">hash(x)</span></code> to be the constant value <code class="docutils literal"><span class="pre">sys.hash_info.inf</span></code>.</li>
<li>If <code class="docutils literal"><span class="pre">x</span> <span class="pre">=</span> <span class="pre">m</span> <span class="pre">/</span> <span class="pre">n</span></code> is a negative rational number define <code class="docutils literal"><span class="pre">hash(x)</span></code>
as <code class="docutils literal"><span class="pre">-hash(-x)</span></code>.  If the resulting hash is <code class="docutils literal"><span class="pre">-1</span></code>, replace it with
<code class="docutils literal"><span class="pre">-2</span></code>.</li>
<li>The particular values <code class="docutils literal"><span class="pre">sys.hash_info.inf</span></code>, <code class="docutils literal"><span class="pre">-sys.hash_info.inf</span></code>
and <code class="docutils literal"><span class="pre">sys.hash_info.nan</span></code> are used as hash values for positive
infinity, negative infinity, or nans (respectively).  (All hashable
nans have the same hash value.)</li>
<li>For a <a class="reference internal" href="functions.html#complex" title="complex"><code class="xref py py-class docutils literal"><span class="pre">complex</span></code></a> number <code class="docutils literal"><span class="pre">z</span></code>, the hash values of the real
and imaginary parts are combined by computing <code class="docutils literal"><span class="pre">hash(z.real)</span> <span class="pre">+</span>
<span class="pre">sys.hash_info.imag</span> <span class="pre">*</span> <span class="pre">hash(z.imag)</span></code>, reduced modulo
<code class="docutils literal"><span class="pre">2**sys.hash_info.width</span></code> so that it lies in
<code class="docutils literal"><span class="pre">range(-2**(sys.hash_info.width</span> <span class="pre">-</span> <span class="pre">1),</span> <span class="pre">2**(sys.hash_info.width</span> <span class="pre">-</span>
<span class="pre">1))</span></code>.  Again, if the result is <code class="docutils literal"><span class="pre">-1</span></code>, it&#8217;s replaced with <code class="docutils literal"><span class="pre">-2</span></code>.</li>
</ul>
<p>To clarify the above rules, here&#8217;s some example Python code,
equivalent to the built-in hash, for computing the hash of a rational
number, <a class="reference internal" href="functions.html#float" title="float"><code class="xref py py-class docutils literal"><span class="pre">float</span></code></a>, or <a class="reference internal" href="functions.html#complex" title="complex"><code class="xref py py-class docutils literal"><span class="pre">complex</span></code></a>:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sys</span><span class="o">,</span> <span class="nn">math</span>

<span class="k">def</span> <span class="nf">hash_fraction</span><span class="p">(</span><span class="n">m</span><span class="p">,</span> <span class="n">n</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;Compute the hash of a rational number m / n.</span>

<span class="sd">    Assumes m and n are integers, with n positive.</span>
<span class="sd">    Equivalent to hash(fractions.Fraction(m, n)).</span>

<span class="sd">    &quot;&quot;&quot;</span>
    <span class="n">P</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">hash_info</span><span class="o">.</span><span class="n">modulus</span>
    <span class="c1"># Remove common factors of P.  (Unnecessary if m and n already coprime.)</span>
    <span class="k">while</span> <span class="n">m</span> <span class="o">%</span> <span class="n">P</span> <span class="o">==</span> <span class="n">n</span> <span class="o">%</span> <span class="n">P</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
        <span class="n">m</span><span class="p">,</span> <span class="n">n</span> <span class="o">=</span> <span class="n">m</span> <span class="o">//</span> <span class="n">P</span><span class="p">,</span> <span class="n">n</span> <span class="o">//</span> <span class="n">P</span>

    <span class="k">if</span> <span class="n">n</span> <span class="o">%</span> <span class="n">P</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
        <span class="n">hash_value</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">hash_info</span><span class="o">.</span><span class="n">inf</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="c1"># Fermat&#39;s Little Theorem: pow(n, P-1, P) is 1, so</span>
        <span class="c1"># pow(n, P-2, P) gives the inverse of n modulo P.</span>
        <span class="n">hash_value</span> <span class="o">=</span> <span class="p">(</span><span class="nb">abs</span><span class="p">(</span><span class="n">m</span><span class="p">)</span> <span class="o">%</span> <span class="n">P</span><span class="p">)</span> <span class="o">*</span> <span class="nb">pow</span><span class="p">(</span><span class="n">n</span><span class="p">,</span> <span class="n">P</span> <span class="o">-</span> <span class="mi">2</span><span class="p">,</span> <span class="n">P</span><span class="p">)</span> <span class="o">%</span> <span class="n">P</span>
    <span class="k">if</span> <span class="n">m</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span>
        <span class="n">hash_value</span> <span class="o">=</span> <span class="o">-</span><span class="n">hash_value</span>
    <span class="k">if</span> <span class="n">hash_value</span> <span class="o">==</span> <span class="o">-</span><span class="mi">1</span><span class="p">:</span>
        <span class="n">hash_value</span> <span class="o">=</span> <span class="o">-</span><span class="mi">2</span>
    <span class="k">return</span> <span class="n">hash_value</span>

<span class="k">def</span> <span class="nf">hash_float</span><span class="p">(</span><span class="n">x</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;Compute the hash of a float x.&quot;&quot;&quot;</span>

    <span class="k">if</span> <span class="n">math</span><span class="o">.</span><span class="n">isnan</span><span class="p">(</span><span class="n">x</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">sys</span><span class="o">.</span><span class="n">hash_info</span><span class="o">.</span><span class="n">nan</span>
    <span class="k">elif</span> <span class="n">math</span><span class="o">.</span><span class="n">isinf</span><span class="p">(</span><span class="n">x</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">sys</span><span class="o">.</span><span class="n">hash_info</span><span class="o">.</span><span class="n">inf</span> <span class="k">if</span> <span class="n">x</span> <span class="o">&gt;</span> <span class="mi">0</span> <span class="k">else</span> <span class="o">-</span><span class="n">sys</span><span class="o">.</span><span class="n">hash_info</span><span class="o">.</span><span class="n">inf</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">hash_fraction</span><span class="p">(</span><span class="o">*</span><span class="n">x</span><span class="o">.</span><span class="n">as_integer_ratio</span><span class="p">())</span>

<span class="k">def</span> <span class="nf">hash_complex</span><span class="p">(</span><span class="n">z</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;Compute the hash of a complex number z.&quot;&quot;&quot;</span>

    <span class="n">hash_value</span> <span class="o">=</span> <span class="n">hash_float</span><span class="p">(</span><span class="n">z</span><span class="o">.</span><span class="n">real</span><span class="p">)</span> <span class="o">+</span> <span class="n">sys</span><span class="o">.</span><span class="n">hash_info</span><span class="o">.</span><span class="n">imag</span> <span class="o">*</span> <span class="n">hash_float</span><span class="p">(</span><span class="n">z</span><span class="o">.</span><span class="n">imag</span><span class="p">)</span>
    <span class="c1"># do a signed reduction modulo 2**sys.hash_info.width</span>
    <span class="n">M</span> <span class="o">=</span> <span class="mi">2</span><span class="o">**</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">hash_info</span><span class="o">.</span><span class="n">width</span> <span class="o">-</span> <span class="mi">1</span><span class="p">)</span>
    <span class="n">hash_value</span> <span class="o">=</span> <span class="p">(</span><span class="n">hash_value</span> <span class="o">&amp;</span> <span class="p">(</span><span class="n">M</span> <span class="o">-</span> <span class="mi">1</span><span class="p">))</span> <span class="o">-</span> <span class="p">(</span><span class="n">hash_value</span> <span class="o">&amp;</span> <span class="n">M</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">hash_value</span> <span class="o">==</span> <span class="o">-</span><span class="mi">1</span><span class="p">:</span>
        <span class="n">hash_value</span> <span class="o">=</span> <span class="o">-</span><span class="mi">2</span>
    <span class="k">return</span> <span class="n">hash_value</span>
</pre></div>
</div>
</div>
</div>
<div class="section" id="iterator-types">
<span id="typeiter"></span><h2>4.5. Iterator Types<a class="headerlink" href="#iterator-types" title="Permalink to this headline">¶</a></h2>
<p id="index-18">Python supports a concept of iteration over containers.  This is implemented
using two distinct methods; these are used to allow user-defined classes to
support iteration.  Sequences, described below in more detail, always support
the iteration methods.</p>
<p>One method needs to be defined for container objects to provide iteration
support:</p>
<dl class="method">
<dt id="container.__iter__">
<code class="descclassname">container.</code><code class="descname">__iter__</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#container.__iter__" title="Permalink to this definition">¶</a></dt>
<dd><p>Return an iterator object.  The object is required to support the iterator
protocol described below.  If a container supports different types of
iteration, additional methods can be provided to specifically request
iterators for those iteration types.  (An example of an object supporting
multiple forms of iteration would be a tree structure which supports both
breadth-first and depth-first traversal.)  This method corresponds to the
<a class="reference internal" href="../c-api/typeobj.html#c.PyTypeObject.tp_iter" title="PyTypeObject.tp_iter"><code class="xref c c-member docutils literal"><span class="pre">tp_iter</span></code></a> slot of the type structure for Python objects in the Python/C
API.</p>
</dd></dl>

<p>The iterator objects themselves are required to support the following two
methods, which together form the <em class="dfn">iterator protocol</em>:</p>
<dl class="method">
<dt id="iterator.__iter__">
<code class="descclassname">iterator.</code><code class="descname">__iter__</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#iterator.__iter__" title="Permalink to this definition">¶</a></dt>
<dd><p>Return the iterator object itself.  This is required to allow both containers
and iterators to be used with the <a class="reference internal" href="../reference/compound_stmts.html#for"><code class="xref std std-keyword docutils literal"><span class="pre">for</span></code></a> and <a class="reference internal" href="../reference/expressions.html#in"><code class="xref std std-keyword docutils literal"><span class="pre">in</span></code></a> statements.
This method corresponds to the <a class="reference internal" href="../c-api/typeobj.html#c.PyTypeObject.tp_iter" title="PyTypeObject.tp_iter"><code class="xref c c-member docutils literal"><span class="pre">tp_iter</span></code></a> slot of the type structure for
Python objects in the Python/C API.</p>
</dd></dl>

<dl class="method">
<dt id="iterator.__next__">
<code class="descclassname">iterator.</code><code class="descname">__next__</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#iterator.__next__" title="Permalink to this definition">¶</a></dt>
<dd><p>Return the next item from the container.  If there are no further items, raise
the <a class="reference internal" href="exceptions.html#StopIteration" title="StopIteration"><code class="xref py py-exc docutils literal"><span class="pre">StopIteration</span></code></a> exception.  This method corresponds to the
<a class="reference internal" href="../c-api/typeobj.html#c.PyTypeObject.tp_iternext" title="PyTypeObject.tp_iternext"><code class="xref c c-member docutils literal"><span class="pre">tp_iternext</span></code></a> slot of the type structure for Python objects in the
Python/C API.</p>
</dd></dl>

<p>Python defines several iterator objects to support iteration over general and
specific sequence types, dictionaries, and other more specialized forms.  The
specific types are not important beyond their implementation of the iterator
protocol.</p>
<p>Once an iterator&#8217;s <a class="reference internal" href="#iterator.__next__" title="iterator.__next__"><code class="xref py py-meth docutils literal"><span class="pre">__next__()</span></code></a> method raises
<a class="reference internal" href="exceptions.html#StopIteration" title="StopIteration"><code class="xref py py-exc docutils literal"><span class="pre">StopIteration</span></code></a>, it must continue to do so on subsequent calls.
Implementations that do not obey this property are deemed broken.</p>
<div class="section" id="generator-types">
<span id="id3"></span><h3>4.5.1. Generator Types<a class="headerlink" href="#generator-types" title="Permalink to this headline">¶</a></h3>
<p>Python&#8217;s <a class="reference internal" href="../glossary.html#term-generator"><span class="xref std std-term">generator</span></a>s provide a convenient way to implement the iterator
protocol.  If a container object&#8217;s <a class="reference internal" href="../reference/datamodel.html#object.__iter__" title="object.__iter__"><code class="xref py py-meth docutils literal"><span class="pre">__iter__()</span></code></a> method is implemented as a
generator, it will automatically return an iterator object (technically, a
generator object) supplying the <a class="reference internal" href="../reference/datamodel.html#object.__iter__" title="object.__iter__"><code class="xref py py-meth docutils literal"><span class="pre">__iter__()</span></code></a> and <a class="reference internal" href="../reference/expressions.html#generator.__next__" title="generator.__next__"><code class="xref py py-meth docutils literal"><span class="pre">__next__()</span></code></a>
methods.
More information about generators can be found in <a class="reference internal" href="../reference/expressions.html#yieldexpr"><span>the documentation for
the yield expression</span></a>.</p>
</div>
</div>
<div class="section" id="sequence-types-list-tuple-range">
<span id="typesseq"></span><h2>4.6. Sequence Types &#8212; <a class="reference internal" href="#list" title="list"><code class="xref py py-class docutils literal"><span class="pre">list</span></code></a>, <a class="reference internal" href="#tuple" title="tuple"><code class="xref py py-class docutils literal"><span class="pre">tuple</span></code></a>, <a class="reference internal" href="#range" title="range"><code class="xref py py-class docutils literal"><span class="pre">range</span></code></a><a class="headerlink" href="#sequence-types-list-tuple-range" title="Permalink to this headline">¶</a></h2>
<p>There are three basic sequence types: lists, tuples, and range objects.
Additional sequence types tailored for processing of
<a class="reference internal" href="#binaryseq"><span>binary data</span></a> and <a class="reference internal" href="#textseq"><span>text strings</span></a> are
described in dedicated sections.</p>
<div class="section" id="common-sequence-operations">
<span id="typesseq-common"></span><h3>4.6.1. Common Sequence Operations<a class="headerlink" href="#common-sequence-operations" title="Permalink to this headline">¶</a></h3>
<p id="index-19">The operations in the following table are supported by most sequence types,
both mutable and immutable. The <a class="reference internal" href="collections.abc.html#collections.abc.Sequence" title="collections.abc.Sequence"><code class="xref py py-class docutils literal"><span class="pre">collections.abc.Sequence</span></code></a> ABC is
provided to make it easier to correctly implement these operations on
custom sequence types.</p>
<p>This table lists the sequence operations sorted in ascending priority.  In the
table, <em>s</em> and <em>t</em> are sequences of the same type, <em>n</em>, <em>i</em>, <em>j</em> and <em>k</em> are
integers and <em>x</em> is an arbitrary object that meets any type and value
restrictions imposed by <em>s</em>.</p>
<p>The <code class="docutils literal"><span class="pre">in</span></code> and <code class="docutils literal"><span class="pre">not</span> <span class="pre">in</span></code> operations have the same priorities as the
comparison operations. The <code class="docutils literal"><span class="pre">+</span></code> (concatenation) and <code class="docutils literal"><span class="pre">*</span></code> (repetition)
operations have the same priority as the corresponding numeric operations.</p>
<table border="1" class="docutils" id="index-20">
<colgroup>
<col width="38%" />
<col width="47%" />
<col width="15%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Operation</th>
<th class="head">Result</th>
<th class="head">Notes</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><code class="docutils literal"><span class="pre">x</span> <span class="pre">in</span> <span class="pre">s</span></code></td>
<td><code class="docutils literal"><span class="pre">True</span></code> if an item of <em>s</em> is
equal to <em>x</em>, else <code class="docutils literal"><span class="pre">False</span></code></td>
<td>(1)</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">x</span> <span class="pre">not</span> <span class="pre">in</span> <span class="pre">s</span></code></td>
<td><code class="docutils literal"><span class="pre">False</span></code> if an item of <em>s</em> is
equal to <em>x</em>, else <code class="docutils literal"><span class="pre">True</span></code></td>
<td>(1)</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">s</span> <span class="pre">+</span> <span class="pre">t</span></code></td>
<td>the concatenation of <em>s</em> and
<em>t</em></td>
<td>(6)(7)</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">s</span> <span class="pre">*</span> <span class="pre">n</span></code> or
<code class="docutils literal"><span class="pre">n</span> <span class="pre">*</span> <span class="pre">s</span></code></td>
<td>equivalent to adding <em>s</em> to
itself <em>n</em> times</td>
<td>(2)(7)</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">s[i]</span></code></td>
<td><em>i</em>th item of <em>s</em>, origin 0</td>
<td>(3)</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">s[i:j]</span></code></td>
<td>slice of <em>s</em> from <em>i</em> to <em>j</em></td>
<td>(3)(4)</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">s[i:j:k]</span></code></td>
<td>slice of <em>s</em> from <em>i</em> to <em>j</em>
with step <em>k</em></td>
<td>(3)(5)</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">len(s)</span></code></td>
<td>length of <em>s</em></td>
<td>&nbsp;</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">min(s)</span></code></td>
<td>smallest item of <em>s</em></td>
<td>&nbsp;</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">max(s)</span></code></td>
<td>largest item of <em>s</em></td>
<td>&nbsp;</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">s.index(x[,</span> <span class="pre">i[,</span> <span class="pre">j]])</span></code></td>
<td>index of the first occurrence
of <em>x</em> in <em>s</em> (at or after
index <em>i</em> and before index <em>j</em>)</td>
<td>(8)</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">s.count(x)</span></code></td>
<td>total number of occurrences of
<em>x</em> in <em>s</em></td>
<td>&nbsp;</td>
</tr>
</tbody>
</table>
<p>Sequences of the same type also support comparisons.  In particular, tuples
and lists are compared lexicographically by comparing corresponding elements.
This means that to compare equal, every element must compare equal and the
two sequences must be of the same type and have the same length.  (For full
details see <a class="reference internal" href="../reference/expressions.html#comparisons"><span>Comparisons</span></a> in the language reference.)</p>
<p>Notes:</p>
<ol class="arabic">
<li><p class="first">While the <code class="docutils literal"><span class="pre">in</span></code> and <code class="docutils literal"><span class="pre">not</span> <span class="pre">in</span></code> operations are used only for simple
containment testing in the general case, some specialised sequences
(such as <a class="reference internal" href="#str" title="str"><code class="xref py py-class docutils literal"><span class="pre">str</span></code></a>, <a class="reference internal" href="functions.html#bytes" title="bytes"><code class="xref py py-class docutils literal"><span class="pre">bytes</span></code></a> and <a class="reference internal" href="functions.html#bytearray" title="bytearray"><code class="xref py py-class docutils literal"><span class="pre">bytearray</span></code></a>) also use
them for subsequence testing:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s2">&quot;gg&quot;</span> <span class="ow">in</span> <span class="s2">&quot;eggs&quot;</span>
<span class="go">True</span>
</pre></div>
</div>
</li>
<li><p class="first">Values of <em>n</em> less than <code class="docutils literal"><span class="pre">0</span></code> are treated as <code class="docutils literal"><span class="pre">0</span></code> (which yields an empty
sequence of the same type as <em>s</em>).  Note that items in the sequence <em>s</em>
are not copied; they are referenced multiple times.  This often haunts
new Python programmers; consider:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">lists</span> <span class="o">=</span> <span class="p">[[]]</span> <span class="o">*</span> <span class="mi">3</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">lists</span>
<span class="go">[[], [], []]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">lists</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">lists</span>
<span class="go">[[3], [3], [3]]</span>
</pre></div>
</div>
<p>What has happened is that <code class="docutils literal"><span class="pre">[[]]</span></code> is a one-element list containing an empty
list, so all three elements of <code class="docutils literal"><span class="pre">[[]]</span> <span class="pre">*</span> <span class="pre">3</span></code> are references to this single empty
list.  Modifying any of the elements of <code class="docutils literal"><span class="pre">lists</span></code> modifies this single list.
You can create a list of different lists this way:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">lists</span> <span class="o">=</span> <span class="p">[[]</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">3</span><span class="p">)]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">lists</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">lists</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="mi">5</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">lists</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="mi">7</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">lists</span>
<span class="go">[[3], [5], [7]]</span>
</pre></div>
</div>
<p>Further explanation is available in the FAQ entry
<a class="reference internal" href="../faq/programming.html#faq-multidimensional-list"><span>How do I create a multidimensional list?</span></a>.</p>
</li>
<li><p class="first">If <em>i</em> or <em>j</em> is negative, the index is relative to the end of sequence <em>s</em>:
<code class="docutils literal"><span class="pre">len(s)</span> <span class="pre">+</span> <span class="pre">i</span></code> or <code class="docutils literal"><span class="pre">len(s)</span> <span class="pre">+</span> <span class="pre">j</span></code> is substituted.  But note that <code class="docutils literal"><span class="pre">-0</span></code> is
still <code class="docutils literal"><span class="pre">0</span></code>.</p>
</li>
<li><p class="first">The slice of <em>s</em> from <em>i</em> to <em>j</em> is defined as the sequence of items with index
<em>k</em> such that <code class="docutils literal"><span class="pre">i</span> <span class="pre">&lt;=</span> <span class="pre">k</span> <span class="pre">&lt;</span> <span class="pre">j</span></code>.  If <em>i</em> or <em>j</em> is greater than <code class="docutils literal"><span class="pre">len(s)</span></code>, use
<code class="docutils literal"><span class="pre">len(s)</span></code>.  If <em>i</em> is omitted or <code class="docutils literal"><span class="pre">None</span></code>, use <code class="docutils literal"><span class="pre">0</span></code>.  If <em>j</em> is omitted or
<code class="docutils literal"><span class="pre">None</span></code>, use <code class="docutils literal"><span class="pre">len(s)</span></code>.  If <em>i</em> is greater than or equal to <em>j</em>, the slice is
empty.</p>
</li>
<li><p class="first">The slice of <em>s</em> from <em>i</em> to <em>j</em> with step <em>k</em> is defined as the sequence of
items with index  <code class="docutils literal"><span class="pre">x</span> <span class="pre">=</span> <span class="pre">i</span> <span class="pre">+</span> <span class="pre">n*k</span></code> such that <code class="docutils literal"><span class="pre">0</span> <span class="pre">&lt;=</span> <span class="pre">n</span> <span class="pre">&lt;</span> <span class="pre">(j-i)/k</span></code>.  In other words,
the indices are <code class="docutils literal"><span class="pre">i</span></code>, <code class="docutils literal"><span class="pre">i+k</span></code>, <code class="docutils literal"><span class="pre">i+2*k</span></code>, <code class="docutils literal"><span class="pre">i+3*k</span></code> and so on, stopping when
<em>j</em> is reached (but never including <em>j</em>).  When <em>k</em> is positive,
<em>i</em> and <em>j</em> are reduced to <code class="docutils literal"><span class="pre">len(s)</span></code> if they are greater.
When <em>k</em> is negative, <em>i</em> and <em>j</em> are reduced to <code class="docutils literal"><span class="pre">len(s)</span> <span class="pre">-</span> <span class="pre">1</span></code> if
they are greater.  If <em>i</em> or <em>j</em> are omitted or <code class="docutils literal"><span class="pre">None</span></code>, they become
&#8220;end&#8221; values (which end depends on the sign of <em>k</em>).  Note, <em>k</em> cannot be zero.
If <em>k</em> is <code class="docutils literal"><span class="pre">None</span></code>, it is treated like <code class="docutils literal"><span class="pre">1</span></code>.</p>
</li>
<li><p class="first">Concatenating immutable sequences always results in a new object.  This
means that building up a sequence by repeated concatenation will have a
quadratic runtime cost in the total sequence length.  To get a linear
runtime cost, you must switch to one of the alternatives below:</p>
<ul class="simple">
<li>if concatenating <a class="reference internal" href="#str" title="str"><code class="xref py py-class docutils literal"><span class="pre">str</span></code></a> objects, you can build a list and use
<a class="reference internal" href="#str.join" title="str.join"><code class="xref py py-meth docutils literal"><span class="pre">str.join()</span></code></a> at the end or else write to an <a class="reference internal" href="io.html#io.StringIO" title="io.StringIO"><code class="xref py py-class docutils literal"><span class="pre">io.StringIO</span></code></a>
instance and retrieve its value when complete</li>
<li>if concatenating <a class="reference internal" href="functions.html#bytes" title="bytes"><code class="xref py py-class docutils literal"><span class="pre">bytes</span></code></a> objects, you can similarly use
<a class="reference internal" href="#bytes.join" title="bytes.join"><code class="xref py py-meth docutils literal"><span class="pre">bytes.join()</span></code></a> or <a class="reference internal" href="io.html#io.BytesIO" title="io.BytesIO"><code class="xref py py-class docutils literal"><span class="pre">io.BytesIO</span></code></a>, or you can do in-place
concatenation with a <a class="reference internal" href="functions.html#bytearray" title="bytearray"><code class="xref py py-class docutils literal"><span class="pre">bytearray</span></code></a> object.  <a class="reference internal" href="functions.html#bytearray" title="bytearray"><code class="xref py py-class docutils literal"><span class="pre">bytearray</span></code></a>
objects are mutable and have an efficient overallocation mechanism</li>
<li>if concatenating <a class="reference internal" href="#tuple" title="tuple"><code class="xref py py-class docutils literal"><span class="pre">tuple</span></code></a> objects, extend a <a class="reference internal" href="#list" title="list"><code class="xref py py-class docutils literal"><span class="pre">list</span></code></a> instead</li>
<li>for other types, investigate the relevant class documentation</li>
</ul>
</li>
<li><p class="first">Some sequence types (such as <a class="reference internal" href="#range" title="range"><code class="xref py py-class docutils literal"><span class="pre">range</span></code></a>) only support item sequences
that follow specific patterns, and hence don&#8217;t support sequence
concatenation or repetition.</p>
</li>
<li><p class="first"><code class="docutils literal"><span class="pre">index</span></code> raises <a class="reference internal" href="exceptions.html#ValueError" title="ValueError"><code class="xref py py-exc docutils literal"><span class="pre">ValueError</span></code></a> when <em>x</em> is not found in <em>s</em>.
When supported, the additional arguments to the index method allow
efficient searching of subsections of the sequence. Passing the extra
arguments is roughly equivalent to using <code class="docutils literal"><span class="pre">s[i:j].index(x)</span></code>, only
without copying any data and with the returned index being relative to
the start of the sequence rather than the start of the slice.</p>
</li>
</ol>
</div>
<div class="section" id="immutable-sequence-types">
<span id="typesseq-immutable"></span><h3>4.6.2. Immutable Sequence Types<a class="headerlink" href="#immutable-sequence-types" title="Permalink to this headline">¶</a></h3>
<p id="index-21">The only operation that immutable sequence types generally implement that is
not also implemented by mutable sequence types is support for the <a class="reference internal" href="functions.html#hash" title="hash"><code class="xref py py-func docutils literal"><span class="pre">hash()</span></code></a>
built-in.</p>
<p>This support allows immutable sequences, such as <a class="reference internal" href="#tuple" title="tuple"><code class="xref py py-class docutils literal"><span class="pre">tuple</span></code></a> instances, to
be used as <a class="reference internal" href="#dict" title="dict"><code class="xref py py-class docutils literal"><span class="pre">dict</span></code></a> keys and stored in <a class="reference internal" href="#set" title="set"><code class="xref py py-class docutils literal"><span class="pre">set</span></code></a> and <a class="reference internal" href="#frozenset" title="frozenset"><code class="xref py py-class docutils literal"><span class="pre">frozenset</span></code></a>
instances.</p>
<p>Attempting to hash an immutable sequence that contains unhashable values will
result in <a class="reference internal" href="exceptions.html#TypeError" title="TypeError"><code class="xref py py-exc docutils literal"><span class="pre">TypeError</span></code></a>.</p>
</div>
<div class="section" id="mutable-sequence-types">
<span id="typesseq-mutable"></span><h3>4.6.3. Mutable Sequence Types<a class="headerlink" href="#mutable-sequence-types" title="Permalink to this headline">¶</a></h3>
<p id="index-22">The operations in the following table are defined on mutable sequence types.
The <a class="reference internal" href="collections.abc.html#collections.abc.MutableSequence" title="collections.abc.MutableSequence"><code class="xref py py-class docutils literal"><span class="pre">collections.abc.MutableSequence</span></code></a> ABC is provided to make it
easier to correctly implement these operations on custom sequence types.</p>
<p>In the table <em>s</em> is an instance of a mutable sequence type, <em>t</em> is any
iterable object and <em>x</em> is an arbitrary object that meets any type
and value restrictions imposed by <em>s</em> (for example, <a class="reference internal" href="functions.html#bytearray" title="bytearray"><code class="xref py py-class docutils literal"><span class="pre">bytearray</span></code></a> only
accepts integers that meet the value restriction <code class="docutils literal"><span class="pre">0</span> <span class="pre">&lt;=</span> <span class="pre">x</span> <span class="pre">&lt;=</span> <span class="pre">255</span></code>).</p>
<table border="1" class="docutils" id="index-23">
<colgroup>
<col width="36%" />
<col width="39%" />
<col width="25%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Operation</th>
<th class="head">Result</th>
<th class="head">Notes</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><code class="docutils literal"><span class="pre">s[i]</span> <span class="pre">=</span> <span class="pre">x</span></code></td>
<td>item <em>i</em> of <em>s</em> is replaced by
<em>x</em></td>
<td>&nbsp;</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">s[i:j]</span> <span class="pre">=</span> <span class="pre">t</span></code></td>
<td>slice of <em>s</em> from <em>i</em> to <em>j</em>
is replaced by the contents of
the iterable <em>t</em></td>
<td>&nbsp;</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">del</span> <span class="pre">s[i:j]</span></code></td>
<td>same as <code class="docutils literal"><span class="pre">s[i:j]</span> <span class="pre">=</span> <span class="pre">[]</span></code></td>
<td>&nbsp;</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">s[i:j:k]</span> <span class="pre">=</span> <span class="pre">t</span></code></td>
<td>the elements of <code class="docutils literal"><span class="pre">s[i:j:k]</span></code>
are replaced by those of <em>t</em></td>
<td>(1)</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">del</span> <span class="pre">s[i:j:k]</span></code></td>
<td>removes the elements of
<code class="docutils literal"><span class="pre">s[i:j:k]</span></code> from the list</td>
<td>&nbsp;</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">s.append(x)</span></code></td>
<td>appends <em>x</em> to the end of the
sequence (same as
<code class="docutils literal"><span class="pre">s[len(s):len(s)]</span> <span class="pre">=</span> <span class="pre">[x]</span></code>)</td>
<td>&nbsp;</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">s.clear()</span></code></td>
<td>removes all items from <code class="docutils literal"><span class="pre">s</span></code>
(same as <code class="docutils literal"><span class="pre">del</span> <span class="pre">s[:]</span></code>)</td>
<td>(5)</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">s.copy()</span></code></td>
<td>creates a shallow copy of <code class="docutils literal"><span class="pre">s</span></code>
(same as <code class="docutils literal"><span class="pre">s[:]</span></code>)</td>
<td>(5)</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">s.extend(t)</span></code> or
<code class="docutils literal"><span class="pre">s</span> <span class="pre">+=</span> <span class="pre">t</span></code></td>
<td>extends <em>s</em> with the
contents of <em>t</em> (for the
most part the same as
<code class="docutils literal"><span class="pre">s[len(s):len(s)]</span> <span class="pre">=</span> <span class="pre">t</span></code>)</td>
<td>&nbsp;</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">s</span> <span class="pre">*=</span> <span class="pre">n</span></code></td>
<td>updates <em>s</em> with its contents
repeated <em>n</em> times</td>
<td>(6)</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">s.insert(i,</span> <span class="pre">x)</span></code></td>
<td>inserts <em>x</em> into <em>s</em> at the
index given by <em>i</em>
(same as <code class="docutils literal"><span class="pre">s[i:i]</span> <span class="pre">=</span> <span class="pre">[x]</span></code>)</td>
<td>&nbsp;</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">s.pop([i])</span></code></td>
<td>retrieves the item at <em>i</em> and
also removes it from <em>s</em></td>
<td>(2)</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">s.remove(x)</span></code></td>
<td>remove the first item from <em>s</em>
where <code class="docutils literal"><span class="pre">s[i]</span> <span class="pre">==</span> <span class="pre">x</span></code></td>
<td>(3)</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">s.reverse()</span></code></td>
<td>reverses the items of <em>s</em> in
place</td>
<td>(4)</td>
</tr>
</tbody>
</table>
<p>Notes:</p>
<ol class="arabic">
<li><p class="first"><em>t</em> must have the same length as the slice it is replacing.</p>
</li>
<li><p class="first">The optional argument <em>i</em> defaults to <code class="docutils literal"><span class="pre">-1</span></code>, so that by default the last
item is removed and returned.</p>
</li>
<li><p class="first"><code class="docutils literal"><span class="pre">remove</span></code> raises <a class="reference internal" href="exceptions.html#ValueError" title="ValueError"><code class="xref py py-exc docutils literal"><span class="pre">ValueError</span></code></a> when <em>x</em> is not found in <em>s</em>.</p>
</li>
<li><p class="first">The <code class="xref py py-meth docutils literal"><span class="pre">reverse()</span></code> method modifies the sequence in place for economy of
space when reversing a large sequence.  To remind users that it operates by
side effect, it does not return the reversed sequence.</p>
</li>
<li><p class="first"><code class="xref py py-meth docutils literal"><span class="pre">clear()</span></code> and <code class="xref py py-meth docutils literal"><span class="pre">copy()</span></code> are included for consistency with the
interfaces of mutable containers that don&#8217;t support slicing operations
(such as <a class="reference internal" href="#dict" title="dict"><code class="xref py py-class docutils literal"><span class="pre">dict</span></code></a> and <a class="reference internal" href="#set" title="set"><code class="xref py py-class docutils literal"><span class="pre">set</span></code></a>)</p>
<div class="versionadded">
<p><span class="versionmodified">New in version 3.3: </span><code class="xref py py-meth docutils literal"><span class="pre">clear()</span></code> and <code class="xref py py-meth docutils literal"><span class="pre">copy()</span></code> methods.</p>
</div>
</li>
<li><p class="first">The value <em>n</em> is an integer, or an object implementing
<a class="reference internal" href="../reference/datamodel.html#object.__index__" title="object.__index__"><code class="xref py py-meth docutils literal"><span class="pre">__index__()</span></code></a>.  Zero and negative values of <em>n</em> clear
the sequence.  Items in the sequence are not copied; they are referenced
multiple times, as explained for <code class="docutils literal"><span class="pre">s</span> <span class="pre">*</span> <span class="pre">n</span></code> under <a class="reference internal" href="#typesseq-common"><span>Common Sequence Operations</span></a>.</p>
</li>
</ol>
</div>
<div class="section" id="lists">
<span id="typesseq-list"></span><h3>4.6.4. Lists<a class="headerlink" href="#lists" title="Permalink to this headline">¶</a></h3>
<p id="index-24">Lists are mutable sequences, typically used to store collections of
homogeneous items (where the precise degree of similarity will vary by
application).</p>
<dl class="class">
<dt id="list">
<em class="property">class </em><code class="descname">list</code><span class="sig-paren">(</span><span class="optional">[</span><em>iterable</em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#list" title="Permalink to this definition">¶</a></dt>
<dd><p>Lists may be constructed in several ways:</p>
<ul class="simple">
<li>Using a pair of square brackets to denote the empty list: <code class="docutils literal"><span class="pre">[]</span></code></li>
<li>Using square brackets, separating items with commas: <code class="docutils literal"><span class="pre">[a]</span></code>, <code class="docutils literal"><span class="pre">[a,</span> <span class="pre">b,</span> <span class="pre">c]</span></code></li>
<li>Using a list comprehension: <code class="docutils literal"><span class="pre">[x</span> <span class="pre">for</span> <span class="pre">x</span> <span class="pre">in</span> <span class="pre">iterable]</span></code></li>
<li>Using the type constructor: <code class="docutils literal"><span class="pre">list()</span></code> or <code class="docutils literal"><span class="pre">list(iterable)</span></code></li>
</ul>
<p>The constructor builds a list whose items are the same and in the same
order as <em>iterable</em>&#8216;s items.  <em>iterable</em> may be either a sequence, a
container that supports iteration, or an iterator object.  If <em>iterable</em>
is already a list, a copy is made and returned, similar to <code class="docutils literal"><span class="pre">iterable[:]</span></code>.
For example, <code class="docutils literal"><span class="pre">list('abc')</span></code> returns <code class="docutils literal"><span class="pre">['a',</span> <span class="pre">'b',</span> <span class="pre">'c']</span></code> and
<code class="docutils literal"><span class="pre">list(</span> <span class="pre">(1,</span> <span class="pre">2,</span> <span class="pre">3)</span> <span class="pre">)</span></code> returns <code class="docutils literal"><span class="pre">[1,</span> <span class="pre">2,</span> <span class="pre">3]</span></code>.
If no argument is given, the constructor creates a new empty list, <code class="docutils literal"><span class="pre">[]</span></code>.</p>
<p>Many other operations also produce lists, including the <a class="reference internal" href="functions.html#sorted" title="sorted"><code class="xref py py-func docutils literal"><span class="pre">sorted()</span></code></a>
built-in.</p>
<p>Lists implement all of the <a class="reference internal" href="#typesseq-common"><span>common</span></a> and
<a class="reference internal" href="#typesseq-mutable"><span>mutable</span></a> sequence operations. Lists also provide the
following additional method:</p>
<dl class="method">
<dt id="list.sort">
<code class="descname">sort</code><span class="sig-paren">(</span><em>*</em>, <em>key=None</em>, <em>reverse=None</em><span class="sig-paren">)</span><a class="headerlink" href="#list.sort" title="Permalink to this definition">¶</a></dt>
<dd><p>This method sorts the list in place, using only <code class="docutils literal"><span class="pre">&lt;</span></code> comparisons
between items. Exceptions are not suppressed - if any comparison operations
fail, the entire sort operation will fail (and the list will likely be left
in a partially modified state).</p>
<p><a class="reference internal" href="#list.sort" title="list.sort"><code class="xref py py-meth docutils literal"><span class="pre">sort()</span></code></a> accepts two arguments that can only be passed by keyword
(<a class="reference internal" href="../glossary.html#keyword-only-parameter"><span>keyword-only arguments</span></a>):</p>
<p><em>key</em> specifies a function of one argument that is used to extract a
comparison key from each list element (for example, <code class="docutils literal"><span class="pre">key=str.lower</span></code>).
The key corresponding to each item in the list is calculated once and
then used for the entire sorting process. The default value of <code class="docutils literal"><span class="pre">None</span></code>
means that list items are sorted directly without calculating a separate
key value.</p>
<p>The <a class="reference internal" href="functools.html#functools.cmp_to_key" title="functools.cmp_to_key"><code class="xref py py-func docutils literal"><span class="pre">functools.cmp_to_key()</span></code></a> utility is available to convert a 2.x
style <em>cmp</em> function to a <em>key</em> function.</p>
<p><em>reverse</em> is a boolean value.  If set to <code class="docutils literal"><span class="pre">True</span></code>, then the list elements
are sorted as if each comparison were reversed.</p>
<p>This method modifies the sequence in place for economy of space when
sorting a large sequence.  To remind users that it operates by side
effect, it does not return the sorted sequence (use <a class="reference internal" href="functions.html#sorted" title="sorted"><code class="xref py py-func docutils literal"><span class="pre">sorted()</span></code></a> to
explicitly request a new sorted list instance).</p>
<p>The <a class="reference internal" href="#list.sort" title="list.sort"><code class="xref py py-meth docutils literal"><span class="pre">sort()</span></code></a> method is guaranteed to be stable.  A sort is stable if it
guarantees not to change the relative order of elements that compare equal
&#8212; this is helpful for sorting in multiple passes (for example, sort by
department, then by salary grade).</p>
<div class="impl-detail compound">
<p><strong>CPython implementation detail:</strong> While a list is being sorted, the effect of attempting to mutate, or even
inspect, the list is undefined.  The C implementation of Python makes the
list appear empty for the duration, and raises <a class="reference internal" href="exceptions.html#ValueError" title="ValueError"><code class="xref py py-exc docutils literal"><span class="pre">ValueError</span></code></a> if it can
detect that the list has been mutated during a sort.</p>
</div>
</dd></dl>

</dd></dl>

</div>
<div class="section" id="tuples">
<span id="typesseq-tuple"></span><h3>4.6.5. Tuples<a class="headerlink" href="#tuples" title="Permalink to this headline">¶</a></h3>
<p id="index-25">Tuples are immutable sequences, typically used to store collections of
heterogeneous data (such as the 2-tuples produced by the <a class="reference internal" href="functions.html#enumerate" title="enumerate"><code class="xref py py-func docutils literal"><span class="pre">enumerate()</span></code></a>
built-in). Tuples are also used for cases where an immutable sequence of
homogeneous data is needed (such as allowing storage in a <a class="reference internal" href="#set" title="set"><code class="xref py py-class docutils literal"><span class="pre">set</span></code></a> or
<a class="reference internal" href="#dict" title="dict"><code class="xref py py-class docutils literal"><span class="pre">dict</span></code></a> instance).</p>
<dl class="class">
<dt id="tuple">
<em class="property">class </em><code class="descname">tuple</code><span class="sig-paren">(</span><span class="optional">[</span><em>iterable</em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#tuple" title="Permalink to this definition">¶</a></dt>
<dd><p>Tuples may be constructed in a number of ways:</p>
<ul class="simple">
<li>Using a pair of parentheses to denote the empty tuple: <code class="docutils literal"><span class="pre">()</span></code></li>
<li>Using a trailing comma for a singleton tuple: <code class="docutils literal"><span class="pre">a,</span></code> or <code class="docutils literal"><span class="pre">(a,)</span></code></li>
<li>Separating items with commas: <code class="docutils literal"><span class="pre">a,</span> <span class="pre">b,</span> <span class="pre">c</span></code> or <code class="docutils literal"><span class="pre">(a,</span> <span class="pre">b,</span> <span class="pre">c)</span></code></li>
<li>Using the <a class="reference internal" href="#tuple" title="tuple"><code class="xref py py-func docutils literal"><span class="pre">tuple()</span></code></a> built-in: <code class="docutils literal"><span class="pre">tuple()</span></code> or <code class="docutils literal"><span class="pre">tuple(iterable)</span></code></li>
</ul>
<p>The constructor builds a tuple whose items are the same and in the same
order as <em>iterable</em>&#8216;s items.  <em>iterable</em> may be either a sequence, a
container that supports iteration, or an iterator object.  If <em>iterable</em>
is already a tuple, it is returned unchanged. For example,
<code class="docutils literal"><span class="pre">tuple('abc')</span></code> returns <code class="docutils literal"><span class="pre">('a',</span> <span class="pre">'b',</span> <span class="pre">'c')</span></code> and
<code class="docutils literal"><span class="pre">tuple(</span> <span class="pre">[1,</span> <span class="pre">2,</span> <span class="pre">3]</span> <span class="pre">)</span></code> returns <code class="docutils literal"><span class="pre">(1,</span> <span class="pre">2,</span> <span class="pre">3)</span></code>.
If no argument is given, the constructor creates a new empty tuple, <code class="docutils literal"><span class="pre">()</span></code>.</p>
<p>Note that it is actually the comma which makes a tuple, not the parentheses.
The parentheses are optional, except in the empty tuple case, or
when they are needed to avoid syntactic ambiguity. For example,
<code class="docutils literal"><span class="pre">f(a,</span> <span class="pre">b,</span> <span class="pre">c)</span></code> is a function call with three arguments, while
<code class="docutils literal"><span class="pre">f((a,</span> <span class="pre">b,</span> <span class="pre">c))</span></code> is a function call with a 3-tuple as the sole argument.</p>
<p>Tuples implement all of the <a class="reference internal" href="#typesseq-common"><span>common</span></a> sequence
operations.</p>
</dd></dl>

<p>For heterogeneous collections of data where access by name is clearer than
access by index, <a class="reference internal" href="collections.html#collections.namedtuple" title="collections.namedtuple"><code class="xref py py-func docutils literal"><span class="pre">collections.namedtuple()</span></code></a> may be a more appropriate
choice than a simple tuple object.</p>
</div>
<div class="section" id="ranges">
<span id="typesseq-range"></span><h3>4.6.6. Ranges<a class="headerlink" href="#ranges" title="Permalink to this headline">¶</a></h3>
<p id="index-26">The <a class="reference internal" href="#range" title="range"><code class="xref py py-class docutils literal"><span class="pre">range</span></code></a> type represents an immutable sequence of numbers and is
commonly used for looping a specific number of times in <a class="reference internal" href="../reference/compound_stmts.html#for"><code class="xref std std-keyword docutils literal"><span class="pre">for</span></code></a>
loops.</p>
<dl class="class">
<dt id="range">
<em class="property">class </em><code class="descname">range</code><span class="sig-paren">(</span><em>stop</em><span class="sig-paren">)</span><a class="headerlink" href="#range" title="Permalink to this definition">¶</a></dt>
<dt>
<em class="property">class </em><code class="descname">range</code><span class="sig-paren">(</span><em>start</em>, <em>stop</em><span class="optional">[</span>, <em>step</em><span class="optional">]</span><span class="sig-paren">)</span></dt>
<dd><p>The arguments to the range constructor must be integers (either built-in
<a class="reference internal" href="functions.html#int" title="int"><code class="xref py py-class docutils literal"><span class="pre">int</span></code></a> or any object that implements the <code class="docutils literal"><span class="pre">__index__</span></code> special
method).  If the <em>step</em> argument is omitted, it defaults to <code class="docutils literal"><span class="pre">1</span></code>.
If the <em>start</em> argument is omitted, it defaults to <code class="docutils literal"><span class="pre">0</span></code>.
If <em>step</em> is zero, <a class="reference internal" href="exceptions.html#ValueError" title="ValueError"><code class="xref py py-exc docutils literal"><span class="pre">ValueError</span></code></a> is raised.</p>
<p>For a positive <em>step</em>, the contents of a range <code class="docutils literal"><span class="pre">r</span></code> are determined by the
formula <code class="docutils literal"><span class="pre">r[i]</span> <span class="pre">=</span> <span class="pre">start</span> <span class="pre">+</span> <span class="pre">step*i</span></code> where <code class="docutils literal"><span class="pre">i</span> <span class="pre">&gt;=</span> <span class="pre">0</span></code> and
<code class="docutils literal"><span class="pre">r[i]</span> <span class="pre">&lt;</span> <span class="pre">stop</span></code>.</p>
<p>For a negative <em>step</em>, the contents of the range are still determined by
the formula <code class="docutils literal"><span class="pre">r[i]</span> <span class="pre">=</span> <span class="pre">start</span> <span class="pre">+</span> <span class="pre">step*i</span></code>, but the constraints are <code class="docutils literal"><span class="pre">i</span> <span class="pre">&gt;=</span> <span class="pre">0</span></code>
and <code class="docutils literal"><span class="pre">r[i]</span> <span class="pre">&gt;</span> <span class="pre">stop</span></code>.</p>
<p>A range object will be empty if <code class="docutils literal"><span class="pre">r[0]</span></code> does not meet the value
constraint. Ranges do support negative indices, but these are interpreted
as indexing from the end of the sequence determined by the positive
indices.</p>
<p>Ranges containing absolute values larger than <a class="reference internal" href="sys.html#sys.maxsize" title="sys.maxsize"><code class="xref py py-data docutils literal"><span class="pre">sys.maxsize</span></code></a> are
permitted but some features (such as <a class="reference internal" href="functions.html#len" title="len"><code class="xref py py-func docutils literal"><span class="pre">len()</span></code></a>) may raise
<a class="reference internal" href="exceptions.html#OverflowError" title="OverflowError"><code class="xref py py-exc docutils literal"><span class="pre">OverflowError</span></code></a>.</p>
<p>Range examples:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="nb">list</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="mi">10</span><span class="p">))</span>
<span class="go">[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">list</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">11</span><span class="p">))</span>
<span class="go">[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">list</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">30</span><span class="p">,</span> <span class="mi">5</span><span class="p">))</span>
<span class="go">[0, 5, 10, 15, 20, 25]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">list</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">10</span><span class="p">,</span> <span class="mi">3</span><span class="p">))</span>
<span class="go">[0, 3, 6, 9]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">list</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="o">-</span><span class="mi">10</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">))</span>
<span class="go">[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">list</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">))</span>
<span class="go">[]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">list</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">0</span><span class="p">))</span>
<span class="go">[]</span>
</pre></div>
</div>
<p>Ranges implement all of the <a class="reference internal" href="#typesseq-common"><span>common</span></a> sequence operations
except concatenation and repetition (due to the fact that range objects can
only represent sequences that follow a strict pattern and repetition and
concatenation will usually violate that pattern).</p>
<dl class="attribute">
<dt id="range.start">
<code class="descname">start</code><a class="headerlink" href="#range.start" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of the <em>start</em> parameter (or <code class="docutils literal"><span class="pre">0</span></code> if the parameter was
not supplied)</p>
</dd></dl>

<dl class="attribute">
<dt id="range.stop">
<code class="descname">stop</code><a class="headerlink" href="#range.stop" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of the <em>stop</em> parameter</p>
</dd></dl>

<dl class="attribute">
<dt id="range.step">
<code class="descname">step</code><a class="headerlink" href="#range.step" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of the <em>step</em> parameter (or <code class="docutils literal"><span class="pre">1</span></code> if the parameter was
not supplied)</p>
</dd></dl>

</dd></dl>

<p>The advantage of the <a class="reference internal" href="#range" title="range"><code class="xref py py-class docutils literal"><span class="pre">range</span></code></a> type over a regular <a class="reference internal" href="#list" title="list"><code class="xref py py-class docutils literal"><span class="pre">list</span></code></a> or
<a class="reference internal" href="#tuple" title="tuple"><code class="xref py py-class docutils literal"><span class="pre">tuple</span></code></a> is that a <a class="reference internal" href="#range" title="range"><code class="xref py py-class docutils literal"><span class="pre">range</span></code></a> object will always take the same
(small) amount of memory, no matter the size of the range it represents (as it
only stores the <code class="docutils literal"><span class="pre">start</span></code>, <code class="docutils literal"><span class="pre">stop</span></code> and <code class="docutils literal"><span class="pre">step</span></code> values, calculating individual
items and subranges as needed).</p>
<p>Range objects implement the <a class="reference internal" href="collections.abc.html#collections.abc.Sequence" title="collections.abc.Sequence"><code class="xref py py-class docutils literal"><span class="pre">collections.abc.Sequence</span></code></a> ABC, and provide
features such as containment tests, element index lookup, slicing and
support for negative indices (see <a class="reference internal" href="#typesseq"><span>Sequence Types &#8212; list, tuple, range</span></a>):</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">r</span> <span class="o">=</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">20</span><span class="p">,</span> <span class="mi">2</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">r</span>
<span class="go">range(0, 20, 2)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="mi">11</span> <span class="ow">in</span> <span class="n">r</span>
<span class="go">False</span>
<span class="gp">&gt;&gt;&gt; </span><span class="mi">10</span> <span class="ow">in</span> <span class="n">r</span>
<span class="go">True</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">r</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="mi">10</span><span class="p">)</span>
<span class="go">5</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">r</span><span class="p">[</span><span class="mi">5</span><span class="p">]</span>
<span class="go">10</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">r</span><span class="p">[:</span><span class="mi">5</span><span class="p">]</span>
<span class="go">range(0, 10, 2)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">r</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
<span class="go">18</span>
</pre></div>
</div>
<p>Testing range objects for equality with <code class="docutils literal"><span class="pre">==</span></code> and <code class="docutils literal"><span class="pre">!=</span></code> compares
them as sequences.  That is, two range objects are considered equal if
they represent the same sequence of values.  (Note that two range
objects that compare equal might have different <a class="reference internal" href="#range.start" title="range.start"><code class="xref py py-attr docutils literal"><span class="pre">start</span></code></a>,
<a class="reference internal" href="#range.stop" title="range.stop"><code class="xref py py-attr docutils literal"><span class="pre">stop</span></code></a> and <a class="reference internal" href="#range.step" title="range.step"><code class="xref py py-attr docutils literal"><span class="pre">step</span></code></a> attributes, for example
<code class="docutils literal"><span class="pre">range(0)</span> <span class="pre">==</span> <span class="pre">range(2,</span> <span class="pre">1,</span> <span class="pre">3)</span></code> or <code class="docutils literal"><span class="pre">range(0,</span> <span class="pre">3,</span> <span class="pre">2)</span> <span class="pre">==</span> <span class="pre">range(0,</span> <span class="pre">4,</span> <span class="pre">2)</span></code>.)</p>
<div class="versionchanged">
<p><span class="versionmodified">Changed in version 3.2: </span>Implement the Sequence ABC.
Support slicing and negative indices.
Test <a class="reference internal" href="functions.html#int" title="int"><code class="xref py py-class docutils literal"><span class="pre">int</span></code></a> objects for membership in constant time instead of
iterating through all items.</p>
</div>
<div class="versionchanged">
<p><span class="versionmodified">Changed in version 3.3: </span>Define &#8216;==&#8217; and &#8216;!=&#8217; to compare range objects based on the
sequence of values they define (instead of comparing based on
object identity).</p>
</div>
<div class="versionadded">
<p><span class="versionmodified">New in version 3.3: </span>The <a class="reference internal" href="#range.start" title="range.start"><code class="xref py py-attr docutils literal"><span class="pre">start</span></code></a>, <a class="reference internal" href="#range.stop" title="range.stop"><code class="xref py py-attr docutils literal"><span class="pre">stop</span></code></a> and <a class="reference internal" href="#range.step" title="range.step"><code class="xref py py-attr docutils literal"><span class="pre">step</span></code></a>
attributes.</p>
</div>
<div class="admonition seealso">
<p class="first admonition-title">See also</p>
<ul class="last simple">
<li>The <a class="reference external" href="http://code.activestate.com/recipes/579000/">linspace recipe</a>
shows how to implement a lazy version of range that suitable for floating
point applications.</li>
</ul>
</div>
</div>
</div>
<div class="section" id="text-sequence-type-str">
<span id="textseq"></span><span id="index-27"></span><h2>4.7. Text Sequence Type &#8212; <a class="reference internal" href="#str" title="str"><code class="xref py py-class docutils literal"><span class="pre">str</span></code></a><a class="headerlink" href="#text-sequence-type-str" title="Permalink to this headline">¶</a></h2>
<p>Textual data in Python is handled with <a class="reference internal" href="#str" title="str"><code class="xref py py-class docutils literal"><span class="pre">str</span></code></a> objects, or <em class="dfn">strings</em>.
Strings are immutable
<a class="reference internal" href="#typesseq"><span>sequences</span></a> of Unicode code points.  String literals are
written in a variety of ways:</p>
<ul class="simple">
<li>Single quotes: <code class="docutils literal"><span class="pre">'allows</span> <span class="pre">embedded</span> <span class="pre">&quot;double&quot;</span> <span class="pre">quotes'</span></code></li>
<li>Double quotes: <code class="docutils literal"><span class="pre">&quot;allows</span> <span class="pre">embedded</span> <span class="pre">'single'</span> <span class="pre">quotes&quot;</span></code>.</li>
<li>Triple quoted: <code class="docutils literal"><span class="pre">'''Three</span> <span class="pre">single</span> <span class="pre">quotes'''</span></code>, <code class="docutils literal"><span class="pre">&quot;&quot;&quot;Three</span> <span class="pre">double</span> <span class="pre">quotes&quot;&quot;&quot;</span></code></li>
</ul>
<p>Triple quoted strings may span multiple lines - all associated whitespace will
be included in the string literal.</p>
<p>String literals that are part of a single expression and have only whitespace
between them will be implicitly converted to a single string literal. That
is, <code class="docutils literal"><span class="pre">(&quot;spam</span> <span class="pre">&quot;</span> <span class="pre">&quot;eggs&quot;)</span> <span class="pre">==</span> <span class="pre">&quot;spam</span> <span class="pre">eggs&quot;</span></code>.</p>
<p>See <a class="reference internal" href="../reference/lexical_analysis.html#strings"><span>String and Bytes literals</span></a> for more about the various forms of string literal,
including supported escape sequences, and the <code class="docutils literal"><span class="pre">r</span></code> (&#8220;raw&#8221;) prefix that
disables most escape sequence processing.</p>
<p>Strings may also be created from other objects using the <a class="reference internal" href="#str" title="str"><code class="xref py py-class docutils literal"><span class="pre">str</span></code></a>
constructor.</p>
<p>Since there is no separate &#8220;character&#8221; type, indexing a string produces
strings of length 1. That is, for a non-empty string <em>s</em>, <code class="docutils literal"><span class="pre">s[0]</span> <span class="pre">==</span> <span class="pre">s[0:1]</span></code>.</p>
<p id="index-28">There is also no mutable string type, but <a class="reference internal" href="#str.join" title="str.join"><code class="xref py py-meth docutils literal"><span class="pre">str.join()</span></code></a> or
<a class="reference internal" href="io.html#io.StringIO" title="io.StringIO"><code class="xref py py-class docutils literal"><span class="pre">io.StringIO</span></code></a> can be used to efficiently construct strings from
multiple fragments.</p>
<div class="versionchanged">
<p><span class="versionmodified">Changed in version 3.3: </span>For backwards compatibility with the Python 2 series, the <code class="docutils literal"><span class="pre">u</span></code> prefix is
once again permitted on string literals. It has no effect on the meaning
of string literals and cannot be combined with the <code class="docutils literal"><span class="pre">r</span></code> prefix.</p>
</div>
<span class="target" id="index-29"></span><dl class="class">
<dt id="str">
<em class="property">class </em><code class="descname">str</code><span class="sig-paren">(</span><em>object=''</em><span class="sig-paren">)</span><a class="headerlink" href="#str" title="Permalink to this definition">¶</a></dt>
<dt>
<em class="property">class </em><code class="descname">str</code><span class="sig-paren">(</span><em>object=b''</em>, <em>encoding='utf-8'</em>, <em>errors='strict'</em><span class="sig-paren">)</span></dt>
<dd><p>Return a <a class="reference internal" href="#textseq"><span>string</span></a> version of <em>object</em>.  If <em>object</em> is not
provided, returns the empty string.  Otherwise, the behavior of <code class="docutils literal"><span class="pre">str()</span></code>
depends on whether <em>encoding</em> or <em>errors</em> is given, as follows.</p>
<p>If neither <em>encoding</em> nor <em>errors</em> is given, <code class="docutils literal"><span class="pre">str(object)</span></code> returns
<a class="reference internal" href="../reference/datamodel.html#object.__str__" title="object.__str__"><code class="xref py py-meth docutils literal"><span class="pre">object.__str__()</span></code></a>, which is the &#8220;informal&#8221; or nicely
printable string representation of <em>object</em>.  For string objects, this is
the string itself.  If <em>object</em> does not have a <a class="reference internal" href="../reference/datamodel.html#object.__str__" title="object.__str__"><code class="xref py py-meth docutils literal"><span class="pre">__str__()</span></code></a>
method, then <a class="reference internal" href="#str" title="str"><code class="xref py py-func docutils literal"><span class="pre">str()</span></code></a> falls back to returning
<a class="reference internal" href="functions.html#repr" title="repr"><code class="xref py py-meth docutils literal"><span class="pre">repr(object)</span></code></a>.</p>
<p id="index-30">If at least one of <em>encoding</em> or <em>errors</em> is given, <em>object</em> should be a
<a class="reference internal" href="../glossary.html#term-bytes-like-object"><span class="xref std std-term">bytes-like object</span></a> (e.g. <a class="reference internal" href="functions.html#bytes" title="bytes"><code class="xref py py-class docutils literal"><span class="pre">bytes</span></code></a> or <a class="reference internal" href="functions.html#bytearray" title="bytearray"><code class="xref py py-class docutils literal"><span class="pre">bytearray</span></code></a>).  In
this case, if <em>object</em> is a <a class="reference internal" href="functions.html#bytes" title="bytes"><code class="xref py py-class docutils literal"><span class="pre">bytes</span></code></a> (or <a class="reference internal" href="functions.html#bytearray" title="bytearray"><code class="xref py py-class docutils literal"><span class="pre">bytearray</span></code></a>) object,
then <code class="docutils literal"><span class="pre">str(bytes,</span> <span class="pre">encoding,</span> <span class="pre">errors)</span></code> is equivalent to
<a class="reference internal" href="#bytes.decode" title="bytes.decode"><code class="xref py py-meth docutils literal"><span class="pre">bytes.decode(encoding,</span> <span class="pre">errors)</span></code></a>.  Otherwise, the bytes
object underlying the buffer object is obtained before calling
<a class="reference internal" href="#bytes.decode" title="bytes.decode"><code class="xref py py-meth docutils literal"><span class="pre">bytes.decode()</span></code></a>.  See <a class="reference internal" href="#binaryseq"><span>Binary Sequence Types &#8212; bytes, bytearray, memoryview</span></a> and
<a class="reference internal" href="../c-api/buffer.html#bufferobjects"><span>Buffer Protocol</span></a> for information on buffer objects.</p>
<p>Passing a <a class="reference internal" href="functions.html#bytes" title="bytes"><code class="xref py py-class docutils literal"><span class="pre">bytes</span></code></a> object to <a class="reference internal" href="#str" title="str"><code class="xref py py-func docutils literal"><span class="pre">str()</span></code></a> without the <em>encoding</em>
or <em>errors</em> arguments falls under the first case of returning the informal
string representation (see also the <a class="reference internal" href="../using/cmdline.html#cmdoption-b"><code class="xref std std-option docutils literal"><span class="pre">-b</span></code></a> command-line option to
Python).  For example:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="nb">str</span><span class="p">(</span><span class="n">b</span><span class="s1">&#39;Zoot!&#39;</span><span class="p">)</span>
<span class="go">&quot;b&#39;Zoot!&#39;&quot;</span>
</pre></div>
</div>
<p>For more information on the <code class="docutils literal"><span class="pre">str</span></code> class and its methods, see
<a class="reference internal" href="#textseq"><span>Text Sequence Type &#8212; str</span></a> and the <a class="reference internal" href="#string-methods"><span>String Methods</span></a> section below.  To output
formatted strings, see the <a class="reference internal" href="../reference/lexical_analysis.html#f-strings"><span>Formatted string literals</span></a> and <a class="reference internal" href="string.html#formatstrings"><span>Format String Syntax</span></a>
sections.  In addition, see the <a class="reference internal" href="text.html#stringservices"><span>Text Processing Services</span></a> section.</p>
</dd></dl>

<div class="section" id="string-methods">
<span id="index-31"></span><span id="id4"></span><h3>4.7.1. String Methods<a class="headerlink" href="#string-methods" title="Permalink to this headline">¶</a></h3>
<p id="index-32">Strings implement all of the <a class="reference internal" href="#typesseq-common"><span>common</span></a> sequence
operations, along with the additional methods described below.</p>
<p>Strings also support two styles of string formatting, one providing a large
degree of flexibility and customization (see <a class="reference internal" href="#str.format" title="str.format"><code class="xref py py-meth docutils literal"><span class="pre">str.format()</span></code></a>,
<a class="reference internal" href="string.html#formatstrings"><span>Format String Syntax</span></a> and <a class="reference internal" href="string.html#string-formatting"><span>Custom String Formatting</span></a>) and the other based on C
<code class="docutils literal"><span class="pre">printf</span></code> style formatting that handles a narrower range of types and is
slightly harder to use correctly, but is often faster for the cases it can
handle (<a class="reference internal" href="#old-string-formatting"><span>printf-style String Formatting</span></a>).</p>
<p>The <a class="reference internal" href="text.html#textservices"><span>Text Processing Services</span></a> section of the standard library covers a number of
other modules that provide various text related utilities (including regular
expression support in the <a class="reference internal" href="re.html#module-re" title="re: Regular expression operations."><code class="xref py py-mod docutils literal"><span class="pre">re</span></code></a> module).</p>
<dl class="method">
<dt id="str.capitalize">
<code class="descclassname">str.</code><code class="descname">capitalize</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#str.capitalize" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a copy of the string with its first character capitalized and the
rest lowercased.</p>
</dd></dl>

<dl class="method">
<dt id="str.casefold">
<code class="descclassname">str.</code><code class="descname">casefold</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#str.casefold" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a casefolded copy of the string. Casefolded strings may be used for
caseless matching.</p>
<p>Casefolding is similar to lowercasing but more aggressive because it is
intended to remove all case distinctions in a string. For example, the German
lowercase letter <code class="docutils literal"><span class="pre">'ß'</span></code> is equivalent to <code class="docutils literal"><span class="pre">&quot;ss&quot;</span></code>. Since it is already
lowercase, <a class="reference internal" href="#str.lower" title="str.lower"><code class="xref py py-meth docutils literal"><span class="pre">lower()</span></code></a> would do nothing to <code class="docutils literal"><span class="pre">'ß'</span></code>; <a class="reference internal" href="#str.casefold" title="str.casefold"><code class="xref py py-meth docutils literal"><span class="pre">casefold()</span></code></a>
converts it to <code class="docutils literal"><span class="pre">&quot;ss&quot;</span></code>.</p>
<p>The casefolding algorithm is described in section 3.13 of the Unicode
Standard.</p>
<div class="versionadded">
<p><span class="versionmodified">New in version 3.3.</span></p>
</div>
</dd></dl>

<dl class="method">
<dt id="str.center">
<code class="descclassname">str.</code><code class="descname">center</code><span class="sig-paren">(</span><em>width</em><span class="optional">[</span>, <em>fillchar</em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#str.center" title="Permalink to this definition">¶</a></dt>
<dd><p>Return centered in a string of length <em>width</em>. Padding is done using the
specified <em>fillchar</em> (default is an ASCII space). The original string is
returned if <em>width</em> is less than or equal to <code class="docutils literal"><span class="pre">len(s)</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="str.count">
<code class="descclassname">str.</code><code class="descname">count</code><span class="sig-paren">(</span><em>sub</em><span class="optional">[</span>, <em>start</em><span class="optional">[</span>, <em>end</em><span class="optional">]</span><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#str.count" title="Permalink to this definition">¶</a></dt>
<dd><p>Return the number of non-overlapping occurrences of substring <em>sub</em> in the
range [<em>start</em>, <em>end</em>].  Optional arguments <em>start</em> and <em>end</em> are
interpreted as in slice notation.</p>
</dd></dl>

<dl class="method">
<dt id="str.encode">
<code class="descclassname">str.</code><code class="descname">encode</code><span class="sig-paren">(</span><em>encoding=&quot;utf-8&quot;</em>, <em>errors=&quot;strict&quot;</em><span class="sig-paren">)</span><a class="headerlink" href="#str.encode" title="Permalink to this definition">¶</a></dt>
<dd><p>Return an encoded version of the string as a bytes object. Default encoding
is <code class="docutils literal"><span class="pre">'utf-8'</span></code>. <em>errors</em> may be given to set a different error handling scheme.
The default for <em>errors</em> is <code class="docutils literal"><span class="pre">'strict'</span></code>, meaning that encoding errors raise
a <a class="reference internal" href="exceptions.html#UnicodeError" title="UnicodeError"><code class="xref py py-exc docutils literal"><span class="pre">UnicodeError</span></code></a>. Other possible
values are <code class="docutils literal"><span class="pre">'ignore'</span></code>, <code class="docutils literal"><span class="pre">'replace'</span></code>, <code class="docutils literal"><span class="pre">'xmlcharrefreplace'</span></code>,
<code class="docutils literal"><span class="pre">'backslashreplace'</span></code> and any other name registered via
<a class="reference internal" href="codecs.html#codecs.register_error" title="codecs.register_error"><code class="xref py py-func docutils literal"><span class="pre">codecs.register_error()</span></code></a>, see section <a class="reference internal" href="codecs.html#error-handlers"><span>Error Handlers</span></a>. For a
list of possible encodings, see section <a class="reference internal" href="codecs.html#standard-encodings"><span>Standard Encodings</span></a>.</p>
<div class="versionchanged">
<p><span class="versionmodified">Changed in version 3.1: </span>Support for keyword arguments added.</p>
</div>
</dd></dl>

<dl class="method">
<dt id="str.endswith">
<code class="descclassname">str.</code><code class="descname">endswith</code><span class="sig-paren">(</span><em>suffix</em><span class="optional">[</span>, <em>start</em><span class="optional">[</span>, <em>end</em><span class="optional">]</span><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#str.endswith" title="Permalink to this definition">¶</a></dt>
<dd><p>Return <code class="docutils literal"><span class="pre">True</span></code> if the string ends with the specified <em>suffix</em>, otherwise return
<code class="docutils literal"><span class="pre">False</span></code>.  <em>suffix</em> can also be a tuple of suffixes to look for.  With optional
<em>start</em>, test beginning at that position.  With optional <em>end</em>, stop comparing
at that position.</p>
</dd></dl>

<dl class="method">
<dt id="str.expandtabs">
<code class="descclassname">str.</code><code class="descname">expandtabs</code><span class="sig-paren">(</span><em>tabsize=8</em><span class="sig-paren">)</span><a class="headerlink" href="#str.expandtabs" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a copy of the string where all tab characters are replaced by one or
more spaces, depending on the current column and the given tab size.  Tab
positions occur every <em>tabsize</em> characters (default is 8, giving tab
positions at columns 0, 8, 16 and so on).  To expand the string, the current
column is set to zero and the string is examined character by character.  If
the character is a tab (<code class="docutils literal"><span class="pre">\t</span></code>), one or more space characters are inserted
in the result until the current column is equal to the next tab position.
(The tab character itself is not copied.)  If the character is a newline
(<code class="docutils literal"><span class="pre">\n</span></code>) or return (<code class="docutils literal"><span class="pre">\r</span></code>), it is copied and the current column is reset to
zero.  Any other character is copied unchanged and the current column is
incremented by one regardless of how the character is represented when
printed.</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s1">&#39;01</span><span class="se">\t</span><span class="s1">012</span><span class="se">\t</span><span class="s1">0123</span><span class="se">\t</span><span class="s1">01234&#39;</span><span class="o">.</span><span class="n">expandtabs</span><span class="p">()</span>
<span class="go">&#39;01      012     0123    01234&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s1">&#39;01</span><span class="se">\t</span><span class="s1">012</span><span class="se">\t</span><span class="s1">0123</span><span class="se">\t</span><span class="s1">01234&#39;</span><span class="o">.</span><span class="n">expandtabs</span><span class="p">(</span><span class="mi">4</span><span class="p">)</span>
<span class="go">&#39;01  012 0123    01234&#39;</span>
</pre></div>
</div>
</dd></dl>

<dl class="method">
<dt id="str.find">
<code class="descclassname">str.</code><code class="descname">find</code><span class="sig-paren">(</span><em>sub</em><span class="optional">[</span>, <em>start</em><span class="optional">[</span>, <em>end</em><span class="optional">]</span><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#str.find" title="Permalink to this definition">¶</a></dt>
<dd><p>Return the lowest index in the string where substring <em>sub</em> is found within
the slice <code class="docutils literal"><span class="pre">s[start:end]</span></code>.  Optional arguments <em>start</em> and <em>end</em> are
interpreted as in slice notation.  Return <code class="docutils literal"><span class="pre">-1</span></code> if <em>sub</em> is not found.</p>
<div class="admonition note">
<p class="first admonition-title">Note</p>
<p>The <a class="reference internal" href="#str.find" title="str.find"><code class="xref py py-meth docutils literal"><span class="pre">find()</span></code></a> method should be used only if you need to know the
position of <em>sub</em>.  To check if <em>sub</em> is a substring or not, use the
<a class="reference internal" href="../reference/expressions.html#in"><code class="xref std std-keyword docutils literal"><span class="pre">in</span></code></a> operator:</p>
<div class="last highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s1">&#39;Py&#39;</span> <span class="ow">in</span> <span class="s1">&#39;Python&#39;</span>
<span class="go">True</span>
</pre></div>
</div>
</div>
</dd></dl>

<dl class="method">
<dt id="str.format">
<code class="descclassname">str.</code><code class="descname">format</code><span class="sig-paren">(</span><em>*args</em>, <em>**kwargs</em><span class="sig-paren">)</span><a class="headerlink" href="#str.format" title="Permalink to this definition">¶</a></dt>
<dd><p>Perform a string formatting operation.  The string on which this method is
called can contain literal text or replacement fields delimited by braces
<code class="docutils literal"><span class="pre">{}</span></code>.  Each replacement field contains either the numeric index of a
positional argument, or the name of a keyword argument.  Returns a copy of
the string where each replacement field is replaced with the string value of
the corresponding argument.</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s2">&quot;The sum of 1 + 2 is </span><span class="si">{0}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="mi">1</span><span class="o">+</span><span class="mi">2</span><span class="p">)</span>
<span class="go">&#39;The sum of 1 + 2 is 3&#39;</span>
</pre></div>
</div>
<p>See <a class="reference internal" href="string.html#formatstrings"><span>Format String Syntax</span></a> for a description of the various formatting options
that can be specified in format strings.</p>
</dd></dl>

<dl class="method">
<dt id="str.format_map">
<code class="descclassname">str.</code><code class="descname">format_map</code><span class="sig-paren">(</span><em>mapping</em><span class="sig-paren">)</span><a class="headerlink" href="#str.format_map" title="Permalink to this definition">¶</a></dt>
<dd><p>Similar to <code class="docutils literal"><span class="pre">str.format(**mapping)</span></code>, except that <code class="docutils literal"><span class="pre">mapping</span></code> is
used directly and not copied to a <a class="reference internal" href="#dict" title="dict"><code class="xref py py-class docutils literal"><span class="pre">dict</span></code></a>.  This is useful
if for example <code class="docutils literal"><span class="pre">mapping</span></code> is a dict subclass:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="k">class</span> <span class="nc">Default</span><span class="p">(</span><span class="nb">dict</span><span class="p">):</span>
<span class="gp">... </span>    <span class="k">def</span> <span class="nf">__missing__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">):</span>
<span class="gp">... </span>        <span class="k">return</span> <span class="n">key</span>
<span class="gp">...</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s1">&#39;</span><span class="si">{name}</span><span class="s1"> was born in </span><span class="si">{country}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">format_map</span><span class="p">(</span><span class="n">Default</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s1">&#39;Guido&#39;</span><span class="p">))</span>
<span class="go">&#39;Guido was born in country&#39;</span>
</pre></div>
</div>
<div class="versionadded">
<p><span class="versionmodified">New in version 3.2.</span></p>
</div>
</dd></dl>

<dl class="method">
<dt id="str.index">
<code class="descclassname">str.</code><code class="descname">index</code><span class="sig-paren">(</span><em>sub</em><span class="optional">[</span>, <em>start</em><span class="optional">[</span>, <em>end</em><span class="optional">]</span><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#str.index" title="Permalink to this definition">¶</a></dt>
<dd><p>Like <a class="reference internal" href="#str.find" title="str.find"><code class="xref py py-meth docutils literal"><span class="pre">find()</span></code></a>, but raise <a class="reference internal" href="exceptions.html#ValueError" title="ValueError"><code class="xref py py-exc docutils literal"><span class="pre">ValueError</span></code></a> when the substring is
not found.</p>
</dd></dl>

<dl class="method">
<dt id="str.isalnum">
<code class="descclassname">str.</code><code class="descname">isalnum</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#str.isalnum" title="Permalink to this definition">¶</a></dt>
<dd><p>Return true if all characters in the string are alphanumeric and there is at
least one character, false otherwise.  A character <code class="docutils literal"><span class="pre">c</span></code> is alphanumeric if one
of the following returns <code class="docutils literal"><span class="pre">True</span></code>: <code class="docutils literal"><span class="pre">c.isalpha()</span></code>, <code class="docutils literal"><span class="pre">c.isdecimal()</span></code>,
<code class="docutils literal"><span class="pre">c.isdigit()</span></code>, or <code class="docutils literal"><span class="pre">c.isnumeric()</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="str.isalpha">
<code class="descclassname">str.</code><code class="descname">isalpha</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#str.isalpha" title="Permalink to this definition">¶</a></dt>
<dd><p>Return true if all characters in the string are alphabetic and there is at least
one character, false otherwise.  Alphabetic characters are those characters defined
in the Unicode character database as &#8220;Letter&#8221;, i.e., those with general category
property being one of &#8220;Lm&#8221;, &#8220;Lt&#8221;, &#8220;Lu&#8221;, &#8220;Ll&#8221;, or &#8220;Lo&#8221;.  Note that this is different
from the &#8220;Alphabetic&#8221; property defined in the Unicode Standard.</p>
</dd></dl>

<dl class="method">
<dt id="str.isdecimal">
<code class="descclassname">str.</code><code class="descname">isdecimal</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#str.isdecimal" title="Permalink to this definition">¶</a></dt>
<dd><p>Return true if all characters in the string are decimal
characters and there is at least one character, false
otherwise. Decimal characters are those that can be used to form
numbers in base 10, e.g. U+0660, ARABIC-INDIC DIGIT
ZERO.  Formally a decimal character is a character in the Unicode
General Category &#8220;Nd&#8221;.</p>
</dd></dl>

<dl class="method">
<dt id="str.isdigit">
<code class="descclassname">str.</code><code class="descname">isdigit</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#str.isdigit" title="Permalink to this definition">¶</a></dt>
<dd><p>Return true if all characters in the string are digits and there is at least one
character, false otherwise.  Digits include decimal characters and digits that need
special handling, such as the compatibility superscript digits.
This covers digits which cannot be used to form numbers in base 10,
like the Kharosthi numbers.  Formally, a digit is a character that has the
property value Numeric_Type=Digit or Numeric_Type=Decimal.</p>
</dd></dl>

<dl class="method">
<dt id="str.isidentifier">
<code class="descclassname">str.</code><code class="descname">isidentifier</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#str.isidentifier" title="Permalink to this definition">¶</a></dt>
<dd><p>Return true if the string is a valid identifier according to the language
definition, section <a class="reference internal" href="../reference/lexical_analysis.html#identifiers"><span>Identifiers and keywords</span></a>.</p>
<p>Use <a class="reference internal" href="keyword.html#keyword.iskeyword" title="keyword.iskeyword"><code class="xref py py-func docutils literal"><span class="pre">keyword.iskeyword()</span></code></a> to test for reserved identifiers such as
<a class="reference internal" href="../reference/compound_stmts.html#def"><code class="xref std std-keyword docutils literal"><span class="pre">def</span></code></a> and <a class="reference internal" href="../reference/compound_stmts.html#class"><code class="xref std std-keyword docutils literal"><span class="pre">class</span></code></a>.</p>
</dd></dl>

<dl class="method">
<dt id="str.islower">
<code class="descclassname">str.</code><code class="descname">islower</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#str.islower" title="Permalink to this definition">¶</a></dt>
<dd><p>Return true if all cased characters <a class="footnote-reference" href="#id14" id="id5">[4]</a> in the string are lowercase and
there is at least one cased character, false otherwise.</p>
</dd></dl>

<dl class="method">
<dt id="str.isnumeric">
<code class="descclassname">str.</code><code class="descname">isnumeric</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#str.isnumeric" title="Permalink to this definition">¶</a></dt>
<dd><p>Return true if all characters in the string are numeric
characters, and there is at least one character, false
otherwise. Numeric characters include digit characters, and all characters
that have the Unicode numeric value property, e.g. U+2155,
VULGAR FRACTION ONE FIFTH.  Formally, numeric characters are those with the property
value Numeric_Type=Digit, Numeric_Type=Decimal or Numeric_Type=Numeric.</p>
</dd></dl>

<dl class="method">
<dt id="str.isprintable">
<code class="descclassname">str.</code><code class="descname">isprintable</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#str.isprintable" title="Permalink to this definition">¶</a></dt>
<dd><p>Return true if all characters in the string are printable or the string is
empty, false otherwise.  Nonprintable characters are those characters defined
in the Unicode character database as &#8220;Other&#8221; or &#8220;Separator&#8221;, excepting the
ASCII space (0x20) which is considered printable.  (Note that printable
characters in this context are those which should not be escaped when
<a class="reference internal" href="functions.html#repr" title="repr"><code class="xref py py-func docutils literal"><span class="pre">repr()</span></code></a> is invoked on a string.  It has no bearing on the handling of
strings written to <a class="reference internal" href="sys.html#sys.stdout" title="sys.stdout"><code class="xref py py-data docutils literal"><span class="pre">sys.stdout</span></code></a> or <a class="reference internal" href="sys.html#sys.stderr" title="sys.stderr"><code class="xref py py-data docutils literal"><span class="pre">sys.stderr</span></code></a>.)</p>
</dd></dl>

<dl class="method">
<dt id="str.isspace">
<code class="descclassname">str.</code><code class="descname">isspace</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#str.isspace" title="Permalink to this definition">¶</a></dt>
<dd><p>Return true if there are only whitespace characters in the string and there is
at least one character, false otherwise.  Whitespace characters  are those
characters defined in the Unicode character database as &#8220;Other&#8221; or &#8220;Separator&#8221;
and those with bidirectional property being one of &#8220;WS&#8221;, &#8220;B&#8221;, or &#8220;S&#8221;.</p>
</dd></dl>

<dl class="method">
<dt id="str.istitle">
<code class="descclassname">str.</code><code class="descname">istitle</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#str.istitle" title="Permalink to this definition">¶</a></dt>
<dd><p>Return true if the string is a titlecased string and there is at least one
character, for example uppercase characters may only follow uncased characters
and lowercase characters only cased ones.  Return false otherwise.</p>
</dd></dl>

<dl class="method">
<dt id="str.isupper">
<code class="descclassname">str.</code><code class="descname">isupper</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#str.isupper" title="Permalink to this definition">¶</a></dt>
<dd><p>Return true if all cased characters <a class="footnote-reference" href="#id14" id="id6">[4]</a> in the string are uppercase and
there is at least one cased character, false otherwise.</p>
</dd></dl>

<dl class="method">
<dt id="str.join">
<code class="descclassname">str.</code><code class="descname">join</code><span class="sig-paren">(</span><em>iterable</em><span class="sig-paren">)</span><a class="headerlink" href="#str.join" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a string which is the concatenation of the strings in the
<a class="reference internal" href="../glossary.html#term-iterable"><span class="xref std std-term">iterable</span></a> <em>iterable</em>.  A <a class="reference internal" href="exceptions.html#TypeError" title="TypeError"><code class="xref py py-exc docutils literal"><span class="pre">TypeError</span></code></a> will be raised if there are
any non-string values in <em>iterable</em>, including <a class="reference internal" href="functions.html#bytes" title="bytes"><code class="xref py py-class docutils literal"><span class="pre">bytes</span></code></a> objects.  The
separator between elements is the string providing this method.</p>
</dd></dl>

<dl class="method">
<dt id="str.ljust">
<code class="descclassname">str.</code><code class="descname">ljust</code><span class="sig-paren">(</span><em>width</em><span class="optional">[</span>, <em>fillchar</em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#str.ljust" title="Permalink to this definition">¶</a></dt>
<dd><p>Return the string left justified in a string of length <em>width</em>. Padding is
done using the specified <em>fillchar</em> (default is an ASCII space). The
original string is returned if <em>width</em> is less than or equal to <code class="docutils literal"><span class="pre">len(s)</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="str.lower">
<code class="descclassname">str.</code><code class="descname">lower</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#str.lower" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a copy of the string with all the cased characters <a class="footnote-reference" href="#id14" id="id7">[4]</a> converted to
lowercase.</p>
<p>The lowercasing algorithm used is described in section 3.13 of the Unicode
Standard.</p>
</dd></dl>

<dl class="method">
<dt id="str.lstrip">
<code class="descclassname">str.</code><code class="descname">lstrip</code><span class="sig-paren">(</span><span class="optional">[</span><em>chars</em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#str.lstrip" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a copy of the string with leading characters removed.  The <em>chars</em>
argument is a string specifying the set of characters to be removed.  If omitted
or <code class="docutils literal"><span class="pre">None</span></code>, the <em>chars</em> argument defaults to removing whitespace.  The <em>chars</em>
argument is not a prefix; rather, all combinations of its values are stripped:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s1">&#39;   spacious   &#39;</span><span class="o">.</span><span class="n">lstrip</span><span class="p">()</span>
<span class="go">&#39;spacious   &#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s1">&#39;www.example.com&#39;</span><span class="o">.</span><span class="n">lstrip</span><span class="p">(</span><span class="s1">&#39;cmowz.&#39;</span><span class="p">)</span>
<span class="go">&#39;example.com&#39;</span>
</pre></div>
</div>
</dd></dl>

<dl class="staticmethod">
<dt id="str.maketrans">
<em class="property">static </em><code class="descclassname">str.</code><code class="descname">maketrans</code><span class="sig-paren">(</span><em>x</em><span class="optional">[</span>, <em>y</em><span class="optional">[</span>, <em>z</em><span class="optional">]</span><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#str.maketrans" title="Permalink to this definition">¶</a></dt>
<dd><p>This static method returns a translation table usable for <a class="reference internal" href="#str.translate" title="str.translate"><code class="xref py py-meth docutils literal"><span class="pre">str.translate()</span></code></a>.</p>
<p>If there is only one argument, it must be a dictionary mapping Unicode
ordinals (integers) or characters (strings of length 1) to Unicode ordinals,
strings (of arbitrary lengths) or <code class="docutils literal"><span class="pre">None</span></code>.  Character keys will then be
converted to ordinals.</p>
<p>If there are two arguments, they must be strings of equal length, and in the
resulting dictionary, each character in x will be mapped to the character at
the same position in y.  If there is a third argument, it must be a string,
whose characters will be mapped to <code class="docutils literal"><span class="pre">None</span></code> in the result.</p>
</dd></dl>

<dl class="method">
<dt id="str.partition">
<code class="descclassname">str.</code><code class="descname">partition</code><span class="sig-paren">(</span><em>sep</em><span class="sig-paren">)</span><a class="headerlink" href="#str.partition" title="Permalink to this definition">¶</a></dt>
<dd><p>Split the string at the first occurrence of <em>sep</em>, and return a 3-tuple
containing the part before the separator, the separator itself, and the part
after the separator.  If the separator is not found, return a 3-tuple containing
the string itself, followed by two empty strings.</p>
</dd></dl>

<dl class="method">
<dt id="str.replace">
<code class="descclassname">str.</code><code class="descname">replace</code><span class="sig-paren">(</span><em>old</em>, <em>new</em><span class="optional">[</span>, <em>count</em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#str.replace" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a copy of the string with all occurrences of substring <em>old</em> replaced by
<em>new</em>.  If the optional argument <em>count</em> is given, only the first <em>count</em>
occurrences are replaced.</p>
</dd></dl>

<dl class="method">
<dt id="str.rfind">
<code class="descclassname">str.</code><code class="descname">rfind</code><span class="sig-paren">(</span><em>sub</em><span class="optional">[</span>, <em>start</em><span class="optional">[</span>, <em>end</em><span class="optional">]</span><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#str.rfind" title="Permalink to this definition">¶</a></dt>
<dd><p>Return the highest index in the string where substring <em>sub</em> is found, such
that <em>sub</em> is contained within <code class="docutils literal"><span class="pre">s[start:end]</span></code>.  Optional arguments <em>start</em>
and <em>end</em> are interpreted as in slice notation.  Return <code class="docutils literal"><span class="pre">-1</span></code> on failure.</p>
</dd></dl>

<dl class="method">
<dt id="str.rindex">
<code class="descclassname">str.</code><code class="descname">rindex</code><span class="sig-paren">(</span><em>sub</em><span class="optional">[</span>, <em>start</em><span class="optional">[</span>, <em>end</em><span class="optional">]</span><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#str.rindex" title="Permalink to this definition">¶</a></dt>
<dd><p>Like <a class="reference internal" href="#str.rfind" title="str.rfind"><code class="xref py py-meth docutils literal"><span class="pre">rfind()</span></code></a> but raises <a class="reference internal" href="exceptions.html#ValueError" title="ValueError"><code class="xref py py-exc docutils literal"><span class="pre">ValueError</span></code></a> when the substring <em>sub</em> is not
found.</p>
</dd></dl>

<dl class="method">
<dt id="str.rjust">
<code class="descclassname">str.</code><code class="descname">rjust</code><span class="sig-paren">(</span><em>width</em><span class="optional">[</span>, <em>fillchar</em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#str.rjust" title="Permalink to this definition">¶</a></dt>
<dd><p>Return the string right justified in a string of length <em>width</em>. Padding is
done using the specified <em>fillchar</em> (default is an ASCII space). The
original string is returned if <em>width</em> is less than or equal to <code class="docutils literal"><span class="pre">len(s)</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="str.rpartition">
<code class="descclassname">str.</code><code class="descname">rpartition</code><span class="sig-paren">(</span><em>sep</em><span class="sig-paren">)</span><a class="headerlink" href="#str.rpartition" title="Permalink to this definition">¶</a></dt>
<dd><p>Split the string at the last occurrence of <em>sep</em>, and return a 3-tuple
containing the part before the separator, the separator itself, and the part
after the separator.  If the separator is not found, return a 3-tuple containing
two empty strings, followed by the string itself.</p>
</dd></dl>

<dl class="method">
<dt id="str.rsplit">
<code class="descclassname">str.</code><code class="descname">rsplit</code><span class="sig-paren">(</span><em>sep=None</em>, <em>maxsplit=-1</em><span class="sig-paren">)</span><a class="headerlink" href="#str.rsplit" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a list of the words in the string, using <em>sep</em> as the delimiter string.
If <em>maxsplit</em> is given, at most <em>maxsplit</em> splits are done, the <em>rightmost</em>
ones.  If <em>sep</em> is not specified or <code class="docutils literal"><span class="pre">None</span></code>, any whitespace string is a
separator.  Except for splitting from the right, <a class="reference internal" href="#str.rsplit" title="str.rsplit"><code class="xref py py-meth docutils literal"><span class="pre">rsplit()</span></code></a> behaves like
<a class="reference internal" href="#str.split" title="str.split"><code class="xref py py-meth docutils literal"><span class="pre">split()</span></code></a> which is described in detail below.</p>
</dd></dl>

<dl class="method">
<dt id="str.rstrip">
<code class="descclassname">str.</code><code class="descname">rstrip</code><span class="sig-paren">(</span><span class="optional">[</span><em>chars</em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#str.rstrip" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a copy of the string with trailing characters removed.  The <em>chars</em>
argument is a string specifying the set of characters to be removed.  If omitted
or <code class="docutils literal"><span class="pre">None</span></code>, the <em>chars</em> argument defaults to removing whitespace.  The <em>chars</em>
argument is not a suffix; rather, all combinations of its values are stripped:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s1">&#39;   spacious   &#39;</span><span class="o">.</span><span class="n">rstrip</span><span class="p">()</span>
<span class="go">&#39;   spacious&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s1">&#39;mississippi&#39;</span><span class="o">.</span><span class="n">rstrip</span><span class="p">(</span><span class="s1">&#39;ipz&#39;</span><span class="p">)</span>
<span class="go">&#39;mississ&#39;</span>
</pre></div>
</div>
</dd></dl>

<dl class="method">
<dt id="str.split">
<code class="descclassname">str.</code><code class="descname">split</code><span class="sig-paren">(</span><em>sep=None</em>, <em>maxsplit=-1</em><span class="sig-paren">)</span><a class="headerlink" href="#str.split" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a list of the words in the string, using <em>sep</em> as the delimiter
string.  If <em>maxsplit</em> is given, at most <em>maxsplit</em> splits are done (thus,
the list will have at most <code class="docutils literal"><span class="pre">maxsplit+1</span></code> elements).  If <em>maxsplit</em> is not
specified or <code class="docutils literal"><span class="pre">-1</span></code>, then there is no limit on the number of splits
(all possible splits are made).</p>
<p>If <em>sep</em> is given, consecutive delimiters are not grouped together and are
deemed to delimit empty strings (for example, <code class="docutils literal"><span class="pre">'1,,2'.split(',')</span></code> returns
<code class="docutils literal"><span class="pre">['1',</span> <span class="pre">'',</span> <span class="pre">'2']</span></code>).  The <em>sep</em> argument may consist of multiple characters
(for example, <code class="docutils literal"><span class="pre">'1&lt;&gt;2&lt;&gt;3'.split('&lt;&gt;')</span></code> returns <code class="docutils literal"><span class="pre">['1',</span> <span class="pre">'2',</span> <span class="pre">'3']</span></code>).
Splitting an empty string with a specified separator returns <code class="docutils literal"><span class="pre">['']</span></code>.</p>
<p>For example:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s1">&#39;1,2,3&#39;</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">&#39;,&#39;</span><span class="p">)</span>
<span class="go">[&#39;1&#39;, &#39;2&#39;, &#39;3&#39;]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s1">&#39;1,2,3&#39;</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">&#39;,&#39;</span><span class="p">,</span> <span class="n">maxsplit</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="go">[&#39;1&#39;, &#39;2,3&#39;]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s1">&#39;1,2,,3,&#39;</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">&#39;,&#39;</span><span class="p">)</span>
<span class="go">[&#39;1&#39;, &#39;2&#39;, &#39;&#39;, &#39;3&#39;, &#39;&#39;]</span>
</pre></div>
</div>
<p>If <em>sep</em> is not specified or is <code class="docutils literal"><span class="pre">None</span></code>, a different splitting algorithm is
applied: runs of consecutive whitespace are regarded as a single separator,
and the result will contain no empty strings at the start or end if the
string has leading or trailing whitespace.  Consequently, splitting an empty
string or a string consisting of just whitespace with a <code class="docutils literal"><span class="pre">None</span></code> separator
returns <code class="docutils literal"><span class="pre">[]</span></code>.</p>
<p>For example:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s1">&#39;1 2 3&#39;</span><span class="o">.</span><span class="n">split</span><span class="p">()</span>
<span class="go">[&#39;1&#39;, &#39;2&#39;, &#39;3&#39;]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s1">&#39;1 2 3&#39;</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">maxsplit</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="go">[&#39;1&#39;, &#39;2 3&#39;]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s1">&#39;   1   2   3   &#39;</span><span class="o">.</span><span class="n">split</span><span class="p">()</span>
<span class="go">[&#39;1&#39;, &#39;2&#39;, &#39;3&#39;]</span>
</pre></div>
</div>
</dd></dl>

<span class="target" id="index-33"></span><dl class="method">
<dt id="str.splitlines">
<code class="descclassname">str.</code><code class="descname">splitlines</code><span class="sig-paren">(</span><span class="optional">[</span><em>keepends</em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#str.splitlines" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a list of the lines in the string, breaking at line boundaries.  Line
breaks are not included in the resulting list unless <em>keepends</em> is given and
true.</p>
<p>This method splits on the following line boundaries.  In particular, the
boundaries are a superset of <a class="reference internal" href="../glossary.html#term-universal-newlines"><span class="xref std std-term">universal newlines</span></a>.</p>
<table border="1" class="docutils">
<colgroup>
<col width="44%" />
<col width="56%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Representation</th>
<th class="head">Description</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><code class="docutils literal"><span class="pre">\n</span></code></td>
<td>Line Feed</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">\r</span></code></td>
<td>Carriage Return</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">\r\n</span></code></td>
<td>Carriage Return + Line Feed</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">\v</span></code> or <code class="docutils literal"><span class="pre">\x0b</span></code></td>
<td>Line Tabulation</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">\f</span></code> or <code class="docutils literal"><span class="pre">\x0c</span></code></td>
<td>Form Feed</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">\x1c</span></code></td>
<td>File Separator</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">\x1d</span></code></td>
<td>Group Separator</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">\x1e</span></code></td>
<td>Record Separator</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">\x85</span></code></td>
<td>Next Line (C1 Control Code)</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">\u2028</span></code></td>
<td>Line Separator</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">\u2029</span></code></td>
<td>Paragraph Separator</td>
</tr>
</tbody>
</table>
<div class="versionchanged">
<p><span class="versionmodified">Changed in version 3.2: </span><code class="docutils literal"><span class="pre">\v</span></code> and <code class="docutils literal"><span class="pre">\f</span></code> added to list of line boundaries.</p>
</div>
<p>For example:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s1">&#39;ab c</span><span class="se">\n\n</span><span class="s1">de fg</span><span class="se">\r</span><span class="s1">kl</span><span class="se">\r\n</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">splitlines</span><span class="p">()</span>
<span class="go">[&#39;ab c&#39;, &#39;&#39;, &#39;de fg&#39;, &#39;kl&#39;]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s1">&#39;ab c</span><span class="se">\n\n</span><span class="s1">de fg</span><span class="se">\r</span><span class="s1">kl</span><span class="se">\r\n</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">splitlines</span><span class="p">(</span><span class="n">keepends</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="go">[&#39;ab c\n&#39;, &#39;\n&#39;, &#39;de fg\r&#39;, &#39;kl\r\n&#39;]</span>
</pre></div>
</div>
<p>Unlike <a class="reference internal" href="#str.split" title="str.split"><code class="xref py py-meth docutils literal"><span class="pre">split()</span></code></a> when a delimiter string <em>sep</em> is given, this
method returns an empty list for the empty string, and a terminal line
break does not result in an extra line:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s2">&quot;&quot;</span><span class="o">.</span><span class="n">splitlines</span><span class="p">()</span>
<span class="go">[]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s2">&quot;One line</span><span class="se">\n</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">splitlines</span><span class="p">()</span>
<span class="go">[&#39;One line&#39;]</span>
</pre></div>
</div>
<p>For comparison, <code class="docutils literal"><span class="pre">split('\n')</span></code> gives:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s1">&#39;&#39;</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">&#39;</span><span class="se">\n</span><span class="s1">&#39;</span><span class="p">)</span>
<span class="go">[&#39;&#39;]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s1">&#39;Two lines</span><span class="se">\n</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">&#39;</span><span class="se">\n</span><span class="s1">&#39;</span><span class="p">)</span>
<span class="go">[&#39;Two lines&#39;, &#39;&#39;]</span>
</pre></div>
</div>
</dd></dl>

<dl class="method">
<dt id="str.startswith">
<code class="descclassname">str.</code><code class="descname">startswith</code><span class="sig-paren">(</span><em>prefix</em><span class="optional">[</span>, <em>start</em><span class="optional">[</span>, <em>end</em><span class="optional">]</span><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#str.startswith" title="Permalink to this definition">¶</a></dt>
<dd><p>Return <code class="docutils literal"><span class="pre">True</span></code> if string starts with the <em>prefix</em>, otherwise return <code class="docutils literal"><span class="pre">False</span></code>.
<em>prefix</em> can also be a tuple of prefixes to look for.  With optional <em>start</em>,
test string beginning at that position.  With optional <em>end</em>, stop comparing
string at that position.</p>
</dd></dl>

<dl class="method">
<dt id="str.strip">
<code class="descclassname">str.</code><code class="descname">strip</code><span class="sig-paren">(</span><span class="optional">[</span><em>chars</em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#str.strip" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a copy of the string with the leading and trailing characters removed.
The <em>chars</em> argument is a string specifying the set of characters to be removed.
If omitted or <code class="docutils literal"><span class="pre">None</span></code>, the <em>chars</em> argument defaults to removing whitespace.
The <em>chars</em> argument is not a prefix or suffix; rather, all combinations of its
values are stripped:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s1">&#39;   spacious   &#39;</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>
<span class="go">&#39;spacious&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s1">&#39;www.example.com&#39;</span><span class="o">.</span><span class="n">strip</span><span class="p">(</span><span class="s1">&#39;cmowz.&#39;</span><span class="p">)</span>
<span class="go">&#39;example&#39;</span>
</pre></div>
</div>
<p>The outermost leading and trailing <em>chars</em> argument values are stripped
from the string. Characters are removed from the leading end until
reaching a string character that is not contained in the set of
characters in <em>chars</em>. A similar action takes place on the trailing end.
For example:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">comment_string</span> <span class="o">=</span> <span class="s1">&#39;#....... Section 3.2.1 Issue #32 .......&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">comment_string</span><span class="o">.</span><span class="n">strip</span><span class="p">(</span><span class="s1">&#39;.#! &#39;</span><span class="p">)</span>
<span class="go">&#39;Section 3.2.1 Issue #32&#39;</span>
</pre></div>
</div>
</dd></dl>

<dl class="method">
<dt id="str.swapcase">
<code class="descclassname">str.</code><code class="descname">swapcase</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#str.swapcase" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a copy of the string with uppercase characters converted to lowercase and
vice versa. Note that it is not necessarily true that
<code class="docutils literal"><span class="pre">s.swapcase().swapcase()</span> <span class="pre">==</span> <span class="pre">s</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="str.title">
<code class="descclassname">str.</code><code class="descname">title</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#str.title" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a titlecased version of the string where words start with an uppercase
character and the remaining characters are lowercase.</p>
<p>For example:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s1">&#39;Hello world&#39;</span><span class="o">.</span><span class="n">title</span><span class="p">()</span>
<span class="go">&#39;Hello World&#39;</span>
</pre></div>
</div>
<p>The algorithm uses a simple language-independent definition of a word as
groups of consecutive letters.  The definition works in many contexts but
it means that apostrophes in contractions and possessives form word
boundaries, which may not be the desired result:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s2">&quot;they&#39;re bill&#39;s friends from the UK&quot;</span><span class="o">.</span><span class="n">title</span><span class="p">()</span>
<span class="go">&quot;They&#39;Re Bill&#39;S Friends From The Uk&quot;</span>
</pre></div>
</div>
<p>A workaround for apostrophes can be constructed using regular expressions:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="kn">import</span> <span class="nn">re</span>
<span class="gp">&gt;&gt;&gt; </span><span class="k">def</span> <span class="nf">titlecase</span><span class="p">(</span><span class="n">s</span><span class="p">):</span>
<span class="gp">... </span>    <span class="k">return</span> <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="s2">r&quot;[A-Za-z]+(&#39;[A-Za-z]+)?&quot;</span><span class="p">,</span>
<span class="gp">... </span>                  <span class="k">lambda</span> <span class="n">mo</span><span class="p">:</span> <span class="n">mo</span><span class="o">.</span><span class="n">group</span><span class="p">(</span><span class="mi">0</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">upper</span><span class="p">()</span> <span class="o">+</span>
<span class="gp">... </span>                             <span class="n">mo</span><span class="o">.</span><span class="n">group</span><span class="p">(</span><span class="mi">0</span><span class="p">)[</span><span class="mi">1</span><span class="p">:]</span><span class="o">.</span><span class="n">lower</span><span class="p">(),</span>
<span class="gp">... </span>                  <span class="n">s</span><span class="p">)</span>
<span class="gp">...</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">titlecase</span><span class="p">(</span><span class="s2">&quot;they&#39;re bill&#39;s friends.&quot;</span><span class="p">)</span>
<span class="go">&quot;They&#39;re Bill&#39;s Friends.&quot;</span>
</pre></div>
</div>
</dd></dl>

<dl class="method">
<dt id="str.translate">
<code class="descclassname">str.</code><code class="descname">translate</code><span class="sig-paren">(</span><em>table</em><span class="sig-paren">)</span><a class="headerlink" href="#str.translate" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a copy of the string in which each character has been mapped through
the given translation table.  The table must be an object that implements
indexing via <a class="reference internal" href="../reference/datamodel.html#object.__getitem__" title="object.__getitem__"><code class="xref py py-meth docutils literal"><span class="pre">__getitem__()</span></code></a>, typically a <a class="reference internal" href="../glossary.html#term-mapping"><span class="xref std std-term">mapping</span></a> or
<a class="reference internal" href="../glossary.html#term-sequence"><span class="xref std std-term">sequence</span></a>.  When indexed by a Unicode ordinal (an integer), the
table object can do any of the following: return a Unicode ordinal or a
string, to map the character to one or more other characters; return
<code class="docutils literal"><span class="pre">None</span></code>, to delete the character from the return string; or raise a
<a class="reference internal" href="exceptions.html#LookupError" title="LookupError"><code class="xref py py-exc docutils literal"><span class="pre">LookupError</span></code></a> exception, to map the character to itself.</p>
<p>You can use <a class="reference internal" href="#str.maketrans" title="str.maketrans"><code class="xref py py-meth docutils literal"><span class="pre">str.maketrans()</span></code></a> to create a translation map from
character-to-character mappings in different formats.</p>
<p>See also the <a class="reference internal" href="codecs.html#module-codecs" title="codecs: Encode and decode data and streams."><code class="xref py py-mod docutils literal"><span class="pre">codecs</span></code></a> module for a more flexible approach to custom
character mappings.</p>
</dd></dl>

<dl class="method">
<dt id="str.upper">
<code class="descclassname">str.</code><code class="descname">upper</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#str.upper" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a copy of the string with all the cased characters <a class="footnote-reference" href="#id14" id="id8">[4]</a> converted to
uppercase.  Note that <code class="docutils literal"><span class="pre">str.upper().isupper()</span></code> might be <code class="docutils literal"><span class="pre">False</span></code> if <code class="docutils literal"><span class="pre">s</span></code>
contains uncased characters or if the Unicode category of the resulting
character(s) is not &#8220;Lu&#8221; (Letter, uppercase), but e.g. &#8220;Lt&#8221; (Letter,
titlecase).</p>
<p>The uppercasing algorithm used is described in section 3.13 of the Unicode
Standard.</p>
</dd></dl>

<dl class="method">
<dt id="str.zfill">
<code class="descclassname">str.</code><code class="descname">zfill</code><span class="sig-paren">(</span><em>width</em><span class="sig-paren">)</span><a class="headerlink" href="#str.zfill" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a copy of the string left filled with ASCII <code class="docutils literal"><span class="pre">'0'</span></code> digits to
make a string of length <em>width</em>. A leading sign prefix (<code class="docutils literal"><span class="pre">'+'</span></code>/<code class="docutils literal"><span class="pre">'-'</span></code>)
is handled by inserting the padding <em>after</em> the sign character rather
than before. The original string is returned if <em>width</em> is less than
or equal to <code class="docutils literal"><span class="pre">len(s)</span></code>.</p>
<p>For example:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s2">&quot;42&quot;</span><span class="o">.</span><span class="n">zfill</span><span class="p">(</span><span class="mi">5</span><span class="p">)</span>
<span class="go">&#39;00042&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s2">&quot;-42&quot;</span><span class="o">.</span><span class="n">zfill</span><span class="p">(</span><span class="mi">5</span><span class="p">)</span>
<span class="go">&#39;-0042&#39;</span>
</pre></div>
</div>
</dd></dl>

</div>
<div class="section" id="printf-style-string-formatting">
<span id="old-string-formatting"></span><h3>4.7.2. <code class="docutils literal"><span class="pre">printf</span></code>-style String Formatting<a class="headerlink" href="#printf-style-string-formatting" title="Permalink to this headline">¶</a></h3>
<div class="admonition note" id="index-34">
<p class="first admonition-title">Note</p>
<p class="last">The formatting operations described here exhibit a variety of quirks that
lead to a number of common errors (such as failing to display tuples and
dictionaries correctly).  Using the newer <a class="reference internal" href="../reference/lexical_analysis.html#f-strings"><span>formatted
string literals</span></a> or the <a class="reference internal" href="#str.format" title="str.format"><code class="xref py py-meth docutils literal"><span class="pre">str.format()</span></code></a> interface
helps avoid these errors.  These alternatives also provide more powerful,
flexible and extensible approaches to formatting text.</p>
</div>
<p>String objects have one unique built-in operation: the <code class="docutils literal"><span class="pre">%</span></code> operator (modulo).
This is also known as the string <em>formatting</em> or <em>interpolation</em> operator.
Given <code class="docutils literal"><span class="pre">format</span> <span class="pre">%</span> <span class="pre">values</span></code> (where <em>format</em> is a string), <code class="docutils literal"><span class="pre">%</span></code> conversion
specifications in <em>format</em> are replaced with zero or more elements of <em>values</em>.
The effect is similar to using the <code class="xref c c-func docutils literal"><span class="pre">sprintf()</span></code> in the C language.</p>
<p>If <em>format</em> requires a single argument, <em>values</em> may be a single non-tuple
object. <a class="footnote-reference" href="#id15" id="id9">[5]</a>  Otherwise, <em>values</em> must be a tuple with exactly the number of
items specified by the format string, or a single mapping object (for example, a
dictionary).</p>
<p>A conversion specifier contains two or more characters and has the following
components, which must occur in this order:</p>
<ol class="arabic simple">
<li>The <code class="docutils literal"><span class="pre">'%'</span></code> character, which marks the start of the specifier.</li>
<li>Mapping key (optional), consisting of a parenthesised sequence of characters
(for example, <code class="docutils literal"><span class="pre">(somename)</span></code>).</li>
<li>Conversion flags (optional), which affect the result of some conversion
types.</li>
<li>Minimum field width (optional).  If specified as an <code class="docutils literal"><span class="pre">'*'</span></code> (asterisk), the
actual width is read from the next element of the tuple in <em>values</em>, and the
object to convert comes after the minimum field width and optional precision.</li>
<li>Precision (optional), given as a <code class="docutils literal"><span class="pre">'.'</span></code> (dot) followed by the precision.  If
specified as <code class="docutils literal"><span class="pre">'*'</span></code> (an asterisk), the actual precision is read from the next
element of the tuple in <em>values</em>, and the value to convert comes after the
precision.</li>
<li>Length modifier (optional).</li>
<li>Conversion type.</li>
</ol>
<p>When the right argument is a dictionary (or other mapping type), then the
formats in the string <em>must</em> include a parenthesised mapping key into that
dictionary inserted immediately after the <code class="docutils literal"><span class="pre">'%'</span></code> character. The mapping key
selects the value to be formatted from the mapping.  For example:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="nb">print</span><span class="p">(</span><span class="s1">&#39;</span><span class="si">%(language)s</span><span class="s1"> has </span><span class="si">%(number)03d</span><span class="s1"> quote types.&#39;</span> <span class="o">%</span>
<span class="gp">... </span>      <span class="p">{</span><span class="s1">&#39;language&#39;</span><span class="p">:</span> <span class="s2">&quot;Python&quot;</span><span class="p">,</span> <span class="s2">&quot;number&quot;</span><span class="p">:</span> <span class="mi">2</span><span class="p">})</span>
<span class="go">Python has 002 quote types.</span>
</pre></div>
</div>
<p>In this case no <code class="docutils literal"><span class="pre">*</span></code> specifiers may occur in a format (since they require a
sequential parameter list).</p>
<p>The conversion flag characters are:</p>
<table border="1" class="docutils">
<colgroup>
<col width="12%" />
<col width="88%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Flag</th>
<th class="head">Meaning</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><code class="docutils literal"><span class="pre">'#'</span></code></td>
<td>The value conversion will use the &#8220;alternate form&#8221; (where defined
below).</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">'0'</span></code></td>
<td>The conversion will be zero padded for numeric values.</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">'-'</span></code></td>
<td>The converted value is left adjusted (overrides the <code class="docutils literal"><span class="pre">'0'</span></code>
conversion if both are given).</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">'</span> <span class="pre">'</span></code></td>
<td>(a space) A blank should be left before a positive number (or empty
string) produced by a signed conversion.</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">'+'</span></code></td>
<td>A sign character (<code class="docutils literal"><span class="pre">'+'</span></code> or <code class="docutils literal"><span class="pre">'-'</span></code>) will precede the conversion
(overrides a &#8220;space&#8221; flag).</td>
</tr>
</tbody>
</table>
<p>A length modifier (<code class="docutils literal"><span class="pre">h</span></code>, <code class="docutils literal"><span class="pre">l</span></code>, or <code class="docutils literal"><span class="pre">L</span></code>) may be present, but is ignored as it
is not necessary for Python &#8211; so e.g. <code class="docutils literal"><span class="pre">%ld</span></code> is identical to <code class="docutils literal"><span class="pre">%d</span></code>.</p>
<p>The conversion types are:</p>
<table border="1" class="docutils">
<colgroup>
<col width="17%" />
<col width="74%" />
<col width="10%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Conversion</th>
<th class="head">Meaning</th>
<th class="head">Notes</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><code class="docutils literal"><span class="pre">'d'</span></code></td>
<td>Signed integer decimal.</td>
<td>&nbsp;</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">'i'</span></code></td>
<td>Signed integer decimal.</td>
<td>&nbsp;</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">'o'</span></code></td>
<td>Signed octal value.</td>
<td>(1)</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">'u'</span></code></td>
<td>Obsolete type &#8211; it is identical to <code class="docutils literal"><span class="pre">'d'</span></code>.</td>
<td>(6)</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">'x'</span></code></td>
<td>Signed hexadecimal (lowercase).</td>
<td>(2)</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">'X'</span></code></td>
<td>Signed hexadecimal (uppercase).</td>
<td>(2)</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">'e'</span></code></td>
<td>Floating point exponential format (lowercase).</td>
<td>(3)</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">'E'</span></code></td>
<td>Floating point exponential format (uppercase).</td>
<td>(3)</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">'f'</span></code></td>
<td>Floating point decimal format.</td>
<td>(3)</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">'F'</span></code></td>
<td>Floating point decimal format.</td>
<td>(3)</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">'g'</span></code></td>
<td>Floating point format. Uses lowercase exponential
format if exponent is less than -4 or not less than
precision, decimal format otherwise.</td>
<td>(4)</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">'G'</span></code></td>
<td>Floating point format. Uses uppercase exponential
format if exponent is less than -4 or not less than
precision, decimal format otherwise.</td>
<td>(4)</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">'c'</span></code></td>
<td>Single character (accepts integer or single
character string).</td>
<td>&nbsp;</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">'r'</span></code></td>
<td>String (converts any Python object using
<a class="reference internal" href="functions.html#repr" title="repr"><code class="xref py py-func docutils literal"><span class="pre">repr()</span></code></a>).</td>
<td>(5)</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">'s'</span></code></td>
<td>String (converts any Python object using
<a class="reference internal" href="#str" title="str"><code class="xref py py-func docutils literal"><span class="pre">str()</span></code></a>).</td>
<td>(5)</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">'a'</span></code></td>
<td>String (converts any Python object using
<a class="reference internal" href="functions.html#ascii" title="ascii"><code class="xref py py-func docutils literal"><span class="pre">ascii()</span></code></a>).</td>
<td>(5)</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">'%'</span></code></td>
<td>No argument is converted, results in a <code class="docutils literal"><span class="pre">'%'</span></code>
character in the result.</td>
<td>&nbsp;</td>
</tr>
</tbody>
</table>
<p>Notes:</p>
<ol class="arabic">
<li><p class="first">The alternate form causes a leading octal specifier (<code class="docutils literal"><span class="pre">'0o'</span></code>) to be
inserted before the first digit.</p>
</li>
<li><p class="first">The alternate form causes a leading <code class="docutils literal"><span class="pre">'0x'</span></code> or <code class="docutils literal"><span class="pre">'0X'</span></code> (depending on whether
the <code class="docutils literal"><span class="pre">'x'</span></code> or <code class="docutils literal"><span class="pre">'X'</span></code> format was used) to be inserted before the first digit.</p>
</li>
<li><p class="first">The alternate form causes the result to always contain a decimal point, even if
no digits follow it.</p>
<p>The precision determines the number of digits after the decimal point and
defaults to 6.</p>
</li>
<li><p class="first">The alternate form causes the result to always contain a decimal point, and
trailing zeroes are not removed as they would otherwise be.</p>
<p>The precision determines the number of significant digits before and after the
decimal point and defaults to 6.</p>
</li>
<li><p class="first">If precision is <code class="docutils literal"><span class="pre">N</span></code>, the output is truncated to <code class="docutils literal"><span class="pre">N</span></code> characters.</p>
</li>
<li><p class="first">See <span class="target" id="index-35"></span><a class="pep reference external" href="https://www.python.org/dev/peps/pep-0237"><strong>PEP 237</strong></a>.</p>
</li>
</ol>
<p>Since Python strings have an explicit length, <code class="docutils literal"><span class="pre">%s</span></code> conversions do not assume
that <code class="docutils literal"><span class="pre">'\0'</span></code> is the end of the string.</p>
<div class="versionchanged">
<p><span class="versionmodified">Changed in version 3.1: </span><code class="docutils literal"><span class="pre">%f</span></code> conversions for numbers whose absolute value is over 1e50 are no
longer replaced by <code class="docutils literal"><span class="pre">%g</span></code> conversions.</p>
</div>
</div>
</div>
<div class="section" id="binary-sequence-types-bytes-bytearray-memoryview">
<span id="binaryseq"></span><span id="index-36"></span><h2>4.8. Binary Sequence Types &#8212; <a class="reference internal" href="functions.html#bytes" title="bytes"><code class="xref py py-class docutils literal"><span class="pre">bytes</span></code></a>, <a class="reference internal" href="functions.html#bytearray" title="bytearray"><code class="xref py py-class docutils literal"><span class="pre">bytearray</span></code></a>, <a class="reference internal" href="#memoryview" title="memoryview"><code class="xref py py-class docutils literal"><span class="pre">memoryview</span></code></a><a class="headerlink" href="#binary-sequence-types-bytes-bytearray-memoryview" title="Permalink to this headline">¶</a></h2>
<p id="index-37">The core built-in types for manipulating binary data are <a class="reference internal" href="functions.html#bytes" title="bytes"><code class="xref py py-class docutils literal"><span class="pre">bytes</span></code></a> and
<a class="reference internal" href="functions.html#bytearray" title="bytearray"><code class="xref py py-class docutils literal"><span class="pre">bytearray</span></code></a>. They are supported by <a class="reference internal" href="#memoryview" title="memoryview"><code class="xref py py-class docutils literal"><span class="pre">memoryview</span></code></a> which uses
the <a class="reference internal" href="../c-api/buffer.html#bufferobjects"><span>buffer protocol</span></a> to access the memory of other
binary objects without needing to make a copy.</p>
<p>The <a class="reference internal" href="array.html#module-array" title="array: Space efficient arrays of uniformly typed numeric values."><code class="xref py py-mod docutils literal"><span class="pre">array</span></code></a> module supports efficient storage of basic data types like
32-bit integers and IEEE754 double-precision floating values.</p>
<div class="section" id="bytes">
<span id="typebytes"></span><h3>4.8.1. Bytes<a class="headerlink" href="#bytes" title="Permalink to this headline">¶</a></h3>
<p id="index-38">Bytes objects are immutable sequences of single bytes. Since many major
binary protocols are based on the ASCII text encoding, bytes objects offer
several methods that are only valid when working with ASCII compatible
data and are closely related to string objects in a variety of other ways.</p>
<p>Firstly, the syntax for bytes literals is largely the same as that for string
literals, except that a <code class="docutils literal"><span class="pre">b</span></code> prefix is added:</p>
<ul class="simple">
<li>Single quotes: <code class="docutils literal"><span class="pre">b'still</span> <span class="pre">allows</span> <span class="pre">embedded</span> <span class="pre">&quot;double&quot;</span> <span class="pre">quotes'</span></code></li>
<li>Double quotes: <code class="docutils literal"><span class="pre">b&quot;still</span> <span class="pre">allows</span> <span class="pre">embedded</span> <span class="pre">'single'</span> <span class="pre">quotes&quot;</span></code>.</li>
<li>Triple quoted: <code class="docutils literal"><span class="pre">b'''3</span> <span class="pre">single</span> <span class="pre">quotes'''</span></code>, <code class="docutils literal"><span class="pre">b&quot;&quot;&quot;3</span> <span class="pre">double</span> <span class="pre">quotes&quot;&quot;&quot;</span></code></li>
</ul>
<p>Only ASCII characters are permitted in bytes literals (regardless of the
declared source code encoding). Any binary values over 127 must be entered
into bytes literals using the appropriate escape sequence.</p>
<p>As with string literals, bytes literals may also use a <code class="docutils literal"><span class="pre">r</span></code> prefix to disable
processing of escape sequences. See <a class="reference internal" href="../reference/lexical_analysis.html#strings"><span>String and Bytes literals</span></a> for more about the various
forms of bytes literal, including supported escape sequences.</p>
<p>While bytes literals and representations are based on ASCII text, bytes
objects actually behave like immutable sequences of integers, with each
value in the sequence restricted such that <code class="docutils literal"><span class="pre">0</span> <span class="pre">&lt;=</span> <span class="pre">x</span> <span class="pre">&lt;</span> <span class="pre">256</span></code> (attempts to
violate this restriction will trigger <a class="reference internal" href="exceptions.html#ValueError" title="ValueError"><code class="xref py py-exc docutils literal"><span class="pre">ValueError</span></code></a>. This is done
deliberately to emphasise that while many binary formats include ASCII based
elements and can be usefully manipulated with some text-oriented algorithms,
this is not generally the case for arbitrary binary data (blindly applying
text processing algorithms to binary data formats that are not ASCII
compatible will usually lead to data corruption).</p>
<p>In addition to the literal forms, bytes objects can be created in a number of
other ways:</p>
<ul class="simple">
<li>A zero-filled bytes object of a specified length: <code class="docutils literal"><span class="pre">bytes(10)</span></code></li>
<li>From an iterable of integers: <code class="docutils literal"><span class="pre">bytes(range(20))</span></code></li>
<li>Copying existing binary data via the buffer protocol:  <code class="docutils literal"><span class="pre">bytes(obj)</span></code></li>
</ul>
<p>Also see the <a class="reference internal" href="functions.html#func-bytes"><span>bytes</span></a> built-in.</p>
<p>Since 2 hexadecimal digits correspond precisely to a single byte, hexadecimal
numbers are a commonly used format for describing binary data. Accordingly,
the bytes type has an additional class method to read data in that format:</p>
<dl class="classmethod">
<dt id="bytes.fromhex">
<em class="property">classmethod </em><code class="descclassname">bytes.</code><code class="descname">fromhex</code><span class="sig-paren">(</span><em>string</em><span class="sig-paren">)</span><a class="headerlink" href="#bytes.fromhex" title="Permalink to this definition">¶</a></dt>
<dd><p>This <a class="reference internal" href="functions.html#bytes" title="bytes"><code class="xref py py-class docutils literal"><span class="pre">bytes</span></code></a> class method returns a bytes object, decoding the
given string object.  The string must contain two hexadecimal digits per
byte, with ASCII spaces being ignored.</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="nb">bytes</span><span class="o">.</span><span class="n">fromhex</span><span class="p">(</span><span class="s1">&#39;2Ef0 F1f2  &#39;</span><span class="p">)</span>
<span class="go">b&#39;.\xf0\xf1\xf2&#39;</span>
</pre></div>
</div>
</dd></dl>

<p>A reverse conversion function exists to transform a bytes object into its
hexadecimal representation.</p>
<dl class="method">
<dt id="bytes.hex">
<code class="descclassname">bytes.</code><code class="descname">hex</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#bytes.hex" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a string object containing two hexadecimal digits for each
byte in the instance.</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">b</span><span class="s1">&#39;</span><span class="se">\xf0\xf1\xf2</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">hex</span><span class="p">()</span>
<span class="go">&#39;f0f1f2&#39;</span>
</pre></div>
</div>
<div class="versionadded">
<p><span class="versionmodified">New in version 3.5.</span></p>
</div>
</dd></dl>

<p>Since bytes objects are sequences of integers (akin to a tuple), for a bytes
object <em>b</em>, <code class="docutils literal"><span class="pre">b[0]</span></code> will be an integer, while <code class="docutils literal"><span class="pre">b[0:1]</span></code> will be a bytes
object of length 1.  (This contrasts with text strings, where both indexing
and slicing will produce a string of length 1)</p>
<p>The representation of bytes objects uses the literal format (<code class="docutils literal"><span class="pre">b'...'</span></code>)
since it is often more useful than e.g. <code class="docutils literal"><span class="pre">bytes([46,</span> <span class="pre">46,</span> <span class="pre">46])</span></code>.  You can
always convert a bytes object into a list of integers using <code class="docutils literal"><span class="pre">list(b)</span></code>.</p>
<div class="admonition note">
<p class="first admonition-title">Note</p>
<p class="last">For Python 2.x users: In the Python 2.x series, a variety of implicit
conversions between 8-bit strings (the closest thing 2.x offers to a
built-in binary data type) and Unicode strings were permitted. This was a
backwards compatibility workaround to account for the fact that Python
originally only supported 8-bit text, and Unicode text was a later
addition. In Python 3.x, those implicit conversions are gone - conversions
between 8-bit binary data and Unicode text must be explicit, and bytes and
string objects will always compare unequal.</p>
</div>
</div>
<div class="section" id="bytearray-objects">
<span id="typebytearray"></span><h3>4.8.2. Bytearray Objects<a class="headerlink" href="#bytearray-objects" title="Permalink to this headline">¶</a></h3>
<p id="index-39"><a class="reference internal" href="functions.html#bytearray" title="bytearray"><code class="xref py py-class docutils literal"><span class="pre">bytearray</span></code></a> objects are a mutable counterpart to <a class="reference internal" href="functions.html#bytes" title="bytes"><code class="xref py py-class docutils literal"><span class="pre">bytes</span></code></a>
objects. There is no dedicated literal syntax for bytearray objects, instead
they are always created by calling the constructor:</p>
<ul class="simple">
<li>Creating an empty instance: <code class="docutils literal"><span class="pre">bytearray()</span></code></li>
<li>Creating a zero-filled instance with a given length: <code class="docutils literal"><span class="pre">bytearray(10)</span></code></li>
<li>From an iterable of integers: <code class="docutils literal"><span class="pre">bytearray(range(20))</span></code></li>
<li>Copying existing binary data via the buffer protocol:  <code class="docutils literal"><span class="pre">bytearray(b'Hi!')</span></code></li>
</ul>
<p>As bytearray objects are mutable, they support the
<a class="reference internal" href="#typesseq-mutable"><span>mutable</span></a> sequence operations in addition to the
common bytes and bytearray operations described in <a class="reference internal" href="#bytes-methods"><span>Bytes and Bytearray Operations</span></a>.</p>
<p>Also see the <a class="reference internal" href="functions.html#func-bytearray"><span>bytearray</span></a> built-in.</p>
<p>Since 2 hexadecimal digits correspond precisely to a single byte, hexadecimal
numbers are a commonly used format for describing binary data. Accordingly,
the bytearray type has an additional class method to read data in that format:</p>
<dl class="classmethod">
<dt id="bytearray.fromhex">
<em class="property">classmethod </em><code class="descclassname">bytearray.</code><code class="descname">fromhex</code><span class="sig-paren">(</span><em>string</em><span class="sig-paren">)</span><a class="headerlink" href="#bytearray.fromhex" title="Permalink to this definition">¶</a></dt>
<dd><p>This <a class="reference internal" href="functions.html#bytearray" title="bytearray"><code class="xref py py-class docutils literal"><span class="pre">bytearray</span></code></a> class method returns bytearray object, decoding
the given string object.  The string must contain two hexadecimal digits
per byte, with ASCII spaces being ignored.</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="nb">bytearray</span><span class="o">.</span><span class="n">fromhex</span><span class="p">(</span><span class="s1">&#39;2Ef0 F1f2  &#39;</span><span class="p">)</span>
<span class="go">bytearray(b&#39;.\xf0\xf1\xf2&#39;)</span>
</pre></div>
</div>
</dd></dl>

<p>A reverse conversion function exists to transform a bytearray object into its
hexadecimal representation.</p>
<dl class="method">
<dt id="bytearray.hex">
<code class="descclassname">bytearray.</code><code class="descname">hex</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#bytearray.hex" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a string object containing two hexadecimal digits for each
byte in the instance.</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="nb">bytearray</span><span class="p">(</span><span class="n">b</span><span class="s1">&#39;</span><span class="se">\xf0\xf1\xf2</span><span class="s1">&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">hex</span><span class="p">()</span>
<span class="go">&#39;f0f1f2&#39;</span>
</pre></div>
</div>
<div class="versionadded">
<p><span class="versionmodified">New in version 3.5.</span></p>
</div>
</dd></dl>

<p>Since bytearray objects are sequences of integers (akin to a list), for a
bytearray object <em>b</em>, <code class="docutils literal"><span class="pre">b[0]</span></code> will be an integer, while <code class="docutils literal"><span class="pre">b[0:1]</span></code> will be
a bytearray object of length 1.  (This contrasts with text strings, where
both indexing and slicing will produce a string of length 1)</p>
<p>The representation of bytearray objects uses the bytes literal format
(<code class="docutils literal"><span class="pre">bytearray(b'...')</span></code>) since it is often more useful than e.g.
<code class="docutils literal"><span class="pre">bytearray([46,</span> <span class="pre">46,</span> <span class="pre">46])</span></code>.  You can always convert a bytearray object into
a list of integers using <code class="docutils literal"><span class="pre">list(b)</span></code>.</p>
</div>
<div class="section" id="bytes-and-bytearray-operations">
<span id="bytes-methods"></span><h3>4.8.3. Bytes and Bytearray Operations<a class="headerlink" href="#bytes-and-bytearray-operations" title="Permalink to this headline">¶</a></h3>
<p id="index-40">Both bytes and bytearray objects support the <a class="reference internal" href="#typesseq-common"><span>common</span></a>
sequence operations. They interoperate not just with operands of the same
type, but with any <a class="reference internal" href="../glossary.html#term-bytes-like-object"><span class="xref std std-term">bytes-like object</span></a>. Due to this flexibility, they can be
freely mixed in operations without causing errors. However, the return type
of the result may depend on the order of operands.</p>
<div class="admonition note">
<p class="first admonition-title">Note</p>
<p>The methods on bytes and bytearray objects don&#8217;t accept strings as their
arguments, just as the methods on strings don&#8217;t accept bytes as their
arguments.  For example, you have to write:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="n">a</span> <span class="o">=</span> <span class="s2">&quot;abc&quot;</span>
<span class="n">b</span> <span class="o">=</span> <span class="n">a</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">&quot;a&quot;</span><span class="p">,</span> <span class="s2">&quot;f&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>and:</p>
<div class="last highlight-python3"><div class="highlight"><pre><span></span><span class="n">a</span> <span class="o">=</span> <span class="n">b</span><span class="s2">&quot;abc&quot;</span>
<span class="n">b</span> <span class="o">=</span> <span class="n">a</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="n">b</span><span class="s2">&quot;a&quot;</span><span class="p">,</span> <span class="n">b</span><span class="s2">&quot;f&quot;</span><span class="p">)</span>
</pre></div>
</div>
</div>
<p>Some bytes and bytearray operations assume the use of ASCII compatible
binary formats, and hence should be avoided when working with arbitrary
binary data. These restrictions are covered below.</p>
<div class="admonition note">
<p class="first admonition-title">Note</p>
<p class="last">Using these ASCII based operations to manipulate binary data that is not
stored in an ASCII based format may lead to data corruption.</p>
</div>
<p>The following methods on bytes and bytearray objects can be used with
arbitrary binary data.</p>
<dl class="method">
<dt id="bytes.count">
<code class="descclassname">bytes.</code><code class="descname">count</code><span class="sig-paren">(</span><em>sub</em><span class="optional">[</span>, <em>start</em><span class="optional">[</span>, <em>end</em><span class="optional">]</span><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#bytes.count" title="Permalink to this definition">¶</a></dt>
<dt id="bytearray.count">
<code class="descclassname">bytearray.</code><code class="descname">count</code><span class="sig-paren">(</span><em>sub</em><span class="optional">[</span>, <em>start</em><span class="optional">[</span>, <em>end</em><span class="optional">]</span><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#bytearray.count" title="Permalink to this definition">¶</a></dt>
<dd><p>Return the number of non-overlapping occurrences of subsequence <em>sub</em> in
the range [<em>start</em>, <em>end</em>].  Optional arguments <em>start</em> and <em>end</em> are
interpreted as in slice notation.</p>
<p>The subsequence to search for may be any <a class="reference internal" href="../glossary.html#term-bytes-like-object"><span class="xref std std-term">bytes-like object</span></a> or an
integer in the range 0 to 255.</p>
<div class="versionchanged">
<p><span class="versionmodified">Changed in version 3.3: </span>Also accept an integer in the range 0 to 255 as the subsequence.</p>
</div>
</dd></dl>

<dl class="method">
<dt id="bytes.decode">
<code class="descclassname">bytes.</code><code class="descname">decode</code><span class="sig-paren">(</span><em>encoding=&quot;utf-8&quot;</em>, <em>errors=&quot;strict&quot;</em><span class="sig-paren">)</span><a class="headerlink" href="#bytes.decode" title="Permalink to this definition">¶</a></dt>
<dt id="bytearray.decode">
<code class="descclassname">bytearray.</code><code class="descname">decode</code><span class="sig-paren">(</span><em>encoding=&quot;utf-8&quot;</em>, <em>errors=&quot;strict&quot;</em><span class="sig-paren">)</span><a class="headerlink" href="#bytearray.decode" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a string decoded from the given bytes.  Default encoding is
<code class="docutils literal"><span class="pre">'utf-8'</span></code>. <em>errors</em> may be given to set a different
error handling scheme.  The default for <em>errors</em> is <code class="docutils literal"><span class="pre">'strict'</span></code>, meaning
that encoding errors raise a <a class="reference internal" href="exceptions.html#UnicodeError" title="UnicodeError"><code class="xref py py-exc docutils literal"><span class="pre">UnicodeError</span></code></a>.  Other possible values are
<code class="docutils literal"><span class="pre">'ignore'</span></code>, <code class="docutils literal"><span class="pre">'replace'</span></code> and any other name registered via
<a class="reference internal" href="codecs.html#codecs.register_error" title="codecs.register_error"><code class="xref py py-func docutils literal"><span class="pre">codecs.register_error()</span></code></a>, see section <a class="reference internal" href="codecs.html#error-handlers"><span>Error Handlers</span></a>. For a
list of possible encodings, see section <a class="reference internal" href="codecs.html#standard-encodings"><span>Standard Encodings</span></a>.</p>
<div class="admonition note">
<p class="first admonition-title">Note</p>
<p class="last">Passing the <em>encoding</em> argument to <a class="reference internal" href="#str" title="str"><code class="xref py py-class docutils literal"><span class="pre">str</span></code></a> allows decoding any
<a class="reference internal" href="../glossary.html#term-bytes-like-object"><span class="xref std std-term">bytes-like object</span></a> directly, without needing to make a temporary
bytes or bytearray object.</p>
</div>
<div class="versionchanged">
<p><span class="versionmodified">Changed in version 3.1: </span>Added support for keyword arguments.</p>
</div>
</dd></dl>

<dl class="method">
<dt id="bytes.endswith">
<code class="descclassname">bytes.</code><code class="descname">endswith</code><span class="sig-paren">(</span><em>suffix</em><span class="optional">[</span>, <em>start</em><span class="optional">[</span>, <em>end</em><span class="optional">]</span><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#bytes.endswith" title="Permalink to this definition">¶</a></dt>
<dt id="bytearray.endswith">
<code class="descclassname">bytearray.</code><code class="descname">endswith</code><span class="sig-paren">(</span><em>suffix</em><span class="optional">[</span>, <em>start</em><span class="optional">[</span>, <em>end</em><span class="optional">]</span><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#bytearray.endswith" title="Permalink to this definition">¶</a></dt>
<dd><p>Return <code class="docutils literal"><span class="pre">True</span></code> if the binary data ends with the specified <em>suffix</em>,
otherwise return <code class="docutils literal"><span class="pre">False</span></code>.  <em>suffix</em> can also be a tuple of suffixes to
look for.  With optional <em>start</em>, test beginning at that position.  With
optional <em>end</em>, stop comparing at that position.</p>
<p>The suffix(es) to search for may be any <a class="reference internal" href="../glossary.html#term-bytes-like-object"><span class="xref std std-term">bytes-like object</span></a>.</p>
</dd></dl>

<dl class="method">
<dt id="bytes.find">
<code class="descclassname">bytes.</code><code class="descname">find</code><span class="sig-paren">(</span><em>sub</em><span class="optional">[</span>, <em>start</em><span class="optional">[</span>, <em>end</em><span class="optional">]</span><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#bytes.find" title="Permalink to this definition">¶</a></dt>
<dt id="bytearray.find">
<code class="descclassname">bytearray.</code><code class="descname">find</code><span class="sig-paren">(</span><em>sub</em><span class="optional">[</span>, <em>start</em><span class="optional">[</span>, <em>end</em><span class="optional">]</span><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#bytearray.find" title="Permalink to this definition">¶</a></dt>
<dd><p>Return the lowest index in the data where the subsequence <em>sub</em> is found,
such that <em>sub</em> is contained in the slice <code class="docutils literal"><span class="pre">s[start:end]</span></code>.  Optional
arguments <em>start</em> and <em>end</em> are interpreted as in slice notation.  Return
<code class="docutils literal"><span class="pre">-1</span></code> if <em>sub</em> is not found.</p>
<p>The subsequence to search for may be any <a class="reference internal" href="../glossary.html#term-bytes-like-object"><span class="xref std std-term">bytes-like object</span></a> or an
integer in the range 0 to 255.</p>
<div class="admonition note">
<p class="first admonition-title">Note</p>
<p>The <a class="reference internal" href="#bytes.find" title="bytes.find"><code class="xref py py-meth docutils literal"><span class="pre">find()</span></code></a> method should be used only if you need to know the
position of <em>sub</em>.  To check if <em>sub</em> is a substring or not, use the
<a class="reference internal" href="../reference/expressions.html#in"><code class="xref std std-keyword docutils literal"><span class="pre">in</span></code></a> operator:</p>
<div class="last highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">b</span><span class="s1">&#39;Py&#39;</span> <span class="ow">in</span> <span class="n">b</span><span class="s1">&#39;Python&#39;</span>
<span class="go">True</span>
</pre></div>
</div>
</div>
<div class="versionchanged">
<p><span class="versionmodified">Changed in version 3.3: </span>Also accept an integer in the range 0 to 255 as the subsequence.</p>
</div>
</dd></dl>

<dl class="method">
<dt id="bytes.index">
<code class="descclassname">bytes.</code><code class="descname">index</code><span class="sig-paren">(</span><em>sub</em><span class="optional">[</span>, <em>start</em><span class="optional">[</span>, <em>end</em><span class="optional">]</span><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#bytes.index" title="Permalink to this definition">¶</a></dt>
<dt id="bytearray.index">
<code class="descclassname">bytearray.</code><code class="descname">index</code><span class="sig-paren">(</span><em>sub</em><span class="optional">[</span>, <em>start</em><span class="optional">[</span>, <em>end</em><span class="optional">]</span><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#bytearray.index" title="Permalink to this definition">¶</a></dt>
<dd><p>Like <a class="reference internal" href="#bytes.find" title="bytes.find"><code class="xref py py-meth docutils literal"><span class="pre">find()</span></code></a>, but raise <a class="reference internal" href="exceptions.html#ValueError" title="ValueError"><code class="xref py py-exc docutils literal"><span class="pre">ValueError</span></code></a> when the
subsequence is not found.</p>
<p>The subsequence to search for may be any <a class="reference internal" href="../glossary.html#term-bytes-like-object"><span class="xref std std-term">bytes-like object</span></a> or an
integer in the range 0 to 255.</p>
<div class="versionchanged">
<p><span class="versionmodified">Changed in version 3.3: </span>Also accept an integer in the range 0 to 255 as the subsequence.</p>
</div>
</dd></dl>

<dl class="method">
<dt id="bytes.join">
<code class="descclassname">bytes.</code><code class="descname">join</code><span class="sig-paren">(</span><em>iterable</em><span class="sig-paren">)</span><a class="headerlink" href="#bytes.join" title="Permalink to this definition">¶</a></dt>
<dt id="bytearray.join">
<code class="descclassname">bytearray.</code><code class="descname">join</code><span class="sig-paren">(</span><em>iterable</em><span class="sig-paren">)</span><a class="headerlink" href="#bytearray.join" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a bytes or bytearray object which is the concatenation of the
binary data sequences in the <a class="reference internal" href="../glossary.html#term-iterable"><span class="xref std std-term">iterable</span></a> <em>iterable</em>.  A
<a class="reference internal" href="exceptions.html#TypeError" title="TypeError"><code class="xref py py-exc docutils literal"><span class="pre">TypeError</span></code></a> will be raised if there are any values in <em>iterable</em>
that are not <a class="reference internal" href="../glossary.html#term-bytes-like-object"><span class="xref std std-term">bytes-like objects</span></a>, including
<a class="reference internal" href="#str" title="str"><code class="xref py py-class docutils literal"><span class="pre">str</span></code></a> objects.  The separator between elements is the contents
of the bytes or bytearray object providing this method.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="bytes.maketrans">
<em class="property">static </em><code class="descclassname">bytes.</code><code class="descname">maketrans</code><span class="sig-paren">(</span><em>from</em>, <em>to</em><span class="sig-paren">)</span><a class="headerlink" href="#bytes.maketrans" title="Permalink to this definition">¶</a></dt>
<dt id="bytearray.maketrans">
<em class="property">static </em><code class="descclassname">bytearray.</code><code class="descname">maketrans</code><span class="sig-paren">(</span><em>from</em>, <em>to</em><span class="sig-paren">)</span><a class="headerlink" href="#bytearray.maketrans" title="Permalink to this definition">¶</a></dt>
<dd><p>This static method returns a translation table usable for
<a class="reference internal" href="#bytes.translate" title="bytes.translate"><code class="xref py py-meth docutils literal"><span class="pre">bytes.translate()</span></code></a> that will map each character in <em>from</em> into the
character at the same position in <em>to</em>; <em>from</em> and <em>to</em> must both be
<a class="reference internal" href="../glossary.html#term-bytes-like-object"><span class="xref std std-term">bytes-like objects</span></a> and have the same length.</p>
<div class="versionadded">
<p><span class="versionmodified">New in version 3.1.</span></p>
</div>
</dd></dl>

<dl class="method">
<dt id="bytes.partition">
<code class="descclassname">bytes.</code><code class="descname">partition</code><span class="sig-paren">(</span><em>sep</em><span class="sig-paren">)</span><a class="headerlink" href="#bytes.partition" title="Permalink to this definition">¶</a></dt>
<dt id="bytearray.partition">
<code class="descclassname">bytearray.</code><code class="descname">partition</code><span class="sig-paren">(</span><em>sep</em><span class="sig-paren">)</span><a class="headerlink" href="#bytearray.partition" title="Permalink to this definition">¶</a></dt>
<dd><p>Split the sequence at the first occurrence of <em>sep</em>, and return a 3-tuple
containing the part before the separator, the separator, and the part
after the separator.  If the separator is not found, return a 3-tuple
containing a copy of the original sequence, followed by two empty bytes or
bytearray objects.</p>
<p>The separator to search for may be any <a class="reference internal" href="../glossary.html#term-bytes-like-object"><span class="xref std std-term">bytes-like object</span></a>.</p>
</dd></dl>

<dl class="method">
<dt id="bytes.replace">
<code class="descclassname">bytes.</code><code class="descname">replace</code><span class="sig-paren">(</span><em>old</em>, <em>new</em><span class="optional">[</span>, <em>count</em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#bytes.replace" title="Permalink to this definition">¶</a></dt>
<dt id="bytearray.replace">
<code class="descclassname">bytearray.</code><code class="descname">replace</code><span class="sig-paren">(</span><em>old</em>, <em>new</em><span class="optional">[</span>, <em>count</em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#bytearray.replace" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a copy of the sequence with all occurrences of subsequence <em>old</em>
replaced by <em>new</em>.  If the optional argument <em>count</em> is given, only the
first <em>count</em> occurrences are replaced.</p>
<p>The subsequence to search for and its replacement may be any
<a class="reference internal" href="../glossary.html#term-bytes-like-object"><span class="xref std std-term">bytes-like object</span></a>.</p>
<div class="admonition note">
<p class="first admonition-title">Note</p>
<p class="last">The bytearray version of this method does <em>not</em> operate in place - it
always produces a new object, even if no changes were made.</p>
</div>
</dd></dl>

<dl class="method">
<dt id="bytes.rfind">
<code class="descclassname">bytes.</code><code class="descname">rfind</code><span class="sig-paren">(</span><em>sub</em><span class="optional">[</span>, <em>start</em><span class="optional">[</span>, <em>end</em><span class="optional">]</span><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#bytes.rfind" title="Permalink to this definition">¶</a></dt>
<dt id="bytearray.rfind">
<code class="descclassname">bytearray.</code><code class="descname">rfind</code><span class="sig-paren">(</span><em>sub</em><span class="optional">[</span>, <em>start</em><span class="optional">[</span>, <em>end</em><span class="optional">]</span><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#bytearray.rfind" title="Permalink to this definition">¶</a></dt>
<dd><p>Return the highest index in the sequence where the subsequence <em>sub</em> is
found, such that <em>sub</em> is contained within <code class="docutils literal"><span class="pre">s[start:end]</span></code>.  Optional
arguments <em>start</em> and <em>end</em> are interpreted as in slice notation. Return
<code class="docutils literal"><span class="pre">-1</span></code> on failure.</p>
<p>The subsequence to search for may be any <a class="reference internal" href="../glossary.html#term-bytes-like-object"><span class="xref std std-term">bytes-like object</span></a> or an
integer in the range 0 to 255.</p>
<div class="versionchanged">
<p><span class="versionmodified">Changed in version 3.3: </span>Also accept an integer in the range 0 to 255 as the subsequence.</p>
</div>
</dd></dl>

<dl class="method">
<dt id="bytes.rindex">
<code class="descclassname">bytes.</code><code class="descname">rindex</code><span class="sig-paren">(</span><em>sub</em><span class="optional">[</span>, <em>start</em><span class="optional">[</span>, <em>end</em><span class="optional">]</span><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#bytes.rindex" title="Permalink to this definition">¶</a></dt>
<dt id="bytearray.rindex">
<code class="descclassname">bytearray.</code><code class="descname">rindex</code><span class="sig-paren">(</span><em>sub</em><span class="optional">[</span>, <em>start</em><span class="optional">[</span>, <em>end</em><span class="optional">]</span><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#bytearray.rindex" title="Permalink to this definition">¶</a></dt>
<dd><p>Like <a class="reference internal" href="#bytes.rfind" title="bytes.rfind"><code class="xref py py-meth docutils literal"><span class="pre">rfind()</span></code></a> but raises <a class="reference internal" href="exceptions.html#ValueError" title="ValueError"><code class="xref py py-exc docutils literal"><span class="pre">ValueError</span></code></a> when the
subsequence <em>sub</em> is not found.</p>
<p>The subsequence to search for may be any <a class="reference internal" href="../glossary.html#term-bytes-like-object"><span class="xref std std-term">bytes-like object</span></a> or an
integer in the range 0 to 255.</p>
<div class="versionchanged">
<p><span class="versionmodified">Changed in version 3.3: </span>Also accept an integer in the range 0 to 255 as the subsequence.</p>
</div>
</dd></dl>

<dl class="method">
<dt id="bytes.rpartition">
<code class="descclassname">bytes.</code><code class="descname">rpartition</code><span class="sig-paren">(</span><em>sep</em><span class="sig-paren">)</span><a class="headerlink" href="#bytes.rpartition" title="Permalink to this definition">¶</a></dt>
<dt id="bytearray.rpartition">
<code class="descclassname">bytearray.</code><code class="descname">rpartition</code><span class="sig-paren">(</span><em>sep</em><span class="sig-paren">)</span><a class="headerlink" href="#bytearray.rpartition" title="Permalink to this definition">¶</a></dt>
<dd><p>Split the sequence at the last occurrence of <em>sep</em>, and return a 3-tuple
containing the part before the separator, the separator, and the part
after the separator.  If the separator is not found, return a 3-tuple
containing a copy of the original sequence, followed by two empty bytes or
bytearray objects.</p>
<p>The separator to search for may be any <a class="reference internal" href="../glossary.html#term-bytes-like-object"><span class="xref std std-term">bytes-like object</span></a>.</p>
</dd></dl>

<dl class="method">
<dt id="bytes.startswith">
<code class="descclassname">bytes.</code><code class="descname">startswith</code><span class="sig-paren">(</span><em>prefix</em><span class="optional">[</span>, <em>start</em><span class="optional">[</span>, <em>end</em><span class="optional">]</span><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#bytes.startswith" title="Permalink to this definition">¶</a></dt>
<dt id="bytearray.startswith">
<code class="descclassname">bytearray.</code><code class="descname">startswith</code><span class="sig-paren">(</span><em>prefix</em><span class="optional">[</span>, <em>start</em><span class="optional">[</span>, <em>end</em><span class="optional">]</span><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#bytearray.startswith" title="Permalink to this definition">¶</a></dt>
<dd><p>Return <code class="docutils literal"><span class="pre">True</span></code> if the binary data starts with the specified <em>prefix</em>,
otherwise return <code class="docutils literal"><span class="pre">False</span></code>.  <em>prefix</em> can also be a tuple of prefixes to
look for.  With optional <em>start</em>, test beginning at that position.  With
optional <em>end</em>, stop comparing at that position.</p>
<p>The prefix(es) to search for may be any <a class="reference internal" href="../glossary.html#term-bytes-like-object"><span class="xref std std-term">bytes-like object</span></a>.</p>
</dd></dl>

<dl class="method">
<dt id="bytes.translate">
<code class="descclassname">bytes.</code><code class="descname">translate</code><span class="sig-paren">(</span><em>table</em>, <em>delete=b''</em><span class="sig-paren">)</span><a class="headerlink" href="#bytes.translate" title="Permalink to this definition">¶</a></dt>
<dt id="bytearray.translate">
<code class="descclassname">bytearray.</code><code class="descname">translate</code><span class="sig-paren">(</span><em>table</em>, <em>delete=b''</em><span class="sig-paren">)</span><a class="headerlink" href="#bytearray.translate" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a copy of the bytes or bytearray object where all bytes occurring in
the optional argument <em>delete</em> are removed, and the remaining bytes have
been mapped through the given translation table, which must be a bytes
object of length 256.</p>
<p>You can use the <a class="reference internal" href="#bytes.maketrans" title="bytes.maketrans"><code class="xref py py-func docutils literal"><span class="pre">bytes.maketrans()</span></code></a> method to create a translation
table.</p>
<p>Set the <em>table</em> argument to <code class="docutils literal"><span class="pre">None</span></code> for translations that only delete
characters:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">b</span><span class="s1">&#39;read this short text&#39;</span><span class="o">.</span><span class="n">translate</span><span class="p">(</span><span class="kc">None</span><span class="p">,</span> <span class="n">b</span><span class="s1">&#39;aeiou&#39;</span><span class="p">)</span>
<span class="go">b&#39;rd ths shrt txt&#39;</span>
</pre></div>
</div>
<div class="versionchanged">
<p><span class="versionmodified">Changed in version 3.6: </span><em>delete</em> is now supported as a keyword argument.</p>
</div>
</dd></dl>

<p>The following methods on bytes and bytearray objects have default behaviours
that assume the use of ASCII compatible binary formats, but can still be used
with arbitrary binary data by passing appropriate arguments. Note that all of
the bytearray methods in this section do <em>not</em> operate in place, and instead
produce new objects.</p>
<dl class="method">
<dt id="bytes.center">
<code class="descclassname">bytes.</code><code class="descname">center</code><span class="sig-paren">(</span><em>width</em><span class="optional">[</span>, <em>fillbyte</em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#bytes.center" title="Permalink to this definition">¶</a></dt>
<dt id="bytearray.center">
<code class="descclassname">bytearray.</code><code class="descname">center</code><span class="sig-paren">(</span><em>width</em><span class="optional">[</span>, <em>fillbyte</em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#bytearray.center" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a copy of the object centered in a sequence of length <em>width</em>.
Padding is done using the specified <em>fillbyte</em> (default is an ASCII
space). For <a class="reference internal" href="functions.html#bytes" title="bytes"><code class="xref py py-class docutils literal"><span class="pre">bytes</span></code></a> objects, the original sequence is returned if
<em>width</em> is less than or equal to <code class="docutils literal"><span class="pre">len(s)</span></code>.</p>
<div class="admonition note">
<p class="first admonition-title">Note</p>
<p class="last">The bytearray version of this method does <em>not</em> operate in place -
it always produces a new object, even if no changes were made.</p>
</div>
</dd></dl>

<dl class="method">
<dt id="bytes.ljust">
<code class="descclassname">bytes.</code><code class="descname">ljust</code><span class="sig-paren">(</span><em>width</em><span class="optional">[</span>, <em>fillbyte</em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#bytes.ljust" title="Permalink to this definition">¶</a></dt>
<dt id="bytearray.ljust">
<code class="descclassname">bytearray.</code><code class="descname">ljust</code><span class="sig-paren">(</span><em>width</em><span class="optional">[</span>, <em>fillbyte</em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#bytearray.ljust" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a copy of the object left justified in a sequence of length <em>width</em>.
Padding is done using the specified <em>fillbyte</em> (default is an ASCII
space). For <a class="reference internal" href="functions.html#bytes" title="bytes"><code class="xref py py-class docutils literal"><span class="pre">bytes</span></code></a> objects, the original sequence is returned if
<em>width</em> is less than or equal to <code class="docutils literal"><span class="pre">len(s)</span></code>.</p>
<div class="admonition note">
<p class="first admonition-title">Note</p>
<p class="last">The bytearray version of this method does <em>not</em> operate in place -
it always produces a new object, even if no changes were made.</p>
</div>
</dd></dl>

<dl class="method">
<dt id="bytes.lstrip">
<code class="descclassname">bytes.</code><code class="descname">lstrip</code><span class="sig-paren">(</span><span class="optional">[</span><em>chars</em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#bytes.lstrip" title="Permalink to this definition">¶</a></dt>
<dt id="bytearray.lstrip">
<code class="descclassname">bytearray.</code><code class="descname">lstrip</code><span class="sig-paren">(</span><span class="optional">[</span><em>chars</em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#bytearray.lstrip" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a copy of the sequence with specified leading bytes removed.  The
<em>chars</em> argument is a binary sequence specifying the set of byte values to
be removed - the name refers to the fact this method is usually used with
ASCII characters.  If omitted or <code class="docutils literal"><span class="pre">None</span></code>, the <em>chars</em> argument defaults
to removing ASCII whitespace.  The <em>chars</em> argument is not a prefix;
rather, all combinations of its values are stripped:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">b</span><span class="s1">&#39;   spacious   &#39;</span><span class="o">.</span><span class="n">lstrip</span><span class="p">()</span>
<span class="go">b&#39;spacious   &#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">b</span><span class="s1">&#39;www.example.com&#39;</span><span class="o">.</span><span class="n">lstrip</span><span class="p">(</span><span class="n">b</span><span class="s1">&#39;cmowz.&#39;</span><span class="p">)</span>
<span class="go">b&#39;example.com&#39;</span>
</pre></div>
</div>
<p>The binary sequence of byte values to remove may be any
<a class="reference internal" href="../glossary.html#term-bytes-like-object"><span class="xref std std-term">bytes-like object</span></a>.</p>
<div class="admonition note">
<p class="first admonition-title">Note</p>
<p class="last">The bytearray version of this method does <em>not</em> operate in place -
it always produces a new object, even if no changes were made.</p>
</div>
</dd></dl>

<dl class="method">
<dt id="bytes.rjust">
<code class="descclassname">bytes.</code><code class="descname">rjust</code><span class="sig-paren">(</span><em>width</em><span class="optional">[</span>, <em>fillbyte</em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#bytes.rjust" title="Permalink to this definition">¶</a></dt>
<dt id="bytearray.rjust">
<code class="descclassname">bytearray.</code><code class="descname">rjust</code><span class="sig-paren">(</span><em>width</em><span class="optional">[</span>, <em>fillbyte</em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#bytearray.rjust" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a copy of the object right justified in a sequence of length <em>width</em>.
Padding is done using the specified <em>fillbyte</em> (default is an ASCII
space). For <a class="reference internal" href="functions.html#bytes" title="bytes"><code class="xref py py-class docutils literal"><span class="pre">bytes</span></code></a> objects, the original sequence is returned if
<em>width</em> is less than or equal to <code class="docutils literal"><span class="pre">len(s)</span></code>.</p>
<div class="admonition note">
<p class="first admonition-title">Note</p>
<p class="last">The bytearray version of this method does <em>not</em> operate in place -
it always produces a new object, even if no changes were made.</p>
</div>
</dd></dl>

<dl class="method">
<dt id="bytes.rsplit">
<code class="descclassname">bytes.</code><code class="descname">rsplit</code><span class="sig-paren">(</span><em>sep=None</em>, <em>maxsplit=-1</em><span class="sig-paren">)</span><a class="headerlink" href="#bytes.rsplit" title="Permalink to this definition">¶</a></dt>
<dt id="bytearray.rsplit">
<code class="descclassname">bytearray.</code><code class="descname">rsplit</code><span class="sig-paren">(</span><em>sep=None</em>, <em>maxsplit=-1</em><span class="sig-paren">)</span><a class="headerlink" href="#bytearray.rsplit" title="Permalink to this definition">¶</a></dt>
<dd><p>Split the binary sequence into subsequences of the same type, using <em>sep</em>
as the delimiter string. If <em>maxsplit</em> is given, at most <em>maxsplit</em> splits
are done, the <em>rightmost</em> ones.  If <em>sep</em> is not specified or <code class="docutils literal"><span class="pre">None</span></code>,
any subsequence consisting solely of ASCII whitespace is a separator.
Except for splitting from the right, <a class="reference internal" href="#bytearray.rsplit" title="bytearray.rsplit"><code class="xref py py-meth docutils literal"><span class="pre">rsplit()</span></code></a> behaves like
<a class="reference internal" href="#bytearray.split" title="bytearray.split"><code class="xref py py-meth docutils literal"><span class="pre">split()</span></code></a> which is described in detail below.</p>
</dd></dl>

<dl class="method">
<dt id="bytes.rstrip">
<code class="descclassname">bytes.</code><code class="descname">rstrip</code><span class="sig-paren">(</span><span class="optional">[</span><em>chars</em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#bytes.rstrip" title="Permalink to this definition">¶</a></dt>
<dt id="bytearray.rstrip">
<code class="descclassname">bytearray.</code><code class="descname">rstrip</code><span class="sig-paren">(</span><span class="optional">[</span><em>chars</em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#bytearray.rstrip" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a copy of the sequence with specified trailing bytes removed.  The
<em>chars</em> argument is a binary sequence specifying the set of byte values to
be removed - the name refers to the fact this method is usually used with
ASCII characters.  If omitted or <code class="docutils literal"><span class="pre">None</span></code>, the <em>chars</em> argument defaults to
removing ASCII whitespace.  The <em>chars</em> argument is not a suffix; rather,
all combinations of its values are stripped:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">b</span><span class="s1">&#39;   spacious   &#39;</span><span class="o">.</span><span class="n">rstrip</span><span class="p">()</span>
<span class="go">b&#39;   spacious&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">b</span><span class="s1">&#39;mississippi&#39;</span><span class="o">.</span><span class="n">rstrip</span><span class="p">(</span><span class="n">b</span><span class="s1">&#39;ipz&#39;</span><span class="p">)</span>
<span class="go">b&#39;mississ&#39;</span>
</pre></div>
</div>
<p>The binary sequence of byte values to remove may be any
<a class="reference internal" href="../glossary.html#term-bytes-like-object"><span class="xref std std-term">bytes-like object</span></a>.</p>
<div class="admonition note">
<p class="first admonition-title">Note</p>
<p class="last">The bytearray version of this method does <em>not</em> operate in place -
it always produces a new object, even if no changes were made.</p>
</div>
</dd></dl>

<dl class="method">
<dt id="bytes.split">
<code class="descclassname">bytes.</code><code class="descname">split</code><span class="sig-paren">(</span><em>sep=None</em>, <em>maxsplit=-1</em><span class="sig-paren">)</span><a class="headerlink" href="#bytes.split" title="Permalink to this definition">¶</a></dt>
<dt id="bytearray.split">
<code class="descclassname">bytearray.</code><code class="descname">split</code><span class="sig-paren">(</span><em>sep=None</em>, <em>maxsplit=-1</em><span class="sig-paren">)</span><a class="headerlink" href="#bytearray.split" title="Permalink to this definition">¶</a></dt>
<dd><p>Split the binary sequence into subsequences of the same type, using <em>sep</em>
as the delimiter string. If <em>maxsplit</em> is given and non-negative, at most
<em>maxsplit</em> splits are done (thus, the list will have at most <code class="docutils literal"><span class="pre">maxsplit+1</span></code>
elements).  If <em>maxsplit</em> is not specified or is <code class="docutils literal"><span class="pre">-1</span></code>, then there is no
limit on the number of splits (all possible splits are made).</p>
<p>If <em>sep</em> is given, consecutive delimiters are not grouped together and are
deemed to delimit empty subsequences (for example, <code class="docutils literal"><span class="pre">b'1,,2'.split(b',')</span></code>
returns <code class="docutils literal"><span class="pre">[b'1',</span> <span class="pre">b'',</span> <span class="pre">b'2']</span></code>).  The <em>sep</em> argument may consist of a
multibyte sequence (for example, <code class="docutils literal"><span class="pre">b'1&lt;&gt;2&lt;&gt;3'.split(b'&lt;&gt;')</span></code> returns
<code class="docutils literal"><span class="pre">[b'1',</span> <span class="pre">b'2',</span> <span class="pre">b'3']</span></code>). Splitting an empty sequence with a specified
separator returns <code class="docutils literal"><span class="pre">[b'']</span></code> or <code class="docutils literal"><span class="pre">[bytearray(b'')]</span></code> depending on the type
of object being split.  The <em>sep</em> argument may be any
<a class="reference internal" href="../glossary.html#term-bytes-like-object"><span class="xref std std-term">bytes-like object</span></a>.</p>
<p>For example:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">b</span><span class="s1">&#39;1,2,3&#39;</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">b</span><span class="s1">&#39;,&#39;</span><span class="p">)</span>
<span class="go">[b&#39;1&#39;, b&#39;2&#39;, b&#39;3&#39;]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">b</span><span class="s1">&#39;1,2,3&#39;</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">b</span><span class="s1">&#39;,&#39;</span><span class="p">,</span> <span class="n">maxsplit</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="go">[b&#39;1&#39;, b&#39;2,3&#39;]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">b</span><span class="s1">&#39;1,2,,3,&#39;</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">b</span><span class="s1">&#39;,&#39;</span><span class="p">)</span>
<span class="go">[b&#39;1&#39;, b&#39;2&#39;, b&#39;&#39;, b&#39;3&#39;, b&#39;&#39;]</span>
</pre></div>
</div>
<p>If <em>sep</em> is not specified or is <code class="docutils literal"><span class="pre">None</span></code>, a different splitting algorithm
is applied: runs of consecutive ASCII whitespace are regarded as a single
separator, and the result will contain no empty strings at the start or
end if the sequence has leading or trailing whitespace.  Consequently,
splitting an empty sequence or a sequence consisting solely of ASCII
whitespace without a specified separator returns <code class="docutils literal"><span class="pre">[]</span></code>.</p>
<p>For example:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">b</span><span class="s1">&#39;1 2 3&#39;</span><span class="o">.</span><span class="n">split</span><span class="p">()</span>
<span class="go">[b&#39;1&#39;, b&#39;2&#39;, b&#39;3&#39;]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">b</span><span class="s1">&#39;1 2 3&#39;</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">maxsplit</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="go">[b&#39;1&#39;, b&#39;2 3&#39;]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">b</span><span class="s1">&#39;   1   2   3   &#39;</span><span class="o">.</span><span class="n">split</span><span class="p">()</span>
<span class="go">[b&#39;1&#39;, b&#39;2&#39;, b&#39;3&#39;]</span>
</pre></div>
</div>
</dd></dl>

<dl class="method">
<dt id="bytes.strip">
<code class="descclassname">bytes.</code><code class="descname">strip</code><span class="sig-paren">(</span><span class="optional">[</span><em>chars</em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#bytes.strip" title="Permalink to this definition">¶</a></dt>
<dt id="bytearray.strip">
<code class="descclassname">bytearray.</code><code class="descname">strip</code><span class="sig-paren">(</span><span class="optional">[</span><em>chars</em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#bytearray.strip" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a copy of the sequence with specified leading and trailing bytes
removed. The <em>chars</em> argument is a binary sequence specifying the set of
byte values to be removed - the name refers to the fact this method is
usually used with ASCII characters.  If omitted or <code class="docutils literal"><span class="pre">None</span></code>, the <em>chars</em>
argument defaults to removing ASCII whitespace. The <em>chars</em> argument is
not a prefix or suffix; rather, all combinations of its values are
stripped:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">b</span><span class="s1">&#39;   spacious   &#39;</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>
<span class="go">b&#39;spacious&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">b</span><span class="s1">&#39;www.example.com&#39;</span><span class="o">.</span><span class="n">strip</span><span class="p">(</span><span class="n">b</span><span class="s1">&#39;cmowz.&#39;</span><span class="p">)</span>
<span class="go">b&#39;example&#39;</span>
</pre></div>
</div>
<p>The binary sequence of byte values to remove may be any
<a class="reference internal" href="../glossary.html#term-bytes-like-object"><span class="xref std std-term">bytes-like object</span></a>.</p>
<div class="admonition note">
<p class="first admonition-title">Note</p>
<p class="last">The bytearray version of this method does <em>not</em> operate in place -
it always produces a new object, even if no changes were made.</p>
</div>
</dd></dl>

<p>The following methods on bytes and bytearray objects assume the use of ASCII
compatible binary formats and should not be applied to arbitrary binary data.
Note that all of the bytearray methods in this section do <em>not</em> operate in
place, and instead produce new objects.</p>
<dl class="method">
<dt id="bytes.capitalize">
<code class="descclassname">bytes.</code><code class="descname">capitalize</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#bytes.capitalize" title="Permalink to this definition">¶</a></dt>
<dt id="bytearray.capitalize">
<code class="descclassname">bytearray.</code><code class="descname">capitalize</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#bytearray.capitalize" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a copy of the sequence with each byte interpreted as an ASCII
character, and the first byte capitalized and the rest lowercased.
Non-ASCII byte values are passed through unchanged.</p>
<div class="admonition note">
<p class="first admonition-title">Note</p>
<p class="last">The bytearray version of this method does <em>not</em> operate in place - it
always produces a new object, even if no changes were made.</p>
</div>
</dd></dl>

<dl class="method">
<dt id="bytes.expandtabs">
<code class="descclassname">bytes.</code><code class="descname">expandtabs</code><span class="sig-paren">(</span><em>tabsize=8</em><span class="sig-paren">)</span><a class="headerlink" href="#bytes.expandtabs" title="Permalink to this definition">¶</a></dt>
<dt id="bytearray.expandtabs">
<code class="descclassname">bytearray.</code><code class="descname">expandtabs</code><span class="sig-paren">(</span><em>tabsize=8</em><span class="sig-paren">)</span><a class="headerlink" href="#bytearray.expandtabs" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a copy of the sequence where all ASCII tab characters are replaced
by one or more ASCII spaces, depending on the current column and the given
tab size.  Tab positions occur every <em>tabsize</em> bytes (default is 8,
giving tab positions at columns 0, 8, 16 and so on).  To expand the
sequence, the current column is set to zero and the sequence is examined
byte by byte.  If the byte is an ASCII tab character (<code class="docutils literal"><span class="pre">b'\t'</span></code>), one or
more space characters are inserted in the result until the current column
is equal to the next tab position. (The tab character itself is not
copied.)  If the current byte is an ASCII newline (<code class="docutils literal"><span class="pre">b'\n'</span></code>) or
carriage return (<code class="docutils literal"><span class="pre">b'\r'</span></code>), it is copied and the current column is reset
to zero.  Any other byte value is copied unchanged and the current column
is incremented by one regardless of how the byte value is represented when
printed:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">b</span><span class="s1">&#39;01</span><span class="se">\t</span><span class="s1">012</span><span class="se">\t</span><span class="s1">0123</span><span class="se">\t</span><span class="s1">01234&#39;</span><span class="o">.</span><span class="n">expandtabs</span><span class="p">()</span>
<span class="go">b&#39;01      012     0123    01234&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">b</span><span class="s1">&#39;01</span><span class="se">\t</span><span class="s1">012</span><span class="se">\t</span><span class="s1">0123</span><span class="se">\t</span><span class="s1">01234&#39;</span><span class="o">.</span><span class="n">expandtabs</span><span class="p">(</span><span class="mi">4</span><span class="p">)</span>
<span class="go">b&#39;01  012 0123    01234&#39;</span>
</pre></div>
</div>
<div class="admonition note">
<p class="first admonition-title">Note</p>
<p class="last">The bytearray version of this method does <em>not</em> operate in place - it
always produces a new object, even if no changes were made.</p>
</div>
</dd></dl>

<dl class="method">
<dt id="bytes.isalnum">
<code class="descclassname">bytes.</code><code class="descname">isalnum</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#bytes.isalnum" title="Permalink to this definition">¶</a></dt>
<dt id="bytearray.isalnum">
<code class="descclassname">bytearray.</code><code class="descname">isalnum</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#bytearray.isalnum" title="Permalink to this definition">¶</a></dt>
<dd><p>Return true if all bytes in the sequence are alphabetical ASCII characters
or ASCII decimal digits and the sequence is not empty, false otherwise.
Alphabetic ASCII characters are those byte values in the sequence
<code class="docutils literal"><span class="pre">b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'</span></code>. ASCII decimal
digits are those byte values in the sequence <code class="docutils literal"><span class="pre">b'0123456789'</span></code>.</p>
<p>For example:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">b</span><span class="s1">&#39;ABCabc1&#39;</span><span class="o">.</span><span class="n">isalnum</span><span class="p">()</span>
<span class="go">True</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">b</span><span class="s1">&#39;ABC abc1&#39;</span><span class="o">.</span><span class="n">isalnum</span><span class="p">()</span>
<span class="go">False</span>
</pre></div>
</div>
</dd></dl>

<dl class="method">
<dt id="bytes.isalpha">
<code class="descclassname">bytes.</code><code class="descname">isalpha</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#bytes.isalpha" title="Permalink to this definition">¶</a></dt>
<dt id="bytearray.isalpha">
<code class="descclassname">bytearray.</code><code class="descname">isalpha</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#bytearray.isalpha" title="Permalink to this definition">¶</a></dt>
<dd><p>Return true if all bytes in the sequence are alphabetic ASCII characters
and the sequence is not empty, false otherwise.  Alphabetic ASCII
characters are those byte values in the sequence
<code class="docutils literal"><span class="pre">b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'</span></code>.</p>
<p>For example:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">b</span><span class="s1">&#39;ABCabc&#39;</span><span class="o">.</span><span class="n">isalpha</span><span class="p">()</span>
<span class="go">True</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">b</span><span class="s1">&#39;ABCabc1&#39;</span><span class="o">.</span><span class="n">isalpha</span><span class="p">()</span>
<span class="go">False</span>
</pre></div>
</div>
</dd></dl>

<dl class="method">
<dt id="bytes.isdigit">
<code class="descclassname">bytes.</code><code class="descname">isdigit</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#bytes.isdigit" title="Permalink to this definition">¶</a></dt>
<dt id="bytearray.isdigit">
<code class="descclassname">bytearray.</code><code class="descname">isdigit</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#bytearray.isdigit" title="Permalink to this definition">¶</a></dt>
<dd><p>Return true if all bytes in the sequence are ASCII decimal digits
and the sequence is not empty, false otherwise. ASCII decimal digits are
those byte values in the sequence <code class="docutils literal"><span class="pre">b'0123456789'</span></code>.</p>
<p>For example:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">b</span><span class="s1">&#39;1234&#39;</span><span class="o">.</span><span class="n">isdigit</span><span class="p">()</span>
<span class="go">True</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">b</span><span class="s1">&#39;1.23&#39;</span><span class="o">.</span><span class="n">isdigit</span><span class="p">()</span>
<span class="go">False</span>
</pre></div>
</div>
</dd></dl>

<dl class="method">
<dt id="bytes.islower">
<code class="descclassname">bytes.</code><code class="descname">islower</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#bytes.islower" title="Permalink to this definition">¶</a></dt>
<dt id="bytearray.islower">
<code class="descclassname">bytearray.</code><code class="descname">islower</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#bytearray.islower" title="Permalink to this definition">¶</a></dt>
<dd><p>Return true if there is at least one lowercase ASCII character
in the sequence and no uppercase ASCII characters, false otherwise.</p>
<p>For example:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">b</span><span class="s1">&#39;hello world&#39;</span><span class="o">.</span><span class="n">islower</span><span class="p">()</span>
<span class="go">True</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">b</span><span class="s1">&#39;Hello world&#39;</span><span class="o">.</span><span class="n">islower</span><span class="p">()</span>
<span class="go">False</span>
</pre></div>
</div>
<p>Lowercase ASCII characters are those byte values in the sequence
<code class="docutils literal"><span class="pre">b'abcdefghijklmnopqrstuvwxyz'</span></code>. Uppercase ASCII characters
are those byte values in the sequence <code class="docutils literal"><span class="pre">b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="bytes.isspace">
<code class="descclassname">bytes.</code><code class="descname">isspace</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#bytes.isspace" title="Permalink to this definition">¶</a></dt>
<dt id="bytearray.isspace">
<code class="descclassname">bytearray.</code><code class="descname">isspace</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#bytearray.isspace" title="Permalink to this definition">¶</a></dt>
<dd><p>Return true if all bytes in the sequence are ASCII whitespace and the
sequence is not empty, false otherwise.  ASCII whitespace characters are
those byte values in the sequence <code class="docutils literal"><span class="pre">b'</span> <span class="pre">\t\n\r\x0b\f'</span></code> (space, tab, newline,
carriage return, vertical tab, form feed).</p>
</dd></dl>

<dl class="method">
<dt id="bytes.istitle">
<code class="descclassname">bytes.</code><code class="descname">istitle</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#bytes.istitle" title="Permalink to this definition">¶</a></dt>
<dt id="bytearray.istitle">
<code class="descclassname">bytearray.</code><code class="descname">istitle</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#bytearray.istitle" title="Permalink to this definition">¶</a></dt>
<dd><p>Return true if the sequence is ASCII titlecase and the sequence is not
empty, false otherwise. See <a class="reference internal" href="#bytes.title" title="bytes.title"><code class="xref py py-meth docutils literal"><span class="pre">bytes.title()</span></code></a> for more details on the
definition of &#8220;titlecase&#8221;.</p>
<p>For example:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">b</span><span class="s1">&#39;Hello World&#39;</span><span class="o">.</span><span class="n">istitle</span><span class="p">()</span>
<span class="go">True</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">b</span><span class="s1">&#39;Hello world&#39;</span><span class="o">.</span><span class="n">istitle</span><span class="p">()</span>
<span class="go">False</span>
</pre></div>
</div>
</dd></dl>

<dl class="method">
<dt id="bytes.isupper">
<code class="descclassname">bytes.</code><code class="descname">isupper</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#bytes.isupper" title="Permalink to this definition">¶</a></dt>
<dt id="bytearray.isupper">
<code class="descclassname">bytearray.</code><code class="descname">isupper</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#bytearray.isupper" title="Permalink to this definition">¶</a></dt>
<dd><p>Return true if there is at least one uppercase alphabetic ASCII character
in the sequence and no lowercase ASCII characters, false otherwise.</p>
<p>For example:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">b</span><span class="s1">&#39;HELLO WORLD&#39;</span><span class="o">.</span><span class="n">isupper</span><span class="p">()</span>
<span class="go">True</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">b</span><span class="s1">&#39;Hello world&#39;</span><span class="o">.</span><span class="n">isupper</span><span class="p">()</span>
<span class="go">False</span>
</pre></div>
</div>
<p>Lowercase ASCII characters are those byte values in the sequence
<code class="docutils literal"><span class="pre">b'abcdefghijklmnopqrstuvwxyz'</span></code>. Uppercase ASCII characters
are those byte values in the sequence <code class="docutils literal"><span class="pre">b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="bytes.lower">
<code class="descclassname">bytes.</code><code class="descname">lower</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#bytes.lower" title="Permalink to this definition">¶</a></dt>
<dt id="bytearray.lower">
<code class="descclassname">bytearray.</code><code class="descname">lower</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#bytearray.lower" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a copy of the sequence with all the uppercase ASCII characters
converted to their corresponding lowercase counterpart.</p>
<p>For example:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">b</span><span class="s1">&#39;Hello World&#39;</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span>
<span class="go">b&#39;hello world&#39;</span>
</pre></div>
</div>
<p>Lowercase ASCII characters are those byte values in the sequence
<code class="docutils literal"><span class="pre">b'abcdefghijklmnopqrstuvwxyz'</span></code>. Uppercase ASCII characters
are those byte values in the sequence <code class="docutils literal"><span class="pre">b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'</span></code>.</p>
<div class="admonition note">
<p class="first admonition-title">Note</p>
<p class="last">The bytearray version of this method does <em>not</em> operate in place - it
always produces a new object, even if no changes were made.</p>
</div>
</dd></dl>

<span class="target" id="index-41"></span><dl class="method">
<dt id="bytes.splitlines">
<code class="descclassname">bytes.</code><code class="descname">splitlines</code><span class="sig-paren">(</span><em>keepends=False</em><span class="sig-paren">)</span><a class="headerlink" href="#bytes.splitlines" title="Permalink to this definition">¶</a></dt>
<dt id="bytearray.splitlines">
<code class="descclassname">bytearray.</code><code class="descname">splitlines</code><span class="sig-paren">(</span><em>keepends=False</em><span class="sig-paren">)</span><a class="headerlink" href="#bytearray.splitlines" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a list of the lines in the binary sequence, breaking at ASCII
line boundaries. This method uses the <a class="reference internal" href="../glossary.html#term-universal-newlines"><span class="xref std std-term">universal newlines</span></a> approach
to splitting lines. Line breaks are not included in the resulting list
unless <em>keepends</em> is given and true.</p>
<p>For example:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">b</span><span class="s1">&#39;ab c</span><span class="se">\n\n</span><span class="s1">de fg</span><span class="se">\r</span><span class="s1">kl</span><span class="se">\r\n</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">splitlines</span><span class="p">()</span>
<span class="go">[b&#39;ab c&#39;, b&#39;&#39;, b&#39;de fg&#39;, b&#39;kl&#39;]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">b</span><span class="s1">&#39;ab c</span><span class="se">\n\n</span><span class="s1">de fg</span><span class="se">\r</span><span class="s1">kl</span><span class="se">\r\n</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">splitlines</span><span class="p">(</span><span class="n">keepends</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="go">[b&#39;ab c\n&#39;, b&#39;\n&#39;, b&#39;de fg\r&#39;, b&#39;kl\r\n&#39;]</span>
</pre></div>
</div>
<p>Unlike <a class="reference internal" href="#bytes.split" title="bytes.split"><code class="xref py py-meth docutils literal"><span class="pre">split()</span></code></a> when a delimiter string <em>sep</em> is given, this
method returns an empty list for the empty string, and a terminal line
break does not result in an extra line:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">b</span><span class="s2">&quot;&quot;</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">b</span><span class="s1">&#39;</span><span class="se">\n</span><span class="s1">&#39;</span><span class="p">),</span> <span class="n">b</span><span class="s2">&quot;Two lines</span><span class="se">\n</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">b</span><span class="s1">&#39;</span><span class="se">\n</span><span class="s1">&#39;</span><span class="p">)</span>
<span class="go">([b&#39;&#39;], [b&#39;Two lines&#39;, b&#39;&#39;])</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">b</span><span class="s2">&quot;&quot;</span><span class="o">.</span><span class="n">splitlines</span><span class="p">(),</span> <span class="n">b</span><span class="s2">&quot;One line</span><span class="se">\n</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">splitlines</span><span class="p">()</span>
<span class="go">([], [b&#39;One line&#39;])</span>
</pre></div>
</div>
</dd></dl>

<dl class="method">
<dt id="bytes.swapcase">
<code class="descclassname">bytes.</code><code class="descname">swapcase</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#bytes.swapcase" title="Permalink to this definition">¶</a></dt>
<dt id="bytearray.swapcase">
<code class="descclassname">bytearray.</code><code class="descname">swapcase</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#bytearray.swapcase" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a copy of the sequence with all the lowercase ASCII characters
converted to their corresponding uppercase counterpart and vice-versa.</p>
<p>For example:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">b</span><span class="s1">&#39;Hello World&#39;</span><span class="o">.</span><span class="n">swapcase</span><span class="p">()</span>
<span class="go">b&#39;hELLO wORLD&#39;</span>
</pre></div>
</div>
<p>Lowercase ASCII characters are those byte values in the sequence
<code class="docutils literal"><span class="pre">b'abcdefghijklmnopqrstuvwxyz'</span></code>. Uppercase ASCII characters
are those byte values in the sequence <code class="docutils literal"><span class="pre">b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'</span></code>.</p>
<p>Unlike <a class="reference internal" href="#str.swapcase" title="str.swapcase"><code class="xref py py-func docutils literal"><span class="pre">str.swapcase()</span></code></a>, it is always the case that
<code class="docutils literal"><span class="pre">bin.swapcase().swapcase()</span> <span class="pre">==</span> <span class="pre">bin</span></code> for the binary versions. Case
conversions are symmetrical in ASCII, even though that is not generally
true for arbitrary Unicode code points.</p>
<div class="admonition note">
<p class="first admonition-title">Note</p>
<p class="last">The bytearray version of this method does <em>not</em> operate in place - it
always produces a new object, even if no changes were made.</p>
</div>
</dd></dl>

<dl class="method">
<dt id="bytes.title">
<code class="descclassname">bytes.</code><code class="descname">title</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#bytes.title" title="Permalink to this definition">¶</a></dt>
<dt id="bytearray.title">
<code class="descclassname">bytearray.</code><code class="descname">title</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#bytearray.title" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a titlecased version of the binary sequence where words start with
an uppercase ASCII character and the remaining characters are lowercase.
Uncased byte values are left unmodified.</p>
<p>For example:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">b</span><span class="s1">&#39;Hello world&#39;</span><span class="o">.</span><span class="n">title</span><span class="p">()</span>
<span class="go">b&#39;Hello World&#39;</span>
</pre></div>
</div>
<p>Lowercase ASCII characters are those byte values in the sequence
<code class="docutils literal"><span class="pre">b'abcdefghijklmnopqrstuvwxyz'</span></code>. Uppercase ASCII characters
are those byte values in the sequence <code class="docutils literal"><span class="pre">b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'</span></code>.
All other byte values are uncased.</p>
<p>The algorithm uses a simple language-independent definition of a word as
groups of consecutive letters.  The definition works in many contexts but
it means that apostrophes in contractions and possessives form word
boundaries, which may not be the desired result:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">b</span><span class="s2">&quot;they&#39;re bill&#39;s friends from the UK&quot;</span><span class="o">.</span><span class="n">title</span><span class="p">()</span>
<span class="go">b&quot;They&#39;Re Bill&#39;S Friends From The Uk&quot;</span>
</pre></div>
</div>
<p>A workaround for apostrophes can be constructed using regular expressions:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="kn">import</span> <span class="nn">re</span>
<span class="gp">&gt;&gt;&gt; </span><span class="k">def</span> <span class="nf">titlecase</span><span class="p">(</span><span class="n">s</span><span class="p">):</span>
<span class="gp">... </span>    <span class="k">return</span> <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="n">rb</span><span class="s2">&quot;[A-Za-z]+(&#39;[A-Za-z]+)?&quot;</span><span class="p">,</span>
<span class="gp">... </span>                  <span class="k">lambda</span> <span class="n">mo</span><span class="p">:</span> <span class="n">mo</span><span class="o">.</span><span class="n">group</span><span class="p">(</span><span class="mi">0</span><span class="p">)[</span><span class="mi">0</span><span class="p">:</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">upper</span><span class="p">()</span> <span class="o">+</span>
<span class="gp">... </span>                             <span class="n">mo</span><span class="o">.</span><span class="n">group</span><span class="p">(</span><span class="mi">0</span><span class="p">)[</span><span class="mi">1</span><span class="p">:]</span><span class="o">.</span><span class="n">lower</span><span class="p">(),</span>
<span class="gp">... </span>                  <span class="n">s</span><span class="p">)</span>
<span class="gp">...</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">titlecase</span><span class="p">(</span><span class="n">b</span><span class="s2">&quot;they&#39;re bill&#39;s friends.&quot;</span><span class="p">)</span>
<span class="go">b&quot;They&#39;re Bill&#39;s Friends.&quot;</span>
</pre></div>
</div>
<div class="admonition note">
<p class="first admonition-title">Note</p>
<p class="last">The bytearray version of this method does <em>not</em> operate in place - it
always produces a new object, even if no changes were made.</p>
</div>
</dd></dl>

<dl class="method">
<dt id="bytes.upper">
<code class="descclassname">bytes.</code><code class="descname">upper</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#bytes.upper" title="Permalink to this definition">¶</a></dt>
<dt id="bytearray.upper">
<code class="descclassname">bytearray.</code><code class="descname">upper</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#bytearray.upper" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a copy of the sequence with all the lowercase ASCII characters
converted to their corresponding uppercase counterpart.</p>
<p>For example:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">b</span><span class="s1">&#39;Hello World&#39;</span><span class="o">.</span><span class="n">upper</span><span class="p">()</span>
<span class="go">b&#39;HELLO WORLD&#39;</span>
</pre></div>
</div>
<p>Lowercase ASCII characters are those byte values in the sequence
<code class="docutils literal"><span class="pre">b'abcdefghijklmnopqrstuvwxyz'</span></code>. Uppercase ASCII characters
are those byte values in the sequence <code class="docutils literal"><span class="pre">b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'</span></code>.</p>
<div class="admonition note">
<p class="first admonition-title">Note</p>
<p class="last">The bytearray version of this method does <em>not</em> operate in place - it
always produces a new object, even if no changes were made.</p>
</div>
</dd></dl>

<dl class="method">
<dt id="bytes.zfill">
<code class="descclassname">bytes.</code><code class="descname">zfill</code><span class="sig-paren">(</span><em>width</em><span class="sig-paren">)</span><a class="headerlink" href="#bytes.zfill" title="Permalink to this definition">¶</a></dt>
<dt id="bytearray.zfill">
<code class="descclassname">bytearray.</code><code class="descname">zfill</code><span class="sig-paren">(</span><em>width</em><span class="sig-paren">)</span><a class="headerlink" href="#bytearray.zfill" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a copy of the sequence left filled with ASCII <code class="docutils literal"><span class="pre">b'0'</span></code> digits to
make a sequence of length <em>width</em>. A leading sign prefix (<code class="docutils literal"><span class="pre">b'+'</span></code>/
<code class="docutils literal"><span class="pre">b'-'</span></code> is handled by inserting the padding <em>after</em> the sign character
rather than before. For <a class="reference internal" href="functions.html#bytes" title="bytes"><code class="xref py py-class docutils literal"><span class="pre">bytes</span></code></a> objects, the original sequence is
returned if <em>width</em> is less than or equal to <code class="docutils literal"><span class="pre">len(seq)</span></code>.</p>
<p>For example:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">b</span><span class="s2">&quot;42&quot;</span><span class="o">.</span><span class="n">zfill</span><span class="p">(</span><span class="mi">5</span><span class="p">)</span>
<span class="go">b&#39;00042&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">b</span><span class="s2">&quot;-42&quot;</span><span class="o">.</span><span class="n">zfill</span><span class="p">(</span><span class="mi">5</span><span class="p">)</span>
<span class="go">b&#39;-0042&#39;</span>
</pre></div>
</div>
<div class="admonition note">
<p class="first admonition-title">Note</p>
<p class="last">The bytearray version of this method does <em>not</em> operate in place - it
always produces a new object, even if no changes were made.</p>
</div>
</dd></dl>

</div>
<div class="section" id="printf-style-bytes-formatting">
<span id="bytes-formatting"></span><h3>4.8.4. <code class="docutils literal"><span class="pre">printf</span></code>-style Bytes Formatting<a class="headerlink" href="#printf-style-bytes-formatting" title="Permalink to this headline">¶</a></h3>
<div class="admonition note" id="index-42">
<p class="first admonition-title">Note</p>
<p class="last">The formatting operations described here exhibit a variety of quirks that
lead to a number of common errors (such as failing to display tuples and
dictionaries correctly).  If the value being printed may be a tuple or
dictionary, wrap it in a tuple.</p>
</div>
<p>Bytes objects (<code class="docutils literal"><span class="pre">bytes</span></code>/<code class="docutils literal"><span class="pre">bytearray</span></code>) have one unique built-in operation:
the <code class="docutils literal"><span class="pre">%</span></code> operator (modulo).
This is also known as the bytes <em>formatting</em> or <em>interpolation</em> operator.
Given <code class="docutils literal"><span class="pre">format</span> <span class="pre">%</span> <span class="pre">values</span></code> (where <em>format</em> is a bytes object), <code class="docutils literal"><span class="pre">%</span></code> conversion
specifications in <em>format</em> are replaced with zero or more elements of <em>values</em>.
The effect is similar to using the <code class="xref c c-func docutils literal"><span class="pre">sprintf()</span></code> in the C language.</p>
<p>If <em>format</em> requires a single argument, <em>values</em> may be a single non-tuple
object. <a class="footnote-reference" href="#id15" id="id10">[5]</a>  Otherwise, <em>values</em> must be a tuple with exactly the number of
items specified by the format bytes object, or a single mapping object (for
example, a dictionary).</p>
<p>A conversion specifier contains two or more characters and has the following
components, which must occur in this order:</p>
<ol class="arabic simple">
<li>The <code class="docutils literal"><span class="pre">'%'</span></code> character, which marks the start of the specifier.</li>
<li>Mapping key (optional), consisting of a parenthesised sequence of characters
(for example, <code class="docutils literal"><span class="pre">(somename)</span></code>).</li>
<li>Conversion flags (optional), which affect the result of some conversion
types.</li>
<li>Minimum field width (optional).  If specified as an <code class="docutils literal"><span class="pre">'*'</span></code> (asterisk), the
actual width is read from the next element of the tuple in <em>values</em>, and the
object to convert comes after the minimum field width and optional precision.</li>
<li>Precision (optional), given as a <code class="docutils literal"><span class="pre">'.'</span></code> (dot) followed by the precision.  If
specified as <code class="docutils literal"><span class="pre">'*'</span></code> (an asterisk), the actual precision is read from the next
element of the tuple in <em>values</em>, and the value to convert comes after the
precision.</li>
<li>Length modifier (optional).</li>
<li>Conversion type.</li>
</ol>
<p>When the right argument is a dictionary (or other mapping type), then the
formats in the bytes object <em>must</em> include a parenthesised mapping key into that
dictionary inserted immediately after the <code class="docutils literal"><span class="pre">'%'</span></code> character. The mapping key
selects the value to be formatted from the mapping.  For example:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="nb">print</span><span class="p">(</span><span class="n">b</span><span class="s1">&#39;</span><span class="si">%(language)s</span><span class="s1"> has </span><span class="si">%(number)03d</span><span class="s1"> quote types.&#39;</span> <span class="o">%</span>
<span class="gp">... </span>      <span class="p">{</span><span class="n">b</span><span class="s1">&#39;language&#39;</span><span class="p">:</span> <span class="n">b</span><span class="s2">&quot;Python&quot;</span><span class="p">,</span> <span class="n">b</span><span class="s2">&quot;number&quot;</span><span class="p">:</span> <span class="mi">2</span><span class="p">})</span>
<span class="go">b&#39;Python has 002 quote types.&#39;</span>
</pre></div>
</div>
<p>In this case no <code class="docutils literal"><span class="pre">*</span></code> specifiers may occur in a format (since they require a
sequential parameter list).</p>
<p>The conversion flag characters are:</p>
<table border="1" class="docutils">
<colgroup>
<col width="12%" />
<col width="88%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Flag</th>
<th class="head">Meaning</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><code class="docutils literal"><span class="pre">'#'</span></code></td>
<td>The value conversion will use the &#8220;alternate form&#8221; (where defined
below).</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">'0'</span></code></td>
<td>The conversion will be zero padded for numeric values.</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">'-'</span></code></td>
<td>The converted value is left adjusted (overrides the <code class="docutils literal"><span class="pre">'0'</span></code>
conversion if both are given).</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">'</span> <span class="pre">'</span></code></td>
<td>(a space) A blank should be left before a positive number (or empty
string) produced by a signed conversion.</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">'+'</span></code></td>
<td>A sign character (<code class="docutils literal"><span class="pre">'+'</span></code> or <code class="docutils literal"><span class="pre">'-'</span></code>) will precede the conversion
(overrides a &#8220;space&#8221; flag).</td>
</tr>
</tbody>
</table>
<p>A length modifier (<code class="docutils literal"><span class="pre">h</span></code>, <code class="docutils literal"><span class="pre">l</span></code>, or <code class="docutils literal"><span class="pre">L</span></code>) may be present, but is ignored as it
is not necessary for Python &#8211; so e.g. <code class="docutils literal"><span class="pre">%ld</span></code> is identical to <code class="docutils literal"><span class="pre">%d</span></code>.</p>
<p>The conversion types are:</p>
<table border="1" class="docutils">
<colgroup>
<col width="17%" />
<col width="74%" />
<col width="10%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Conversion</th>
<th class="head">Meaning</th>
<th class="head">Notes</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><code class="docutils literal"><span class="pre">'d'</span></code></td>
<td>Signed integer decimal.</td>
<td>&nbsp;</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">'i'</span></code></td>
<td>Signed integer decimal.</td>
<td>&nbsp;</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">'o'</span></code></td>
<td>Signed octal value.</td>
<td>(1)</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">'u'</span></code></td>
<td>Obsolete type &#8211; it is identical to <code class="docutils literal"><span class="pre">'d'</span></code>.</td>
<td>(8)</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">'x'</span></code></td>
<td>Signed hexadecimal (lowercase).</td>
<td>(2)</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">'X'</span></code></td>
<td>Signed hexadecimal (uppercase).</td>
<td>(2)</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">'e'</span></code></td>
<td>Floating point exponential format (lowercase).</td>
<td>(3)</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">'E'</span></code></td>
<td>Floating point exponential format (uppercase).</td>
<td>(3)</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">'f'</span></code></td>
<td>Floating point decimal format.</td>
<td>(3)</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">'F'</span></code></td>
<td>Floating point decimal format.</td>
<td>(3)</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">'g'</span></code></td>
<td>Floating point format. Uses lowercase exponential
format if exponent is less than -4 or not less than
precision, decimal format otherwise.</td>
<td>(4)</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">'G'</span></code></td>
<td>Floating point format. Uses uppercase exponential
format if exponent is less than -4 or not less than
precision, decimal format otherwise.</td>
<td>(4)</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">'c'</span></code></td>
<td>Single byte (accepts integer or single
byte objects).</td>
<td>&nbsp;</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">'b'</span></code></td>
<td>Bytes (any object that follows the
<a class="reference internal" href="../c-api/buffer.html#bufferobjects"><span>buffer protocol</span></a> or has
<a class="reference internal" href="../reference/datamodel.html#object.__bytes__" title="object.__bytes__"><code class="xref py py-meth docutils literal"><span class="pre">__bytes__()</span></code></a>).</td>
<td>(5)</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">'s'</span></code></td>
<td><code class="docutils literal"><span class="pre">'s'</span></code> is an alias for <code class="docutils literal"><span class="pre">'b'</span></code> and should only
be used for Python2/3 code bases.</td>
<td>(6)</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">'a'</span></code></td>
<td>Bytes (converts any Python object using
<code class="docutils literal"><span class="pre">repr(obj).encode('ascii','backslashreplace)</span></code>).</td>
<td>(5)</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">'r'</span></code></td>
<td><code class="docutils literal"><span class="pre">'r'</span></code> is an alias for <code class="docutils literal"><span class="pre">'a'</span></code> and should only
be used for Python2/3 code bases.</td>
<td>(7)</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">'%'</span></code></td>
<td>No argument is converted, results in a <code class="docutils literal"><span class="pre">'%'</span></code>
character in the result.</td>
<td>&nbsp;</td>
</tr>
</tbody>
</table>
<p>Notes:</p>
<ol class="arabic">
<li><p class="first">The alternate form causes a leading octal specifier (<code class="docutils literal"><span class="pre">'0o'</span></code>) to be
inserted before the first digit.</p>
</li>
<li><p class="first">The alternate form causes a leading <code class="docutils literal"><span class="pre">'0x'</span></code> or <code class="docutils literal"><span class="pre">'0X'</span></code> (depending on whether
the <code class="docutils literal"><span class="pre">'x'</span></code> or <code class="docutils literal"><span class="pre">'X'</span></code> format was used) to be inserted before the first digit.</p>
</li>
<li><p class="first">The alternate form causes the result to always contain a decimal point, even if
no digits follow it.</p>
<p>The precision determines the number of digits after the decimal point and
defaults to 6.</p>
</li>
<li><p class="first">The alternate form causes the result to always contain a decimal point, and
trailing zeroes are not removed as they would otherwise be.</p>
<p>The precision determines the number of significant digits before and after the
decimal point and defaults to 6.</p>
</li>
<li><p class="first">If precision is <code class="docutils literal"><span class="pre">N</span></code>, the output is truncated to <code class="docutils literal"><span class="pre">N</span></code> characters.</p>
</li>
<li><p class="first"><code class="docutils literal"><span class="pre">b'%s'</span></code> is deprecated, but will not be removed during the 3.x series.</p>
</li>
<li><p class="first"><code class="docutils literal"><span class="pre">b'%r'</span></code> is deprecated, but will not be removed during the 3.x series.</p>
</li>
<li><p class="first">See <span class="target" id="index-43"></span><a class="pep reference external" href="https://www.python.org/dev/peps/pep-0237"><strong>PEP 237</strong></a>.</p>
</li>
</ol>
<div class="admonition note">
<p class="first admonition-title">Note</p>
<p class="last">The bytearray version of this method does <em>not</em> operate in place - it
always produces a new object, even if no changes were made.</p>
</div>
<div class="admonition seealso">
<p class="first admonition-title">See also</p>
<p class="last"><span class="target" id="index-44"></span><a class="pep reference external" href="https://www.python.org/dev/peps/pep-0461"><strong>PEP 461</strong></a>.</p>
</div>
<div class="versionadded">
<p><span class="versionmodified">New in version 3.5.</span></p>
</div>
</div>
<div class="section" id="memory-views">
<span id="typememoryview"></span><h3>4.8.5. Memory Views<a class="headerlink" href="#memory-views" title="Permalink to this headline">¶</a></h3>
<p><a class="reference internal" href="#memoryview" title="memoryview"><code class="xref py py-class docutils literal"><span class="pre">memoryview</span></code></a> objects allow Python code to access the internal data
of an object that supports the <a class="reference internal" href="../c-api/buffer.html#bufferobjects"><span>buffer protocol</span></a> without
copying.</p>
<dl class="class">
<dt id="memoryview">
<em class="property">class </em><code class="descname">memoryview</code><span class="sig-paren">(</span><em>obj</em><span class="sig-paren">)</span><a class="headerlink" href="#memoryview" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a <a class="reference internal" href="#memoryview" title="memoryview"><code class="xref py py-class docutils literal"><span class="pre">memoryview</span></code></a> that references <em>obj</em>.  <em>obj</em> must support the
buffer protocol.  Built-in objects that support the buffer protocol include
<a class="reference internal" href="functions.html#bytes" title="bytes"><code class="xref py py-class docutils literal"><span class="pre">bytes</span></code></a> and <a class="reference internal" href="functions.html#bytearray" title="bytearray"><code class="xref py py-class docutils literal"><span class="pre">bytearray</span></code></a>.</p>
<p>A <a class="reference internal" href="#memoryview" title="memoryview"><code class="xref py py-class docutils literal"><span class="pre">memoryview</span></code></a> has the notion of an <em>element</em>, which is the
atomic memory unit handled by the originating object <em>obj</em>.  For many
simple types such as <a class="reference internal" href="functions.html#bytes" title="bytes"><code class="xref py py-class docutils literal"><span class="pre">bytes</span></code></a> and <a class="reference internal" href="functions.html#bytearray" title="bytearray"><code class="xref py py-class docutils literal"><span class="pre">bytearray</span></code></a>, an element
is a single byte, but other types such as <a class="reference internal" href="array.html#array.array" title="array.array"><code class="xref py py-class docutils literal"><span class="pre">array.array</span></code></a> may have
bigger elements.</p>
<p><code class="docutils literal"><span class="pre">len(view)</span></code> is equal to the length of <a class="reference internal" href="#memoryview.tolist" title="memoryview.tolist"><code class="xref py py-class docutils literal"><span class="pre">tolist</span></code></a>.
If <code class="docutils literal"><span class="pre">view.ndim</span> <span class="pre">=</span> <span class="pre">0</span></code>, the length is 1. If <code class="docutils literal"><span class="pre">view.ndim</span> <span class="pre">=</span> <span class="pre">1</span></code>, the length
is equal to the number of elements in the view. For higher dimensions,
the length is equal to the length of the nested list representation of
the view. The <a class="reference internal" href="#memoryview.itemsize" title="memoryview.itemsize"><code class="xref py py-class docutils literal"><span class="pre">itemsize</span></code></a> attribute will give you the
number of bytes in a single element.</p>
<p>A <a class="reference internal" href="#memoryview" title="memoryview"><code class="xref py py-class docutils literal"><span class="pre">memoryview</span></code></a> supports slicing and indexing to expose its data.
One-dimensional slicing will result in a subview:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">v</span> <span class="o">=</span> <span class="nb">memoryview</span><span class="p">(</span><span class="n">b</span><span class="s1">&#39;abcefg&#39;</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">v</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
<span class="go">98</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">v</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
<span class="go">103</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">v</span><span class="p">[</span><span class="mi">1</span><span class="p">:</span><span class="mi">4</span><span class="p">]</span>
<span class="go">&lt;memory at 0x7f3ddc9f4350&gt;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">bytes</span><span class="p">(</span><span class="n">v</span><span class="p">[</span><span class="mi">1</span><span class="p">:</span><span class="mi">4</span><span class="p">])</span>
<span class="go">b&#39;bce&#39;</span>
</pre></div>
</div>
<p>If <a class="reference internal" href="#memoryview.format" title="memoryview.format"><code class="xref py py-class docutils literal"><span class="pre">format</span></code></a> is one of the native format specifiers
from the <a class="reference internal" href="struct.html#module-struct" title="struct: Interpret bytes as packed binary data."><code class="xref py py-mod docutils literal"><span class="pre">struct</span></code></a> module, indexing with an integer or a tuple of
integers is also supported and returns a single <em>element</em> with
the correct type.  One-dimensional memoryviews can be indexed
with an integer or a one-integer tuple.  Multi-dimensional memoryviews
can be indexed with tuples of exactly <em>ndim</em> integers where <em>ndim</em> is
the number of dimensions.  Zero-dimensional memoryviews can be indexed
with the empty tuple.</p>
<p>Here is an example with a non-byte format:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="kn">import</span> <span class="nn">array</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">a</span> <span class="o">=</span> <span class="n">array</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="s1">&#39;l&#39;</span><span class="p">,</span> <span class="p">[</span><span class="o">-</span><span class="mi">11111111</span><span class="p">,</span> <span class="mi">22222222</span><span class="p">,</span> <span class="o">-</span><span class="mi">33333333</span><span class="p">,</span> <span class="mi">44444444</span><span class="p">])</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">m</span> <span class="o">=</span> <span class="nb">memoryview</span><span class="p">(</span><span class="n">a</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">m</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<span class="go">-11111111</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">m</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
<span class="go">44444444</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">m</span><span class="p">[::</span><span class="mi">2</span><span class="p">]</span><span class="o">.</span><span class="n">tolist</span><span class="p">()</span>
<span class="go">[-11111111, -33333333]</span>
</pre></div>
</div>
<p>If the underlying object is writable, the memoryview supports
one-dimensional slice assignment. Resizing is not allowed:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">data</span> <span class="o">=</span> <span class="nb">bytearray</span><span class="p">(</span><span class="n">b</span><span class="s1">&#39;abcefg&#39;</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">v</span> <span class="o">=</span> <span class="nb">memoryview</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">v</span><span class="o">.</span><span class="n">readonly</span>
<span class="go">False</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">v</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">=</span> <span class="nb">ord</span><span class="p">(</span><span class="n">b</span><span class="s1">&#39;z&#39;</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">data</span>
<span class="go">bytearray(b&#39;zbcefg&#39;)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">v</span><span class="p">[</span><span class="mi">1</span><span class="p">:</span><span class="mi">4</span><span class="p">]</span> <span class="o">=</span> <span class="n">b</span><span class="s1">&#39;123&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">data</span>
<span class="go">bytearray(b&#39;z123fg&#39;)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">v</span><span class="p">[</span><span class="mi">2</span><span class="p">:</span><span class="mi">3</span><span class="p">]</span> <span class="o">=</span> <span class="n">b</span><span class="s1">&#39;spam&#39;</span>
<span class="gt">Traceback (most recent call last):</span>
  File <span class="nb">&quot;&lt;stdin&gt;&quot;</span>, line <span class="m">1</span>, in <span class="n">&lt;module&gt;</span>
<span class="gr">ValueError</span>: <span class="n">memoryview assignment: lvalue and rvalue have different structures</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">v</span><span class="p">[</span><span class="mi">2</span><span class="p">:</span><span class="mi">6</span><span class="p">]</span> <span class="o">=</span> <span class="n">b</span><span class="s1">&#39;spam&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">data</span>
<span class="go">bytearray(b&#39;z1spam&#39;)</span>
</pre></div>
</div>
<p>One-dimensional memoryviews of hashable (read-only) types with formats
&#8216;B&#8217;, &#8216;b&#8217; or &#8216;c&#8217; are also hashable. The hash is defined as
<code class="docutils literal"><span class="pre">hash(m)</span> <span class="pre">==</span> <span class="pre">hash(m.tobytes())</span></code>:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">v</span> <span class="o">=</span> <span class="nb">memoryview</span><span class="p">(</span><span class="n">b</span><span class="s1">&#39;abcefg&#39;</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">hash</span><span class="p">(</span><span class="n">v</span><span class="p">)</span> <span class="o">==</span> <span class="nb">hash</span><span class="p">(</span><span class="n">b</span><span class="s1">&#39;abcefg&#39;</span><span class="p">)</span>
<span class="go">True</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">hash</span><span class="p">(</span><span class="n">v</span><span class="p">[</span><span class="mi">2</span><span class="p">:</span><span class="mi">4</span><span class="p">])</span> <span class="o">==</span> <span class="nb">hash</span><span class="p">(</span><span class="n">b</span><span class="s1">&#39;ce&#39;</span><span class="p">)</span>
<span class="go">True</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">hash</span><span class="p">(</span><span class="n">v</span><span class="p">[::</span><span class="o">-</span><span class="mi">2</span><span class="p">])</span> <span class="o">==</span> <span class="nb">hash</span><span class="p">(</span><span class="n">b</span><span class="s1">&#39;abcefg&#39;</span><span class="p">[::</span><span class="o">-</span><span class="mi">2</span><span class="p">])</span>
<span class="go">True</span>
</pre></div>
</div>
<div class="versionchanged">
<p><span class="versionmodified">Changed in version 3.3: </span>One-dimensional memoryviews can now be sliced.
One-dimensional memoryviews with formats &#8216;B&#8217;, &#8216;b&#8217; or &#8216;c&#8217; are now hashable.</p>
</div>
<div class="versionchanged">
<p><span class="versionmodified">Changed in version 3.4: </span>memoryview is now registered automatically with
<a class="reference internal" href="collections.abc.html#collections.abc.Sequence" title="collections.abc.Sequence"><code class="xref py py-class docutils literal"><span class="pre">collections.abc.Sequence</span></code></a></p>
</div>
<div class="versionchanged">
<p><span class="versionmodified">Changed in version 3.5: </span>memoryviews can now be indexed with tuple of integers.</p>
</div>
<p><a class="reference internal" href="#memoryview" title="memoryview"><code class="xref py py-class docutils literal"><span class="pre">memoryview</span></code></a> has several methods:</p>
<dl class="method">
<dt id="memoryview.__eq__">
<code class="descname">__eq__</code><span class="sig-paren">(</span><em>exporter</em><span class="sig-paren">)</span><a class="headerlink" href="#memoryview.__eq__" title="Permalink to this definition">¶</a></dt>
<dd><p>A memoryview and a <span class="target" id="index-45"></span><a class="pep reference external" href="https://www.python.org/dev/peps/pep-3118"><strong>PEP 3118</strong></a> exporter are equal if their shapes are
equivalent and if all corresponding values are equal when the operands&#8217;
respective format codes are interpreted using <a class="reference internal" href="struct.html#module-struct" title="struct: Interpret bytes as packed binary data."><code class="xref py py-mod docutils literal"><span class="pre">struct</span></code></a> syntax.</p>
<p>For the subset of <a class="reference internal" href="struct.html#module-struct" title="struct: Interpret bytes as packed binary data."><code class="xref py py-mod docutils literal"><span class="pre">struct</span></code></a> format strings currently supported by
<a class="reference internal" href="#memoryview.tolist" title="memoryview.tolist"><code class="xref py py-meth docutils literal"><span class="pre">tolist()</span></code></a>, <code class="docutils literal"><span class="pre">v</span></code> and <code class="docutils literal"><span class="pre">w</span></code> are equal if <code class="docutils literal"><span class="pre">v.tolist()</span> <span class="pre">==</span> <span class="pre">w.tolist()</span></code>:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="kn">import</span> <span class="nn">array</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">a</span> <span class="o">=</span> <span class="n">array</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="s1">&#39;I&#39;</span><span class="p">,</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">])</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">b</span> <span class="o">=</span> <span class="n">array</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="s1">&#39;d&#39;</span><span class="p">,</span> <span class="p">[</span><span class="mf">1.0</span><span class="p">,</span> <span class="mf">2.0</span><span class="p">,</span> <span class="mf">3.0</span><span class="p">,</span> <span class="mf">4.0</span><span class="p">,</span> <span class="mf">5.0</span><span class="p">])</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">c</span> <span class="o">=</span> <span class="n">array</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="s1">&#39;b&#39;</span><span class="p">,</span> <span class="p">[</span><span class="mi">5</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">1</span><span class="p">])</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">x</span> <span class="o">=</span> <span class="nb">memoryview</span><span class="p">(</span><span class="n">a</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">y</span> <span class="o">=</span> <span class="nb">memoryview</span><span class="p">(</span><span class="n">b</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">x</span> <span class="o">==</span> <span class="n">a</span> <span class="o">==</span> <span class="n">y</span> <span class="o">==</span> <span class="n">b</span>
<span class="go">True</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">x</span><span class="o">.</span><span class="n">tolist</span><span class="p">()</span> <span class="o">==</span> <span class="n">a</span><span class="o">.</span><span class="n">tolist</span><span class="p">()</span> <span class="o">==</span> <span class="n">y</span><span class="o">.</span><span class="n">tolist</span><span class="p">()</span> <span class="o">==</span> <span class="n">b</span><span class="o">.</span><span class="n">tolist</span><span class="p">()</span>
<span class="go">True</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">z</span> <span class="o">=</span> <span class="n">y</span><span class="p">[::</span><span class="o">-</span><span class="mi">2</span><span class="p">]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">z</span> <span class="o">==</span> <span class="n">c</span>
<span class="go">True</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">z</span><span class="o">.</span><span class="n">tolist</span><span class="p">()</span> <span class="o">==</span> <span class="n">c</span><span class="o">.</span><span class="n">tolist</span><span class="p">()</span>
<span class="go">True</span>
</pre></div>
</div>
<p>If either format string is not supported by the <a class="reference internal" href="struct.html#module-struct" title="struct: Interpret bytes as packed binary data."><code class="xref py py-mod docutils literal"><span class="pre">struct</span></code></a> module,
then the objects will always compare as unequal (even if the format
strings and buffer contents are identical):</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="kn">from</span> <span class="nn">ctypes</span> <span class="k">import</span> <span class="n">BigEndianStructure</span><span class="p">,</span> <span class="n">c_long</span>
<span class="gp">&gt;&gt;&gt; </span><span class="k">class</span> <span class="nc">BEPoint</span><span class="p">(</span><span class="n">BigEndianStructure</span><span class="p">):</span>
<span class="gp">... </span>    <span class="n">_fields_</span> <span class="o">=</span> <span class="p">[(</span><span class="s2">&quot;x&quot;</span><span class="p">,</span> <span class="n">c_long</span><span class="p">),</span> <span class="p">(</span><span class="s2">&quot;y&quot;</span><span class="p">,</span> <span class="n">c_long</span><span class="p">)]</span>
<span class="gp">...</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">point</span> <span class="o">=</span> <span class="n">BEPoint</span><span class="p">(</span><span class="mi">100</span><span class="p">,</span> <span class="mi">200</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">a</span> <span class="o">=</span> <span class="nb">memoryview</span><span class="p">(</span><span class="n">point</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">b</span> <span class="o">=</span> <span class="nb">memoryview</span><span class="p">(</span><span class="n">point</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">a</span> <span class="o">==</span> <span class="n">point</span>
<span class="go">False</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">a</span> <span class="o">==</span> <span class="n">b</span>
<span class="go">False</span>
</pre></div>
</div>
<p>Note that, as with floating point numbers, <code class="docutils literal"><span class="pre">v</span> <span class="pre">is</span> <span class="pre">w</span></code> does <em>not</em> imply
<code class="docutils literal"><span class="pre">v</span> <span class="pre">==</span> <span class="pre">w</span></code> for memoryview objects.</p>
<div class="versionchanged">
<p><span class="versionmodified">Changed in version 3.3: </span>Previous versions compared the raw memory disregarding the item format
and the logical array structure.</p>
</div>
</dd></dl>

<dl class="method">
<dt id="memoryview.tobytes">
<code class="descname">tobytes</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#memoryview.tobytes" title="Permalink to this definition">¶</a></dt>
<dd><p>Return the data in the buffer as a bytestring.  This is equivalent to
calling the <a class="reference internal" href="functions.html#bytes" title="bytes"><code class="xref py py-class docutils literal"><span class="pre">bytes</span></code></a> constructor on the memoryview.</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">m</span> <span class="o">=</span> <span class="nb">memoryview</span><span class="p">(</span><span class="n">b</span><span class="s2">&quot;abc&quot;</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">m</span><span class="o">.</span><span class="n">tobytes</span><span class="p">()</span>
<span class="go">b&#39;abc&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">bytes</span><span class="p">(</span><span class="n">m</span><span class="p">)</span>
<span class="go">b&#39;abc&#39;</span>
</pre></div>
</div>
<p>For non-contiguous arrays the result is equal to the flattened list
representation with all elements converted to bytes. <a class="reference internal" href="#memoryview.tobytes" title="memoryview.tobytes"><code class="xref py py-meth docutils literal"><span class="pre">tobytes()</span></code></a>
supports all format strings, including those that are not in
<a class="reference internal" href="struct.html#module-struct" title="struct: Interpret bytes as packed binary data."><code class="xref py py-mod docutils literal"><span class="pre">struct</span></code></a> module syntax.</p>
</dd></dl>

<dl class="method">
<dt id="memoryview.hex">
<code class="descname">hex</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#memoryview.hex" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a string object containing two hexadecimal digits for each
byte in the buffer.</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">m</span> <span class="o">=</span> <span class="nb">memoryview</span><span class="p">(</span><span class="n">b</span><span class="s2">&quot;abc&quot;</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">m</span><span class="o">.</span><span class="n">hex</span><span class="p">()</span>
<span class="go">&#39;616263&#39;</span>
</pre></div>
</div>
<div class="versionadded">
<p><span class="versionmodified">New in version 3.5.</span></p>
</div>
</dd></dl>

<dl class="method">
<dt id="memoryview.tolist">
<code class="descname">tolist</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#memoryview.tolist" title="Permalink to this definition">¶</a></dt>
<dd><p>Return the data in the buffer as a list of elements.</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="nb">memoryview</span><span class="p">(</span><span class="n">b</span><span class="s1">&#39;abc&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">tolist</span><span class="p">()</span>
<span class="go">[97, 98, 99]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="kn">import</span> <span class="nn">array</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">a</span> <span class="o">=</span> <span class="n">array</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="s1">&#39;d&#39;</span><span class="p">,</span> <span class="p">[</span><span class="mf">1.1</span><span class="p">,</span> <span class="mf">2.2</span><span class="p">,</span> <span class="mf">3.3</span><span class="p">])</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">m</span> <span class="o">=</span> <span class="nb">memoryview</span><span class="p">(</span><span class="n">a</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">m</span><span class="o">.</span><span class="n">tolist</span><span class="p">()</span>
<span class="go">[1.1, 2.2, 3.3]</span>
</pre></div>
</div>
<div class="versionchanged">
<p><span class="versionmodified">Changed in version 3.3: </span><a class="reference internal" href="#memoryview.tolist" title="memoryview.tolist"><code class="xref py py-meth docutils literal"><span class="pre">tolist()</span></code></a> now supports all single character native formats in
<a class="reference internal" href="struct.html#module-struct" title="struct: Interpret bytes as packed binary data."><code class="xref py py-mod docutils literal"><span class="pre">struct</span></code></a> module syntax as well as multi-dimensional
representations.</p>
</div>
</dd></dl>

<dl class="method">
<dt id="memoryview.release">
<code class="descname">release</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#memoryview.release" title="Permalink to this definition">¶</a></dt>
<dd><p>Release the underlying buffer exposed by the memoryview object.  Many
objects take special actions when a view is held on them (for example,
a <a class="reference internal" href="functions.html#bytearray" title="bytearray"><code class="xref py py-class docutils literal"><span class="pre">bytearray</span></code></a> would temporarily forbid resizing); therefore,
calling release() is handy to remove these restrictions (and free any
dangling resources) as soon as possible.</p>
<p>After this method has been called, any further operation on the view
raises a <a class="reference internal" href="exceptions.html#ValueError" title="ValueError"><code class="xref py py-class docutils literal"><span class="pre">ValueError</span></code></a> (except <a class="reference internal" href="#memoryview.release" title="memoryview.release"><code class="xref py py-meth docutils literal"><span class="pre">release()</span></code></a> itself which can
be called multiple times):</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">m</span> <span class="o">=</span> <span class="nb">memoryview</span><span class="p">(</span><span class="n">b</span><span class="s1">&#39;abc&#39;</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">m</span><span class="o">.</span><span class="n">release</span><span class="p">()</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">m</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<span class="gt">Traceback (most recent call last):</span>
  File <span class="nb">&quot;&lt;stdin&gt;&quot;</span>, line <span class="m">1</span>, in <span class="n">&lt;module&gt;</span>
<span class="gr">ValueError</span>: <span class="n">operation forbidden on released memoryview object</span>
</pre></div>
</div>
<p>The context management protocol can be used for a similar effect,
using the <code class="docutils literal"><span class="pre">with</span></code> statement:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="k">with</span> <span class="nb">memoryview</span><span class="p">(</span><span class="n">b</span><span class="s1">&#39;abc&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">m</span><span class="p">:</span>
<span class="gp">... </span>    <span class="n">m</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<span class="gp">...</span>
<span class="go">97</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">m</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<span class="gt">Traceback (most recent call last):</span>
  File <span class="nb">&quot;&lt;stdin&gt;&quot;</span>, line <span class="m">1</span>, in <span class="n">&lt;module&gt;</span>
<span class="gr">ValueError</span>: <span class="n">operation forbidden on released memoryview object</span>
</pre></div>
</div>
<div class="versionadded">
<p><span class="versionmodified">New in version 3.2.</span></p>
</div>
</dd></dl>

<dl class="method">
<dt id="memoryview.cast">
<code class="descname">cast</code><span class="sig-paren">(</span><em>format</em><span class="optional">[</span>, <em>shape</em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#memoryview.cast" title="Permalink to this definition">¶</a></dt>
<dd><p>Cast a memoryview to a new format or shape. <em>shape</em> defaults to
<code class="docutils literal"><span class="pre">[byte_length//new_itemsize]</span></code>, which means that the result view
will be one-dimensional. The return value is a new memoryview, but
the buffer itself is not copied. Supported casts are 1D -&gt; C-<a class="reference internal" href="../glossary.html#term-contiguous"><span class="xref std std-term">contiguous</span></a>
and C-contiguous -&gt; 1D.</p>
<p>The destination format is restricted to a single element native format in
<a class="reference internal" href="struct.html#module-struct" title="struct: Interpret bytes as packed binary data."><code class="xref py py-mod docutils literal"><span class="pre">struct</span></code></a> syntax. One of the formats must be a byte format
(&#8216;B&#8217;, &#8216;b&#8217; or &#8216;c&#8217;). The byte length of the result must be the same
as the original length.</p>
<p>Cast 1D/long to 1D/unsigned bytes:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="kn">import</span> <span class="nn">array</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">a</span> <span class="o">=</span> <span class="n">array</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="s1">&#39;l&#39;</span><span class="p">,</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">])</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">x</span> <span class="o">=</span> <span class="nb">memoryview</span><span class="p">(</span><span class="n">a</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">x</span><span class="o">.</span><span class="n">format</span>
<span class="go">&#39;l&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">x</span><span class="o">.</span><span class="n">itemsize</span>
<span class="go">8</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">len</span><span class="p">(</span><span class="n">x</span><span class="p">)</span>
<span class="go">3</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">x</span><span class="o">.</span><span class="n">nbytes</span>
<span class="go">24</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">y</span> <span class="o">=</span> <span class="n">x</span><span class="o">.</span><span class="n">cast</span><span class="p">(</span><span class="s1">&#39;B&#39;</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">y</span><span class="o">.</span><span class="n">format</span>
<span class="go">&#39;B&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">y</span><span class="o">.</span><span class="n">itemsize</span>
<span class="go">1</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">len</span><span class="p">(</span><span class="n">y</span><span class="p">)</span>
<span class="go">24</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">y</span><span class="o">.</span><span class="n">nbytes</span>
<span class="go">24</span>
</pre></div>
</div>
<p>Cast 1D/unsigned bytes to 1D/char:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">b</span> <span class="o">=</span> <span class="nb">bytearray</span><span class="p">(</span><span class="n">b</span><span class="s1">&#39;zyz&#39;</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">x</span> <span class="o">=</span> <span class="nb">memoryview</span><span class="p">(</span><span class="n">b</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">x</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">=</span> <span class="n">b</span><span class="s1">&#39;a&#39;</span>
<span class="gt">Traceback (most recent call last):</span>
  File <span class="nb">&quot;&lt;stdin&gt;&quot;</span>, line <span class="m">1</span>, in <span class="n">&lt;module&gt;</span>
<span class="gr">ValueError</span>: <span class="n">memoryview: invalid value for format &quot;B&quot;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">y</span> <span class="o">=</span> <span class="n">x</span><span class="o">.</span><span class="n">cast</span><span class="p">(</span><span class="s1">&#39;c&#39;</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">y</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">=</span> <span class="n">b</span><span class="s1">&#39;a&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">b</span>
<span class="go">bytearray(b&#39;ayz&#39;)</span>
</pre></div>
</div>
<p>Cast 1D/bytes to 3D/ints to 1D/signed char:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="kn">import</span> <span class="nn">struct</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">buf</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="s2">&quot;i&quot;</span><span class="o">*</span><span class="mi">12</span><span class="p">,</span> <span class="o">*</span><span class="nb">list</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="mi">12</span><span class="p">)))</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">x</span> <span class="o">=</span> <span class="nb">memoryview</span><span class="p">(</span><span class="n">buf</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">y</span> <span class="o">=</span> <span class="n">x</span><span class="o">.</span><span class="n">cast</span><span class="p">(</span><span class="s1">&#39;i&#39;</span><span class="p">,</span> <span class="n">shape</span><span class="o">=</span><span class="p">[</span><span class="mi">2</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">])</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">y</span><span class="o">.</span><span class="n">tolist</span><span class="p">()</span>
<span class="go">[[[0, 1, 2], [3, 4, 5]], [[6, 7, 8], [9, 10, 11]]]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">y</span><span class="o">.</span><span class="n">format</span>
<span class="go">&#39;i&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">y</span><span class="o">.</span><span class="n">itemsize</span>
<span class="go">4</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">len</span><span class="p">(</span><span class="n">y</span><span class="p">)</span>
<span class="go">2</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">y</span><span class="o">.</span><span class="n">nbytes</span>
<span class="go">48</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">z</span> <span class="o">=</span> <span class="n">y</span><span class="o">.</span><span class="n">cast</span><span class="p">(</span><span class="s1">&#39;b&#39;</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">z</span><span class="o">.</span><span class="n">format</span>
<span class="go">&#39;b&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">z</span><span class="o">.</span><span class="n">itemsize</span>
<span class="go">1</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">len</span><span class="p">(</span><span class="n">z</span><span class="p">)</span>
<span class="go">48</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">z</span><span class="o">.</span><span class="n">nbytes</span>
<span class="go">48</span>
</pre></div>
</div>
<p>Cast 1D/unsigned char to 2D/unsigned long:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">buf</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="s2">&quot;L&quot;</span><span class="o">*</span><span class="mi">6</span><span class="p">,</span> <span class="o">*</span><span class="nb">list</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="mi">6</span><span class="p">)))</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">x</span> <span class="o">=</span> <span class="nb">memoryview</span><span class="p">(</span><span class="n">buf</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">y</span> <span class="o">=</span> <span class="n">x</span><span class="o">.</span><span class="n">cast</span><span class="p">(</span><span class="s1">&#39;L&#39;</span><span class="p">,</span> <span class="n">shape</span><span class="o">=</span><span class="p">[</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">])</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">len</span><span class="p">(</span><span class="n">y</span><span class="p">)</span>
<span class="go">2</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">y</span><span class="o">.</span><span class="n">nbytes</span>
<span class="go">48</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">y</span><span class="o">.</span><span class="n">tolist</span><span class="p">()</span>
<span class="go">[[0, 1, 2], [3, 4, 5]]</span>
</pre></div>
</div>
<div class="versionadded">
<p><span class="versionmodified">New in version 3.3.</span></p>
</div>
<div class="versionchanged">
<p><span class="versionmodified">Changed in version 3.5: </span>The source format is no longer restricted when casting to a byte view.</p>
</div>
</dd></dl>

<p>There are also several readonly attributes available:</p>
<dl class="attribute">
<dt id="memoryview.obj">
<code class="descname">obj</code><a class="headerlink" href="#memoryview.obj" title="Permalink to this definition">¶</a></dt>
<dd><p>The underlying object of the memoryview:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">b</span>  <span class="o">=</span> <span class="nb">bytearray</span><span class="p">(</span><span class="n">b</span><span class="s1">&#39;xyz&#39;</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">m</span> <span class="o">=</span> <span class="nb">memoryview</span><span class="p">(</span><span class="n">b</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">m</span><span class="o">.</span><span class="n">obj</span> <span class="ow">is</span> <span class="n">b</span>
<span class="go">True</span>
</pre></div>
</div>
<div class="versionadded">
<p><span class="versionmodified">New in version 3.3.</span></p>
</div>
</dd></dl>

<dl class="attribute">
<dt id="memoryview.nbytes">
<code class="descname">nbytes</code><a class="headerlink" href="#memoryview.nbytes" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal"><span class="pre">nbytes</span> <span class="pre">==</span> <span class="pre">product(shape)</span> <span class="pre">*</span> <span class="pre">itemsize</span> <span class="pre">==</span> <span class="pre">len(m.tobytes())</span></code>. This is
the amount of space in bytes that the array would use in a contiguous
representation. It is not necessarily equal to len(m):</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="kn">import</span> <span class="nn">array</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">a</span> <span class="o">=</span> <span class="n">array</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="s1">&#39;i&#39;</span><span class="p">,</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">,</span><span class="mi">4</span><span class="p">,</span><span class="mi">5</span><span class="p">])</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">m</span> <span class="o">=</span> <span class="nb">memoryview</span><span class="p">(</span><span class="n">a</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">len</span><span class="p">(</span><span class="n">m</span><span class="p">)</span>
<span class="go">5</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">m</span><span class="o">.</span><span class="n">nbytes</span>
<span class="go">20</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">y</span> <span class="o">=</span> <span class="n">m</span><span class="p">[::</span><span class="mi">2</span><span class="p">]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">len</span><span class="p">(</span><span class="n">y</span><span class="p">)</span>
<span class="go">3</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">y</span><span class="o">.</span><span class="n">nbytes</span>
<span class="go">12</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">len</span><span class="p">(</span><span class="n">y</span><span class="o">.</span><span class="n">tobytes</span><span class="p">())</span>
<span class="go">12</span>
</pre></div>
</div>
<p>Multi-dimensional arrays:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="kn">import</span> <span class="nn">struct</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">buf</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="s2">&quot;d&quot;</span><span class="o">*</span><span class="mi">12</span><span class="p">,</span> <span class="o">*</span><span class="p">[</span><span class="mf">1.5</span><span class="o">*</span><span class="n">x</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">12</span><span class="p">)])</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">x</span> <span class="o">=</span> <span class="nb">memoryview</span><span class="p">(</span><span class="n">buf</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">y</span> <span class="o">=</span> <span class="n">x</span><span class="o">.</span><span class="n">cast</span><span class="p">(</span><span class="s1">&#39;d&#39;</span><span class="p">,</span> <span class="n">shape</span><span class="o">=</span><span class="p">[</span><span class="mi">3</span><span class="p">,</span><span class="mi">4</span><span class="p">])</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">y</span><span class="o">.</span><span class="n">tolist</span><span class="p">()</span>
<span class="go">[[0.0, 1.5, 3.0, 4.5], [6.0, 7.5, 9.0, 10.5], [12.0, 13.5, 15.0, 16.5]]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">len</span><span class="p">(</span><span class="n">y</span><span class="p">)</span>
<span class="go">3</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">y</span><span class="o">.</span><span class="n">nbytes</span>
<span class="go">96</span>
</pre></div>
</div>
<div class="versionadded">
<p><span class="versionmodified">New in version 3.3.</span></p>
</div>
</dd></dl>

<dl class="attribute">
<dt id="memoryview.readonly">
<code class="descname">readonly</code><a class="headerlink" href="#memoryview.readonly" title="Permalink to this definition">¶</a></dt>
<dd><p>A bool indicating whether the memory is read only.</p>
</dd></dl>

<dl class="attribute">
<dt id="memoryview.format">
<code class="descname">format</code><a class="headerlink" href="#memoryview.format" title="Permalink to this definition">¶</a></dt>
<dd><p>A string containing the format (in <a class="reference internal" href="struct.html#module-struct" title="struct: Interpret bytes as packed binary data."><code class="xref py py-mod docutils literal"><span class="pre">struct</span></code></a> module style) for each
element in the view. A memoryview can be created from exporters with
arbitrary format strings, but some methods (e.g. <a class="reference internal" href="#memoryview.tolist" title="memoryview.tolist"><code class="xref py py-meth docutils literal"><span class="pre">tolist()</span></code></a>) are
restricted to native single element formats.</p>
<div class="versionchanged">
<p><span class="versionmodified">Changed in version 3.3: </span>format <code class="docutils literal"><span class="pre">'B'</span></code> is now handled according to the struct module syntax.
This means that <code class="docutils literal"><span class="pre">memoryview(b'abc')[0]</span> <span class="pre">==</span> <span class="pre">b'abc'[0]</span> <span class="pre">==</span> <span class="pre">97</span></code>.</p>
</div>
</dd></dl>

<dl class="attribute">
<dt id="memoryview.itemsize">
<code class="descname">itemsize</code><a class="headerlink" href="#memoryview.itemsize" title="Permalink to this definition">¶</a></dt>
<dd><p>The size in bytes of each element of the memoryview:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="kn">import</span> <span class="nn">array</span><span class="o">,</span> <span class="nn">struct</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">m</span> <span class="o">=</span> <span class="nb">memoryview</span><span class="p">(</span><span class="n">array</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="s1">&#39;H&#39;</span><span class="p">,</span> <span class="p">[</span><span class="mi">32000</span><span class="p">,</span> <span class="mi">32001</span><span class="p">,</span> <span class="mi">32002</span><span class="p">]))</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">m</span><span class="o">.</span><span class="n">itemsize</span>
<span class="go">2</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">m</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<span class="go">32000</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">struct</span><span class="o">.</span><span class="n">calcsize</span><span class="p">(</span><span class="s1">&#39;H&#39;</span><span class="p">)</span> <span class="o">==</span> <span class="n">m</span><span class="o">.</span><span class="n">itemsize</span>
<span class="go">True</span>
</pre></div>
</div>
</dd></dl>

<dl class="attribute">
<dt id="memoryview.ndim">
<code class="descname">ndim</code><a class="headerlink" href="#memoryview.ndim" title="Permalink to this definition">¶</a></dt>
<dd><p>An integer indicating how many dimensions of a multi-dimensional array the
memory represents.</p>
</dd></dl>

<dl class="attribute">
<dt id="memoryview.shape">
<code class="descname">shape</code><a class="headerlink" href="#memoryview.shape" title="Permalink to this definition">¶</a></dt>
<dd><p>A tuple of integers the length of <a class="reference internal" href="#memoryview.ndim" title="memoryview.ndim"><code class="xref py py-attr docutils literal"><span class="pre">ndim</span></code></a> giving the shape of the
memory as an N-dimensional array.</p>
<div class="versionchanged">
<p><span class="versionmodified">Changed in version 3.3: </span>An empty tuple instead of <code class="docutils literal"><span class="pre">None</span></code> when ndim = 0.</p>
</div>
</dd></dl>

<dl class="attribute">
<dt id="memoryview.strides">
<code class="descname">strides</code><a class="headerlink" href="#memoryview.strides" title="Permalink to this definition">¶</a></dt>
<dd><p>A tuple of integers the length of <a class="reference internal" href="#memoryview.ndim" title="memoryview.ndim"><code class="xref py py-attr docutils literal"><span class="pre">ndim</span></code></a> giving the size in bytes to
access each element for each dimension of the array.</p>
<div class="versionchanged">
<p><span class="versionmodified">Changed in version 3.3: </span>An empty tuple instead of <code class="docutils literal"><span class="pre">None</span></code> when ndim = 0.</p>
</div>
</dd></dl>

<dl class="attribute">
<dt id="memoryview.suboffsets">
<code class="descname">suboffsets</code><a class="headerlink" href="#memoryview.suboffsets" title="Permalink to this definition">¶</a></dt>
<dd><p>Used internally for PIL-style arrays. The value is informational only.</p>
</dd></dl>

<dl class="attribute">
<dt id="memoryview.c_contiguous">
<code class="descname">c_contiguous</code><a class="headerlink" href="#memoryview.c_contiguous" title="Permalink to this definition">¶</a></dt>
<dd><p>A bool indicating whether the memory is C-<a class="reference internal" href="../glossary.html#term-contiguous"><span class="xref std std-term">contiguous</span></a>.</p>
<div class="versionadded">
<p><span class="versionmodified">New in version 3.3.</span></p>
</div>
</dd></dl>

<dl class="attribute">
<dt id="memoryview.f_contiguous">
<code class="descname">f_contiguous</code><a class="headerlink" href="#memoryview.f_contiguous" title="Permalink to this definition">¶</a></dt>
<dd><p>A bool indicating whether the memory is Fortran <a class="reference internal" href="../glossary.html#term-contiguous"><span class="xref std std-term">contiguous</span></a>.</p>
<div class="versionadded">
<p><span class="versionmodified">New in version 3.3.</span></p>
</div>
</dd></dl>

<dl class="attribute">
<dt id="memoryview.contiguous">
<code class="descname">contiguous</code><a class="headerlink" href="#memoryview.contiguous" title="Permalink to this definition">¶</a></dt>
<dd><p>A bool indicating whether the memory is <a class="reference internal" href="../glossary.html#term-contiguous"><span class="xref std std-term">contiguous</span></a>.</p>
<div class="versionadded">
<p><span class="versionmodified">New in version 3.3.</span></p>
</div>
</dd></dl>

</dd></dl>

</div>
</div>
<div class="section" id="set-types-set-frozenset">
<span id="types-set"></span><h2>4.9. Set Types &#8212; <a class="reference internal" href="#set" title="set"><code class="xref py py-class docutils literal"><span class="pre">set</span></code></a>, <a class="reference internal" href="#frozenset" title="frozenset"><code class="xref py py-class docutils literal"><span class="pre">frozenset</span></code></a><a class="headerlink" href="#set-types-set-frozenset" title="Permalink to this headline">¶</a></h2>
<p id="index-46">A <em class="dfn">set</em> object is an unordered collection of distinct <a class="reference internal" href="../glossary.html#term-hashable"><span class="xref std std-term">hashable</span></a> objects.
Common uses include membership testing, removing duplicates from a sequence, and
computing mathematical operations such as intersection, union, difference, and
symmetric difference.
(For other containers see the built-in <a class="reference internal" href="#dict" title="dict"><code class="xref py py-class docutils literal"><span class="pre">dict</span></code></a>, <a class="reference internal" href="#list" title="list"><code class="xref py py-class docutils literal"><span class="pre">list</span></code></a>,
and <a class="reference internal" href="#tuple" title="tuple"><code class="xref py py-class docutils literal"><span class="pre">tuple</span></code></a> classes, and the <a class="reference internal" href="collections.html#module-collections" title="collections: Container datatypes"><code class="xref py py-mod docutils literal"><span class="pre">collections</span></code></a> module.)</p>
<p>Like other collections, sets support <code class="docutils literal"><span class="pre">x</span> <span class="pre">in</span> <span class="pre">set</span></code>, <code class="docutils literal"><span class="pre">len(set)</span></code>, and <code class="docutils literal"><span class="pre">for</span> <span class="pre">x</span> <span class="pre">in</span>
<span class="pre">set</span></code>.  Being an unordered collection, sets do not record element position or
order of insertion.  Accordingly, sets do not support indexing, slicing, or
other sequence-like behavior.</p>
<p>There are currently two built-in set types, <a class="reference internal" href="#set" title="set"><code class="xref py py-class docutils literal"><span class="pre">set</span></code></a> and <a class="reference internal" href="#frozenset" title="frozenset"><code class="xref py py-class docutils literal"><span class="pre">frozenset</span></code></a>.
The <a class="reference internal" href="#set" title="set"><code class="xref py py-class docutils literal"><span class="pre">set</span></code></a> type is mutable &#8212; the contents can be changed using methods
like <a class="reference internal" href="#set.add" title="set.add"><code class="xref py py-meth docutils literal"><span class="pre">add()</span></code></a> and <a class="reference internal" href="#set.remove" title="set.remove"><code class="xref py py-meth docutils literal"><span class="pre">remove()</span></code></a>.  Since it is mutable, it has no
hash value and cannot be used as either a dictionary key or as an element of
another set.  The <a class="reference internal" href="#frozenset" title="frozenset"><code class="xref py py-class docutils literal"><span class="pre">frozenset</span></code></a> type is immutable and <a class="reference internal" href="../glossary.html#term-hashable"><span class="xref std std-term">hashable</span></a> &#8212;
its contents cannot be altered after it is created; it can therefore be used as
a dictionary key or as an element of another set.</p>
<p>Non-empty sets (not frozensets) can be created by placing a comma-separated list
of elements within braces, for example: <code class="docutils literal"><span class="pre">{'jack',</span> <span class="pre">'sjoerd'}</span></code>, in addition to the
<a class="reference internal" href="#set" title="set"><code class="xref py py-class docutils literal"><span class="pre">set</span></code></a> constructor.</p>
<p>The constructors for both classes work the same:</p>
<dl class="class">
<dt id="set">
<em class="property">class </em><code class="descname">set</code><span class="sig-paren">(</span><span class="optional">[</span><em>iterable</em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#set" title="Permalink to this definition">¶</a></dt>
<dt id="frozenset">
<em class="property">class </em><code class="descname">frozenset</code><span class="sig-paren">(</span><span class="optional">[</span><em>iterable</em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#frozenset" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a new set or frozenset object whose elements are taken from
<em>iterable</em>.  The elements of a set must be <a class="reference internal" href="../glossary.html#term-hashable"><span class="xref std std-term">hashable</span></a>.  To
represent sets of sets, the inner sets must be <a class="reference internal" href="#frozenset" title="frozenset"><code class="xref py py-class docutils literal"><span class="pre">frozenset</span></code></a>
objects.  If <em>iterable</em> is not specified, a new empty set is
returned.</p>
<p>Instances of <a class="reference internal" href="#set" title="set"><code class="xref py py-class docutils literal"><span class="pre">set</span></code></a> and <a class="reference internal" href="#frozenset" title="frozenset"><code class="xref py py-class docutils literal"><span class="pre">frozenset</span></code></a> provide the following
operations:</p>
<dl class="describe">
<dt>
<code class="descname">len(s)</code></dt>
<dd><p>Return the number of elements in set <em>s</em> (cardinality of <em>s</em>).</p>
</dd></dl>

<dl class="describe">
<dt>
<code class="descname">x in s</code></dt>
<dd><p>Test <em>x</em> for membership in <em>s</em>.</p>
</dd></dl>

<dl class="describe">
<dt>
<code class="descname">x not in s</code></dt>
<dd><p>Test <em>x</em> for non-membership in <em>s</em>.</p>
</dd></dl>

<dl class="method">
<dt id="set.isdisjoint">
<code class="descname">isdisjoint</code><span class="sig-paren">(</span><em>other</em><span class="sig-paren">)</span><a class="headerlink" href="#set.isdisjoint" title="Permalink to this definition">¶</a></dt>
<dd><p>Return <code class="docutils literal"><span class="pre">True</span></code> if the set has no elements in common with <em>other</em>.  Sets are
disjoint if and only if their intersection is the empty set.</p>
</dd></dl>

<dl class="method">
<dt id="set.issubset">
<code class="descname">issubset</code><span class="sig-paren">(</span><em>other</em><span class="sig-paren">)</span><a class="headerlink" href="#set.issubset" title="Permalink to this definition">¶</a></dt>
<dt>
<code class="descname">set &lt;= other</code></dt>
<dd><p>Test whether every element in the set is in <em>other</em>.</p>
</dd></dl>

<dl class="method">
<dt>
<code class="descname">set &lt; other</code></dt>
<dd><p>Test whether the set is a proper subset of <em>other</em>, that is,
<code class="docutils literal"><span class="pre">set</span> <span class="pre">&lt;=</span> <span class="pre">other</span> <span class="pre">and</span> <span class="pre">set</span> <span class="pre">!=</span> <span class="pre">other</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="set.issuperset">
<code class="descname">issuperset</code><span class="sig-paren">(</span><em>other</em><span class="sig-paren">)</span><a class="headerlink" href="#set.issuperset" title="Permalink to this definition">¶</a></dt>
<dt>
<code class="descname">set &gt;= other</code></dt>
<dd><p>Test whether every element in <em>other</em> is in the set.</p>
</dd></dl>

<dl class="method">
<dt>
<code class="descname">set &gt; other</code></dt>
<dd><p>Test whether the set is a proper superset of <em>other</em>, that is, <code class="docutils literal"><span class="pre">set</span> <span class="pre">&gt;=</span>
<span class="pre">other</span> <span class="pre">and</span> <span class="pre">set</span> <span class="pre">!=</span> <span class="pre">other</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="set.union">
<code class="descname">union</code><span class="sig-paren">(</span><em>*others</em><span class="sig-paren">)</span><a class="headerlink" href="#set.union" title="Permalink to this definition">¶</a></dt>
<dt>
<code class="descname">set | other | ...</code></dt>
<dd><p>Return a new set with elements from the set and all others.</p>
</dd></dl>

<dl class="method">
<dt id="set.intersection">
<code class="descname">intersection</code><span class="sig-paren">(</span><em>*others</em><span class="sig-paren">)</span><a class="headerlink" href="#set.intersection" title="Permalink to this definition">¶</a></dt>
<dt>
<code class="descname">set &amp; other &amp; ...</code></dt>
<dd><p>Return a new set with elements common to the set and all others.</p>
</dd></dl>

<dl class="method">
<dt id="set.difference">
<code class="descname">difference</code><span class="sig-paren">(</span><em>*others</em><span class="sig-paren">)</span><a class="headerlink" href="#set.difference" title="Permalink to this definition">¶</a></dt>
<dt>
<code class="descname">set - other - ...</code></dt>
<dd><p>Return a new set with elements in the set that are not in the others.</p>
</dd></dl>

<dl class="method">
<dt id="set.symmetric_difference">
<code class="descname">symmetric_difference</code><span class="sig-paren">(</span><em>other</em><span class="sig-paren">)</span><a class="headerlink" href="#set.symmetric_difference" title="Permalink to this definition">¶</a></dt>
<dt>
<code class="descname">set ^ other</code></dt>
<dd><p>Return a new set with elements in either the set or <em>other</em> but not both.</p>
</dd></dl>

<dl class="method">
<dt id="set.copy">
<code class="descname">copy</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#set.copy" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a new set with a shallow copy of <em>s</em>.</p>
</dd></dl>

<p>Note, the non-operator versions of <a class="reference internal" href="#set.union" title="set.union"><code class="xref py py-meth docutils literal"><span class="pre">union()</span></code></a>, <a class="reference internal" href="#set.intersection" title="set.intersection"><code class="xref py py-meth docutils literal"><span class="pre">intersection()</span></code></a>,
<a class="reference internal" href="#set.difference" title="set.difference"><code class="xref py py-meth docutils literal"><span class="pre">difference()</span></code></a>, and <a class="reference internal" href="#set.symmetric_difference" title="set.symmetric_difference"><code class="xref py py-meth docutils literal"><span class="pre">symmetric_difference()</span></code></a>, <a class="reference internal" href="#set.issubset" title="set.issubset"><code class="xref py py-meth docutils literal"><span class="pre">issubset()</span></code></a>, and
<a class="reference internal" href="#set.issuperset" title="set.issuperset"><code class="xref py py-meth docutils literal"><span class="pre">issuperset()</span></code></a> methods will accept any iterable as an argument.  In
contrast, their operator based counterparts require their arguments to be
sets.  This precludes error-prone constructions like <code class="docutils literal"><span class="pre">set('abc')</span> <span class="pre">&amp;</span> <span class="pre">'cbs'</span></code>
in favor of the more readable <code class="docutils literal"><span class="pre">set('abc').intersection('cbs')</span></code>.</p>
<p>Both <a class="reference internal" href="#set" title="set"><code class="xref py py-class docutils literal"><span class="pre">set</span></code></a> and <a class="reference internal" href="#frozenset" title="frozenset"><code class="xref py py-class docutils literal"><span class="pre">frozenset</span></code></a> support set to set comparisons. Two
sets are equal if and only if every element of each set is contained in the
other (each is a subset of the other). A set is less than another set if and
only if the first set is a proper subset of the second set (is a subset, but
is not equal). A set is greater than another set if and only if the first set
is a proper superset of the second set (is a superset, but is not equal).</p>
<p>Instances of <a class="reference internal" href="#set" title="set"><code class="xref py py-class docutils literal"><span class="pre">set</span></code></a> are compared to instances of <a class="reference internal" href="#frozenset" title="frozenset"><code class="xref py py-class docutils literal"><span class="pre">frozenset</span></code></a>
based on their members.  For example, <code class="docutils literal"><span class="pre">set('abc')</span> <span class="pre">==</span> <span class="pre">frozenset('abc')</span></code>
returns <code class="docutils literal"><span class="pre">True</span></code> and so does <code class="docutils literal"><span class="pre">set('abc')</span> <span class="pre">in</span> <span class="pre">set([frozenset('abc')])</span></code>.</p>
<p>The subset and equality comparisons do not generalize to a total ordering
function.  For example, any two nonempty disjoint sets are not equal and are not
subsets of each other, so <em>all</em> of the following return <code class="docutils literal"><span class="pre">False</span></code>: <code class="docutils literal"><span class="pre">a&lt;b</span></code>,
<code class="docutils literal"><span class="pre">a==b</span></code>, or <code class="docutils literal"><span class="pre">a&gt;b</span></code>.</p>
<p>Since sets only define partial ordering (subset relationships), the output of
the <a class="reference internal" href="#list.sort" title="list.sort"><code class="xref py py-meth docutils literal"><span class="pre">list.sort()</span></code></a> method is undefined for lists of sets.</p>
<p>Set elements, like dictionary keys, must be <a class="reference internal" href="../glossary.html#term-hashable"><span class="xref std std-term">hashable</span></a>.</p>
<p>Binary operations that mix <a class="reference internal" href="#set" title="set"><code class="xref py py-class docutils literal"><span class="pre">set</span></code></a> instances with <a class="reference internal" href="#frozenset" title="frozenset"><code class="xref py py-class docutils literal"><span class="pre">frozenset</span></code></a>
return the type of the first operand.  For example: <code class="docutils literal"><span class="pre">frozenset('ab')</span> <span class="pre">|</span>
<span class="pre">set('bc')</span></code> returns an instance of <a class="reference internal" href="#frozenset" title="frozenset"><code class="xref py py-class docutils literal"><span class="pre">frozenset</span></code></a>.</p>
<p>The following table lists operations available for <a class="reference internal" href="#set" title="set"><code class="xref py py-class docutils literal"><span class="pre">set</span></code></a> that do not
apply to immutable instances of <a class="reference internal" href="#frozenset" title="frozenset"><code class="xref py py-class docutils literal"><span class="pre">frozenset</span></code></a>:</p>
<dl class="method">
<dt id="set.update">
<code class="descname">update</code><span class="sig-paren">(</span><em>*others</em><span class="sig-paren">)</span><a class="headerlink" href="#set.update" title="Permalink to this definition">¶</a></dt>
<dt>
<code class="descname">set |= other | ...</code></dt>
<dd><p>Update the set, adding elements from all others.</p>
</dd></dl>

<dl class="method">
<dt id="set.intersection_update">
<code class="descname">intersection_update</code><span class="sig-paren">(</span><em>*others</em><span class="sig-paren">)</span><a class="headerlink" href="#set.intersection_update" title="Permalink to this definition">¶</a></dt>
<dt>
<code class="descname">set &amp;= other &amp; ...</code></dt>
<dd><p>Update the set, keeping only elements found in it and all others.</p>
</dd></dl>

<dl class="method">
<dt id="set.difference_update">
<code class="descname">difference_update</code><span class="sig-paren">(</span><em>*others</em><span class="sig-paren">)</span><a class="headerlink" href="#set.difference_update" title="Permalink to this definition">¶</a></dt>
<dt>
<code class="descname">set -= other | ...</code></dt>
<dd><p>Update the set, removing elements found in others.</p>
</dd></dl>

<dl class="method">
<dt id="set.symmetric_difference_update">
<code class="descname">symmetric_difference_update</code><span class="sig-paren">(</span><em>other</em><span class="sig-paren">)</span><a class="headerlink" href="#set.symmetric_difference_update" title="Permalink to this definition">¶</a></dt>
<dt>
<code class="descname">set ^= other</code></dt>
<dd><p>Update the set, keeping only elements found in either set, but not in both.</p>
</dd></dl>

<dl class="method">
<dt id="set.add">
<code class="descname">add</code><span class="sig-paren">(</span><em>elem</em><span class="sig-paren">)</span><a class="headerlink" href="#set.add" title="Permalink to this definition">¶</a></dt>
<dd><p>Add element <em>elem</em> to the set.</p>
</dd></dl>

<dl class="method">
<dt id="set.remove">
<code class="descname">remove</code><span class="sig-paren">(</span><em>elem</em><span class="sig-paren">)</span><a class="headerlink" href="#set.remove" title="Permalink to this definition">¶</a></dt>
<dd><p>Remove element <em>elem</em> from the set.  Raises <a class="reference internal" href="exceptions.html#KeyError" title="KeyError"><code class="xref py py-exc docutils literal"><span class="pre">KeyError</span></code></a> if <em>elem</em> is
not contained in the set.</p>
</dd></dl>

<dl class="method">
<dt id="set.discard">
<code class="descname">discard</code><span class="sig-paren">(</span><em>elem</em><span class="sig-paren">)</span><a class="headerlink" href="#set.discard" title="Permalink to this definition">¶</a></dt>
<dd><p>Remove element <em>elem</em> from the set if it is present.</p>
</dd></dl>

<dl class="method">
<dt id="set.pop">
<code class="descname">pop</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#set.pop" title="Permalink to this definition">¶</a></dt>
<dd><p>Remove and return an arbitrary element from the set.  Raises
<a class="reference internal" href="exceptions.html#KeyError" title="KeyError"><code class="xref py py-exc docutils literal"><span class="pre">KeyError</span></code></a> if the set is empty.</p>
</dd></dl>

<dl class="method">
<dt id="set.clear">
<code class="descname">clear</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#set.clear" title="Permalink to this definition">¶</a></dt>
<dd><p>Remove all elements from the set.</p>
</dd></dl>

<p>Note, the non-operator versions of the <a class="reference internal" href="#set.update" title="set.update"><code class="xref py py-meth docutils literal"><span class="pre">update()</span></code></a>,
<a class="reference internal" href="#set.intersection_update" title="set.intersection_update"><code class="xref py py-meth docutils literal"><span class="pre">intersection_update()</span></code></a>, <a class="reference internal" href="#set.difference_update" title="set.difference_update"><code class="xref py py-meth docutils literal"><span class="pre">difference_update()</span></code></a>, and
<a class="reference internal" href="#set.symmetric_difference_update" title="set.symmetric_difference_update"><code class="xref py py-meth docutils literal"><span class="pre">symmetric_difference_update()</span></code></a> methods will accept any iterable as an
argument.</p>
<p>Note, the <em>elem</em> argument to the <a class="reference internal" href="../reference/datamodel.html#object.__contains__" title="object.__contains__"><code class="xref py py-meth docutils literal"><span class="pre">__contains__()</span></code></a>, <a class="reference internal" href="#set.remove" title="set.remove"><code class="xref py py-meth docutils literal"><span class="pre">remove()</span></code></a>, and
<a class="reference internal" href="#set.discard" title="set.discard"><code class="xref py py-meth docutils literal"><span class="pre">discard()</span></code></a> methods may be a set.  To support searching for an equivalent
frozenset, the <em>elem</em> set is temporarily mutated during the search and then
restored.  During the search, the <em>elem</em> set should not be read or mutated
since it does not have a meaningful value.</p>
</dd></dl>

</div>
<div class="section" id="mapping-types-dict">
<span id="typesmapping"></span><h2>4.10. Mapping Types &#8212; <a class="reference internal" href="#dict" title="dict"><code class="xref py py-class docutils literal"><span class="pre">dict</span></code></a><a class="headerlink" href="#mapping-types-dict" title="Permalink to this headline">¶</a></h2>
<p id="index-47">A <a class="reference internal" href="../glossary.html#term-mapping"><span class="xref std std-term">mapping</span></a> object maps <a class="reference internal" href="../glossary.html#term-hashable"><span class="xref std std-term">hashable</span></a> values to arbitrary objects.
Mappings are mutable objects.  There is currently only one standard mapping
type, the <em class="dfn">dictionary</em>.  (For other containers see the built-in
<a class="reference internal" href="#list" title="list"><code class="xref py py-class docutils literal"><span class="pre">list</span></code></a>, <a class="reference internal" href="#set" title="set"><code class="xref py py-class docutils literal"><span class="pre">set</span></code></a>, and <a class="reference internal" href="#tuple" title="tuple"><code class="xref py py-class docutils literal"><span class="pre">tuple</span></code></a> classes, and the
<a class="reference internal" href="collections.html#module-collections" title="collections: Container datatypes"><code class="xref py py-mod docutils literal"><span class="pre">collections</span></code></a> module.)</p>
<p>A dictionary&#8217;s keys are <em>almost</em> arbitrary values.  Values that are not
<a class="reference internal" href="../glossary.html#term-hashable"><span class="xref std std-term">hashable</span></a>, that is, values containing lists, dictionaries or other
mutable types (that are compared by value rather than by object identity) may
not be used as keys.  Numeric types used for keys obey the normal rules for
numeric comparison: if two numbers compare equal (such as <code class="docutils literal"><span class="pre">1</span></code> and <code class="docutils literal"><span class="pre">1.0</span></code>)
then they can be used interchangeably to index the same dictionary entry.  (Note
however, that since computers store floating-point numbers as approximations it
is usually unwise to use them as dictionary keys.)</p>
<p>Dictionaries can be created by placing a comma-separated list of <code class="docutils literal"><span class="pre">key:</span> <span class="pre">value</span></code>
pairs within braces, for example: <code class="docutils literal"><span class="pre">{'jack':</span> <span class="pre">4098,</span> <span class="pre">'sjoerd':</span> <span class="pre">4127}</span></code> or <code class="docutils literal"><span class="pre">{4098:</span>
<span class="pre">'jack',</span> <span class="pre">4127:</span> <span class="pre">'sjoerd'}</span></code>, or by the <a class="reference internal" href="#dict" title="dict"><code class="xref py py-class docutils literal"><span class="pre">dict</span></code></a> constructor.</p>
<dl class="class">
<dt id="dict">
<em class="property">class </em><code class="descname">dict</code><span class="sig-paren">(</span><em>**kwarg</em><span class="sig-paren">)</span><a class="headerlink" href="#dict" title="Permalink to this definition">¶</a></dt>
<dt>
<em class="property">class </em><code class="descname">dict</code><span class="sig-paren">(</span><em>mapping</em>, <em>**kwarg</em><span class="sig-paren">)</span></dt>
<dt>
<em class="property">class </em><code class="descname">dict</code><span class="sig-paren">(</span><em>iterable</em>, <em>**kwarg</em><span class="sig-paren">)</span></dt>
<dd><p>Return a new dictionary initialized from an optional positional argument
and a possibly empty set of keyword arguments.</p>
<p>If no positional argument is given, an empty dictionary is created.
If a positional argument is given and it is a mapping object, a dictionary
is created with the same key-value pairs as the mapping object.  Otherwise,
the positional argument must be an <a class="reference internal" href="../glossary.html#term-iterable"><span class="xref std std-term">iterable</span></a> object.  Each item in
the iterable must itself be an iterable with exactly two objects.  The
first object of each item becomes a key in the new dictionary, and the
second object the corresponding value.  If a key occurs more than once, the
last value for that key becomes the corresponding value in the new
dictionary.</p>
<p>If keyword arguments are given, the keyword arguments and their values are
added to the dictionary created from the positional argument.  If a key
being added is already present, the value from the keyword argument
replaces the value from the positional argument.</p>
<p>To illustrate, the following examples all return a dictionary equal to
<code class="docutils literal"><span class="pre">{&quot;one&quot;:</span> <span class="pre">1,</span> <span class="pre">&quot;two&quot;:</span> <span class="pre">2,</span> <span class="pre">&quot;three&quot;:</span> <span class="pre">3}</span></code>:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">a</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">(</span><span class="n">one</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">two</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span> <span class="n">three</span><span class="o">=</span><span class="mi">3</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">b</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;one&#39;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span> <span class="s1">&#39;two&#39;</span><span class="p">:</span> <span class="mi">2</span><span class="p">,</span> <span class="s1">&#39;three&#39;</span><span class="p">:</span> <span class="mi">3</span><span class="p">}</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">c</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">(</span><span class="nb">zip</span><span class="p">([</span><span class="s1">&#39;one&#39;</span><span class="p">,</span> <span class="s1">&#39;two&#39;</span><span class="p">,</span> <span class="s1">&#39;three&#39;</span><span class="p">],</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">]))</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">d</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">([(</span><span class="s1">&#39;two&#39;</span><span class="p">,</span> <span class="mi">2</span><span class="p">),</span> <span class="p">(</span><span class="s1">&#39;one&#39;</span><span class="p">,</span> <span class="mi">1</span><span class="p">),</span> <span class="p">(</span><span class="s1">&#39;three&#39;</span><span class="p">,</span> <span class="mi">3</span><span class="p">)])</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">e</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">({</span><span class="s1">&#39;three&#39;</span><span class="p">:</span> <span class="mi">3</span><span class="p">,</span> <span class="s1">&#39;one&#39;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span> <span class="s1">&#39;two&#39;</span><span class="p">:</span> <span class="mi">2</span><span class="p">})</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">a</span> <span class="o">==</span> <span class="n">b</span> <span class="o">==</span> <span class="n">c</span> <span class="o">==</span> <span class="n">d</span> <span class="o">==</span> <span class="n">e</span>
<span class="go">True</span>
</pre></div>
</div>
<p>Providing keyword arguments as in the first example only works for keys that
are valid Python identifiers.  Otherwise, any valid keys can be used.</p>
<p>These are the operations that dictionaries support (and therefore, custom
mapping types should support too):</p>
<dl class="describe">
<dt>
<code class="descname">len(d)</code></dt>
<dd><p>Return the number of items in the dictionary <em>d</em>.</p>
</dd></dl>

<dl class="describe">
<dt>
<code class="descname">d[key]</code></dt>
<dd><p>Return the item of <em>d</em> with key <em>key</em>.  Raises a <a class="reference internal" href="exceptions.html#KeyError" title="KeyError"><code class="xref py py-exc docutils literal"><span class="pre">KeyError</span></code></a> if <em>key</em> is
not in the map.</p>
<p id="index-48">If a subclass of dict defines a method <a class="reference internal" href="../reference/datamodel.html#object.__missing__" title="object.__missing__"><code class="xref py py-meth docutils literal"><span class="pre">__missing__()</span></code></a> and <em>key</em>
is not present, the <code class="docutils literal"><span class="pre">d[key]</span></code> operation calls that method with the key <em>key</em>
as argument.  The <code class="docutils literal"><span class="pre">d[key]</span></code> operation then returns or raises whatever is
returned or raised by the <code class="docutils literal"><span class="pre">__missing__(key)</span></code> call.
No other operations or methods invoke <a class="reference internal" href="../reference/datamodel.html#object.__missing__" title="object.__missing__"><code class="xref py py-meth docutils literal"><span class="pre">__missing__()</span></code></a>. If
<a class="reference internal" href="../reference/datamodel.html#object.__missing__" title="object.__missing__"><code class="xref py py-meth docutils literal"><span class="pre">__missing__()</span></code></a> is not defined, <a class="reference internal" href="exceptions.html#KeyError" title="KeyError"><code class="xref py py-exc docutils literal"><span class="pre">KeyError</span></code></a> is raised.
<a class="reference internal" href="../reference/datamodel.html#object.__missing__" title="object.__missing__"><code class="xref py py-meth docutils literal"><span class="pre">__missing__()</span></code></a> must be a method; it cannot be an instance variable:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="k">class</span> <span class="nc">Counter</span><span class="p">(</span><span class="nb">dict</span><span class="p">):</span>
<span class="gp">... </span>    <span class="k">def</span> <span class="nf">__missing__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">):</span>
<span class="gp">... </span>        <span class="k">return</span> <span class="mi">0</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">c</span> <span class="o">=</span> <span class="n">Counter</span><span class="p">()</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">c</span><span class="p">[</span><span class="s1">&#39;red&#39;</span><span class="p">]</span>
<span class="go">0</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">c</span><span class="p">[</span><span class="s1">&#39;red&#39;</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">c</span><span class="p">[</span><span class="s1">&#39;red&#39;</span><span class="p">]</span>
<span class="go">1</span>
</pre></div>
</div>
<p>The example above shows part of the implementation of
<a class="reference internal" href="collections.html#collections.Counter" title="collections.Counter"><code class="xref py py-class docutils literal"><span class="pre">collections.Counter</span></code></a>.  A different <code class="docutils literal"><span class="pre">__missing__</span></code> method is used
by <a class="reference internal" href="collections.html#collections.defaultdict" title="collections.defaultdict"><code class="xref py py-class docutils literal"><span class="pre">collections.defaultdict</span></code></a>.</p>
</dd></dl>

<dl class="describe">
<dt>
<code class="descname">d[key] = value</code></dt>
<dd><p>Set <code class="docutils literal"><span class="pre">d[key]</span></code> to <em>value</em>.</p>
</dd></dl>

<dl class="describe">
<dt>
<code class="descname">del d[key]</code></dt>
<dd><p>Remove <code class="docutils literal"><span class="pre">d[key]</span></code> from <em>d</em>.  Raises a <a class="reference internal" href="exceptions.html#KeyError" title="KeyError"><code class="xref py py-exc docutils literal"><span class="pre">KeyError</span></code></a> if <em>key</em> is not in the
map.</p>
</dd></dl>

<dl class="describe">
<dt>
<code class="descname">key in d</code></dt>
<dd><p>Return <code class="docutils literal"><span class="pre">True</span></code> if <em>d</em> has a key <em>key</em>, else <code class="docutils literal"><span class="pre">False</span></code>.</p>
</dd></dl>

<dl class="describe">
<dt>
<code class="descname">key not in d</code></dt>
<dd><p>Equivalent to <code class="docutils literal"><span class="pre">not</span> <span class="pre">key</span> <span class="pre">in</span> <span class="pre">d</span></code>.</p>
</dd></dl>

<dl class="describe">
<dt>
<code class="descname">iter(d)</code></dt>
<dd><p>Return an iterator over the keys of the dictionary.  This is a shortcut
for <code class="docutils literal"><span class="pre">iter(d.keys())</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="dict.clear">
<code class="descname">clear</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#dict.clear" title="Permalink to this definition">¶</a></dt>
<dd><p>Remove all items from the dictionary.</p>
</dd></dl>

<dl class="method">
<dt id="dict.copy">
<code class="descname">copy</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#dict.copy" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a shallow copy of the dictionary.</p>
</dd></dl>

<dl class="classmethod">
<dt id="dict.fromkeys">
<em class="property">classmethod </em><code class="descname">fromkeys</code><span class="sig-paren">(</span><em>seq</em><span class="optional">[</span>, <em>value</em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#dict.fromkeys" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a new dictionary with keys from <em>seq</em> and values set to <em>value</em>.</p>
<p><a class="reference internal" href="#dict.fromkeys" title="dict.fromkeys"><code class="xref py py-meth docutils literal"><span class="pre">fromkeys()</span></code></a> is a class method that returns a new dictionary. <em>value</em>
defaults to <code class="docutils literal"><span class="pre">None</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="dict.get">
<code class="descname">get</code><span class="sig-paren">(</span><em>key</em><span class="optional">[</span>, <em>default</em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#dict.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Return the value for <em>key</em> if <em>key</em> is in the dictionary, else <em>default</em>.
If <em>default</em> is not given, it defaults to <code class="docutils literal"><span class="pre">None</span></code>, so that this method
never raises a <a class="reference internal" href="exceptions.html#KeyError" title="KeyError"><code class="xref py py-exc docutils literal"><span class="pre">KeyError</span></code></a>.</p>
</dd></dl>

<dl class="method">
<dt id="dict.items">
<code class="descname">items</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#dict.items" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a new view of the dictionary&#8217;s items (<code class="docutils literal"><span class="pre">(key,</span> <span class="pre">value)</span></code> pairs).
See the <a class="reference internal" href="#dict-views"><span>documentation of view objects</span></a>.</p>
</dd></dl>

<dl class="method">
<dt id="dict.keys">
<code class="descname">keys</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#dict.keys" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a new view of the dictionary&#8217;s keys.  See the <a class="reference internal" href="#dict-views"><span>documentation
of view objects</span></a>.</p>
</dd></dl>

<dl class="method">
<dt id="dict.pop">
<code class="descname">pop</code><span class="sig-paren">(</span><em>key</em><span class="optional">[</span>, <em>default</em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#dict.pop" title="Permalink to this definition">¶</a></dt>
<dd><p>If <em>key</em> is in the dictionary, remove it and return its value, else return
<em>default</em>.  If <em>default</em> is not given and <em>key</em> is not in the dictionary,
a <a class="reference internal" href="exceptions.html#KeyError" title="KeyError"><code class="xref py py-exc docutils literal"><span class="pre">KeyError</span></code></a> is raised.</p>
</dd></dl>

<dl class="method">
<dt id="dict.popitem">
<code class="descname">popitem</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#dict.popitem" title="Permalink to this definition">¶</a></dt>
<dd><p>Remove and return an arbitrary <code class="docutils literal"><span class="pre">(key,</span> <span class="pre">value)</span></code> pair from the dictionary.</p>
<p><a class="reference internal" href="#dict.popitem" title="dict.popitem"><code class="xref py py-meth docutils literal"><span class="pre">popitem()</span></code></a> is useful to destructively iterate over a dictionary, as
often used in set algorithms.  If the dictionary is empty, calling
<a class="reference internal" href="#dict.popitem" title="dict.popitem"><code class="xref py py-meth docutils literal"><span class="pre">popitem()</span></code></a> raises a <a class="reference internal" href="exceptions.html#KeyError" title="KeyError"><code class="xref py py-exc docutils literal"><span class="pre">KeyError</span></code></a>.</p>
</dd></dl>

<dl class="method">
<dt id="dict.setdefault">
<code class="descname">setdefault</code><span class="sig-paren">(</span><em>key</em><span class="optional">[</span>, <em>default</em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#dict.setdefault" title="Permalink to this definition">¶</a></dt>
<dd><p>If <em>key</em> is in the dictionary, return its value.  If not, insert <em>key</em>
with a value of <em>default</em> and return <em>default</em>.  <em>default</em> defaults to
<code class="docutils literal"><span class="pre">None</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="dict.update">
<code class="descname">update</code><span class="sig-paren">(</span><span class="optional">[</span><em>other</em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#dict.update" title="Permalink to this definition">¶</a></dt>
<dd><p>Update the dictionary with the key/value pairs from <em>other</em>, overwriting
existing keys.  Return <code class="docutils literal"><span class="pre">None</span></code>.</p>
<p><a class="reference internal" href="#dict.update" title="dict.update"><code class="xref py py-meth docutils literal"><span class="pre">update()</span></code></a> accepts either another dictionary object or an iterable of
key/value pairs (as tuples or other iterables of length two).  If keyword
arguments are specified, the dictionary is then updated with those
key/value pairs: <code class="docutils literal"><span class="pre">d.update(red=1,</span> <span class="pre">blue=2)</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="dict.values">
<code class="descname">values</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#dict.values" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a new view of the dictionary&#8217;s values.  See the
<a class="reference internal" href="#dict-views"><span>documentation of view objects</span></a>.</p>
</dd></dl>

<p>Dictionaries compare equal if and only if they have the same <code class="docutils literal"><span class="pre">(key,</span>
<span class="pre">value)</span></code> pairs. Order comparisons (&#8216;&lt;&#8217;, &#8216;&lt;=&#8217;, &#8216;&gt;=&#8217;, &#8216;&gt;&#8217;) raise
<a class="reference internal" href="exceptions.html#TypeError" title="TypeError"><code class="xref py py-exc docutils literal"><span class="pre">TypeError</span></code></a>.</p>
</dd></dl>

<div class="admonition seealso">
<p class="first admonition-title">See also</p>
<p class="last"><a class="reference internal" href="types.html#types.MappingProxyType" title="types.MappingProxyType"><code class="xref py py-class docutils literal"><span class="pre">types.MappingProxyType</span></code></a> can be used to create a read-only view
of a <a class="reference internal" href="#dict" title="dict"><code class="xref py py-class docutils literal"><span class="pre">dict</span></code></a>.</p>
</div>
<div class="section" id="dictionary-view-objects">
<span id="dict-views"></span><h3>4.10.1. Dictionary view objects<a class="headerlink" href="#dictionary-view-objects" title="Permalink to this headline">¶</a></h3>
<p>The objects returned by <a class="reference internal" href="#dict.keys" title="dict.keys"><code class="xref py py-meth docutils literal"><span class="pre">dict.keys()</span></code></a>, <a class="reference internal" href="#dict.values" title="dict.values"><code class="xref py py-meth docutils literal"><span class="pre">dict.values()</span></code></a> and
<a class="reference internal" href="#dict.items" title="dict.items"><code class="xref py py-meth docutils literal"><span class="pre">dict.items()</span></code></a> are <em>view objects</em>.  They provide a dynamic view on the
dictionary&#8217;s entries, which means that when the dictionary changes, the view
reflects these changes.</p>
<p>Dictionary views can be iterated over to yield their respective data, and
support membership tests:</p>
<dl class="describe">
<dt>
<code class="descname">len(dictview)</code></dt>
<dd><p>Return the number of entries in the dictionary.</p>
</dd></dl>

<dl class="describe">
<dt>
<code class="descname">iter(dictview)</code></dt>
<dd><p>Return an iterator over the keys, values or items (represented as tuples of
<code class="docutils literal"><span class="pre">(key,</span> <span class="pre">value)</span></code>) in the dictionary.</p>
<p>Keys and values are iterated over in an arbitrary order which is non-random,
varies across Python implementations, and depends on the dictionary&#8217;s history
of insertions and deletions. If keys, values and items views are iterated
over with no intervening modifications to the dictionary, the order of items
will directly correspond.  This allows the creation of <code class="docutils literal"><span class="pre">(value,</span> <span class="pre">key)</span></code> pairs
using <a class="reference internal" href="functions.html#zip" title="zip"><code class="xref py py-func docutils literal"><span class="pre">zip()</span></code></a>: <code class="docutils literal"><span class="pre">pairs</span> <span class="pre">=</span> <span class="pre">zip(d.values(),</span> <span class="pre">d.keys())</span></code>.  Another way to
create the same list is <code class="docutils literal"><span class="pre">pairs</span> <span class="pre">=</span> <span class="pre">[(v,</span> <span class="pre">k)</span> <span class="pre">for</span> <span class="pre">(k,</span> <span class="pre">v)</span> <span class="pre">in</span> <span class="pre">d.items()]</span></code>.</p>
<p>Iterating views while adding or deleting entries in the dictionary may raise
a <a class="reference internal" href="exceptions.html#RuntimeError" title="RuntimeError"><code class="xref py py-exc docutils literal"><span class="pre">RuntimeError</span></code></a> or fail to iterate over all entries.</p>
</dd></dl>

<dl class="describe">
<dt>
<code class="descname">x in dictview</code></dt>
<dd><p>Return <code class="docutils literal"><span class="pre">True</span></code> if <em>x</em> is in the underlying dictionary&#8217;s keys, values or
items (in the latter case, <em>x</em> should be a <code class="docutils literal"><span class="pre">(key,</span> <span class="pre">value)</span></code> tuple).</p>
</dd></dl>

<p>Keys views are set-like since their entries are unique and hashable.  If all
values are hashable, so that <code class="docutils literal"><span class="pre">(key,</span> <span class="pre">value)</span></code> pairs are unique and hashable,
then the items view is also set-like.  (Values views are not treated as set-like
since the entries are generally not unique.)  For set-like views, all of the
operations defined for the abstract base class <a class="reference internal" href="collections.abc.html#collections.abc.Set" title="collections.abc.Set"><code class="xref py py-class docutils literal"><span class="pre">collections.abc.Set</span></code></a> are
available (for example, <code class="docutils literal"><span class="pre">==</span></code>, <code class="docutils literal"><span class="pre">&lt;</span></code>, or <code class="docutils literal"><span class="pre">^</span></code>).</p>
<p>An example of dictionary view usage:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">dishes</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;eggs&#39;</span><span class="p">:</span> <span class="mi">2</span><span class="p">,</span> <span class="s1">&#39;sausage&#39;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span> <span class="s1">&#39;bacon&#39;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span> <span class="s1">&#39;spam&#39;</span><span class="p">:</span> <span class="mi">500</span><span class="p">}</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">keys</span> <span class="o">=</span> <span class="n">dishes</span><span class="o">.</span><span class="n">keys</span><span class="p">()</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">values</span> <span class="o">=</span> <span class="n">dishes</span><span class="o">.</span><span class="n">values</span><span class="p">()</span>

<span class="gp">&gt;&gt;&gt; </span><span class="c1"># iteration</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">n</span> <span class="o">=</span> <span class="mi">0</span>
<span class="gp">&gt;&gt;&gt; </span><span class="k">for</span> <span class="n">val</span> <span class="ow">in</span> <span class="n">values</span><span class="p">:</span>
<span class="gp">... </span>    <span class="n">n</span> <span class="o">+=</span> <span class="n">val</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">print</span><span class="p">(</span><span class="n">n</span><span class="p">)</span>
<span class="go">504</span>

<span class="gp">&gt;&gt;&gt; </span><span class="c1"># keys and values are iterated over in the same order</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">list</span><span class="p">(</span><span class="n">keys</span><span class="p">)</span>
<span class="go">[&#39;eggs&#39;, &#39;bacon&#39;, &#39;sausage&#39;, &#39;spam&#39;]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">list</span><span class="p">(</span><span class="n">values</span><span class="p">)</span>
<span class="go">[2, 1, 1, 500]</span>

<span class="gp">&gt;&gt;&gt; </span><span class="c1"># view objects are dynamic and reflect dict changes</span>
<span class="gp">&gt;&gt;&gt; </span><span class="k">del</span> <span class="n">dishes</span><span class="p">[</span><span class="s1">&#39;eggs&#39;</span><span class="p">]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="k">del</span> <span class="n">dishes</span><span class="p">[</span><span class="s1">&#39;sausage&#39;</span><span class="p">]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">list</span><span class="p">(</span><span class="n">keys</span><span class="p">)</span>
<span class="go">[&#39;spam&#39;, &#39;bacon&#39;]</span>

<span class="gp">&gt;&gt;&gt; </span><span class="c1"># set operations</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">keys</span> <span class="o">&amp;</span> <span class="p">{</span><span class="s1">&#39;eggs&#39;</span><span class="p">,</span> <span class="s1">&#39;bacon&#39;</span><span class="p">,</span> <span class="s1">&#39;salad&#39;</span><span class="p">}</span>
<span class="go">{&#39;bacon&#39;}</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">keys</span> <span class="o">^</span> <span class="p">{</span><span class="s1">&#39;sausage&#39;</span><span class="p">,</span> <span class="s1">&#39;juice&#39;</span><span class="p">}</span>
<span class="go">{&#39;juice&#39;, &#39;sausage&#39;, &#39;bacon&#39;, &#39;spam&#39;}</span>
</pre></div>
</div>
</div>
</div>
<div class="section" id="context-manager-types">
<span id="typecontextmanager"></span><h2>4.11. Context Manager Types<a class="headerlink" href="#context-manager-types" title="Permalink to this headline">¶</a></h2>
<p id="index-49">Python&#8217;s <a class="reference internal" href="../reference/compound_stmts.html#with"><code class="xref std std-keyword docutils literal"><span class="pre">with</span></code></a> statement supports the concept of a runtime context
defined by a context manager.  This is implemented using a pair of methods
that allow user-defined classes to define a runtime context that is entered
before the statement body is executed and exited when the statement ends:</p>
<dl class="method">
<dt id="contextmanager.__enter__">
<code class="descclassname">contextmanager.</code><code class="descname">__enter__</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#contextmanager.__enter__" title="Permalink to this definition">¶</a></dt>
<dd><p>Enter the runtime context and return either this object or another object
related to the runtime context. The value returned by this method is bound to
the identifier in the <a class="reference internal" href="../reference/compound_stmts.html#as"><code class="xref std std-keyword docutils literal"><span class="pre">as</span></code></a> clause of <a class="reference internal" href="../reference/compound_stmts.html#with"><code class="xref std std-keyword docutils literal"><span class="pre">with</span></code></a> statements using
this context manager.</p>
<p>An example of a context manager that returns itself is a <a class="reference internal" href="../glossary.html#term-file-object"><span class="xref std std-term">file object</span></a>.
File objects return themselves from __enter__() to allow <a class="reference internal" href="functions.html#open" title="open"><code class="xref py py-func docutils literal"><span class="pre">open()</span></code></a> to be
used as the context expression in a <a class="reference internal" href="../reference/compound_stmts.html#with"><code class="xref std std-keyword docutils literal"><span class="pre">with</span></code></a> statement.</p>
<p>An example of a context manager that returns a related object is the one
returned by <a class="reference internal" href="decimal.html#decimal.localcontext" title="decimal.localcontext"><code class="xref py py-func docutils literal"><span class="pre">decimal.localcontext()</span></code></a>. These managers set the active
decimal context to a copy of the original decimal context and then return the
copy. This allows changes to be made to the current decimal context in the body
of the <a class="reference internal" href="../reference/compound_stmts.html#with"><code class="xref std std-keyword docutils literal"><span class="pre">with</span></code></a> statement without affecting code outside the
<a class="reference internal" href="../reference/compound_stmts.html#with"><code class="xref std std-keyword docutils literal"><span class="pre">with</span></code></a> statement.</p>
</dd></dl>

<dl class="method">
<dt id="contextmanager.__exit__">
<code class="descclassname">contextmanager.</code><code class="descname">__exit__</code><span class="sig-paren">(</span><em>exc_type</em>, <em>exc_val</em>, <em>exc_tb</em><span class="sig-paren">)</span><a class="headerlink" href="#contextmanager.__exit__" title="Permalink to this definition">¶</a></dt>
<dd><p>Exit the runtime context and return a Boolean flag indicating if any exception
that occurred should be suppressed. If an exception occurred while executing the
body of the <a class="reference internal" href="../reference/compound_stmts.html#with"><code class="xref std std-keyword docutils literal"><span class="pre">with</span></code></a> statement, the arguments contain the exception type,
value and traceback information. Otherwise, all three arguments are <code class="docutils literal"><span class="pre">None</span></code>.</p>
<p>Returning a true value from this method will cause the <a class="reference internal" href="../reference/compound_stmts.html#with"><code class="xref std std-keyword docutils literal"><span class="pre">with</span></code></a> statement
to suppress the exception and continue execution with the statement immediately
following the <a class="reference internal" href="../reference/compound_stmts.html#with"><code class="xref std std-keyword docutils literal"><span class="pre">with</span></code></a> statement. Otherwise the exception continues
propagating after this method has finished executing. Exceptions that occur
during execution of this method will replace any exception that occurred in the
body of the <a class="reference internal" href="../reference/compound_stmts.html#with"><code class="xref std std-keyword docutils literal"><span class="pre">with</span></code></a> statement.</p>
<p>The exception passed in should never be reraised explicitly - instead, this
method should return a false value to indicate that the method completed
successfully and does not want to suppress the raised exception. This allows
context management code to easily detect whether or not an <a class="reference internal" href="#contextmanager.__exit__" title="contextmanager.__exit__"><code class="xref py py-meth docutils literal"><span class="pre">__exit__()</span></code></a>
method has actually failed.</p>
</dd></dl>

<p>Python defines several context managers to support easy thread synchronisation,
prompt closure of files or other objects, and simpler manipulation of the active
decimal arithmetic context. The specific types are not treated specially beyond
their implementation of the context management protocol. See the
<a class="reference internal" href="contextlib.html#module-contextlib" title="contextlib: Utilities for with-statement contexts."><code class="xref py py-mod docutils literal"><span class="pre">contextlib</span></code></a> module for some examples.</p>
<p>Python&#8217;s <a class="reference internal" href="../glossary.html#term-generator"><span class="xref std std-term">generator</span></a>s and the <a class="reference internal" href="contextlib.html#contextlib.contextmanager" title="contextlib.contextmanager"><code class="xref py py-class docutils literal"><span class="pre">contextlib.contextmanager</span></code></a> decorator
provide a convenient way to implement these protocols.  If a generator function is
decorated with the <a class="reference internal" href="contextlib.html#contextlib.contextmanager" title="contextlib.contextmanager"><code class="xref py py-class docutils literal"><span class="pre">contextlib.contextmanager</span></code></a> decorator, it will return a
context manager implementing the necessary <a class="reference internal" href="../reference/datamodel.html#object.__enter__" title="object.__enter__"><code class="xref py py-meth docutils literal"><span class="pre">__enter__()</span></code></a> and
<a class="reference internal" href="../reference/datamodel.html#object.__exit__" title="object.__exit__"><code class="xref py py-meth docutils literal"><span class="pre">__exit__()</span></code></a> methods, rather than the iterator produced by an undecorated
generator function.</p>
<p>Note that there is no specific slot for any of these methods in the type
structure for Python objects in the Python/C API. Extension types wanting to
define these methods must provide them as a normal Python accessible method.
Compared to the overhead of setting up the runtime context, the overhead of a
single class dictionary lookup is negligible.</p>
</div>
<div class="section" id="other-built-in-types">
<span id="typesother"></span><h2>4.12. Other Built-in Types<a class="headerlink" href="#other-built-in-types" title="Permalink to this headline">¶</a></h2>
<p>The interpreter supports several other kinds of objects. Most of these support
only one or two operations.</p>
<div class="section" id="modules">
<span id="typesmodules"></span><h3>4.12.1. Modules<a class="headerlink" href="#modules" title="Permalink to this headline">¶</a></h3>
<p>The only special operation on a module is attribute access: <code class="docutils literal"><span class="pre">m.name</span></code>, where
<em>m</em> is a module and <em>name</em> accesses a name defined in <em>m</em>&#8216;s symbol table.
Module attributes can be assigned to.  (Note that the <a class="reference internal" href="../reference/simple_stmts.html#import"><code class="xref std std-keyword docutils literal"><span class="pre">import</span></code></a>
statement is not, strictly speaking, an operation on a module object; <code class="docutils literal"><span class="pre">import</span>
<span class="pre">foo</span></code> does not require a module object named <em>foo</em> to exist, rather it requires
an (external) <em>definition</em> for a module named <em>foo</em> somewhere.)</p>
<p>A special attribute of every module is <a class="reference internal" href="#object.__dict__" title="object.__dict__"><code class="xref py py-attr docutils literal"><span class="pre">__dict__</span></code></a>. This is the
dictionary containing the module&#8217;s symbol table. Modifying this dictionary will
actually change the module&#8217;s symbol table, but direct assignment to the
<a class="reference internal" href="#object.__dict__" title="object.__dict__"><code class="xref py py-attr docutils literal"><span class="pre">__dict__</span></code></a> attribute is not possible (you can write
<code class="docutils literal"><span class="pre">m.__dict__['a']</span> <span class="pre">=</span> <span class="pre">1</span></code>, which defines <code class="docutils literal"><span class="pre">m.a</span></code> to be <code class="docutils literal"><span class="pre">1</span></code>, but you can&#8217;t write
<code class="docutils literal"><span class="pre">m.__dict__</span> <span class="pre">=</span> <span class="pre">{}</span></code>).  Modifying <a class="reference internal" href="#object.__dict__" title="object.__dict__"><code class="xref py py-attr docutils literal"><span class="pre">__dict__</span></code></a> directly is
not recommended.</p>
<p>Modules built into the interpreter are written like this: <code class="docutils literal"><span class="pre">&lt;module</span> <span class="pre">'sys'</span>
<span class="pre">(built-in)&gt;</span></code>.  If loaded from a file, they are written as <code class="docutils literal"><span class="pre">&lt;module</span> <span class="pre">'os'</span> <span class="pre">from</span>
<span class="pre">'/usr/local/lib/pythonX.Y/os.pyc'&gt;</span></code>.</p>
</div>
<div class="section" id="classes-and-class-instances">
<span id="typesobjects"></span><h3>4.12.2. Classes and Class Instances<a class="headerlink" href="#classes-and-class-instances" title="Permalink to this headline">¶</a></h3>
<p>See <a class="reference internal" href="../reference/datamodel.html#objects"><span>Objects, values and types</span></a> and <a class="reference internal" href="../reference/compound_stmts.html#class"><span>Class definitions</span></a> for these.</p>
</div>
<div class="section" id="functions">
<span id="typesfunctions"></span><h3>4.12.3. Functions<a class="headerlink" href="#functions" title="Permalink to this headline">¶</a></h3>
<p>Function objects are created by function definitions.  The only operation on a
function object is to call it: <code class="docutils literal"><span class="pre">func(argument-list)</span></code>.</p>
<p>There are really two flavors of function objects: built-in functions and
user-defined functions.  Both support the same operation (to call the function),
but the implementation is different, hence the different object types.</p>
<p>See <a class="reference internal" href="../reference/compound_stmts.html#function"><span>Function definitions</span></a> for more information.</p>
</div>
<div class="section" id="methods">
<span id="typesmethods"></span><h3>4.12.4. Methods<a class="headerlink" href="#methods" title="Permalink to this headline">¶</a></h3>
<p id="index-50">Methods are functions that are called using the attribute notation. There are
two flavors: built-in methods (such as <code class="xref py py-meth docutils literal"><span class="pre">append()</span></code> on lists) and class
instance methods.  Built-in methods are described with the types that support
them.</p>
<p>If you access a method (a function defined in a class namespace) through an
instance, you get a special object: a <em class="dfn">bound method</em> (also called
<em class="dfn">instance method</em>) object. When called, it will add the <code class="docutils literal"><span class="pre">self</span></code> argument
to the argument list.  Bound methods have two special read-only attributes:
<code class="docutils literal"><span class="pre">m.__self__</span></code> is the object on which the method operates, and <code class="docutils literal"><span class="pre">m.__func__</span></code> is
the function implementing the method.  Calling <code class="docutils literal"><span class="pre">m(arg-1,</span> <span class="pre">arg-2,</span> <span class="pre">...,</span> <span class="pre">arg-n)</span></code>
is completely equivalent to calling <code class="docutils literal"><span class="pre">m.__func__(m.__self__,</span> <span class="pre">arg-1,</span> <span class="pre">arg-2,</span> <span class="pre">...,</span>
<span class="pre">arg-n)</span></code>.</p>
<p>Like function objects, bound method objects support getting arbitrary
attributes.  However, since method attributes are actually stored on the
underlying function object (<code class="docutils literal"><span class="pre">meth.__func__</span></code>), setting method attributes on
bound methods is disallowed.  Attempting to set an attribute on a method
results in an <a class="reference internal" href="exceptions.html#AttributeError" title="AttributeError"><code class="xref py py-exc docutils literal"><span class="pre">AttributeError</span></code></a> being raised.  In order to set a method
attribute, you need to explicitly set it on the underlying function object:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="k">class</span> <span class="nc">C</span><span class="p">:</span>
<span class="gp">... </span>    <span class="k">def</span> <span class="nf">method</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<span class="gp">... </span>        <span class="k">pass</span>
<span class="gp">...</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">c</span> <span class="o">=</span> <span class="n">C</span><span class="p">()</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">c</span><span class="o">.</span><span class="n">method</span><span class="o">.</span><span class="n">whoami</span> <span class="o">=</span> <span class="s1">&#39;my name is method&#39;</span>  <span class="c1"># can&#39;t set on the method</span>
<span class="gt">Traceback (most recent call last):</span>
  File <span class="nb">&quot;&lt;stdin&gt;&quot;</span>, line <span class="m">1</span>, in <span class="n">&lt;module&gt;</span>
<span class="gr">AttributeError</span>: <span class="n">&#39;method&#39; object has no attribute &#39;whoami&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">c</span><span class="o">.</span><span class="n">method</span><span class="o">.</span><span class="n">__func__</span><span class="o">.</span><span class="n">whoami</span> <span class="o">=</span> <span class="s1">&#39;my name is method&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">c</span><span class="o">.</span><span class="n">method</span><span class="o">.</span><span class="n">whoami</span>
<span class="go">&#39;my name is method&#39;</span>
</pre></div>
</div>
<p>See <a class="reference internal" href="../reference/datamodel.html#types"><span>The standard type hierarchy</span></a> for more information.</p>
</div>
<div class="section" id="code-objects">
<span id="bltin-code-objects"></span><span id="index-51"></span><h3>4.12.5. Code Objects<a class="headerlink" href="#code-objects" title="Permalink to this headline">¶</a></h3>
<p id="index-52">Code objects are used by the implementation to represent &#8220;pseudo-compiled&#8221;
executable Python code such as a function body. They differ from function
objects because they don&#8217;t contain a reference to their global execution
environment.  Code objects are returned by the built-in <a class="reference internal" href="functions.html#compile" title="compile"><code class="xref py py-func docutils literal"><span class="pre">compile()</span></code></a> function
and can be extracted from function objects through their <code class="xref py py-attr docutils literal"><span class="pre">__code__</span></code>
attribute. See also the <a class="reference internal" href="code.html#module-code" title="code: Facilities to implement read-eval-print loops."><code class="xref py py-mod docutils literal"><span class="pre">code</span></code></a> module.</p>
<p id="index-53">A code object can be executed or evaluated by passing it (instead of a source
string) to the <a class="reference internal" href="functions.html#exec" title="exec"><code class="xref py py-func docutils literal"><span class="pre">exec()</span></code></a> or <a class="reference internal" href="functions.html#eval" title="eval"><code class="xref py py-func docutils literal"><span class="pre">eval()</span></code></a>  built-in functions.</p>
<p>See <a class="reference internal" href="../reference/datamodel.html#types"><span>The standard type hierarchy</span></a> for more information.</p>
</div>
<div class="section" id="type-objects">
<span id="bltin-type-objects"></span><h3>4.12.6. Type Objects<a class="headerlink" href="#type-objects" title="Permalink to this headline">¶</a></h3>
<p id="index-54">Type objects represent the various object types.  An object&#8217;s type is accessed
by the built-in function <a class="reference internal" href="functions.html#type" title="type"><code class="xref py py-func docutils literal"><span class="pre">type()</span></code></a>.  There are no special operations on
types.  The standard module <a class="reference internal" href="types.html#module-types" title="types: Names for built-in types."><code class="xref py py-mod docutils literal"><span class="pre">types</span></code></a> defines names for all standard built-in
types.</p>
<p>Types are written like this: <code class="docutils literal"><span class="pre">&lt;class</span> <span class="pre">'int'&gt;</span></code>.</p>
</div>
<div class="section" id="the-null-object">
<span id="bltin-null-object"></span><h3>4.12.7. The Null Object<a class="headerlink" href="#the-null-object" title="Permalink to this headline">¶</a></h3>
<p>This object is returned by functions that don&#8217;t explicitly return a value.  It
supports no special operations.  There is exactly one null object, named
<code class="docutils literal"><span class="pre">None</span></code> (a built-in name).  <code class="docutils literal"><span class="pre">type(None)()</span></code> produces the same singleton.</p>
<p>It is written as <code class="docutils literal"><span class="pre">None</span></code>.</p>
</div>
<div class="section" id="the-ellipsis-object">
<span id="bltin-ellipsis-object"></span><h3>4.12.8. The Ellipsis Object<a class="headerlink" href="#the-ellipsis-object" title="Permalink to this headline">¶</a></h3>
<p>This object is commonly used by slicing (see <a class="reference internal" href="../reference/expressions.html#slicings"><span>Slicings</span></a>).  It supports no
special operations.  There is exactly one ellipsis object, named
<a class="reference internal" href="constants.html#Ellipsis" title="Ellipsis"><code class="xref py py-const docutils literal"><span class="pre">Ellipsis</span></code></a> (a built-in name).  <code class="docutils literal"><span class="pre">type(Ellipsis)()</span></code> produces the
<a class="reference internal" href="constants.html#Ellipsis" title="Ellipsis"><code class="xref py py-const docutils literal"><span class="pre">Ellipsis</span></code></a> singleton.</p>
<p>It is written as <code class="docutils literal"><span class="pre">Ellipsis</span></code> or <code class="docutils literal"><span class="pre">...</span></code>.</p>
</div>
<div class="section" id="the-notimplemented-object">
<span id="bltin-notimplemented-object"></span><h3>4.12.9. The NotImplemented Object<a class="headerlink" href="#the-notimplemented-object" title="Permalink to this headline">¶</a></h3>
<p>This object is returned from comparisons and binary operations when they are
asked to operate on types they don&#8217;t support. See <a class="reference internal" href="../reference/expressions.html#comparisons"><span>Comparisons</span></a> for more
information.  There is exactly one <code class="docutils literal"><span class="pre">NotImplemented</span></code> object.
<code class="docutils literal"><span class="pre">type(NotImplemented)()</span></code> produces the singleton instance.</p>
<p>It is written as <code class="docutils literal"><span class="pre">NotImplemented</span></code>.</p>
</div>
<div class="section" id="boolean-values">
<span id="bltin-boolean-values"></span><h3>4.12.10. Boolean Values<a class="headerlink" href="#boolean-values" title="Permalink to this headline">¶</a></h3>
<p>Boolean values are the two constant objects <code class="docutils literal"><span class="pre">False</span></code> and <code class="docutils literal"><span class="pre">True</span></code>.  They are
used to represent truth values (although other values can also be considered
false or true).  In numeric contexts (for example when used as the argument to
an arithmetic operator), they behave like the integers 0 and 1, respectively.
The built-in function <a class="reference internal" href="functions.html#bool" title="bool"><code class="xref py py-func docutils literal"><span class="pre">bool()</span></code></a> can be used to convert any value to a
Boolean, if the value can be interpreted as a truth value (see section
<a class="reference internal" href="#truth"><span>Truth Value Testing</span></a> above).</p>
<p id="index-55">They are written as <code class="docutils literal"><span class="pre">False</span></code> and <code class="docutils literal"><span class="pre">True</span></code>, respectively.</p>
</div>
<div class="section" id="internal-objects">
<span id="typesinternal"></span><h3>4.12.11. Internal Objects<a class="headerlink" href="#internal-objects" title="Permalink to this headline">¶</a></h3>
<p>See <a class="reference internal" href="../reference/datamodel.html#types"><span>The standard type hierarchy</span></a> for this information.  It describes stack frame objects,
traceback objects, and slice objects.</p>
</div>
</div>
<div class="section" id="special-attributes">
<span id="specialattrs"></span><h2>4.13. Special Attributes<a class="headerlink" href="#special-attributes" title="Permalink to this headline">¶</a></h2>
<p>The implementation adds a few special read-only attributes to several object
types, where they are relevant.  Some of these are not reported by the
<a class="reference internal" href="functions.html#dir" title="dir"><code class="xref py py-func docutils literal"><span class="pre">dir()</span></code></a> built-in function.</p>
<dl class="attribute">
<dt id="object.__dict__">
<code class="descclassname">object.</code><code class="descname">__dict__</code><a class="headerlink" href="#object.__dict__" title="Permalink to this definition">¶</a></dt>
<dd><p>A dictionary or other mapping object used to store an object&#8217;s (writable)
attributes.</p>
</dd></dl>

<dl class="attribute">
<dt id="instance.__class__">
<code class="descclassname">instance.</code><code class="descname">__class__</code><a class="headerlink" href="#instance.__class__" title="Permalink to this definition">¶</a></dt>
<dd><p>The class to which a class instance belongs.</p>
</dd></dl>

<dl class="attribute">
<dt id="class.__bases__">
<code class="descclassname">class.</code><code class="descname">__bases__</code><a class="headerlink" href="#class.__bases__" title="Permalink to this definition">¶</a></dt>
<dd><p>The tuple of base classes of a class object.</p>
</dd></dl>

<dl class="attribute">
<dt id="definition.__name__">
<code class="descclassname">definition.</code><code class="descname">__name__</code><a class="headerlink" href="#definition.__name__" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the class, function, method, descriptor, or
generator instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="definition.__qualname__">
<code class="descclassname">definition.</code><code class="descname">__qualname__</code><a class="headerlink" href="#definition.__qualname__" title="Permalink to this definition">¶</a></dt>
<dd><p>The <a class="reference internal" href="../glossary.html#term-qualified-name"><span class="xref std std-term">qualified name</span></a> of the class, function, method, descriptor,
or generator instance.</p>
<div class="versionadded">
<p><span class="versionmodified">New in version 3.3.</span></p>
</div>
</dd></dl>

<dl class="attribute">
<dt id="class.__mro__">
<code class="descclassname">class.</code><code class="descname">__mro__</code><a class="headerlink" href="#class.__mro__" title="Permalink to this definition">¶</a></dt>
<dd><p>This attribute is a tuple of classes that are considered when looking for
base classes during method resolution.</p>
</dd></dl>

<dl class="method">
<dt id="class.mro">
<code class="descclassname">class.</code><code class="descname">mro</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#class.mro" title="Permalink to this definition">¶</a></dt>
<dd><p>This method can be overridden by a metaclass to customize the method
resolution order for its instances.  It is called at class instantiation, and
its result is stored in <a class="reference internal" href="#class.__mro__" title="class.__mro__"><code class="xref py py-attr docutils literal"><span class="pre">__mro__</span></code></a>.</p>
</dd></dl>

<dl class="method">
<dt id="class.__subclasses__">
<code class="descclassname">class.</code><code class="descname">__subclasses__</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#class.__subclasses__" title="Permalink to this definition">¶</a></dt>
<dd><p>Each class keeps a list of weak references to its immediate subclasses.  This
method returns a list of all those references still alive.
Example:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="nb">int</span><span class="o">.</span><span class="n">__subclasses__</span><span class="p">()</span>
<span class="go">[&lt;class &#39;bool&#39;&gt;]</span>
</pre></div>
</div>
</dd></dl>

<p class="rubric">Footnotes</p>
<table class="docutils footnote" frame="void" id="id11" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id1">[1]</a></td><td>Additional information on these special methods may be found in the Python
Reference Manual (<a class="reference internal" href="../reference/datamodel.html#customization"><span>Basic customization</span></a>).</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="id12" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id2">[2]</a></td><td>As a consequence, the list <code class="docutils literal"><span class="pre">[1,</span> <span class="pre">2]</span></code> is considered equal to <code class="docutils literal"><span class="pre">[1.0,</span> <span class="pre">2.0]</span></code>, and
similarly for tuples.</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="id13" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label">[3]</td><td>They must have since the parser can&#8217;t tell the type of the operands.</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="id14" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label">[4]</td><td><em>(<a class="fn-backref" href="#id5">1</a>, <a class="fn-backref" href="#id6">2</a>, <a class="fn-backref" href="#id7">3</a>, <a class="fn-backref" href="#id8">4</a>)</em> Cased characters are those with general category property being one of
&#8220;Lu&#8221; (Letter, uppercase), &#8220;Ll&#8221; (Letter, lowercase), or &#8220;Lt&#8221; (Letter, titlecase).</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="id15" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label">[5]</td><td><em>(<a class="fn-backref" href="#id9">1</a>, <a class="fn-backref" href="#id10">2</a>)</em> To format only a tuple you should therefore provide a singleton tuple whose only
element is the tuple to be formatted.</td></tr>
</tbody>
</table>
</div>
</div>


          </div>
        </div>
      </div>
      <div class="sphinxsidebar" role="navigation" aria-label="main navigation">
        <div class="sphinxsidebarwrapper">
  <h3><a href="../contents.html">Table Of Contents</a></h3>
  <ul>
<li><a class="reference internal" href="#">4. Built-in Types</a><ul>
<li><a class="reference internal" href="#truth-value-testing">4.1. Truth Value Testing</a></li>
<li><a class="reference internal" href="#boolean-operations-and-or-not">4.2. Boolean Operations &#8212; <code class="docutils literal"><span class="pre">and</span></code>, <code class="docutils literal"><span class="pre">or</span></code>, <code class="docutils literal"><span class="pre">not</span></code></a></li>
<li><a class="reference internal" href="#comparisons">4.3. Comparisons</a></li>
<li><a class="reference internal" href="#numeric-types-int-float-complex">4.4. Numeric Types &#8212; <code class="docutils literal"><span class="pre">int</span></code>, <code class="docutils literal"><span class="pre">float</span></code>, <code class="docutils literal"><span class="pre">complex</span></code></a><ul>
<li><a class="reference internal" href="#bitwise-operations-on-integer-types">4.4.1. Bitwise Operations on Integer Types</a></li>
<li><a class="reference internal" href="#additional-methods-on-integer-types">4.4.2. Additional Methods on Integer Types</a></li>
<li><a class="reference internal" href="#additional-methods-on-float">4.4.3. Additional Methods on Float</a></li>
<li><a class="reference internal" href="#hashing-of-numeric-types">4.4.4. Hashing of numeric types</a></li>
</ul>
</li>
<li><a class="reference internal" href="#iterator-types">4.5. Iterator Types</a><ul>
<li><a class="reference internal" href="#generator-types">4.5.1. Generator Types</a></li>
</ul>
</li>
<li><a class="reference internal" href="#sequence-types-list-tuple-range">4.6. Sequence Types &#8212; <code class="docutils literal"><span class="pre">list</span></code>, <code class="docutils literal"><span class="pre">tuple</span></code>, <code class="docutils literal"><span class="pre">range</span></code></a><ul>
<li><a class="reference internal" href="#common-sequence-operations">4.6.1. Common Sequence Operations</a></li>
<li><a class="reference internal" href="#immutable-sequence-types">4.6.2. Immutable Sequence Types</a></li>
<li><a class="reference internal" href="#mutable-sequence-types">4.6.3. Mutable Sequence Types</a></li>
<li><a class="reference internal" href="#lists">4.6.4. Lists</a></li>
<li><a class="reference internal" href="#tuples">4.6.5. Tuples</a></li>
<li><a class="reference internal" href="#ranges">4.6.6. Ranges</a></li>
</ul>
</li>
<li><a class="reference internal" href="#text-sequence-type-str">4.7. Text Sequence Type &#8212; <code class="docutils literal"><span class="pre">str</span></code></a><ul>
<li><a class="reference internal" href="#string-methods">4.7.1. String Methods</a></li>
<li><a class="reference internal" href="#printf-style-string-formatting">4.7.2. <code class="docutils literal"><span class="pre">printf</span></code>-style String Formatting</a></li>
</ul>
</li>
<li><a class="reference internal" href="#binary-sequence-types-bytes-bytearray-memoryview">4.8. Binary Sequence Types &#8212; <code class="docutils literal"><span class="pre">bytes</span></code>, <code class="docutils literal"><span class="pre">bytearray</span></code>, <code class="docutils literal"><span class="pre">memoryview</span></code></a><ul>
<li><a class="reference internal" href="#bytes">4.8.1. Bytes</a></li>
<li><a class="reference internal" href="#bytearray-objects">4.8.2. Bytearray Objects</a></li>
<li><a class="reference internal" href="#bytes-and-bytearray-operations">4.8.3. Bytes and Bytearray Operations</a></li>
<li><a class="reference internal" href="#printf-style-bytes-formatting">4.8.4. <code class="docutils literal"><span class="pre">printf</span></code>-style Bytes Formatting</a></li>
<li><a class="reference internal" href="#memory-views">4.8.5. Memory Views</a></li>
</ul>
</li>
<li><a class="reference internal" href="#set-types-set-frozenset">4.9. Set Types &#8212; <code class="docutils literal"><span class="pre">set</span></code>, <code class="docutils literal"><span class="pre">frozenset</span></code></a></li>
<li><a class="reference internal" href="#mapping-types-dict">4.10. Mapping Types &#8212; <code class="docutils literal"><span class="pre">dict</span></code></a><ul>
<li><a class="reference internal" href="#dictionary-view-objects">4.10.1. Dictionary view objects</a></li>
</ul>
</li>
<li><a class="reference internal" href="#context-manager-types">4.11. Context Manager Types</a></li>
<li><a class="reference internal" href="#other-built-in-types">4.12. Other Built-in Types</a><ul>
<li><a class="reference internal" href="#modules">4.12.1. Modules</a></li>
<li><a class="reference internal" href="#classes-and-class-instances">4.12.2. Classes and Class Instances</a></li>
<li><a class="reference internal" href="#functions">4.12.3. Functions</a></li>
<li><a class="reference internal" href="#methods">4.12.4. Methods</a></li>
<li><a class="reference internal" href="#code-objects">4.12.5. Code Objects</a></li>
<li><a class="reference internal" href="#type-objects">4.12.6. Type Objects</a></li>
<li><a class="reference internal" href="#the-null-object">4.12.7. The Null Object</a></li>
<li><a class="reference internal" href="#the-ellipsis-object">4.12.8. The Ellipsis Object</a></li>
<li><a class="reference internal" href="#the-notimplemented-object">4.12.9. The NotImplemented Object</a></li>
<li><a class="reference internal" href="#boolean-values">4.12.10. Boolean Values</a></li>
<li><a class="reference internal" href="#internal-objects">4.12.11. Internal Objects</a></li>
</ul>
</li>
<li><a class="reference internal" href="#special-attributes">4.13. Special Attributes</a></li>
</ul>
</li>
</ul>

  <h4>Previous topic</h4>
  <p class="topless"><a href="constants.html"
                        title="previous chapter">3. Built-in Constants</a></p>
  <h4>Next topic</h4>
  <p class="topless"><a href="exceptions.html"
                        title="next chapter">5. Built-in Exceptions</a></p>
  <div role="note" aria-label="source link">
    <h3>This Page</h3>
    <ul class="this-page-menu">
      <li><a href="../bugs.html">Report a Bug</a></li>
      <li>
        <a href="https://github.com/python/cpython/blob/3.6/Doc/library/stdtypes.rst"
            rel="nofollow">Show Source
        </a>
      </li>
    </ul>
  </div>
        </div>
      </div>
      <div class="clearer"></div>
    </div>
    <div class="related" role="navigation" aria-label="related navigation">
      <h3>Navigation</h3>
      <ul>
        <li class="right" style="margin-right: 10px">
          <a href="../genindex.html" title="General Index"
             >index</a></li>
        <li class="right" >
          <a href="../py-modindex.html" title="Python Module Index"
             >modules</a> |</li>
        <li class="right" >
          <a href="exceptions.html" title="5. Built-in Exceptions"
             >next</a> |</li>
        <li class="right" >
          <a href="constants.html" title="3. Built-in Constants"
             >previous</a> |</li>
        <li><img src="../_static/py.png" alt=""
                 style="vertical-align: middle; margin-top: -1px"/></li>
        <li><a href="https://www.python.org/">Python</a> &raquo;</li>
        <li>
          <span class="version_switcher_placeholder">3.6.1</span>
          <a href="../index.html">Documentation </a> &raquo;
        </li>

          <li class="nav-item nav-item-1"><a href="index.html" >The Python Standard Library</a> &raquo;</li>
    <li class="right">


    <div class="inline-search" style="display: none" role="search">
        <form class="inline-search" action="../search.html" method="get">
          <input placeholder="Quick search" type="text" name="q" />
          <input type="submit" value="Go" />
          <input type="hidden" name="check_keywords" value="yes" />
          <input type="hidden" name="area" value="default" />
        </form>
    </div>
    <script type="text/javascript">$('.inline-search').show(0);</script>
         |
    </li>

      </ul>
    </div>
    <div class="footer">
    &copy; <a href="../copyright.html">Copyright</a> 2001-2017, Python Software Foundation.
    <br />
    The Python Software Foundation is a non-profit corporation.
    <a href="https://www.python.org/psf/donations/">Please donate.</a>
    <br />
    Last updated on Mar 26, 2017.
    <a href="../bugs.html">Found a bug</a>?
    <br />
    Created using <a href="http://sphinx.pocoo.org/">Sphinx</a> 1.3.3.
    </div>

  </body>
</html>

"""

print (crawel_web(seed))
