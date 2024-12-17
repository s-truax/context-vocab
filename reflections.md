
# Table of Contents

-   [Goals](#org38e33b4)
-   [Reflections](#orgcac8eaf)
-   [Further reading](#org20c104c)



<a id="org38e33b4"></a>

# Goals


<a id="orgcac8eaf"></a>

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


<a id="org20c104c"></a>

# Further reading

-   Found [this](https://www.youtube.com/watch?v=3MNVP9-hglc) video about alternatives to object inheritance.
-   Some documents from that video's comments:
    -   <https://prl.ccs.neu.edu/img/p-tr-1971.pdf>
    -   <https://www.cs.tufts.edu/~nr/cs257/archive/barbara-liskov/data-abstraction-and-hierarchy.pdf>

