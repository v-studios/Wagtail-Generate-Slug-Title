===========================
Wagtail Generate Slug Title
===========================

The legacy application we are migrating into Wagtail does not have a
consistent field we can use for Title, so we will generate it based on
the value of other fields -- a "name" if it's available. We also need
to generate unique IDs for our items, which we will also use for the
Slug.

We remove the Title and Slug from the Page form, and set these in
code. We set the Slug to a UUID. If we have "name", we'll use that for
Title, else we'll use the Slug. If they later set or change the name,
we'll update the Title.

It took me some digging to determine how to manipulate these core
Django and Wagtail fields, so I've created this example to demonstrate
how it can be done fairly easily.

In the ``formbased`` Page, we set these in a customer form's
``save()``; in ``modelbased`` Page, we do it in the model's
``clean()``. Both look pretty similar, so you should be able to adapt
them to your needs.
