=====================
 Generate Slug Title
=====================

The legacy application we are crating does not have a consistent field
we can use for Title, so we will generate it based on the value of
other fields -- a "name" if it's available. We also need to generate
unique IDs for our items, which we will use for the Slug.

So we remove the Title and Slug from the Page form, and set these. We
set a title to a UUID; if we have "name", we'll use that for Title,
else we'll use the Slug. If they later set or change the name, we'll
update the title.

How to manipulate these core Django and Wagtail fields took some
digging so I've created this example to demonstrate how it can be done
fairly easily. In the ``formbased`` we set these in a customer form's
``save()``; in ``modelbased`` we do it in the model's ``clean()``.
Both look pretty similar, so you should be able to adapt them to your
needs.
