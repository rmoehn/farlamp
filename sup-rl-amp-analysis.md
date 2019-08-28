---
title: Analysis: How to turn SupAmp into ReAmp?
subtitle: WIP
author: Richard Möhn
date: 2019-08-28
abstract: TBD
---

Before I can experiment with overseer failure, I need to adapt the supervised
learning system from [@CSASupAmp] to reinforcement learning and evaluate the
result on the original tasks from [@CSASupAmp].

# Major adaptations

## Adapting the mechanism

(The following four items are are a close paraphrase of the training process
outline from [@CSASupAmp{sec. 2.2}] with changes to make it work with RL.)

In the following three points I paraphrase [@CSASupAmp{sec. 2.2}] closely, with
adaptations for RL. Note that here we run only three processes in parallel,
while in the original there are four. This is because the original trains $X$
with supervised learning (SL), where we can feed samples asynchronously to the
learner in one direction. Here we need two-way synchronous communication,
because $X$ generates a sample answer, gives it to $Amplify^{H'}(X)$ for
evaluation and gets back a reward that it learns from.

\zkref{Z22a1c1}

1. Sample a question $q ~ D$ and pose it to $X$. $X$ returns answer $a$. Use
   $\Amplify^H(X)$ to evaluate $a$ and calculate a reward $r$ for $X$. Record
   the whole interaction, ie. $(q, a, \left<\text{sub-questions and
   -answers}\right>, r)$. The number of sub-questions $H$ asks is fixed.
2. Using a recording from process 1, train $H'$ to predict the outputs of
   $H$.
3. Sample a question $q ~ D$ and pose it to $X$. $X$ returns answer $a$. Feed
   $q$ and $a$ to $\Amplify^{H'}(X)$ to generate a reward $r$. Train $X$ on $r$
   using reinforcement learning.

At the bottom there are questions whose answers $H$ can evaluate without asking
sub-questions. Cf. [@StuhDelCog].

\OQ If the number $l$ of sub-questions is fixed, does $H$ ask blank
sub-questions if it has fewer than $l$ actual sub-questions?

\OQ Does it always go all the way down to the primitive questions? Or does H
answer higher-level questions directly as well?

\OQ How does pretraining work? How do I have to adapt it?

- \TODO Read what Paul has written about RL-based IDA.


## Adapting the overseer scripts and questions

\zkref{Z22b}

- Almost the same, except that X now suggests an answer to the top-level
  question and H gives it a reward depending on how close the suggested answer
  is to the truth.
- In order to find the truth, H asks sub-questions.

- \TODO Sketch how to adapt all the scripts to evaluation. – Looks like a larger
  task. Need to put this in the project plan.


### Permutation powering

- What is the greatest power that we expect H to figure without asking
  sub-questions?

Given this permutation s:

```
0 → 1
1 → 0
2 → 6
3 → 2
4 → 3
5 → 5
6 → 4
7 → 7

Q1: What is s28(4)?
A1: 7

Q1.1: What is s14(4)?
A1.1: 7

Q1.2: What is s14(A1.1)?
A1.2: 4
```

But the true answer A1\* is 4. (In this example I generated A1.1 and A1.2
randomly, so even though A1.2 is equal to the true answer, it's just a
coincidence.) So the overseer should give reward 0. Only if the result is
correct should it give reward 1.
- Is there any notion of partly correct? For other tasks? Yes, for example for
  Shortest path, one could give a reward > 0 for paths that are almost shortest.

\OQ How does it know when to trust the sub-answers? How does it know it in
SupAmp? Does it blindly rely on them and only with small k compute the correct
answer by itself and thus push the training in the right direction? But then we
would initially push it in the wrong direction.

- Perhaps better training signal if I ask for all the intermediate results and
  make the reward the number of correct mappings? But then I prevent the
  learning of more efficient representations.

- early experiments: Start with the easiest task and very small size. Eg.
  permutation powering with small $k$ and $N$.


## Determining the rewards

- Not clear to me yet.
- Seems like some some tasks, such as \task{permutation powering}, we can only
  give reward 1 for a right answer and reward 0 for a wrong answer.
- On other tasks the reward might be between 1 and 0, depending on how close
  $X$'s response was to the correct answer. For example, for \task{shortest
  path}.
- In the latter case the evaluation scripts might become more complicated,
  though.
- Choosing between two answers as in [@StuhFacCog] wouldn't work well here. Or
  would it? \zkref{Z22a1b1} \zkref{Z22a1b1a} \OQ Why do they do it, though?

- \TODO Get a general idea about how reward are determined in RL.
  \zkref{Z22a1b2}
- \TODO Read again about ‘reward engineering’ [@ChriREngP].


# Efficiency

These are points that came to my mind. Turning SupAmp into ReAmp doesn't depend
on them.

- Can I make sampling more effective by preferring questions that $H$ has asked
  as sub-questions before? – I could try this with SupAmp.
- Is it efficient to start training $X$ and $H'$ at the same time? Wouldn't it
  be better to wait until $H'$ is reasonably accurate in predicting the initial
  behaviour of $H$? And pause training of $X$ whenever the accuracy of $H'$
  drops below a threshold.


# Required learning

\TODO I will have to learn a lot in order to understand the architecture (cf.
CSASupAmp, sec. 2.5).

TODO: List the topics here.
