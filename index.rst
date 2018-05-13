.. image:: https://github.com/ColoradoSchoolOfMines/acm-brand/blob/master/logo/triangle/full_2048.png?raw=true
   :width: 300px
   :target: https://acm.mines.edu
   :class: acm-logo

Mines ACM Officer Resources
===========================

If all of the officers died in a car crash, would Mines ACM still continue to
operate? The goal of this repository is to make the answer to this question
"yes". In other words, this repository is designed to make the bus count for ACM
:math:`\infty`!

This repository is inspired by https://github.com/acmumn/officer-resources/

.. toctree::
   :glob:
   :maxdepth: 1
   :caption: Contents:

   *
   retrospectives/*

Repository Organization
-----------------------

This repository is organized to reflect the *Ownership and Delegation Model* of
club management.  The main concept that governs how this club is run is that
every part of the club **must** be owned by someone. For example, in 2017-18
Jack owned the entire club, Sumner owned the organization of tech talks, Robby
owned the Visplay project, etc.

This idea has proved to be a good way of conceptualizing responsibilities in the
club.

Code (pseudo-Haskell) is a good way of describing this:

.. code-block:: haskell

    -- Responsibility is a tree, it has a description, owner and a list
    -- of sub-responsibilities.
    data Responsibility = Responsibility Description Owner [Responsibility]

The topmost responsibility tree would be:

.. code-block:: haskell

    Responsibility
        "run the club"
        "Chair"
        [organize_tech_talk, get_pizza, deal_with_bso, organize_outreach, ...]

where ``organize_tech_talk``, ``get_pizza``, ``deal_with_bso``, and
``organize_outreach``, are all defined as ``Responsibility``. Note that
ownership is required on every level of the responsibility tree. The chair is
the owner of the root tree, but ownership of subtrees can be delegated.
Sub-delegation is a can always encouraged.

Also note that this tree encodes responsibilities, not positions. The only rule
is that every responsibility must always have an owner.  However, ownership can
be as fluid as necessary. Since positions are not encoded in this tree,
delegation does not necessarily mean that you have to delegate to someone who is
of "lesser rank", you can also delegate to other members of the officer team.

It is up to the chair to perform the delegation of root-level tasks.

This repository is organized to reflect the ``Responsibility`` tree.
