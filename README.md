# Farlamp

Project definition:

```
I'm studying the impact of overseer failure on RL-based IDA,
    because I want to know under what conditions the amplification increases or
    decreases the failure rate,
        in order to help my reader understand whether we need to combine
        capability amplification with explicit reliability amplification in all
        cases.
```

In this project I will:

1. Take the implementation of iterated distillation and amplification from
   Christiano et al.'s ‘Supervising strong learners by amplifying weak experts’
   and adapt it to reinforcement learning. It's using supervised learning now.
2. Introduce overseer failures and see how they impact the overall failure rate.
3. Write a paper a

[Overseer failures in SupAmp and ReAmp](overfail2.pdf) contains a more extensive
introduction, as well as an explanation of the relevant terms, concepts etc.


## Repository contents

- [Overseer failures in SupAmp and ReAmp](overfail2.pdf) – Start here. This is
  the most polished document so far.
- [How to turn SupAmp into ReAmp?](supamp-reamp.pdf) – Less detailed and less
  polished analysis of how to approach the first project phase.
- [What I need for the Farlamp draft](draft-basis.pdf) – Will contain all the
  information I need for planning a draft.
- [Project outline](farlamp-plan.pdf) – Overview of iterations, tasks,
  estimates, deadlines and status.

The other files are only useful for me. The code won't be published here,
because it will be based on the code from CSASupAmp, which underlies some strict
publication policy.


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


## Thanks

Thanks to [Paul Christiano](https://paulfchristiano.com/) for funding this
project and giving me advice. Thanks also to [William
Saunders](http://williamsaunders.net/) for providing his version of the
CSASupAmp code.


## Licence

See [LICENSE.txt].
