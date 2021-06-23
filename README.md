# Flowers, fractals and networks: a nature-inspired approach for network analysis
Master's Thesis of Federica Trevisan
***

Is it possible to implement an algorithm starting from a flower?

This thesis combines three lines of research: natural computing, social network analysis and fractal objects, intertwining them with the aim of developing a hierarchical procedure for network analysis. Drawing inspiration from the inflorescence structure of a plant belonging to the family of umbelliferae, the Daucus Carota, and declining these concepts in an algorithmic context, Daucus Fractal Network Analyzer (DFNA) has been implemented: a procedure that allows to compress and decompress networks by relying on the assumption that fractal structures are present within them.

From the experiments carried out, a hierarchical procedure is born that allows to model and simplify networks. DFNA identifies previously defined patterns within a network, subsequently compresses them in a single node in an iterative manner with three different compression techniques, until it reaches a network without repeated patterns inside.

Experiments were carried out on a vast repertoire of networks of different nature: DFNA was applied by analyzing a total of twelve networks divided into four different groups with different patterns. The experiments confirm the hypothesis that the same types of fractal patterns are present in groups of homogeneous networks.
<p align="center">
  <img width="460" height="300" src="https://user-images.githubusercontent.com/17218213/123143135-82b55880-d45a-11eb-94d6-4670e63eb552.png">
  <figcaption>Comparison picture. On the left there's the Daucus Carota flower and on the right the initial and final step of DFNA procedure.</figcaption>
</p>

The repository contains the following files:
- [Codebase for Daucus Fractal Network Analyzer](https://github.com/kdd-lab/2020_Trevisan/tree/master/code/notebook)
- [Datasets of the corpus of networks tested in the experimental phase](https://github.com/kdd-lab/2020_Trevisan/tree/master/datasets)
- [Literature study for the current state of the art on Natural Computing, Network Science and Fractals](https://github.com/kdd-lab/2020_Trevisan/tree/master/related)
- [Thesis paper in Italian (more than 100 pages) and a shorter version in English (tbd soon)](https://github.com/kdd-lab/2020_Trevisan/tree/master/thesis)
