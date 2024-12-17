
# Table of Contents

-   [Goals](#org29d0e7a)
-   [Reflections](#org1afff46)
-   [Further reading](#org4f1d8b7)
-   [Future ideas](#orgb0882d6)
    -   [A better interface?](#orgf074b46)



<a id="org29d0e7a"></a>

# Goals


<a id="org1afff46"></a>

# Reflections

-   Abstractly, this project was about ingesting data from various
    sources and combining the data in a structured way that made it easy
    to process.
-   Doing things with dictionaries is good for a first pass but having a
    type or data structure with some explicit attributes definitely
    makes the code more readable.
-   When its your own project, you can make it as messy as you want.
-   I found I have a tendency to avoid wanting to write my own types,
    but in this case it was fine. Using a well-documented and understood
    type from the stdlib or another common package has the advantage
    that other programmers will trust and understand your code when they
    frist read it. However, I don't think it's too much to ask someone
    to just read a simple record data structure like the two I used for
    this project.
-   For one -> many mappings, collections.defaultdict(list) is a great option.
-   The plus of using NamedTuple, SimpleNamespace, or @dataclass is that
    you get a free ~\_<sub>repr</sub>\_\_\` and also other programmers recognize the pattern.
-   I decided to write my own little classes because I wanted to enforce
    the use of the constructor. Sort of in the philosophy of "make
    illegal program states unrepresentable"
-   Being able to print out the data structures in a human-readable
    format for debugging is extremely useful.
-   Worry about correctness and intelligibility before performance. I
    probably wasted way too much time thinking about little
    optimizations that didn't matter.
-   Writing out code by hand is good. It's kind of like rubber-duck coding.


<a id="org4f1d8b7"></a>

# Further reading

-   Found [this](https://www.youtube.com/watch?v=3MNVP9-hglc) video about alternatives to object inheritance.
-   Some documents from that video's comments:
    -   <https://prl.ccs.neu.edu/img/p-tr-1971.pdf>
    -   <https://www.cs.tufts.edu/~nr/cs257/archive/barbara-liskov/data-abstraction-and-hierarchy.pdf>


<a id="orgb0882d6"></a>

# Future ideas

-   Rewrite this in Haskell with types.
-   Add `genanki` functionality.


<a id="orgf074b46"></a>

## A better interface?

-   What would be cook is some kind of GUI.
-   You would
    1.  Manually create your vocab list.
    2.  For each term in your vocab list:
    3.  GUI does a Tatoeba search. Search can be paramatarized.
    4.  GUI displays the current term and the search results.
    5.  You can browse through the search results.
    6.  GUI gives you the option to modify the search, either its
        parameters or filters.
    7.  Sentences and translations are displayed like they are in the
        Tatoeba web app.
    8.  When you find a sentence you like, you mark it. You can mark multiple.
    9.  The app stores your choice.
    10. The next term in your list is shown.
    11. At the end, you get a `.tsv` that can be imported as Anki flaschards.
    12. Could also generate an anki deck.
-   The app would be smart enough to figure out what is a phrase, a
    seperable verb, the plural and singular forms of a noun.

