# Farlamp

Note 2021-07-31: I decide to leave AI alignment research last year. See
https://www.lesswrong.com/posts/HDXLTFnSndhpLj2XZ/i-m-leaving-ai-alignment-you-better-stay
This repo shows the state of my research at the time I left.

BLUF: Read [Overseer failures in SupAmp and ReAmp](build/overfail2.pdf), then
the interesting parts of [Training a tiny SupAmp model on easy
tasks](build/tiny-supfail.pdf).

Project definition (CoR):

```
I'm studying the impact of overseer failure on RL-based IDA,
    because I want to know under what conditions amplification and distillation
    increase or decrease the failure rate,
        in order to help my reader understand whether explicit reliability
        amplification is necessary for IDA to work in practice.
```

In this project I will:

1. Take the implementation of iterated distillation and amplification from
   Christiano et al.'s [‘Supervising strong learners by amplifying weak
   experts’](https://arxiv.org/abs/1810.08575), introduce overseer failures and
   see how they influence the overall failure rate.
2. Adapt the system to reinforcement learning. (It uses supervised learning
   now.)
2. Introduce overseer failures in the RL setting and see how they influence the
   overall failure rate.
3. Write a paper about the results.

[Overseer failures in SupAmp and ReAmp](build/overfail2.pdf) contains a more
extensive introduction, as well as an explanation of the relevant terms,
concepts etc.

For the code see
[rmoehn/amplification](https://github.com/rmoehn/amplification), which is a fork
of
[paulfchristiano/amplification](https://github.com/paulfchristiano/amplification).


## Repository contents

- [Overseer failures in SupAmp and ReAmp](build/overfail2.pdf) – Start here.
  This is the most polished document so far.
- [Training a tiny SupAmp model on easy tasks](build/tiny-supfail.pdf) – Report
  on first experiments.
- [How to turn SupAmp into ReAmp?](build/supamp-reamp.pdf) – Less detailed and
  less polished analysis of how to approach the first project phase.
- [What I need for planning the Farlamp draft](build/draft-basis.pdf) – Will
  contain all the information I need for planning a draft of the paper.
- [Literature overview](build/literature.pdf) – Work in progress of searching,
  skimming, filtering, summarizing literature for this project.
- [Current project outline](farlamp-fogbugz-plan.png) – Overview of cases and
  estimates. Most up to date, but doesn't contain upcoming milestones.
- [Old project outline](farlamp-omniplan.pdf) – Outdated, but does contain
  some upcoming milestones.

There are more files, but they are only useful for me. The code won't be
published here, because it will be based on the code from CSASupAmp, which
underlies some strict publication policy.


## Glossary

| Term          | Definition
| ------------- | ----------
| CoR           | Booth et al.: The Craft of Research
| CSASupAmp     | Christiano et al.: Supervising strong learners by amplifying weak experts
| Est. 5 %      | 5th percentile of my estimated duration distribution/leftmost point in triangle distribution
| Est. mode     | mode of my estimated duration distribution
| Est. 95 %     | 95th percentile of my estimated duration distribution/rightmost point in triangle distribution
| Farlamp       | Failures in RL-based amplification (I just had to come up with a short project name.)
| Draft Basis   | A template derived from CoR, p. 175, which when filled in completely, provides all the information necessary for planning a draft. Includes the structure of the argument.
| LW            | LessWrong
| MxD           | MIRIxDiscord
| RL            | reinforcement learning
| ReAmp         | SupAmp adapted to RL
| SL            | supervised learning
| SupAmp        | The system from CSASupAmp for iterated distillation and amplification using supervised learning

For detailed bibliographical information see [references.bib](references.bib).


## Thanks

Thanks to [Paul Christiano](https://paulfchristiano.com/) for funding this
project and giving me advice. Thanks also to [William
Saunders](http://williamsaunders.net/) for providing his version of the
CSASupAmp code.


## Licence

<p xmlns:dct="http://purl.org/dc/terms/" xmlns:vcard="http://www.w3.org/2001/vcard-rdf/3.0#">
  <a rel="license"
     href="http://creativecommons.org/publicdomain/zero/1.0/">
    <img src="http://i.creativecommons.org/p/zero/1.0/88x31.png" style="border-style: none;" alt="CC0" />
  </a>
  <br />
  To the extent possible under law,
  <a rel="dct:publisher"
     href="https://rmoehn.wordpress.com">
    <span property="dct:title">Richard Möhn</span></a>
  has waived all copyright and related or neighboring rights to
  <span property="dct:title">Farlamp documentation</span>.
This work is published from:
<span property="vcard:Country" datatype="dct:ISO3166"
      content="JP" about="https://rmoehn.wordpress.com">
  Japan</span>.
</p>
